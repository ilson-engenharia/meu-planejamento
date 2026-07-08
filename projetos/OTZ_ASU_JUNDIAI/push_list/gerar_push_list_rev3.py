#!/usr/bin/env python3
"""PUSH LIST REV3 — ASU Jundiaí (26001) | OTZ Engenharia × Messer Gases for Life"""

import os, math, base64, io, json
from datetime import date, datetime
from collections import defaultdict

try:
    from PIL import Image
    PIL_OK = True
except ImportError:
    PIL_OK = False

import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# ── Paths ─────────────────────────────────────────────────────────────────────
ROOT     = os.path.dirname(os.path.abspath(__file__))
UPLOAD   = "/root/.claude/uploads/001b7fb0-8857-54b0-9eb5-28053bfc3f61"
CFTV_DIR = os.path.join(ROOT, "cftv_photos")
EXCEL_IN = os.path.join(UPLOAD, "304d1831-DAENG_PUSH_LIST_ASU_JUNDIAI_5__ATUALIZADO_08.07.xlsx")
HTML_OUT = os.path.join(ROOT, "DAENG_PUSH_LIST_ASU_JUNDIAI.html")
XLSX_OUT = os.path.join(ROOT, "DAENG_PUSH_LIST_ASU_JUNDIAI.xlsx")
LOGO_OTZ = ("/tmp/claude-0/-home-user-meu-planejamento"
            "/001b7fb0-8857-54b0-9eb5-28053bfc3f61/scratchpad/logo_p1_img2_210x161.png")

# Data de referência: atualização final 08/07/2026
TODAY         = date(2026, 7, 8)
LEVAN_DATE    = date(2026, 7, 2)
PROJECT_START = date(2026, 7, 4)  # primeiro dia útil do projeto

# 12 dias úteis seg–sáb: 04/07 → 17/07/2026
WORKING_DAYS = [
    date(2026, 7,  4),  # Sáb  — dia 1
    date(2026, 7,  6),  # Seg  — dia 2
    date(2026, 7,  7),  # Ter  — dia 3  ← TODAY
    date(2026, 7,  8),  # Qua  — dia 4
    date(2026, 7,  9),  # Qui  — dia 5
    date(2026, 7, 10),  # Sex  — dia 6
    date(2026, 7, 11),  # Sáb  — dia 7
    date(2026, 7, 13),  # Seg  — dia 8
    date(2026, 7, 14),  # Ter  — dia 9
    date(2026, 7, 15),  # Qua  — dia 10
    date(2026, 7, 16),  # Qui  — dia 11
    date(2026, 7, 17),  # Sex  — dia 12
]
N_DAYS      = len(WORKING_DAYS)
TODAY_IDX   = next((i for i, d in enumerate(WORKING_DAYS) if d >= TODAY), N_DAYS - 1)
# TODAY = dia 3 (índice 2), previsto = 3/12 = 25%
# Dias úteis abertos: contados a partir de PROJECT_START, seg–sáb, sem domingos
DIAS_ABERTO = sum(1 for d in WORKING_DAYS if d <= TODAY)

NOME_FIX = {
    "Escada 3 — Bacia de Contenção":              "Escada 3 — Portaria Definitiva do Projeto ASU",
    "Escada 3 - Bacia de Contenção":              "Escada 3 — Portaria Definitiva do Projeto ASU",
    "Platôr Central":                             "Platô Central",
    "Platôr":                                     "Platô Central",
    "Superfície da Perna — Cota 691":             "Superfície da Berma — Cota 691",
    "Talude / Perna / Platô — Portaria Provisória":"Talude / Berma / Platô — Portaria Provisória",
    "Transição Perna × Platô — Final do Talude":  "Transição Berma × Platô — Final do Talude",
}

DISC_COLOR = {
    "Macrodrenagem":      "#1565C0",
    "Terraplanagem":      "#7B5E3A",
    "Plantio de Grama":   "#2E7D32",
    "Geral / 5S":         "#E65100",
    "Macrodrenagem / 5S": "#0277BD",
    "CFTV":               "#1A237E",
}
DEF_COLOR = "#546E7A"

# ── CFTV Cards — levantamento Caio 07/07/2026 ────────────────────────────────
CFTV_CARDS = [
    {"id_cftv":  1, "area": "Caixa de Interligação 1",
     "horario": "07/07/2026", "data_lev": "",
     "endereco": "Av. Pref. Luís Latorre, 9450 — Setor Industrial, Jundiaí/SP",
     "foto": "cftv_01.jpg",
     "atividades": [
         {"disciplina":"CFTV","descricao":"Instalação da Tampa da Caixa de Interligação do Sistema de CFTV","peso":1,"status":"Pendente","conclusao":""},
     ]},
    {"id_cftv":  2, "area": "Talude do Platô — Frente à Bacia",
     "horario": "07/07/2026", "data_lev": "",
     "endereco": "Rod. Dom Gabriel Paulino Bueno Couto, 6250 — Jundiaí/SP",
     "foto": "cftv_02.jpg",
     "atividades": [
         {"disciplina":"CFTV","descricao":"Abertura de vala e enterramento do cabeamento do Sistema de CFTV","peso":1,"status":"Pendente","conclusao":""},
     ]},
    {"id_cftv":  3, "area": "Talude do Platô — Frente à Bacia",
     "horario": "07/07/2026", "data_lev": "",
     "endereco": "Rod. Dom Gabriel Paulino Bueno Couto, 11010 — Medeiros, Jundiaí/SP",
     "foto": "cftv_03.jpg",
     "atividades": [
         {"disciplina":"CFTV","descricao":"Abertura de vala e enterramento do cabeamento do Sistema de CFTV","peso":1,"status":"Pendente","conclusao":""},
         {"disciplina":"CFTV","descricao":"Instalação da Tampa da Caixa de Interligação do Sistema de CFTV","peso":1,"status":"Pendente","conclusao":""},
     ]},
    {"id_cftv":  4, "area": "Caixa de Interligação 2",
     "horario": "07/07/2026", "data_lev": "",
     "endereco": "Av. Pref. Luís Latorre, 9450 — Setor Industrial, Jundiaí/SP",
     "foto": "cftv_04.jpg",
     "atividades": [
         {"disciplina":"CFTV","descricao":"Instalação da Tampa da Caixa de Interligação do Sistema de CFTV","peso":1,"status":"Pendente","conclusao":""},
     ]},
    {"id_cftv":  5, "area": "Berma Externa — Acomp. da Rua — Frente à Bacia",
     "horario": "07/07/2026", "data_lev": "",
     "endereco": "Rod. Dom Gabriel Paulino Bueno Couto, 11010 — Medeiros, Jundiaí/SP",
     "foto": "cftv_05.jpg",
     "atividades": [
         {"disciplina":"CFTV","descricao":"Abertura de vala, lançamento e enterramento do cabeamento do Sistema de CFTV","peso":1,"status":"Pendente","conclusao":""},
     ]},
    {"id_cftv":  6, "area": "Caixa de Interligação 3",
     "horario": "07/07/2026", "data_lev": "",
     "endereco": "Rod. Dom Gabriel Paulino Bueno Couto, 6250 — Jundiaí/SP",
     "foto": "cftv_06.jpg",
     "atividades": [
         {"disciplina":"CFTV","descricao":"Instalação da Tampa da Caixa de Interligação do Sistema de CFTV","peso":1,"status":"Pendente","conclusao":""},
     ]},
    {"id_cftv":  7, "area": "Caixa de Interligação 4",
     "horario": "07:45 — 07/07/2026", "data_lev": "",
     "endereco": "Av. Pref. Luís Latorre, 9450 — Setor Industrial, Jundiaí/SP",
     "foto": "cftv_07.jpg",
     "atividades": [
         {"disciplina":"CFTV","descricao":"Instalação da Tampa da Caixa de Interligação do Sistema de CFTV","peso":1,"status":"Pendente","conclusao":""},
     ]},
    {"id_cftv":  8, "area": "Talude / Berma / Platô — Portaria Provisória",
     "horario": "07:45 — 07/07/2026", "data_lev": "",
     "endereco": "Av. Pref. Luís Latorre, 9450 — Setor Industrial, Jundiaí/SP",
     "foto": "cftv_08.jpg",
     "atividades": [
         {"disciplina":"CFTV","descricao":"Instalação da Tampa da Caixa de Interligação do Sistema de CFTV","peso":1,"status":"Pendente","conclusao":""},
     ]},
    {"id_cftv":  9, "area": "Talude do Berma — Frente à Bacia",
     "horario": "07:34 — 07/07/2026", "data_lev": "",
     "endereco": "Rod. Dom Gabriel Paulino Bueno Couto, 11010 — Medeiros, Jundiaí/SP",
     "foto": "cftv_10.jpg",
     "atividades": [
         {"disciplina":"CFTV","descricao":"Abertura de vala e enterramento do cabeamento do Sistema de CFTV no talude","peso":1,"status":"Pendente","conclusao":""},
         {"disciplina":"CFTV","descricao":"Finalização da instalação da caixa de passagem do Sistema de CFTV","peso":1,"status":"Pendente","conclusao":""},
         {"disciplina":"CFTV","descricao":"Instalação da Tampa da Caixa de Interligação do Sistema de CFTV","peso":1,"status":"Pendente","conclusao":""},
     ]},
    {"id_cftv": 10, "area": "Caixa de Interligação 5",
     "horario": "07:46 — 07/07/2026", "data_lev": "",
     "endereco": "Av. Pref. Luís Latorre, 9450 — Setor Industrial, Jundiaí/SP",
     "foto": "cftv_01.jpg",
     "atividades": [
         {"disciplina":"CFTV","descricao":"Instalação da Tampa da Caixa de Interligação do Sistema de CFTV","peso":1,"status":"Pendente","conclusao":""},
     ]},
    {"id_cftv": 11, "area": "Caixa de Interligação 6",
     "horario": "07/07/2026", "data_lev": "",
     "endereco": "",
     "foto": "cftv_11.jpg",
     "atividades": [
         {"disciplina":"CFTV","descricao":"Instalação da Tampa da Caixa de Interligação do Sistema de CFTV","peso":1,"status":"Pendente","conclusao":""},
     ]},
    {"id_cftv": 12, "area": "Caixa de Interligação 7",
     "horario": "07:31 — 07/07/2026", "data_lev": "",
     "endereco": "Av. Marginal, 65 — Setor Industrial, Jundiaí/SP",
     "foto": "cftv_12.jpg",
     "atividades": [
         {"disciplina":"CFTV","descricao":"Instalação da Tampa da Caixa de Interligação do Sistema de CFTV","peso":1,"status":"Pendente","conclusao":""},
     ]},
]

# ── CFTV photo + meta lookup (derivado de CFTV_CARDS) ────────────────────────
CFTV_META  = {f"C{cc['id_cftv']:02d}": {"gps":"","horario":cc.get("horario",""),
               "data":cc.get("data_lev",""),"endereco":cc.get("endereco","")}
              for cc in CFTV_CARDS}
CFTV_PHOTO = {f"C{cc['id_cftv']:02d}": cc["foto"] for cc in CFTV_CARDS}

# ── Area meta ─────────────────────────────────────────────────────────────────
AREA_META = {
    "01": {"gps":"23.1710S/46.9501W","horario":"15:14","data":"02/07/2026",
           "endereco":"Av. Pref. Luís Latorre, 9600 — Setor Industrial, Jundiaí/SP",
           "fotos":["0dce6895-1001308572.jpg"]},
    "02": {"gps":"23.1710S/46.9501W","horario":"15:16","data":"02/07/2026",
           "endereco":"Av. Pref. Luís Latorre, 9600 — Setor Industrial, Jundiaí/SP",
           "fotos":["f46133ce-1001308573.jpg"]},
    "03": {"gps":"23.1706S/46.9497W","horario":"15:34","data":"02/07/2026",
           "endereco":"Av. Pref. Luís Latorre, 9600 — Setor Industrial, Jundiaí/SP",
           "fotos":["ee4ec5be-1001308585.jpg"]},
    "04": {"gps":"23.1703S/46.9492W","horario":"15:51","data":"02/07/2026",
           "endereco":"Rod. Dom Gabriel Paulino Bueno Couto, 2045 — Chácara Terra Nova, Jundiaí/SP",
           "fotos":["cbac03ca-1001308613.jpg"]},
    "05": {"gps":"23.1703S/46.9492W","horario":"15:57","data":"02/07/2026",
           "endereco":"Av. Pref. Luís Latorre, 9600 — Setor Industrial, Jundiaí/SP",
           "fotos":["d8dad6bf-1001308617.jpg","c736ad32-1001308623.jpg","98a6888a-1001308624.jpg"]},
    "06": {"gps":"23.1703S/46.9492W","horario":"16:00","data":"02/07/2026",
           "endereco":"Av. Pref. Luís Latorre, 9600 — Setor Industrial, Jundiaí/SP",
           "fotos":["bd51de41-1001308618.jpg","37409c2b-1001308619.jpg"]},
    "07": {"gps":"23.1702S/46.9491W","horario":"16:06","data":"02/07/2026",
           "endereco":"Av. Pref. Luís Latorre, 9450–9600 — Setor Industrial, Jundiaí/SP",
           "fotos":["cb7d3a33-1001308635.jpg","840e9892-1001308642.jpg"]},
    "08": {"gps":"23.1702S/46.9483W","horario":"16:14","data":"02/07/2026",
           "endereco":"Rua Emílio Antonon, 1680 / Rua Nancy Carlota Netto, 120 — Jundiaí/SP",
           "fotos":["38482029-1001308650.jpg","f7549f10-1001308651.jpg",
                    "7d5f4cae-1001308652.jpg","8f08fbcf-1001308653.jpg"]},
    "09": {"gps":"23.1703S/46.9483W","horario":"16:17","data":"02/07/2026",
           "endereco":"Rua Emílio Antonon, 1680 / Av. Pref. Luís Latorre, 2067 — Jundiaí/SP",
           "fotos":["8997db98-1001308654.jpg","a393ade5-1001308655.jpg"]},
    "10": {"gps":"23.1703S/46.9483W","horario":"16:21","data":"02/07/2026",
           "endereco":"Rua Emílio Antonon, 1680 — Chácara Aeroporto, Jundiaí/SP",
           "fotos":["27b3328c-1001308656.jpg","64e95537-1001308657.jpg","b739367c-1001308658.jpg"]},
    "11": {"gps":"23.1702–23.1715S/46.9479–46.9483W","horario":"16:25–16:30","data":"02/07/2026",
           "endereco":"Av. Antonieta Piva Barranqueiros, 982 / Rua Nancy Carlota Netto, 120 — Jundiaí/SP",
           "fotos":["c8236fab-1001308670.jpg","eafa0b33-1001308671.jpg",
                    "3108b587-1001308672.jpg","0ce7bdaa-1001308679.jpg",
                    "bcb014dd-1001308680.jpg","f349934a-1001308681.jpg",
                    "ae810a7b-1001308682.jpg","1ce90304-1001308688.jpg",
                    "3bf04eef-1001308690.jpg","1a6375af-1001308691.jpg",
                    "9f14ec2e-1001308697.jpg","c504e614-1001308703.jpg"]},
    "12": {"gps":"23.1717S/46.9482W","horario":"16:37","data":"02/07/2026",
           "endereco":"Rod. Dom Gabriel Paulino Bueno Couto, 11010 — Medeiros, Jundiaí/SP",
           "fotos":["a3f56521-1001308704.jpg","106c1353-1001308705.jpg"]},
    "13": {"gps":"23.1718S/46.9481–46.9482W","horario":"16:42","data":"02/07/2026",
           "endereco":"Rua Emílio Antonon, 1680 — Chácara Aeroporto, Jundiaí/SP",
           "fotos":["76a9d794-1001308709.jpg","7f48bd14-1001308710.jpg","36220157-1001308711.jpg"]},
    "14": {"gps":"23.1721–23.1722S/46.9480W","horario":"16:45","data":"02/07/2026",
           "endereco":"Rua Emílio Antonon, 1680 / Rod. Dom Gabriel Paulino Bueno Couto, 11010 — Jundiaí/SP",
           "fotos":["f26293ac-1001308715.jpg","cfb019ad-1001308716.jpg",
                    "c7b1c31f-1001308717.jpg","c2fe493a-1001308720.jpg"]},
    "15": {"gps":"23.1721S/46.9488W","horario":"16:51","data":"02/07/2026",
           "endereco":"Rod. Dom Gabriel Paulino Bueno Couto, 11010 — Medeiros, Jundiaí/SP",
           "fotos":["7587ac67-1001308725.jpg","03e95a95-1001308726.jpg",
                    "c133effc-1001308727.jpg","a72461ba-1001308728.jpg"]},
    "16": {"gps":"23.1712S/46.9491W – 23.1710S/46.9494W","horario":"09:36","data":"03/07/2026",
           "endereco":"Rod. Dom Gabriel Paulino Bueno Couto, 11010 + Av. Pref. Luís Latorre, 9450 — Jundiaí/SP",
           "fotos":["2d8dfe0d-1001309522.jpg","90d02fa3-1001309523.jpg","76ef48cc-1001309537.jpg"]},
}

# ── Helpers ───────────────────────────────────────────────────────────────────
def fix_name(s): return NOME_FIX.get(s, s)
def disc_color(d): return DISC_COLOR.get(d, DEF_COLOR)

def encode_photo(fname, max_dim=750, quality=68):
    path = os.path.join(UPLOAD, fname)
    return _encode_path(path, max_dim, quality)

def encode_photo_path(path, max_dim=750, quality=68, landscape=False):
    return _encode_path(path, max_dim, quality, landscape)

def _encode_path(path, max_dim=750, quality=68, landscape=False):
    if not os.path.exists(path): return ""
    try:
        if PIL_OK:
            img = Image.open(path).convert("RGB")
            w, h = img.size
            if landscape and h > w:
                # Center-crop portrait → paisagem 4:3 para consistência com levantamento
                new_h = w * 3 // 4
                top   = (h - new_h) // 2
                img   = img.crop((0, top, w, top + new_h))
                w, h  = img.size
            if max(w, h) > max_dim:
                r = max_dim / max(w, h)
                img = img.resize((int(w*r), int(h*r)), Image.LANCZOS)
            buf = io.BytesIO()
            img.save(buf, "JPEG", quality=quality, optimize=True)
            return base64.b64encode(buf.getvalue()).decode()
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except Exception as e:
        print(f"  [WARN] {path}: {e}"); return ""

def load_otz_logo():
    if not os.path.exists(LOGO_OTZ): return ""
    with open(LOGO_OTZ, "rb") as f:
        return base64.b64encode(f.read()).decode()

# ── Gauge SVG ─────────────────────────────────────────────────────────────────
def gauge_svg(pct, done_cnt, total_cnt, uid, mini=False):
    if mini:
        W, H, cx, cy, R = 158, 122, 79, 74, 54
        pct_sz, sub_sz, tick_out, tick_in = 19, 8, 7, 4
    else:
        W, H, cx, cy, R = 268, 215, 134, 115, 90
        pct_sz, sub_sz, tick_out, tick_in = 28, 9, 10, 6

    SPAN, START = 240, 210

    def polar(deg, r):
        rad = math.radians(deg)
        return (cx + r*math.cos(rad), cy - r*math.sin(rad))

    def arc_d(r, fd, td):
        x0,y0 = polar(fd, r); x1,y1 = polar(td, r)
        lg = 1 if (fd-td) > 180 else 0
        return f"M{x0:.1f},{y0:.1f} A{r},{r} 0 {lg},1 {x1:.1f},{y1:.1f}"

    ea  = START - SPAN
    pa  = START - pct/100*SPAN
    col = "#F44336" if pct<33 else "#FFC107" if pct<66 else "#00E676"

    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
         f'width="{W}" height="{H}" style="display:block">',
         f'<defs>'
         f'<filter id="gl{uid}" x="-40%" y="-40%" width="180%" height="180%">'
         f'<feGaussianBlur in="SourceGraphic" stdDeviation="3.5" result="b"/>'
         f'<feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>'
         f'</filter>'
         f'<linearGradient id="zg{uid}" gradientUnits="userSpaceOnUse" '
         f'x1="{polar(210,R)[0]:.0f}" y1="{polar(210,R)[1]:.0f}" '
         f'x2="{polar(-30,R)[0]:.0f}" y2="{polar(-30,R)[1]:.0f}">'
         f'<stop offset="0%" stop-color="#F44336"/>'
         f'<stop offset="50%" stop-color="#FFC107"/>'
         f'<stop offset="100%" stop-color="#00E676"/>'
         f'</linearGradient></defs>']

    sw = 16 if not mini else 12
    s += [
        f'<path d="{arc_d(R,START,ea)}" fill="none" stroke="#1A3A60" stroke-width="{sw}" stroke-linecap="round"/>',
        f'<path d="{arc_d(R,START,ea)}" fill="none" stroke="url(#zg{uid})" stroke-width="{sw}" stroke-linecap="round" opacity="0.12"/>',
    ]
    if pct > 0.1:
        s.append(f'<path d="{arc_d(R,START,pa)}" fill="none" stroke="{col}" '
                 f'stroke-width="{sw-2}" stroke-linecap="round" filter="url(#gl{uid})"/>')

    for tp in ([0,25,50,75,100] if not mini else [0,50,100]):
        ta = START - tp/100*SPAN
        xi,yi = polar(ta, R-tick_in); xo,yo = polar(ta, R+tick_out)
        s.append(f'<line x1="{xi:.1f}" y1="{yi:.1f}" x2="{xo:.1f}" y2="{yo:.1f}" '
                 f'stroke="#4A90D9" stroke-width="{"2" if tp in(0,100) else "1.5"}"/>')
        if not mini:
            xl,yl = polar(ta, R+24)
            s.append(f'<text x="{xl:.1f}" y="{yl:.1f}" text-anchor="middle" '
                     f'dominant-baseline="middle" fill="#4A90D9" font-size="9" '
                     f'font-family="Arial,sans-serif">{tp}%</text>')

    nx,ny = polar(pa, R-8)
    b1x,b1y = polar(pa+90, 5); b2x,b2y = polar(pa-90, 5)
    s += [
        f'<polygon points="{cx:.1f},{cy:.1f} {b1x:.1f},{b1y:.1f} {nx:.1f},{ny:.1f} {b2x:.1f},{b2y:.1f}" '
        f'fill="white" filter="url(#gl{uid})" opacity="0.9"/>',
        f'<circle cx="{cx}" cy="{cy}" r="{"8" if not mini else "6"}" fill="#0D1F3C" stroke="#00BCD4" stroke-width="2"/>',
        f'<circle cx="{cx}" cy="{cy}" r="{"3.5" if not mini else "2.5"}" fill="#00BCD4"/>',
        f'<text x="{cx}" y="{cy+28}" text-anchor="middle" fill="white" font-size="{pct_sz}" '
        f'font-weight="bold" font-family="Arial,sans-serif">{pct:.0f}%</text>',
        f'<text x="{cx}" y="{cy+41}" text-anchor="middle" fill="#00BCD4" font-size="{sub_sz}" '
        f'font-family="Arial,sans-serif">AVANÇO FÍSICO</text>',
    ]
    if not mini:
        pend_cnt_i = int(total_cnt) - int(done_cnt)
        s += [
            f'<line x1="{cx-62}" y1="{cy+50}" x2="{cx+62}" y2="{cy+50}" '
            f'stroke="#1A3A60" stroke-width="0.8"/>',
            f'<text x="{cx-52}" y="{cy+63}" text-anchor="middle" fill="#00E676" '
            f'font-size="11" font-weight="bold" font-family="Arial,sans-serif">{int(done_cnt)}</text>',
            f'<text x="{cx-52}" y="{cy+74}" text-anchor="middle" fill="#4A90D9" '
            f'font-size="7" font-family="Arial,sans-serif">CONCL.</text>',
            f'<text x="{cx}" y="{cy+63}" text-anchor="middle" fill="#FFC107" '
            f'font-size="11" font-weight="bold" font-family="Arial,sans-serif">{pend_cnt_i}</text>',
            f'<text x="{cx}" y="{cy+74}" text-anchor="middle" fill="#4A90D9" '
            f'font-size="7" font-family="Arial,sans-serif">PEND.</text>',
            f'<text x="{cx+52}" y="{cy+63}" text-anchor="middle" fill="#29B6F6" '
            f'font-size="11" font-weight="bold" font-family="Arial,sans-serif">{int(total_cnt)}</text>',
            f'<text x="{cx+52}" y="{cy+74}" text-anchor="middle" fill="#4A90D9" '
            f'font-size="7" font-family="Arial,sans-serif">TOTAL</text>',
        ]
    s.append('</svg>')
    return "\n".join(s)

# ── Curva-S SVG ───────────────────────────────────────────────────────────────
def curvas_svg(done_atv, tot_atv):
    real_pct = done_atv / tot_atv * 100 if tot_atv else 0
    today_x  = TODAY_IDX + 1   # dias concluídos = 3
    prev_pct = today_x / N_DAYS * 100  # 25.0%

    W, H = 560, 256
    ML, MR, MT, MB = 46, 18, 28, 44
    PW = W - ML - MR
    PH = H - MT - MB

    def px(day, pct):
        x = ML + day * PW / N_DAYS
        y = MT + PH * (1.0 - pct / 100.0)
        return x, y

    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="100%" '
         f'preserveAspectRatio="xMidYMid meet">']
    s.append(f'<rect width="{W}" height="{H}" fill="#0D1F3C" rx="6"/>')
    s.append(f'<text x="{W//2}" y="16" text-anchor="middle" fill="#4A90D9" font-size="10" '
             f'font-weight="600" font-family="Arial,sans-serif">'
             f'Curva-S — Previsto × Realizado &nbsp;|&nbsp; 04/07 → 17/07/2026</text>')

    # Grid horizontal + rótulos Y
    for p in [0, 25, 50, 75, 100]:
        x0, y0 = px(0, p); x1, _ = px(N_DAYS, p)
        s.append(f'<line x1="{x0:.1f}" y1="{y0:.1f}" x2="{x1:.1f}" y2="{y0:.1f}" '
                 f'stroke="#1A3A60" stroke-width="1" stroke-dasharray="4,4"/>')
        s.append(f'<text x="{ML-4}" y="{y0:.1f}" text-anchor="end" dominant-baseline="middle" '
                 f'fill="#4A90D9" font-size="9" font-family="Arial,sans-serif">{p}%</text>')

    # Grid vertical
    for i in range(N_DAYS + 1):
        xv = ML + i * PW / N_DAYS
        s.append(f'<line x1="{xv:.1f}" y1="{MT}" x2="{xv:.1f}" y2="{MT+PH}" '
                 f'stroke="#1A3A60" stroke-width="0.5"/>')

    # Rótulos X
    day_labels = ["04/07","06/07","07/07","08/07","09/07","10/07",
                  "11/07","13/07","14/07","15/07","16/07","17/07"]
    for i, lbl in enumerate(day_labels):
        x = ML + (i + 0.5) * PW / N_DAYS
        s.append(f'<text x="{x:.1f}" y="{MT+PH+14}" text-anchor="middle" fill="#4A90D9" '
                 f'font-size="8" font-family="Arial,sans-serif">{lbl}</text>')

    # Eixos
    s.append(f'<line x1="{ML}" y1="{MT}" x2="{ML}" y2="{MT+PH}" stroke="#2A5090" stroke-width="1.5"/>')
    s.append(f'<line x1="{ML}" y1="{MT+PH}" x2="{ML+PW}" y2="{MT+PH}" stroke="#2A5090" stroke-width="1.5"/>')

    # Previsto (linha tracejada azul — 12 dias completos)
    pts_prev = " ".join(f"{px(i, i/N_DAYS*100)[0]:.1f},{px(i, i/N_DAYS*100)[1]:.1f}"
                        for i in range(N_DAYS + 1))
    s.append(f'<polyline points="{pts_prev}" fill="none" stroke="#29B6F6" '
             f'stroke-width="2" stroke-dasharray="8,4"/>')

    # Defasagem fill — triângulo entre Previsto e Realizado até "hoje"
    xd0, yd0 = px(0, 0)
    xp_hoje, yp_hoje = px(today_x, prev_pct)
    xr0, yr0 = px(0, 0)
    xr1, yr1 = px(today_x, real_pct)
    if real_pct < prev_pct:
        # Atrasado → vermelho (realizado < previsto)
        fill_c  = "#FF525228"
        edge_c  = "#FF5252"
        def_lbl = f"−{prev_pct - real_pct:.1f} pp"
        def_col = "#FF5252"
    else:
        # Adiantado → azul (realizado > previsto)
        fill_c  = "#29B6F628"
        edge_c  = "#29B6F6"
        def_lbl = f"+{real_pct - prev_pct:.1f} pp"
        def_col = "#29B6F6"
    # Triângulo: origem → ponto realizado → ponto previsto (mesmo x) → fecha
    s.append(f'<polygon points="{xd0:.1f},{yd0:.1f} {xr1:.1f},{yr1:.1f} '
             f'{xp_hoje:.1f},{yp_hoje:.1f}" fill="{fill_c}" stroke="{edge_c}" '
             f'stroke-width="0.8" stroke-dasharray="3,3"/>')
    # Label defasagem no centro do triângulo (aprox.)
    def_x = (xd0 + xr1 + xp_hoje) / 3
    def_y = (yd0 + yr1 + yp_hoje) / 3
    s.append(f'<text x="{def_x:.1f}" y="{def_y:.1f}" text-anchor="middle" '
             f'dominant-baseline="middle" fill="{def_col}" font-size="9.5" '
             f'font-weight="bold" font-family="Arial,sans-serif">{def_lbl}</text>')

    # Marcador "Hoje"
    x_hoje, _ = px(today_x, 0)
    s.append(f'<line x1="{x_hoje:.1f}" y1="{MT}" x2="{x_hoje:.1f}" y2="{MT+PH}" '
             f'stroke="#FFC107" stroke-width="1.2" stroke-dasharray="5,3"/>')
    s.append(f'<text x="{x_hoje:.1f}" y="{MT-6}" text-anchor="middle" fill="#FFC107" '
             f'font-size="8.5" font-family="Arial,sans-serif">Hoje</text>')

    # Realizado (linha sólida verde — até hoje)
    s.append(f'<polygon points="{xr0:.1f},{yr0:.1f} {xr1:.1f},{yr1:.1f} '
             f'{xr1:.1f},{MT+PH:.1f} {xr0:.1f},{MT+PH:.1f}" fill="#00E67614"/>')
    s.append(f'<line x1="{xr0:.1f}" y1="{yr0:.1f}" x2="{xr1:.1f}" y2="{yr1:.1f}" '
             f'stroke="#00E676" stroke-width="2.5"/>')

    # Ponto Previsto no dia de hoje
    xp, yp = px(today_x, prev_pct)
    s.append(f'<circle cx="{xp:.1f}" cy="{yp:.1f}" r="4" fill="#29B6F6" stroke="#0D1F3C" stroke-width="1.5"/>')
    s.append(f'<text x="{xp-8:.1f}" y="{yp-9:.1f}" text-anchor="middle" fill="#29B6F6" '
             f'font-size="9" font-family="Arial,sans-serif">{prev_pct:.0f}%</text>')

    # Ponto Realizado no dia de hoje
    s.append(f'<circle cx="{xr1:.1f}" cy="{yr1:.1f}" r="5" fill="#00E676" stroke="#0D1F3C" stroke-width="1.5"/>')
    s.append(f'<text x="{xr1+8:.1f}" y="{yr1-4:.1f}" fill="#00E676" font-size="10" '
             f'font-weight="bold" font-family="Arial,sans-serif">{real_pct:.1f}%</text>')

    # Legenda
    lx, ly = ML + 8, MT + 16
    s.append(f'<line x1="{lx}" y1="{ly}" x2="{lx+22}" y2="{ly}" stroke="#29B6F6" '
             f'stroke-width="2" stroke-dasharray="8,4"/>')
    s.append(f'<text x="{lx+26}" y="{ly}" dominant-baseline="middle" fill="#29B6F6" '
             f'font-size="9" font-family="Arial,sans-serif">Previsto (linear)</text>')
    s.append(f'<line x1="{lx+110}" y1="{ly}" x2="{lx+132}" y2="{ly}" stroke="#00E676" stroke-width="2.5"/>')
    s.append(f'<text x="{lx+136}" y="{ly}" dominant-baseline="middle" fill="#00E676" '
             f'font-size="9" font-family="Arial,sans-serif">Realizado</text>')

    s.append('</svg>')
    return "\n".join(s)

# ── Discipline chart ──────────────────────────────────────────────────────────
def discipline_chart_svg(disc_stats):
    disc_stats = sorted(disc_stats, key=lambda x: x[3], reverse=True)
    RH = 34; LW = 175; BW = 300; SW = 105; PAD = 16
    W  = LW + BW + SW + PAD*2
    H  = len(disc_stats)*RH + PAD*2
    mx = max(d[3] for d in disc_stats) or 1

    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
         f'width="100%" preserveAspectRatio="xMidYMid meet">']
    for i,(name,color,done,total) in enumerate(disc_stats):
        y   = PAD + i*RH
        bw  = int(BW*total/mx)
        dw  = int(BW*done/mx)
        pct = done/total*100 if total else 0
        ym  = y + RH//2
        bx  = PAD + LW
        sx  = bx + BW + 10
        s += [
            f'<text x="{PAD}" y="{ym}" dominant-baseline="middle" fill="#C8D8F0" '
            f'font-size="12" font-family="Arial,sans-serif">{name}</text>',
            f'<rect x="{bx}" y="{ym-9}" width="{bw}" height="18" rx="4" '
            f'fill="{color}22" stroke="{color}44" stroke-width="1"/>',
        ]
        if dw > 0:
            s.append(f'<rect x="{bx}" y="{ym-9}" width="{dw}" height="18" rx="4" '
                     f'fill="{color}" opacity="0.85"/>')
        s += [
            f'<text x="{sx}" y="{ym}" dominant-baseline="middle" fill="{color}" '
            f'font-size="11.5" font-family="Arial,sans-serif" font-weight="600">'
            f'{done}/{total}</text>',
            f'<text x="{sx+48}" y="{ym}" dominant-baseline="middle" fill="#4A90D9" '
            f'font-size="11" font-family="Arial,sans-serif">{pct:.0f}%</text>',
        ]
        if i < len(disc_stats)-1:
            s.append(f'<line x1="{PAD}" y1="{y+RH-1}" x2="{W-PAD}" y2="{y+RH-1}" '
                     f'stroke="#1A3A60" stroke-width="1"/>')
    s.append('</svg>')
    return "\n".join(s)

# ── Read Excel ────────────────────────────────────────────────────────────────
def read_excel():
    wb = openpyxl.load_workbook(EXCEL_IN, data_only=True)
    ws = wb.active
    card_data = {}
    current_key = None  # carry-forward para células mescladas (col A = None)
    for row in ws.iter_rows(min_row=4, values_only=True):
        if not any(row): continue
        if row[0] is not None:
            # Nova linha de card: atualiza chave corrente
            area  = fix_name(str(row[1]).strip()) if row[1] else ""
            lnum  = str(row[2]).strip().zfill(2)  if row[2] else "00"
            lnom  = fix_name(str(row[3]).strip()) if row[3] else ""
            f_val = row[4]
            if f_val is None:
                fstr = "S/F"
            elif isinstance(f_val, (int, float)):
                fstr = str(int(f_val))
            else:
                fstr = str(f_val).strip() or "S/F"
            current_key = (lnum, fstr)
            if current_key not in card_data:
                card_data[current_key] = {"area":area,"nome":lnom,"local_num":lnum,
                                          "foto_str":fstr,"atividades":[]}
        # Se col A é None (célula mesclada): continua com current_key
        if current_key is None:
            continue
        disc  = str(row[6]).strip()  if row[6] else "Geral"
        desc  = str(row[7]).strip()  if row[7] else ""
        peso  = int(row[8]) if row[8] and str(row[8]).strip().isdigit() else 1
        stat  = str(row[9]).strip()  if row[9]  else "Pendente"
        conc  = str(row[11]).strip() if row[11] else ""
        card_data[current_key]["atividades"].append({
            "disciplina":disc,"descricao":desc,"peso":peso,
            "status":stat,"conclusao":conc})
    return card_data

# ── Build cards ───────────────────────────────────────────────────────────────
def build_cards(card_data):
    from_local = defaultdict(list)
    for (lnum, fstr) in card_data:
        try:
            fidx = int(fstr) if fstr != "S/F" else 0
        except ValueError:
            fidx = 0
        from_local[lnum].append((fidx, fstr))

    cards = []
    gid   = 0

    for lnum in sorted(from_local.keys()):
        entries  = sorted(from_local[lnum], key=lambda x: x[0])
        is_cftv  = lnum.startswith("C")

        if is_cftv:
            # Cards CFTV: foto de cftv_photos/, meta de CFTV_META
            meta = CFTV_META.get(lnum, {"gps":"","horario":"","data":"","endereco":""})
            for fidx, fstr in entries:
                data  = card_data[(lnum, fstr)]
                fname = CFTV_PHOTO.get(lnum, "")
                b64   = ""
                if fname:
                    photo_path = os.path.join(CFTV_DIR, fname)
                    if os.path.exists(photo_path):
                        print(f"  Encoding CFTV {fname} ...", end=" ", flush=True)
                        b64 = encode_photo_path(photo_path, landscape=True)
                        print("ok" if b64 else "FAIL")
                gid += 1
                atv, dp, tp = _build_atv(data["atividades"])
                cards.append(_mk_card(gid, data, meta, lnum,
                                      1 if b64 else 0, 1, b64, not b64, atv, dp, tp))
        else:
            # Cards regulares: foto de AREA_META + UPLOAD
            meta  = AREA_META.get(lnum, {})
            fotos = meta.get("fotos", [])
            for fidx, fstr in entries:
                data = card_data[(lnum, fstr)]
                if fstr == "S/F":
                    if fotos:
                        for fi, fname in enumerate(fotos):
                            gid += 1
                            print(f"  Encoding {fname} ...", end=" ", flush=True)
                            b64 = encode_photo(fname); print("ok" if b64 else "FAIL")
                            atv, dp, tp = _build_atv(data["atividades"])
                            cards.append(_mk_card(gid, data, meta, lnum,
                                                  fi+1, len(fotos), b64, False, atv, dp, tp))
                    else:
                        gid += 1
                        atv, dp, tp = _build_atv(data["atividades"])
                        cards.append(_mk_card(gid, data, meta, lnum, 0, 0, "", True, atv, dp, tp))
                else:
                    b64 = ""
                    if 0 < fidx <= len(fotos):
                        fname = fotos[fidx-1]
                        print(f"  Encoding {fname} ...", end=" ", flush=True)
                        b64 = encode_photo(fname); print("ok" if b64 else "FAIL")
                    gid += 1
                    atv, dp, tp = _build_atv(data["atividades"])
                    cards.append(_mk_card(gid, data, meta, lnum, fidx, len(fotos), b64,
                                          not b64 and fidx==0, atv, dp, tp))
    return cards, gid

def build_cftv_cards(start_gid):
    gid = start_gid
    cards = []
    for cc in CFTV_CARDS:
        gid += 1
        photo_path = os.path.join(CFTV_DIR, cc["foto"])
        b64 = ""
        if os.path.exists(photo_path):
            print(f"  Encoding CFTV {cc['foto']} ...", end=" ", flush=True)
            b64 = encode_photo_path(photo_path, landscape=True)
            print("ok" if b64 else "FAIL")
        atv, dp, tp = _build_atv(cc["atividades"])
        pct = dp/tp*100 if tp else 0
        lnum = f"C{cc['id_cftv']:02d}"
        cards.append({
            "id": gid, "area": cc["area"], "nome": cc["area"],
            "local_num": lnum,
            "foto_seq": 1 if b64 else 0, "foto_total": 1,
            "foto_b64": b64, "sem_foto": not b64,
            "gps": "",
            "horario": cc.get("horario",""),
            "data_lev": cc.get("data_lev",""),
            "endereco": cc.get("endereco",""),
            "atividades": atv, "done_peso": dp, "total_peso": tp, "pct": pct,
        })
    return cards

def _build_atv(raw):
    atv=[]; dp=tp=0
    for i,a in enumerate(raw):
        p=a["peso"]; tp+=p
        if a["status"].lower().startswith("conclu"): dp+=p
        atv.append({**a,"num":i+1})
    return atv, dp, tp

def _mk_card(gid, data, meta, lnum, seq, total, b64, sem_foto, atv, dp, tp):
    pct = dp/tp*100 if tp else 0
    return {"id":gid,"area":data["area"],"nome":data["nome"],"local_num":lnum,
            "foto_seq":seq,"foto_total":total,"foto_b64":b64,"sem_foto":sem_foto,
            "gps":meta.get("gps",""),"horario":meta.get("horario",""),
            "data_lev":meta.get("data",""),"endereco":meta.get("endereco",""),
            "atividades":atv,"done_peso":dp,"total_peso":tp,"pct":pct}

# ── KPIs ─────────────────────────────────────────────────────────────────────
def compute_kpis(cards):
    tot_cards = len(cards)
    tot_atv   = sum(len(c["atividades"]) for c in cards)
    done_atv  = sum(1 for c in cards for a in c["atividades"]
                    if a["status"].lower().startswith("conclu"))
    pend_atv  = tot_atv - done_atv
    pct       = done_atv/tot_atv*100 if tot_atv else 0

    prev_pct  = (TODAY_IDX + 1) / N_DAYS * 100  # 3/12 = 25.0%
    defasagem = prev_pct - pct                   # positivo = atrasado

    disc_map = defaultdict(lambda:[0,0])
    for c in cards:
        for a in c["atividades"]:
            disc_map[a["disciplina"]][1]+=1
            if a["status"].lower().startswith("conclu"):
                disc_map[a["disciplina"]][0]+=1
    disc_stats = [(d,disc_color(d),v[0],v[1]) for d,v in disc_map.items()]

    vel  = done_atv/DIAS_ABERTO if done_atv>0 else None
    areas = sorted(set(c["area"] for c in cards))
    discs = sorted(set(a["disciplina"] for c in cards for a in c["atividades"]))

    return {"tot_cards":tot_cards,"tot_atv":tot_atv,"done_atv":done_atv,
            "pend_atv":pend_atv,"pct":pct,"prev_pct":prev_pct,"defasagem":defasagem,
            "dias_aberto":DIAS_ABERTO,"velocidade":vel,
            "disc_stats":disc_stats,"areas":areas,"discs":discs}

# ── HTML helpers ──────────────────────────────────────────────────────────────
def html_activity_row(a):
    color = disc_color(a["disciplina"])
    cls   = "concluido" if a["status"].lower().startswith("conclu") else "pendente"
    return f'''<tr class="atv-row {cls}">
  <td class="atv-num">{a["num"]}</td>
  <td class="atv-disc" style="border-left:4px solid {color};padding-left:9px">
    <span class="ddot" style="background:{color}"></span>{a["disciplina"]}
  </td>
  <td class="atv-desc">{a["descricao"]}</td>
  <td class="atv-peso"><span class="pbadge" style="border-color:{color}">{a["peso"]}</span></td>
  <td class="atv-status {cls}">{a["status"]}</td>
  <td class="atv-date">{a.get("conclusao","") or "—"}</td>
</tr>'''

def html_card(card):
    uid  = str(card["id"])
    mini = gauge_svg(card["pct"], card["done_peso"], card["total_peso"], "m"+uid, mini=True)

    if card["sem_foto"]:
        foto_antes = '''<div class="photo-ph">
  <div class="ph-icon">📷</div>
  <div class="ph-lbl">Foto não disponível</div>
</div>'''
        badge_antes = ""
    else:
        foto_antes  = (f'<img class="card-photo" '
                       f'src="data:image/jpeg;base64,{card["foto_b64"]}" '
                       f'alt="Foto — Local {card["local_num"]}">')
        badge_antes = (f'<div class="photo-badge">'
                       f'Foto {card["foto_seq"]} de {card["foto_total"]}</div>')

    foto_pos = '''<div class="photo-ph pos-ph">
  <div class="ph-icon">📷</div>
  <div class="ph-lbl">Foto Pós</div>
  <div class="ph-sub">Aguardando Conclusão</div>
</div>'''

    done_cnt = sum(1 for a in card["atividades"] if a["status"].lower().startswith("conclu"))
    pend_cnt = len(card["atividades"]) - done_cnt
    pct_c    = "#00E676" if card["pct"]>=66 else "#FFC107" if card["pct"]>=33 else "#F44336"

    # lhue: suporta "C01" para cards CFTV
    try:
        lhue = (int(card["local_num"].replace("C","").lstrip("0") or "0")*23)%360
    except:
        lhue = (card["id"]*17)%360

    atv_rows = "\n".join(html_activity_row(a) for a in card["atividades"])
    discs_js = json.dumps(list(set(a["disciplina"] for a in card["atividades"])))
    stats_js = json.dumps(list(set(a["status"] for a in card["atividades"])))
    text_js  = " ".join(a["descricao"] for a in card["atividades"]).replace('"','&quot;')
    area_js  = card["area"].replace('"','&quot;')

    horario_display = card["horario"]
    if card["data_lev"]:
        horario_display += f' — {card["data_lev"]}'

    return f'''
<div class="push-card" id="card-{card["id"]}"
  data-area="{area_js}"
  data-discs='{discs_js}'
  data-statuses='{stats_js}'
  data-text="{text_js}">

  <div class="card-hbar" style="background:linear-gradient(135deg,hsl({lhue},55%,12%),hsl({lhue},40%,18%))">
    <span class="cid-badge">CARD {card["id"]:02d}</span>
    <span class="cloc-badge">Local {card["local_num"]}</span>
    <span class="cnome">{card["nome"]}</span>
    <span class="cpct" style="color:{pct_c}">{card["pct"]:.0f}%</span>
    <span class="cstats">
      <span class="sb done">{done_cnt} concl.</span>
      <span class="sb pend">{pend_cnt} pend.</span>
    </span>
  </div>

  <div class="card-photos-row">
    <div class="photo-col">
      <div class="photo-label antes-lbl">ANTES / LEVANTAMENTO</div>
      <div class="photo-wrap">
        {foto_antes}
        {badge_antes}
        <div class="area-overlay">{card["area"]}</div>
      </div>
    </div>
    <div class="photo-col">
      <div class="photo-label pos-lbl">PÓS / REALIZADO</div>
      <div class="photo-wrap">
        {foto_pos}
      </div>
    </div>
  </div>

  <div class="card-info-row">
    <div class="card-meta">
      <div class="mrow"><span class="mi">⊕</span><span>{card["gps"] or "—"}</span></div>
      <div class="mrow"><span class="mi">◷</span><span>{horario_display or "—"}</span></div>
      <div class="mrow addr"><span class="mi">⊞</span><span>{card["endereco"] or "—"}</span></div>
    </div>
    <div class="card-mini-gauge">{mini}</div>
  </div>

  <div class="card-activities">
    <table class="atv-table">
      <thead><tr>
        <th style="width:34px">#</th>
        <th>Disciplina</th>
        <th>Atividade / Descrição</th>
        <th style="width:46px">Peso</th>
        <th style="width:95px">Status</th>
        <th style="width:86px">Conclusão</th>
      </tr></thead>
      <tbody>{atv_rows}</tbody>
    </table>
  </div>
</div>'''

# ── Full HTML ─────────────────────────────────────────────────────────────────
def generate_html(cards, kpis, otz_b64):
    today_str = TODAY.strftime("%d/%m/%Y")
    k = kpis

    otz_img = (f'<img src="data:image/png;base64,{otz_b64}" class="logo-otz" alt="OTZ/GPLAN">'
               if otz_b64 else '<div class="logo-fallback">OTZ<br>GPLAN</div>')

    messer_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 68" class="logo-messer">
  <text x="0" y="44" font-family="'Arial Black',Arial,sans-serif"
        font-size="42" font-weight="900" fill="#1A3680">MESSER</text>
  <circle cx="196" cy="22" r="20" fill="none" stroke="#CC2020" stroke-width="2.5"/>
  <rect x="190" y="8"  width="12" height="28" rx="3" fill="#CC2020"/>
  <rect x="183" y="15" width="26" height="14" rx="3" fill="#CC2020"/>
  <circle cx="196" cy="22" r="5.5" fill="white"/>
  <text x="0" y="64" font-family="Arial,sans-serif" font-size="15"
        fill="#CC2020" font-style="italic">Gases for Life</text>
</svg>'''

    global_gauge = gauge_svg(k["pct"], k["done_atv"], k["tot_atv"], "global")
    disc_chart   = discipline_chart_svg(k["disc_stats"])
    curva_chart  = curvas_svg(k["done_atv"], k["tot_atv"])

    def kbox(icon, lbl, val, color="#00BCD4", sub=""):
        sub_h = f'<div class="kpi-sub">{sub}</div>' if sub else ""
        return (f'<div class="kpi-box"><div class="kpi-icon" style="color:{color}">{icon}</div>'
                f'<div class="kpi-val" style="color:{color}">{val}</div>'
                f'<div class="kpi-lbl">{lbl}</div>{sub_h}</div>')

    # Defasagem Curva-S
    def_val = k["defasagem"]
    if def_val > 0:
        def_str   = f'−{def_val:.1f} pp'
        def_color = "#FF5252"
        def_sub   = f'Prev: {k["prev_pct"]:.0f}% / Real: {k["pct"]:.1f}%'
    else:
        def_str   = f'+{abs(def_val):.1f} pp'
        def_color = "#00E676"
        def_sub   = f'Adiantado — Prev: {k["prev_pct"]:.0f}%'

    kpi_boxes = "".join([
        kbox("⊞","Locais / Cards",   str(k["tot_cards"]),  "#00BCD4"),
        kbox("≡","Total Atividades", str(k["tot_atv"]),     "#29B6F6"),
        kbox("✓","Concluídas",       str(k["done_atv"]),    "#00E676"),
        kbox("○","Pendentes",        str(k["pend_atv"]),    "#FFC107"),
        kbox("📉","Defasagem Curva-S", def_str, def_color, def_sub),
        kbox("⏱","Dias em Aberto",   str(k["dias_aberto"]), "#B0BEC5",
             f'úteis desde {PROJECT_START.strftime("%d/%m/%Y")}'),
    ])
    if k["velocidade"]:
        kpi_boxes += kbox("⚡","Velocidade", f'{k["velocidade"]:.2f} atv/dia', "#69F0AE")

    area_opts = "".join(f'<option value="{a}">{a}</option>' for a in k["areas"])
    disc_opts = "".join(f'<option value="{d}">{d}</option>' for d in k["discs"])

    cards_html = "\n".join(html_card(c) for c in cards)
    total_cards = len(cards)

    return f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>PUSH LIST — DAENG | ASU Jundiaí (26001) — REV3</title>
<style>
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
body{{background:#0A1628;color:#C8D8F0;font-family:'Segoe UI',Arial,sans-serif;
     font-size:14px;line-height:1.45;min-height:100vh}}

.site-header{{background:linear-gradient(135deg,#0A1628 0%,#0D2540 40%,#0A1628 100%);
              border-bottom:2px solid #00BCD4}}
.header-top{{display:flex;align-items:center;gap:16px;padding:14px 20px}}
.logo-otz{{height:66px;width:auto;filter:drop-shadow(0 0 6px #00BCD440)}}
.logo-fallback{{background:#0D2540;border:1px solid #00BCD4;border-radius:6px;
                padding:6px 12px;font-size:11px;font-weight:700;color:#00BCD4;text-align:center}}
.logo-messer{{height:54px;width:auto}}
.header-title{{flex:1;text-align:center}}
.header-title h1{{font-size:20px;color:#00BCD4;letter-spacing:1.5px;text-transform:uppercase;
                  text-shadow:0 0 16px #00BCD480}}
.header-title .sub{{font-size:12px;color:#7BAFD4;margin-top:3px}}
.header-refbar{{background:#06101E;border-top:1px solid #1A3A60;padding:8px 20px;
                font-size:10.5px;color:#4A90D9;display:flex;flex-wrap:wrap;gap:8px;align-items:center}}
.rpill{{background:#0D1F3C;border:1px solid #1A3A60;border-radius:4px;padding:2px 8px;white-space:nowrap}}
.rpill.doc{{border-color:#00BCD440;color:#29B6F6;font-weight:600}}

.kpi-section{{background:linear-gradient(180deg,#06101E,#0A1628);
              border-bottom:1px solid #1A3A60;padding:16px 20px}}
.sec-title{{font-size:11px;color:#4A90D9;letter-spacing:2px;text-transform:uppercase;margin-bottom:12px}}
.kpi-top{{display:flex;gap:14px;align-items:stretch;flex-wrap:wrap;margin-bottom:14px}}
.kpi-boxes{{display:flex;flex-wrap:wrap;gap:10px;flex:1}}
.kpi-box{{background:#0D1F3C;border:1px solid #1A3A60;border-radius:8px;padding:12px 14px;
          min-width:110px;flex:1;text-align:center;transition:transform .2s,box-shadow .2s}}
.kpi-box:hover{{transform:translateY(-2px);box-shadow:0 4px 16px #00BCD420}}
.kpi-icon{{font-size:20px;margin-bottom:5px}}
.kpi-val{{font-size:22px;font-weight:700;line-height:1.1}}
.kpi-lbl{{font-size:10.5px;color:#7BAFD4;margin-top:4px;text-transform:uppercase;letter-spacing:.8px}}
.kpi-sub{{font-size:10px;color:#4A90D9;margin-top:2px}}
.gauge-wrap{{background:#0D1F3C;border:1px solid #1A3A60;border-radius:8px;
             padding:12px;display:flex;align-items:center;justify-content:center;flex-shrink:0}}
.disc-panel{{background:#0D1F3C;border:1px solid #1A3A60;border-radius:8px;padding:14px 16px}}
.disc-panel-title{{font-size:10.5px;color:#4A90D9;letter-spacing:1.5px;text-transform:uppercase;
                   margin-bottom:10px}}
.curvas-panel{{background:#0D1F3C;border:1px solid #1A3A60;border-radius:8px;padding:14px 16px}}
.curvas-panel-title{{font-size:10.5px;color:#4A90D9;letter-spacing:1.5px;text-transform:uppercase;
                     margin-bottom:10px}}

.filter-bar{{background:#06101E;border-bottom:1px solid #1A3A60;
             padding:10px 20px;display:flex;flex-wrap:wrap;gap:10px;align-items:center}}
.filter-lbl{{font-size:10.5px;color:#4A90D9;font-weight:600;letter-spacing:1px;
             text-transform:uppercase;white-space:nowrap}}
.filter-select{{background:#0D1F3C;border:1px solid #1A3A60;color:#C8D8F0;
                border-radius:5px;padding:5px 10px;font-size:12px;cursor:pointer;
                outline:none;min-width:160px}}
.filter-select:focus{{border-color:#00BCD4}}
.filter-input{{background:#0D1F3C;border:1px solid #1A3A60;color:#C8D8F0;
               border-radius:5px;padding:5px 12px;font-size:12px;outline:none;
               min-width:200px;flex:1}}
.filter-input::placeholder{{color:#2A4A70}}
.filter-input:focus{{border-color:#00BCD4}}
.btn-clear{{background:#1A3A60;border:none;color:#7BAFD4;border-radius:5px;
            padding:5px 14px;font-size:12px;cursor:pointer;transition:background .2s}}
.btn-clear:hover{{background:#00BCD4;color:#0A1628}}
.filter-count{{font-size:11px;color:#4A90D9;white-space:nowrap;margin-left:auto}}

.cards-section{{padding:16px 20px}}
.sec-header{{font-size:11px;color:#4A90D9;letter-spacing:2px;text-transform:uppercase;
             margin-bottom:14px;display:flex;align-items:center;gap:8px}}
.sec-header::after{{content:'';flex:1;height:1px;background:linear-gradient(90deg,#1A3A60,transparent)}}
.cards-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(700px,1fr));gap:18px}}

.push-card{{background:#0D1F3C;border:1px solid #1A3A60;border-radius:10px;
            overflow:hidden;transition:box-shadow .25s}}
.push-card:hover{{box-shadow:0 4px 28px #00BCD428}}
.push-card[style*="display:none"]{{display:none!important}}

.card-hbar{{display:flex;align-items:center;gap:9px;padding:9px 16px;
            border-bottom:1px solid #1A3A6060}}
.cid-badge{{background:#00BCD4;color:#0A1628;font-size:11px;font-weight:700;
            border-radius:4px;padding:3px 9px;white-space:nowrap;letter-spacing:.5px}}
.cloc-badge{{background:#1A3A60;color:#7BAFD4;font-size:11px;border-radius:4px;
             padding:3px 9px;white-space:nowrap}}
.cnome{{flex:1;font-size:15px;font-weight:700;color:#D8E8FF;
        white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}
.cpct{{font-size:16px;font-weight:700;white-space:nowrap;margin-right:4px}}
.cstats{{display:flex;gap:5px}}
.sb{{font-size:11px;border-radius:4px;padding:2px 8px;font-weight:600}}
.sb.done{{background:#003020;color:#00E676;border:1px solid #00E67640}}
.sb.pend{{background:#302000;color:#FFC107;border:1px solid #FFC10740}}

.card-photos-row{{display:grid;grid-template-columns:1fr 1fr;border-bottom:1px solid #1A3A60}}
.photo-col{{display:flex;flex-direction:column}}
.photo-label{{font-size:10px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;
              padding:5px 12px;}}
.antes-lbl{{background:#06101E;color:#00BCD4;border-bottom:1px solid #1A3A60;
            border-right:1px solid #1A3A60}}
.pos-lbl{{background:#06101E;color:#E65100;border-bottom:1px solid #1A3A60}}
.photo-wrap{{position:relative;height:240px;background:#050F1A;overflow:hidden;flex:1}}
.photo-col:first-child .photo-wrap{{border-right:1px solid #1A3A60}}
.card-photo{{width:100%;height:100%;object-fit:cover;display:block}}
.photo-ph{{width:100%;height:100%;display:flex;flex-direction:column;
           align-items:center;justify-content:center;gap:6px;color:#2A4A70}}
.pos-ph{{background:#050A12;border:none}}
.ph-icon{{font-size:28px;opacity:.45}}
.ph-lbl{{font-size:12px;font-weight:600;color:#2A5070}}
.ph-sub{{font-size:10.5px;color:#1A3A55}}
.photo-badge{{position:absolute;bottom:8px;right:8px;background:#00000090;color:#00BCD4;
              font-size:10px;border-radius:4px;padding:2px 7px;backdrop-filter:blur(4px)}}
.area-overlay{{position:absolute;top:8px;left:8px;background:#00000085;color:#D8E8FF;
               font-size:11px;font-weight:600;border-radius:4px;padding:3px 9px;
               backdrop-filter:blur(4px);max-width:65%;
               white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}

.card-info-row{{display:flex;align-items:center;border-bottom:1px solid #1A3A60;
                background:#070F1C}}
.card-meta{{flex:1;padding:10px 16px;font-size:12px;color:#7BAFD4;
            display:flex;flex-direction:column;gap:6px}}
.mrow{{display:flex;align-items:flex-start;gap:7px}}
.mi{{color:#00BCD4;min-width:15px;flex-shrink:0;font-size:13px}}
.addr{{font-size:11px;color:#4A90D9;line-height:1.35}}
.card-mini-gauge{{padding:8px 12px 8px 0;flex-shrink:0}}

.card-activities{{overflow-x:auto}}
.atv-table{{width:100%;border-collapse:collapse;font-size:13px}}
.atv-table thead tr{{background:#06101E;border-bottom:2px solid #00BCD430}}
.atv-table th{{padding:7px 9px;color:#4A90D9;font-size:11px;font-weight:600;
               text-transform:uppercase;letter-spacing:.5px;text-align:left}}
.atv-table tbody tr{{border-bottom:1px solid #0F2040}}
.atv-table tbody tr:hover{{background:#0A2040}}
.atv-row.concluido{{background:#020A04}}
.atv-num{{padding:8px 9px;color:#4A90D9;font-weight:600;text-align:center;white-space:nowrap;font-size:13px}}
.atv-disc{{padding:8px 9px;color:#C8D8F0;font-size:12px;white-space:nowrap}}
.ddot{{display:inline-block;width:8px;height:8px;border-radius:50%;margin-right:6px;vertical-align:middle}}
.atv-desc{{padding:8px 9px;color:#B0C8E8;line-height:1.4;font-size:13px}}
.atv-peso{{padding:8px 7px;text-align:center}}
.pbadge{{display:inline-block;width:24px;height:24px;line-height:24px;text-align:center;
         border-radius:50%;font-weight:700;font-size:12px;border:2px solid;color:#C8D8F0}}
.atv-status{{padding:8px 9px;font-size:12px;font-weight:600;white-space:nowrap}}
.atv-status.pendente{{color:#FFC107}}
.atv-status.concluido{{color:#00E676}}
.atv-date{{padding:8px 9px;font-size:12px;color:#4A90D9;white-space:nowrap}}

.site-footer{{background:#06101E;border-top:2px solid #00BCD430;padding:14px 20px;
              display:flex;justify-content:space-between;align-items:center;
              flex-wrap:wrap;gap:8px;font-size:11px;color:#4A90D9}}
.footer-by{{color:#7BAFD4;font-style:italic}}
.footer-rev{{background:#0D1F3C;border:1px solid #1A3A60;border-radius:4px;
             padding:3px 10px;font-weight:600;color:#00BCD4}}

::-webkit-scrollbar{{width:6px;height:6px}}
::-webkit-scrollbar-track{{background:#060E1C}}
::-webkit-scrollbar-thumb{{background:#1A3A60;border-radius:3px}}
::-webkit-scrollbar-thumb:hover{{background:#00BCD4}}

@media(max-width:720px){{
  .cards-grid{{grid-template-columns:1fr}}
  .card-photos-row{{grid-template-columns:1fr}}
  .kpi-top{{flex-direction:column}}
  .card-info-row{{flex-direction:column}}
  .card-mini-gauge{{width:100%;display:flex;justify-content:center;padding:6px 0}}
}}
</style>
</head>
<body>

<header class="site-header">
  <div class="header-top">
    {otz_img}
    <div class="header-title">
      <h1>Push List — Serviços DAENG</h1>
      <div class="sub">ASU Jundiaí (26001) &nbsp;|&nbsp; OTZ Engenharia × Messer Gases for Life</div>
    </div>
    {messer_svg}
  </div>
  <div class="header-refbar">
    <span class="rpill doc">P-DE-E-179-CIV18-000-003 — AIR SEPARATION UNIT MASTER PLAN | Terraplanagem — Planta | OTZ PGE | Aprov.: RNW | 19/08/25</span>
    <span class="rpill">Ref: CLM-216</span>
    <span class="rpill">Contratada: Andrade e Rocha (DAENG)</span>
    <span class="rpill">Gerenciadora: OTZ Engenharia — GPLAN</span>
    <span class="rpill">Levantamento: {LEVAN_DATE.strftime("%d/%m/%Y")}</span>
    <span class="rpill">Elaborado por: Caio Sergio Bento da Silva &amp; Ilson do Santos Azevedo</span>
    <span class="rpill" style="color:#00BCD4;font-weight:600">REV3 — {today_str}</span>
  </div>
</header>

<section class="kpi-section">
  <div class="sec-title">&#9670; Indicadores Gerais</div>
  <div class="kpi-top">
    <div class="kpi-boxes">{kpi_boxes}</div>
    <div class="gauge-wrap">{global_gauge}</div>
  </div>

  <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px">
    <div class="disc-panel">
      <div class="disc-panel-title">&#9670; Atividades por Disciplina — Avanço Físico</div>
      {disc_chart}
    </div>
    <div class="curvas-panel">
      <div class="curvas-panel-title">&#9670; Curva-S — Previsto × Realizado</div>
      {curva_chart}
    </div>
  </div>
</section>

<div class="filter-bar">
  <span class="filter-lbl">Área</span>
  <select class="filter-select" id="f-area" onchange="applyFilters()">
    <option value="">Todas</option>
    {area_opts}
  </select>
  <span class="filter-lbl">Disciplina</span>
  <select class="filter-select" id="f-disc" onchange="applyFilters()">
    <option value="">Todas</option>
    {disc_opts}
  </select>
  <span class="filter-lbl">Status</span>
  <select class="filter-select" id="f-status" onchange="applyFilters()" style="min-width:120px">
    <option value="">Todos</option>
    <option value="Pendente">Pendente</option>
    <option value="Concluída">Concluída</option>
  </select>
  <span class="filter-lbl">Busca</span>
  <input class="filter-input" id="f-busca" type="text"
         placeholder="Pesquisar atividade..." oninput="applyFilters()">
  <button class="btn-clear" onclick="clearFilters()">Limpar</button>
  <span class="filter-count" id="filter-count">{total_cards} de {total_cards} cards</span>
</div>

<section class="cards-section">
  <div class="sec-header">
    &#9670; Locais de Serviço &nbsp;·&nbsp; {total_cards} cards &nbsp;·&nbsp;
    {k["tot_atv"]} atividades
  </div>
  <div class="cards-grid" id="cards-grid">
    {cards_html}
  </div>
</section>

<footer class="site-footer">
  <div class="footer-by">Elaborado por: Ilson do Santos Azevedo / Supervisor de Planejamento</div>
  <div>Projeto ASU Jundiaí (26001) &nbsp;|&nbsp; OTZ Engenharia × Messer Gases for Life</div>
  <div class="footer-rev">REV3 &nbsp;·&nbsp; {today_str}</div>
</footer>

<script>
const TOTAL = {total_cards};

function applyFilters() {{
  const fA = document.getElementById('f-area').value;
  const fD = document.getElementById('f-disc').value;
  const fS = document.getElementById('f-status').value;
  const fB = document.getElementById('f-busca').value.toLowerCase().trim();
  let vis = 0;
  document.querySelectorAll('.push-card').forEach(card => {{
    let show = true;
    if (fA && card.dataset.area !== fA) show = false;
    if (fD && !JSON.parse(card.dataset.discs||'[]').includes(fD)) show = false;
    if (fS && !JSON.parse(card.dataset.statuses||'[]').includes(fS)) show = false;
    if (fB && !(card.dataset.text||'').toLowerCase().includes(fB)) show = false;
    card.style.display = show ? '' : 'none';
    if (show) vis++;
  }});
  document.getElementById('filter-count').textContent = vis + ' de ' + TOTAL + ' cards';
}}

function clearFilters() {{
  ['f-area','f-disc','f-status'].forEach(id => document.getElementById(id).value='');
  document.getElementById('f-busca').value='';
  applyFilters();
}}
</script>
</body>
</html>'''

# ── Excel ─────────────────────────────────────────────────────────────────────
def generate_xlsx(cards):
    wb = openpyxl.Workbook(); ws = wb.active; ws.title="Push List REV3"
    ws.sheet_properties.tabColor = "1565C0"

    C_TITLE  = "1A3A6A"; C_SUBTIT = "D6E4F7"; C_HEADER = "1E4D99"
    C_ODD    = "FFFFFF"; C_EVEN   = "EEF4FF"; C_TEXT   = "1A2A40"; C_MUTED  = "5A7090"

    def sc(cell,bold=False,bg=None,fg=C_TEXT,sz=10,wrap=False,ha="left",va="center"):
        cell.font=Font(bold=bold,color=fg,size=sz,name="Calibri")
        cell.alignment=Alignment(horizontal=ha,vertical=va,wrap_text=wrap)
        if bg: cell.fill=PatternFill("solid",fgColor=bg)

    thin = Side(style="thin",   color="BDD0E8")
    med  = Side(style="medium", color="1E4D99")
    brd  = Border(left=thin, right=thin, top=thin, bottom=thin)
    brd_m= Border(left=med,  right=med,  top=med,  bottom=med)

    # Linha 1 — título
    ws.merge_cells("A1:L1"); c=ws["A1"]
    c.value="PUSH LIST — SERVIÇOS DAENG | ASU JUNDIAÍ (26001) | OTZ Engenharia × Messer Gases for Life"
    sc(c,bold=True,bg=C_TITLE,fg="FFFFFF",sz=13,ha="center")
    ws.row_dimensions[1].height=22

    # Linha 2 — subtítulo
    ws.merge_cells("A2:L2"); c=ws["A2"]
    c.value=(f"Ref: CLM-216  |  Contratada: Andrade e Rocha (DAENG)  |  "
             f"Gerenciadora: OTZ Engenharia — GPLAN  |  "
             f"Levantamento: {LEVAN_DATE.strftime('%d/%m/%Y')}  |  REV3 — {TODAY.strftime('%d/%m/%Y')}  |  "
             f"Elaborado por: Ilson do Santos Azevedo / Supervisor de Planejamento")
    sc(c,bg=C_SUBTIT,fg=C_TITLE,sz=9,ha="center")
    ws.row_dimensions[2].height=16

    # Linha 3 — cabeçalhos (sem Previsão)
    headers = ["#Card","Área","Local Nº","Nome do Local","Foto","# Ativ.",
               "Disciplina","Atividade / Descrição","Peso","Status","Conclusão","Avanço (%)"]
    for col,h in enumerate(headers,1):
        c=ws.cell(row=3,column=col,value=h)
        sc(c,bold=True,bg=C_HEADER,fg="FFFFFF",sz=10,ha="center"); c.border=brd_m
    ws.row_dimensions[3].height=18

    for i,w in enumerate([8,30,10,34,8,8,22,52,7,14,12,12],1):
        ws.column_dimensions[get_column_letter(i)].width=w
    ws.freeze_panes="A4"

    rn=4
    for card in cards:
        n=len(card["atividades"]); r0=rn
        for a in card["atividades"]:
            row_bg = C_ODD if rn%2==0 else C_EVEN
            st = (a["status"] or "").strip().lower()
            is_done   = st.startswith("conclu")
            is_active = any(k in st for k in ("anda","execu","progresso"))
            vals=[card["id"],card["area"],card["local_num"],card["nome"],
                  card["foto_seq"] if card["foto_seq"]>0 else "S/F",
                  a["num"],a["disciplina"],a["descricao"],a["peso"],a["status"],
                  a.get("conclusao","") or "",f'{card["pct"]:.1f}%']
            for col,v in enumerate(vals,1):
                c=ws.cell(row=rn,column=col,value=v)
                if col == 10:  # Status
                    if is_done:
                        sc(c,bold=True,bg="C8F0D8",fg="1A5E30",sz=10,ha="center")
                    elif is_active:
                        sc(c,bold=True,bg="FFF3CD",fg="7B4F00",sz=10,ha="center")
                    else:
                        sc(c,bg=row_bg,fg=C_MUTED,sz=10,ha="center")
                elif col == 12:  # Avanço (%)
                    pct_v = card["pct"]
                    p_fg = "1A5E30" if pct_v>=66 else "7B4F00" if pct_v>0 else C_MUTED
                    p_bg = "C8F0D8" if pct_v>=66 else "FFF3CD" if pct_v>0 else row_bg
                    sc(c,bold=(pct_v>0),bg=p_bg,fg=p_fg,sz=10,ha="center")
                else:
                    sc(c,bg=row_bg,fg=C_TEXT,sz=10,wrap=(col==8),
                       ha="center" if col in(1,3,5,6,9,11) else "left")
                c.border=brd
            ws.row_dimensions[rn].height=30 if len(str(a["descricao"]))>70 else 16
            rn+=1
        if n>1:
            for col in(1,2,3,4,5,12):
                try:
                    ws.merge_cells(start_row=r0,start_column=col,end_row=rn-1,end_column=col)
                    ws.cell(r0,col).alignment=Alignment(
                        horizontal="center",vertical="center",wrap_text=(col in(2,4)))
                except: pass
    wb.save(XLSX_OUT)
    print(f"  Excel: {XLSX_OUT}")

# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    print("="*60)
    print("PUSH LIST REV3 — ASU Jundiaí (26001)")
    print(f"Data referência: {TODAY.strftime('%d/%m/%Y')} | Dia {TODAY_IDX+1}/{N_DAYS} úteis")
    print("="*60)
    print("\n[1] Reading Excel …")
    card_data = read_excel(); print(f"    {len(card_data)} card keys")
    print("\n[2] Building cards (regulares + CFTV do Excel) …")
    cards, _ = build_cards(card_data); print(f"    {len(cards)} cards")
    print("\n[4] KPIs …")
    kpis = compute_kpis(cards)
    print(f"    Avanço físico: {kpis['pct']:.1f}%  |  "
          f"Previsto: {kpis['prev_pct']:.0f}%  |  "
          f"Defasagem: {kpis['defasagem']:.1f} pp")
    print("\n[5] OTZ logo …")
    otz_b64 = load_otz_logo(); print(f"    {'OK' if otz_b64 else 'not found'}")
    print("\n[6] Generating HTML …")
    html = generate_html(cards, kpis, otz_b64)
    with open(HTML_OUT,"w",encoding="utf-8") as f: f.write(html)
    print(f"    {HTML_OUT}  ({os.path.getsize(HTML_OUT)/1024/1024:.1f} MB)")
    print("\n[7] Generating Excel …"); generate_xlsx(cards)
    print("\n✓ REV3 concluída")

if __name__ == "__main__":
    main()
