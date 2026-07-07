#!/usr/bin/env python3
"""Dashboard LD — Lista de Documentos E-179 | OTZ Engenharia × Messer Gases for Life"""

import os, math, json
from datetime import date, datetime
from collections import defaultdict

import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# ── Paths ─────────────────────────────────────────────────────────────────────
ROOT     = os.path.dirname(os.path.abspath(__file__))
UPLOAD   = "/root/.claude/uploads/001b7fb0-8857-54b0-9eb5-28053bfc3f61"
EXCEL_IN = os.path.join(UPLOAD, "c958f4f8-PLDE179PLA340000010_2026.07.07_REPLAN.xlsx")
HTML_OUT = os.path.join(ROOT, "OTZ_E179_LISTA_DOCUMENTOS.html")
# JSON que guarda histórico de documentos finalizados (regra: não remover)
FINALIZADOS_JSON = os.path.join(ROOT, "ld_finalizados.json")

TODAY     = date.today()
TODAY_STR = TODAY.strftime("%d/%m/%Y")
LD_DATA   = "07/07/2026"

# ── Cores por disciplina ───────────────────────────────────────────────────────
DISC_COLOR = {
    "CIVIL":                       "#5D8AA8",
    "ELÉTRICA":                    "#1565C0",
    "INFRAESTRUTURA":              "#2E7D32",
    "ESTRUTURA METÁLICA":          "#546E7A",
    "ARQUITETURA":                 "#AD1457",
    "INSTRUMENTAÇÃO":              "#00838F",
    "ARRUAMENTO / PAVIMENTAÇÃO":   "#6D4C41",
    "HVAC":                        "#F57F17",
    "TELECOMUNICAÇÃO":             "#4527A0",
    "MECÂNICA":                    "#BF360C",
    "TUBULAÇÃO":                   "#1B5E20",
    "AUTOMAÇÃO":                   "#006064",
    "GESTÃO":                      "#880E4F",
    "GERAL":                       "#37474F",
    "PROCESSO":                    "#0D47A1",
    "RESISTIVIDADE DO SOLO":       "#3E2723",
    "PLANEJAMENTO":                "#1A237E",
}
DEF_DISC_COLOR = "#546E7A"

# ── Cores por status ───────────────────────────────────────────────────────────
STATUS_COLOR = {
    "DOC. FINALIZADO":        "#00E676",
    "EMITIR EMISSÃO INICIAL": "#FF7043",
    "AGUARDANDO MARKUP":      "#FFC107",
    "ATENDER MARKUP":         "#FF1744",
    "PATEC EMITIDO":          "#CE93D8",
    "NÃO NECESSÁRIO":         "#546E7A",
}
STATUS_ORDER = {
    "ATENDER MARKUP":         0,
    "AGUARDANDO MARKUP":      1,
    "EMITIR EMISSÃO INICIAL": 2,
    "PATEC EMITIDO":          3,
    "DOC. FINALIZADO":        4,
    "NÃO NECESSÁRIO":         5,
}

def status_color(st):
    return STATUS_COLOR.get(str(st).strip().upper(), "#4A90D9")

def status_order(st):
    return STATUS_ORDER.get(str(st).strip().upper(), 99)

def safe_float(v):
    try: return float(v)
    except: return 0.0

def fmt_date(v):
    if v is None: return "—"
    if isinstance(v, (datetime, date)):
        return v.strftime("%d/%m/%Y") if isinstance(v, datetime) else v.strftime("%d/%m/%Y")
    return str(v)

# ── Ler Excel ─────────────────────────────────────────────────────────────────
def read_ld():
    wb = openpyxl.load_workbook(EXCEL_IN, data_only=True)
    ws = wb["LD"]
    # Cabeçalho na linha 8; dados a partir da linha 9
    COLS = {
        "disc":0, "subdisc":1, "area":2, "num_doc":3, "titulo":4, "rev":5, "tipo":6,
        "id_exc":7, "id_1em":8, "base_1em":9, "id_final":10, "base_ult":11,
        "data_1em":12, "fin_1em":13, "grd_1em":14,
        "data_atual":15, "fin_atual":16, "grd_atual":17,
        "horas":18, "peso":19, "avanco":20,
        "status_doc":21, "status_eclic":22, "status":23,
    }
    docs = []
    for row in ws.iter_rows(min_row=9, values_only=True):
        if not any(row): continue
        if not row[COLS["num_doc"]]: continue
        docs.append({k: row[v] for k,v in COLS.items()})
    return docs

# ── Regra: finalizados fixos ───────────────────────────────────────────────────
def load_finalizados():
    if os.path.exists(FINALIZADOS_JSON):
        with open(FINALIZADOS_JSON) as f:
            return set(json.load(f).get("numeros", []))
    return set()

def save_finalizados(docs):
    nums = [d["num_doc"] for d in docs
            if str(d.get("status","")).strip().upper() == "DOC. FINALIZADO"]
    with open(FINALIZADOS_JSON, "w") as f:
        json.dump({"numeros": sorted(nums), "atualizado": TODAY_STR}, f, indent=2, ensure_ascii=False)

# ── Agrupar por disciplina ─────────────────────────────────────────────────────
def build_cards(docs):
    # Apenas ATIVO + NÃO NECESSÁRIO mantido se finalizado no histórico
    finalizados_hist = load_finalizados()
    save_finalizados(docs)

    ativos = [d for d in docs if str(d.get("status_doc","")).strip().upper() in ("ATIVO",)]

    groups = defaultdict(list)
    for d in ativos:
        disc = (d["disc"] or "S/D").strip()
        groups[disc].append(d)

    cards = []
    disc_order = sorted(groups.keys(),
        key=lambda x: -sum(safe_float(d["peso"]) for d in groups[x]))

    for disc in disc_order:
        ddocs = sorted(groups[disc], key=lambda d: status_order(d["status"]))
        peso_tot  = sum(safe_float(d["peso"]) for d in ddocs)
        avanco_w  = sum(safe_float(d["peso"])*safe_float(d["avanco"]) for d in ddocs)
        pct       = (avanco_w/peso_tot*100) if peso_tot else 0
        finais    = sum(1 for d in ddocs if str(d.get("status","")).strip().upper()=="DOC. FINALIZADO")
        pendentes = len(ddocs) - finais
        color     = DISC_COLOR.get(disc, DEF_DISC_COLOR)
        cards.append({
            "disc": disc, "color": color, "docs": ddocs,
            "total": len(ddocs), "finais": finais, "pendentes": pendentes,
            "pct": pct, "peso": peso_tot,
        })
    return cards

# ── KPIs globais ───────────────────────────────────────────────────────────────
def compute_kpis(cards):
    all_docs  = [d for c in cards for d in c["docs"]]
    tot       = len(all_docs)
    finais    = sum(1 for d in all_docs if str(d.get("status","")).strip().upper()=="DOC. FINALIZADO")
    pend      = tot - finais
    peso_tot  = sum(safe_float(d["peso"]) for d in all_docs)
    avanco_w  = sum(safe_float(d["peso"])*safe_float(d["avanco"]) for d in all_docs)
    pct       = (avanco_w/peso_tot*100) if peso_tot else 0
    # por status pendente
    st_count  = defaultdict(int)
    for d in all_docs:
        st = str(d.get("status","")).strip()
        if st.upper() != "DOC. FINALIZADO":
            st_count[st] += 1
    # disciplina mais crítica (mais pendentes)
    crit = max(cards, key=lambda c: c["pendentes"]) if cards else None
    return {
        "tot": tot, "finais": finais, "pend": pend,
        "pct": pct, "peso": peso_tot,
        "n_discs": len(cards),
        "st_count": dict(st_count),
        "crit_disc": crit["disc"] if crit else "—",
        "crit_pend": crit["pendentes"] if crit else 0,
    }

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
    sw  = 16 if not mini else 12

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
        f'font-weight="bold" font-family="Arial,sans-serif">{pct:.1f}%</text>',
        f'<text x="{cx}" y="{cy+41}" text-anchor="middle" fill="#00BCD4" font-size="{sub_sz}" '
        f'font-family="Arial,sans-serif">AVANÇO FÍSICO</text>',
    ]
    if not mini:
        pend_i = int(total_cnt) - int(done_cnt)
        s += [
            f'<line x1="{cx-62}" y1="{cy+50}" x2="{cx+62}" y2="{cy+50}" stroke="#1A3A60" stroke-width="0.8"/>',
            f'<text x="{cx-52}" y="{cy+63}" text-anchor="middle" fill="#00E676" font-size="11" font-weight="bold" font-family="Arial,sans-serif">{int(done_cnt)}</text>',
            f'<text x="{cx-52}" y="{cy+74}" text-anchor="middle" fill="#4A90D9" font-size="7" font-family="Arial,sans-serif">FINAL.</text>',
            f'<text x="{cx}" y="{cy+63}" text-anchor="middle" fill="#FFC107" font-size="11" font-weight="bold" font-family="Arial,sans-serif">{pend_i}</text>',
            f'<text x="{cx}" y="{cy+74}" text-anchor="middle" fill="#4A90D9" font-size="7" font-family="Arial,sans-serif">PEND.</text>',
            f'<text x="{cx+52}" y="{cy+63}" text-anchor="middle" fill="#29B6F6" font-size="11" font-weight="bold" font-family="Arial,sans-serif">{int(total_cnt)}</text>',
            f'<text x="{cx+52}" y="{cy+74}" text-anchor="middle" fill="#4A90D9" font-size="7" font-family="Arial,sans-serif">TOTAL</text>',
        ]
    s.append('</svg>')
    return "\n".join(s)

# ── Gráfico disciplinas ────────────────────────────────────────────────────────
def discipline_chart_svg(cards):
    RH = 34; LW = 190; BW = 280; SW = 110; PAD = 16
    W  = LW + BW + SW + PAD*2
    H  = len(cards)*RH + PAD*2
    mx = max(c["total"] for c in cards) or 1

    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
         f'width="100%" preserveAspectRatio="xMidYMid meet">']
    for i, c in enumerate(cards):
        y   = PAD + i*RH
        ym  = y + RH//2
        bw  = max(4, int(BW * c["total"] / mx))
        fw  = int(bw * c["pct"] / 100)
        color = c["color"]
        sx  = PAD + LW + bw + 8

        s += [
            f'<text x="{PAD}" y="{ym}" dominant-baseline="middle" fill="#C8D8F0" '
            f'font-size="11" font-family="Arial,sans-serif" '
            f'style="white-space:nowrap;overflow:hidden;text-overflow:ellipsis">'
            f'{c["disc"][:28]}</text>',
            f'<rect x="{PAD+LW}" y="{y+6}" width="{bw}" height="{RH-12}" '
            f'fill="{color}22" stroke="{color}44" stroke-width="1" rx="2"/>',
        ]
        if fw > 0:
            s.append(f'<rect x="{PAD+LW}" y="{y+6}" width="{fw}" height="{RH-12}" '
                     f'fill="{color}" opacity="0.85" rx="2"/>')
        s += [
            f'<text x="{sx}" y="{ym}" dominant-baseline="middle" fill="{color}" '
            f'font-size="11" font-weight="bold" font-family="Arial,sans-serif">'
            f'{c["pct"]:.0f}%</text>',
            f'<text x="{sx+38}" y="{ym}" dominant-baseline="middle" fill="#4A90D9" '
            f'font-size="10" font-family="Arial,sans-serif">'
            f'{c["finais"]}/{c["total"]} docs</text>',
        ]
    s.append('</svg>')
    return "\n".join(s)

# ── Card HTML por disciplina ───────────────────────────────────────────────────
def html_doc_row(d, idx):
    st   = str(d.get("status","")).strip()
    col  = status_color(st)
    is_f = st.upper() == "DOC. FINALIZADO"
    cls  = "doc-row finalizado" if is_f else "doc-row pendente"
    rev  = d["rev"] if d["rev"] not in (None, "", "N/A") else "—"
    tipo = d["tipo"] if d["tipo"] not in (None, "", "N/A") else "—"
    fin  = (d["fin_atual"] or d["fin_1em"] or "")
    fin  = str(fin).strip() if fin else "—"
    data = fmt_date(d["data_atual"]) if d["data_atual"] else fmt_date(d["data_1em"])

    return f'''<tr class="{cls}">
  <td class="doc-num">{d["num_doc"] or "—"}</td>
  <td class="doc-titulo">{d["titulo"] or "—"}</td>
  <td class="doc-centro">{rev}</td>
  <td class="doc-centro">{tipo}</td>
  <td class="doc-centro">{data}</td>
  <td class="doc-fin">{fin}</td>
  <td class="doc-status" style="color:{col};border-left:3px solid {col}">
    <span class="st-dot" style="background:{col}"></span>{st}
  </td>
</tr>'''

def html_card(card, idx):
    color = card["color"]
    pct_c = "#00E676" if card["pct"]>=80 else "#FFC107" if card["pct"]>=50 else "#F44336"
    rows  = "\n".join(html_doc_row(d, i) for i,d in enumerate(card["docs"]))
    pend_badge = (f'<span class="pend-badge">{card["pendentes"]} pendentes</span>'
                  if card["pendentes"] > 0 else "")

    # Data-attrs para filtro JS
    statuses_js = json.dumps(list({str(d.get("status","")).strip() for d in card["docs"]}))
    text_js = " ".join(
        f'{d["num_doc"] or ""} {d["titulo"] or ""}'.lower()
        for d in card["docs"]
    ).replace('"', '&quot;')

    return f'''
<div class="disc-card" id="card-{idx}"
  data-disc="{card["disc"].replace('"','&quot;')}"
  data-statuses='{statuses_js}'
  data-text="{text_js}">

  <div class="card-hbar" style="background:linear-gradient(135deg,{color}22,{color}40)">
    <span class="disc-badge" style="background:{color}20;border:1px solid {color}60;color:{color}">
      {card["disc"]}
    </span>
    {pend_badge}
    <span class="card-pct" style="color:{pct_c}">{card["pct"]:.1f}%</span>
    <span class="card-counts">
      <span class="cnt-ok">✓ {card["finais"]}</span>
      <span class="cnt-pend">◌ {card["pendentes"]}</span>
      <span class="cnt-tot">/ {card["total"]} docs</span>
    </span>
    <button class="btn-toggle" onclick="toggleFinal(this)">Ocultar finalizados</button>
  </div>

  <div class="card-table-wrap">
    <table class="doc-table">
      <thead><tr>
        <th style="width:200px">Número Documento</th>
        <th>Título</th>
        <th style="width:44px">Rev</th>
        <th style="width:44px">Tipo</th>
        <th style="width:92px">Data Emissão</th>
        <th style="width:170px">Finalidade</th>
        <th style="width:160px">Status</th>
      </tr></thead>
      <tbody>{rows}</tbody>
    </table>
  </div>
</div>'''

# ── HTML completo ──────────────────────────────────────────────────────────────
def generate_html(cards, kpis):
    k = kpis
    global_gauge = gauge_svg(k["pct"], k["finais"], k["tot"], "global")
    disc_chart   = discipline_chart_svg(cards)

    messer_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 68" class="logo-messer">
  <text x="0" y="44" font-family="'Arial Black',Arial,sans-serif"
        font-size="42" font-weight="900" fill="#1A3680">MESSER</text>
  <circle cx="196" cy="22" r="20" fill="none" stroke="#CC2020" stroke-width="2.5"/>
  <rect x="190" y="8" width="12" height="28" rx="3" fill="#CC2020"/>
  <rect x="183" y="15" width="26" height="14" rx="3" fill="#CC2020"/>
  <circle cx="196" cy="22" r="5.5" fill="white"/>
  <text x="0" y="64" font-family="Arial,sans-serif" font-size="15"
        fill="#CC2020" font-style="italic">Gases for Life</text>
</svg>'''

    def kbox(icon, lbl, val, color="#00BCD4", sub=""):
        sub_h = f'<div class="kpi-sub">{sub}</div>' if sub else ""
        return (f'<div class="kpi-box"><div class="kpi-icon" style="color:{color}">{icon}</div>'
                f'<div class="kpi-val" style="color:{color}">{val}</div>'
                f'<div class="kpi-lbl">{lbl}</div>{sub_h}</div>')

    kpi_boxes = "".join([
        kbox("⊞", "Total Documentos",   str(k["tot"]),    "#00BCD4"),
        kbox("✓", "Finalizados",         str(k["finais"]), "#00E676"),
        kbox("○", "Pendentes",           str(k["pend"]),   "#FFC107"),
        kbox("◈", "Disciplinas",         str(k["n_discs"]),"#29B6F6"),
    ])
    # Status pendentes detalhado
    for st, cnt in sorted(k["st_count"].items(), key=lambda x: -x[1]):
        col = status_color(st)
        kpi_boxes += kbox("▲", st.title(), str(cnt), col)

    # Crítico
    kpi_boxes += kbox("⚠", "Mais Crítica", k["crit_disc"],
                      "#FF5252", f'{k["crit_pend"]} pendentes')

    disc_opts = "".join(f'<option value="{c["disc"]}">{c["disc"]}</option>' for c in cards)
    all_statuses = sorted({str(d.get("status","")).strip()
                           for c in cards for d in c["docs"] if d.get("status")})
    st_opts = "".join(f'<option value="{s}">{s}</option>' for s in all_statuses)

    cards_html = "\n".join(html_card(c, i+1) for i,c in enumerate(cards))
    TOTAL = len(cards)

    return f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Lista de Documentos — E-179 ASU Jundiaí | OTZ Engenharia</title>
<style>
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
body{{background:#0A1628;color:#C8D8F0;font-family:'Segoe UI',Arial,sans-serif;
     font-size:13px;line-height:1.4;min-height:100vh}}

/* Header */
.site-header{{background:linear-gradient(135deg,#0A1628 0%,#0D2540 40%,#0A1628 100%);
              border-bottom:2px solid #00BCD4}}
.header-top{{display:flex;align-items:center;gap:16px;padding:14px 20px}}
.logo-otz-wrap{{background:#0D2540;border:1px solid #00BCD440;border-radius:8px;
                padding:8px 14px;font-size:13px;font-weight:700;color:#00BCD4;
                text-align:center;line-height:1.3}}
.logo-messer{{height:52px;width:auto}}
.header-title{{flex:1;text-align:center}}
.header-title h1{{font-size:20px;color:#00BCD4;letter-spacing:1.5px;text-transform:uppercase;
                  text-shadow:0 0 16px #00BCD480}}
.header-title .sub{{font-size:12px;color:#7BAFD4;margin-top:3px}}
.header-refbar{{background:#06101E;border-top:1px solid #1A3A60;padding:8px 20px;
                font-size:10.5px;color:#4A90D9;display:flex;flex-wrap:wrap;gap:8px;align-items:center}}
.rpill{{background:#0D1F3C;border:1px solid #1A3A60;border-radius:4px;padding:2px 8px;white-space:nowrap}}
.rpill.doc{{border-color:#00BCD440;color:#29B6F6;font-weight:600}}

/* KPI section */
.kpi-section{{background:linear-gradient(180deg,#06101E,#0A1628);
              border-bottom:1px solid #1A3A60;padding:16px 20px}}
.sec-title{{font-size:11px;color:#4A90D9;letter-spacing:2px;text-transform:uppercase;margin-bottom:12px}}
.kpi-top{{display:flex;gap:14px;align-items:stretch;flex-wrap:wrap;margin-bottom:14px}}
.kpi-boxes{{display:flex;flex-wrap:wrap;gap:10px;flex:1}}
.kpi-box{{background:#0D1F3C;border:1px solid #1A3A60;border-radius:8px;padding:12px 14px;
          min-width:110px;flex:1;text-align:center;transition:transform .2s}}
.kpi-box:hover{{transform:translateY(-2px);box-shadow:0 4px 16px #00BCD420}}
.kpi-icon{{font-size:18px;margin-bottom:4px}}
.kpi-val{{font-size:22px;font-weight:700;line-height:1.1}}
.kpi-lbl{{font-size:10px;color:#7BAFD4;margin-top:3px;text-transform:uppercase;letter-spacing:.8px}}
.kpi-sub{{font-size:10px;color:#4A90D9;margin-top:2px}}
.gauge-wrap{{background:#0D1F3C;border:1px solid #1A3A60;border-radius:8px;
             padding:12px;display:flex;align-items:center;justify-content:center;flex-shrink:0}}
.disc-panel{{background:#0D1F3C;border:1px solid #1A3A60;border-radius:8px;padding:14px 16px;flex:1}}
.disc-panel-title{{font-size:10.5px;color:#4A90D9;letter-spacing:1.5px;text-transform:uppercase;
                   margin-bottom:10px}}

/* Filter bar */
.filter-bar{{background:#06101E;border-bottom:1px solid #1A3A60;padding:10px 20px;
             display:flex;flex-wrap:wrap;gap:10px;align-items:center}}
.filter-lbl{{font-size:10.5px;color:#4A90D9;font-weight:600;letter-spacing:1px;
             text-transform:uppercase}}
.filter-select,.filter-input{{background:#0D1F3C;border:1px solid #1A3A60;border-radius:4px;
  color:#C8D8F0;padding:5px 10px;font-size:12px;outline:none;font-family:inherit}}
.filter-select:focus,.filter-input:focus{{border-color:#00BCD4}}
.btn-clear{{background:#0D2540;border:1px solid #1A3A60;border-radius:4px;color:#4A90D9;
            padding:5px 12px;cursor:pointer;font-size:12px}}
.btn-clear:hover{{border-color:#00BCD4;color:#00BCD4}}
.filter-count{{font-size:11px;color:#4A90D9;white-space:nowrap;margin-left:auto}}

/* Cards section */
.cards-section{{padding:16px 20px}}
.sec-header{{font-size:11px;color:#4A90D9;letter-spacing:2px;text-transform:uppercase;
             margin-bottom:14px;display:flex;align-items:center;gap:8px}}
.sec-header::after{{content:'';flex:1;height:1px;background:linear-gradient(90deg,#1A3A60,transparent)}}
.cards-grid{{display:grid;grid-template-columns:1fr;gap:16px}}

/* Discipline card */
.disc-card{{background:#0D1F3C;border:1px solid #1A3A60;border-radius:10px;overflow:hidden}}
.card-hbar{{display:flex;align-items:center;flex-wrap:wrap;gap:10px;padding:10px 14px;
            border-bottom:1px solid #1A3A60}}
.disc-badge{{padding:4px 10px;border-radius:20px;font-size:12px;font-weight:700;
             letter-spacing:.5px}}
.pend-badge{{background:#FF524220;border:1px solid #FF524260;border-radius:4px;
             padding:2px 8px;color:#FF5252;font-size:11px;font-weight:600}}
.card-pct{{font-size:16px;font-weight:700;margin-left:auto}}
.card-counts{{display:flex;gap:8px;font-size:11px}}
.cnt-ok{{color:#00E676}}.cnt-pend{{color:#FFC107}}.cnt-tot{{color:#4A90D9}}
.btn-toggle{{background:#0A1E38;border:1px solid #1A3A60;border-radius:4px;color:#4A90D9;
             padding:3px 10px;cursor:pointer;font-size:10px;white-space:nowrap}}
.btn-toggle:hover{{border-color:#00BCD4;color:#00BCD4}}
.card-table-wrap{{overflow-x:auto}}

/* Document table */
.doc-table{{width:100%;border-collapse:collapse;font-size:12px}}
.doc-table thead tr{{background:#081828}}
.doc-table th{{padding:7px 10px;text-align:left;color:#4A90D9;font-size:10px;
               font-weight:700;letter-spacing:.8px;text-transform:uppercase;
               border-bottom:1px solid #1A3A60;white-space:nowrap}}
.doc-row{{transition:background .15s}}
.doc-row:hover{{background:#132030}}
.doc-row.pendente{{background:#0A1628}}
.doc-row.finalizado{{background:#07111E;opacity:.75}}
.doc-row.finalizado.hidden{{display:none}}
.doc-num{{padding:7px 10px;font-size:11px;color:#7BAFD4;white-space:nowrap;
          font-family:'Courier New',monospace}}
.doc-titulo{{padding:7px 10px;color:#C8D8F0;max-width:360px}}
.doc-centro{{padding:7px 10px;text-align:center;color:#4A90D9;font-size:11px;white-space:nowrap}}
.doc-fin{{padding:7px 10px;color:#7BAFD4;font-size:11px;max-width:160px}}
.doc-status{{padding:7px 10px;font-size:11px;font-weight:600;display:flex;
             align-items:center;gap:6px;white-space:nowrap}}
.st-dot{{width:7px;height:7px;border-radius:50%;flex-shrink:0}}

/* Footer */
.site-footer{{background:#06101E;border-top:1px solid #1A3A60;padding:12px 20px;
              display:flex;flex-wrap:wrap;gap:8px;font-size:11px;color:#4A90D9;
              align-items:center}}
.footer-by{{color:#7BAFD4;font-style:italic}}
.footer-pill{{background:#0D1F3C;border:1px solid #1A3A60;border-radius:4px;
              padding:3px 10px;font-weight:600;color:#00BCD4}}

@media(max-width:768px){{
  .kpi-top{{flex-direction:column}}
  .card-hbar{{flex-direction:column;align-items:flex-start}}
  .card-pct{{margin-left:0}}
}}
</style>
</head>
<body>

<header class="site-header">
  <div class="header-top">
    <div class="logo-otz-wrap">OTZ<br>GPLAN</div>
    <div class="header-title">
      <h1>Lista de Documentos de Projeto</h1>
      <div class="sub">ASU Jundiaí (E-179) &nbsp;|&nbsp; OTZ Engenharia × Messer Gases for Life</div>
    </div>
    {messer_svg}
  </div>
  <div class="header-refbar">
    <span class="rpill doc">P-LD-E-179-PLA34-000-001</span>
    <span class="rpill">Cliente: Messer Gases Ltda</span>
    <span class="rpill">Gerente: Daniel Novas</span>
    <span class="rpill">Atualização LD: {LD_DATA}</span>
    <span class="rpill">Gerado em: {TODAY_STR}</span>
    <span class="rpill" style="color:#00BCD4;font-weight:600">Elaborado por: Ilson do Santos Azevedo</span>
  </div>
</header>

<section class="kpi-section">
  <div class="sec-title">&#9670; Indicadores Gerais</div>
  <div class="kpi-top">
    <div class="kpi-boxes">{kpi_boxes}</div>
    <div class="gauge-wrap">{global_gauge}</div>
  </div>
  <div class="disc-panel">
    <div class="disc-panel-title">&#9670; Avanço por Disciplina — Documentos Finalizados / Total</div>
    {disc_chart}
  </div>
</section>

<div class="filter-bar">
  <span class="filter-lbl">Disciplina</span>
  <select class="filter-select" id="f-disc" onchange="applyFilters()">
    <option value="">Todas</option>
    {disc_opts}
  </select>
  <span class="filter-lbl">Status</span>
  <select class="filter-select" id="f-status" onchange="applyFilters()" style="min-width:160px">
    <option value="">Todos</option>
    {st_opts}
  </select>
  <span class="filter-lbl">Busca</span>
  <input class="filter-input" id="f-busca" type="text"
         placeholder="Nº documento ou título..." oninput="applyFilters()" style="min-width:220px">
  <button class="btn-clear" onclick="clearFilters()">Limpar</button>
  <span class="filter-count" id="filter-count">{TOTAL} de {TOTAL} disciplinas</span>
</div>

<section class="cards-section">
  <div class="sec-header">
    &#9670; Disciplinas &nbsp;·&nbsp; {len(cards)} grupos &nbsp;·&nbsp;
    {k["tot"]} documentos ativos
  </div>
  <div class="cards-grid" id="cards-grid">
    {cards_html}
  </div>
</section>

<footer class="site-footer">
  <span class="footer-by">Elaborado por: Ilson do Santos Azevedo / Supervisor de Planejamento</span>
  <span class="footer-pill">OTZ Engenharia — GPLAN</span>
  <span class="footer-pill">E-179 — ASU Jundiaí</span>
  <span class="footer-pill">Messer Gases for Life</span>
  <span style="margin-left:auto;color:#7BAFD4">Gerado em {TODAY_STR} · Documentos finalizados mantidos fixos por regra GPLAN</span>
</footer>

<script>
const TOTAL = {TOTAL};

function applyFilters() {{
  const fD = document.getElementById('f-disc').value;
  const fS = document.getElementById('f-status').value;
  const fB = document.getElementById('f-busca').value.toLowerCase().trim();
  let vis = 0;
  document.querySelectorAll('.disc-card').forEach(card => {{
    let show = true;
    if (fD && card.dataset.disc !== fD) show = false;
    if (fS && !JSON.parse(card.dataset.statuses||'[]').includes(fS)) show = false;
    if (fB && !(card.dataset.text||'').includes(fB)) show = false;

    // Filtro de status nas linhas internas
    if (show && fS) {{
      card.querySelectorAll('.doc-row').forEach(row => {{
        const st = row.querySelector('.doc-status');
        const rowSt = st ? st.textContent.trim() : '';
        row.style.display = rowSt.includes(fS) ? '' : 'none';
      }});
    }} else if (show) {{
      card.querySelectorAll('.doc-row').forEach(row => {{
        if (!row.classList.contains('hidden')) row.style.display = '';
      }});
    }}

    card.style.display = show ? '' : 'none';
    if (show) vis++;
  }});
  document.getElementById('filter-count').textContent = vis + ' de ' + TOTAL + ' disciplinas';
}}

function clearFilters() {{
  ['f-disc','f-status'].forEach(id => document.getElementById(id).value='');
  document.getElementById('f-busca').value='';
  document.querySelectorAll('.doc-row').forEach(r => {{
    if (!r.classList.contains('hidden')) r.style.display='';
  }});
  applyFilters();
}}

function toggleFinal(btn) {{
  const card = btn.closest('.disc-card');
  const rows = card.querySelectorAll('.doc-row.finalizado');
  const hiding = btn.textContent.trim() === 'Ocultar finalizados';
  rows.forEach(r => r.classList.toggle('hidden', hiding));
  btn.textContent = hiding ? 'Mostrar finalizados' : 'Ocultar finalizados';
}}
</script>
</body>
</html>'''

# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    print("="*60)
    print("LISTA DE DOCUMENTOS — E-179 ASU Jundiaí")
    print("="*60)
    print("\n[1] Lendo Excel LD …")
    docs = read_ld()
    print(f"    {len(docs)} documentos lidos")

    print("\n[2] Agrupando por disciplina …")
    cards = build_cards(docs)
    print(f"    {len(cards)} disciplinas | {sum(c['total'] for c in cards)} docs ATIVO")

    print("\n[3] KPIs …")
    kpis = compute_kpis(cards)
    print(f"    Avanço: {kpis['pct']:.1f}% | Finalizados: {kpis['finais']} | Pendentes: {kpis['pend']}")

    print("\n[4] Gerando HTML …")
    html = generate_html(cards, kpis)
    with open(HTML_OUT, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"    {HTML_OUT}  ({os.path.getsize(HTML_OUT)/1024:.0f} KB)")

    print("\n✓ Dashboard LD concluído")

if __name__ == "__main__":
    main()
