#!/usr/bin/env python3
"""Dashboard LD — Lista de Documentos E-179 | OTZ Engenharia × Messer Gases for Life
   Estilo corporativo: fundo #EAECEF, header #C0392B, cards brancos. Chart.js 4.4.1"""

import os, json
from datetime import date, datetime
from collections import defaultdict
import openpyxl

ROOT             = os.path.dirname(os.path.abspath(__file__))
UPLOAD           = "/root/.claude/uploads/001b7fb0-8857-54b0-9eb5-28053bfc3f61"
EXCEL_IN         = os.path.join(UPLOAD, "054b4699-PLDE179PLA340000010_2026.07.16_REPLAN.xlsx")
HTML_OUT         = os.path.join(ROOT, "OTZ_E179_LISTA_DOCUMENTOS.html")
FINALIZADOS_JSON = os.path.join(ROOT, "ld_finalizados.json")
LOGO_B64_FILE    = "/tmp/messer_logo_b64.txt"

TODAY     = date.today()
TODAY_STR = TODAY.strftime("%d/%m/%Y")
LD_DATA   = "16/07/2026"

COLS = {
    "disc":0,"subdisc":1,"area":2,"num_doc":3,"titulo":4,"rev":5,"tipo":6,
    "id_exc":7,"id_1em":8,"base_1em":9,"id_final":10,"base_ult":11,
    "data_1em":12,"fin_1em":13,"grd_1em":14,
    "data_atual":15,"fin_atual":16,"grd_atual":17,
    "horas":18,"peso":19,"avanco":20,
    "status_doc":21,"status_eclic":22,"status":23,
}

# ── Utilitários ───────────────────────────────────────────────────────────────
def safe_float(v):
    try: return float(v)
    except: return 0.0

def safe_int_rev(v):
    if v is None or str(v).strip() == "": return -1
    try: return int(float(str(v).strip()))
    except: return -1

def to_date(v):
    if v is None: return None
    if isinstance(v, datetime): return v.date()
    if isinstance(v, date): return v
    s = str(v).strip()
    if not s: return None
    for fmt in ("%d/%m/%Y", "%Y-%m-%d", "%m/%d/%Y"):
        try: return datetime.strptime(s, fmt).date()
        except: pass
    return None

# ── Ler Excel ─────────────────────────────────────────────────────────────────
def read_ld():
    wb = openpyxl.load_workbook(EXCEL_IN, data_only=True)
    ws = wb["LD"]
    docs = []
    for row in ws.iter_rows(min_row=9, values_only=True):
        if not any(row): continue
        if not row[COLS["num_doc"]]: continue
        docs.append({k: row[v] for k, v in COLS.items()})
    return docs

# ── Finalizados fixos ──────────────────────────────────────────────────────────
def load_finalizados():
    if os.path.exists(FINALIZADOS_JSON):
        with open(FINALIZADOS_JSON) as f:
            return set(json.load(f).get("numeros", []))
    return set()

def save_finalizados(docs):
    nums = sorted(
        d["num_doc"] for d in docs
        if str(d.get("status", "")).strip().upper() == "DOC. FINALIZADO" and d["num_doc"]
    )
    with open(FINALIZADOS_JSON, "w") as f:
        json.dump({"numeros": nums, "atualizado": TODAY_STR}, f, indent=2, ensure_ascii=False)

# ── Retrabalho ────────────────────────────────────────────────────────────────
def retrabalho_group(group):
    sem_em, sem_rev, sem_ret, com_ret = [], [], [], []
    max_rev = -1
    for d in group:
        rev = safe_int_rev(d.get("rev"))
        if rev > max_rev:
            max_rev = rev
        if rev < 0:
            sem_em.append(d)
        elif rev == 0:
            sem_rev.append(d)
        elif rev == 1:
            sem_ret.append(d)
        else:
            com_ret.append(d)
    return {
        "sem_emissao": sem_em, "sem_revisao": sem_rev,
        "sem_retrabalho": sem_ret, "com_retrabalho": com_ret,
        "max_rev": max(max_rev, 0), "total": len(group),
    }

# ── KPIs ──────────────────────────────────────────────────────────────────────
def compute_all(docs):
    save_finalizados(docs)

    total_all = len(docs)
    # Regra: "NÃO NECESSÁRIO" é sempre excluído do escopo ativo, independente de status_doc.
    # Alguns docs podem ter status_doc=ATIVO mas status=NÃO NECESSÁRIO por ajuste manual na planilha.
    ativos = [
        d for d in docs
        if str(d.get("status_doc", "")).strip().upper() == "ATIVO"
        and str(d.get("status", "")).strip().upper() != "NÃO NECESSÁRIO"
    ]
    excl_cnt = total_all - len(ativos)  # inclui EXCLUÍDO + ATIVO/NÃO NECESSÁRIO

    STATUS_EM_PROC = {"AGUARDANDO MARKUP", "ATENDER MARKUP", "PATEC EMITIDO"}
    finalizados = [d for d in ativos if str(d.get("status", "")).strip().upper() == "DOC. FINALIZADO"]
    em_fluxo    = [d for d in ativos if str(d.get("status", "")).strip().upper() != "DOC. FINALIZADO"]
    nao_ini     = [d for d in em_fluxo if str(d.get("status", "")).strip().upper() == "EMITIR EMISSÃO INICIAL"]
    em_proc     = [d for d in em_fluxo if str(d.get("status", "")).strip().upper() in STATUS_EM_PROC]

    docs_cpeso = [d for d in ativos if safe_float(d["peso"]) > 0]
    peso_tot   = sum(safe_float(d["peso"]) for d in docs_cpeso)
    avanco_w   = sum(safe_float(d["peso"]) * safe_float(d["avanco"]) for d in docs_cpeso)
    avanco_pct = (avanco_w / peso_tot * 100) if peso_tot else 0

    atras_l, semb_l, npz_l = [], [], []
    for d in em_fluxo:
        bd = to_date(d.get("base_ult"))
        if bd is None:
            semb_l.append(d)
        elif bd < TODAY:
            atras_l.append(d)
        else:
            npz_l.append(d)

    ret_fin   = retrabalho_group(finalizados)
    ret_fluxo = retrabalho_group(em_fluxo)

    # Por disciplina — agrupa TODOS os docs para contar excluídos por disc
    all_by_disc = defaultdict(list)
    for d in docs:
        disc = (d.get("disc") or "S/D").strip()
        all_by_disc[disc].append(d)

    disc_data = []
    for disc in sorted(all_by_disc.keys()):
        dall   = all_by_disc[disc]
        dativo = [d for d in dall
                  if str(d.get("status_doc", "")).strip().upper() == "ATIVO"
                  and str(d.get("status", "")).strip().upper() != "NÃO NECESSÁRIO"]
        dexcl  = len(dall) - len(dativo)
        dfin   = sum(1 for d in dativo if str(d.get("status", "")).strip().upper() == "DOC. FINALIZADO")
        dflux  = len(dativo) - dfin
        dpeso  = sum(safe_float(d["peso"]) for d in dativo if safe_float(d["peso"]) > 0)
        davw   = sum(safe_float(d["peso"]) * safe_float(d["avanco"]) for d in dativo if safe_float(d["peso"]) > 0)
        dav    = (davw / dpeso * 100) if dpeso else 0
        datras = 0
        for d in dativo:
            if str(d.get("status", "")).strip().upper() != "DOC. FINALIZADO":
                bd = to_date(d.get("base_ult"))
                if bd is not None and bd < TODAY:
                    datras += 1
        disc_data.append({
            "disc": disc, "total_all": len(dall), "excluidos": dexcl,
            "ativos": len(dativo), "finalizados": dfin, "em_fluxo": dflux,
            "avanco": dav, "atrasados": datras,
        })

    return {
        "total_all":   total_all,
        "ativos_cnt":  len(ativos),
        "excl_cnt":    excl_cnt,
        "fin_cnt":     len(finalizados),
        "fluxo_cnt":   len(em_fluxo),
        "proc_cnt":    len(em_proc),
        "nai_cnt":     len(nao_ini),
        "avanco_pct":  avanco_pct,
        "peso_tot":    peso_tot,
        "docs_cpeso":  len(docs_cpeso),
        "sem_peso_cnt": len(ativos) - len(docs_cpeso),
        "atras_cnt":   len(atras_l),
        "semb_cnt":    len(semb_l),
        "npz_cnt":     len(npz_l),
        "ret_fin":     ret_fin,
        "ret_fluxo":   ret_fluxo,
        "n_discs":     len(disc_data),
        "disc_data":   disc_data,
    }

# ── Helpers HTML ──────────────────────────────────────────────────────────────
def pct_str(a, b):
    if not b: return "—%"
    return "{:.1f}%".format(a / b * 100)

def pbar_color(pct):
    if pct >= 95: return "#1E8449"
    if pct >= 85: return "#CA6F1E"
    return "#C0392B"

def ret_row(label, cnt, total):
    p = "{:.1f}%".format(cnt / total * 100) if total else "—"
    return "<tr><td>{}</td><td>{}</td><td>{}</td></tr>\n".format(label, cnt, p)

def ret_table_rows(r, show_sem_em):
    out = ""
    if show_sem_em:
        out += ret_row('Sem Emissão <small style="color:#95A5A6">(doc não gerado)</small>',
                       len(r["sem_emissao"]), r["total"])
    out += ret_row('Sem Revisão <small style="color:#95A5A6">(Rev 0)</small>',
                   len(r["sem_revisao"]), r["total"])
    out += ret_row('Sem Retrabalho <small style="color:#95A5A6">(Rev 1)</small>',
                   len(r["sem_retrabalho"]), r["total"])
    out += ret_row('Com Retrabalho <small style="color:#95A5A6">(Rev ≥ 2)</small>',
                   len(r["com_retrabalho"]), r["total"])
    if r["max_rev"] >= 2:
        out += '<tr class="t-max"><td>★ Revisão Máxima (Rev {})</td><td>1</td><td>—</td></tr>\n'.format(r["max_rev"])
    out += '<tr class="t-total"><td>TOTAL</td><td>{}</td><td>100%</td></tr>\n'.format(r["total"])
    return out

# ── Gerar HTML ────────────────────────────────────────────────────────────────
def generate_html(kpis):
    k = kpis

    # Messer logo
    try:
        with open(LOGO_B64_FILE) as f:
            logo_b64 = f.read().strip()
        logo_img = '<img src="data:image/jpeg;base64,{}" height="38" alt="Messer"/>'.format(logo_b64)
    except Exception:
        logo_img = '<span style="font-weight:700;font-size:16px;color:#1A3680">MESSER</span>'

    # Pre-compute all values used in template
    total_all   = k["total_all"]
    ativos_cnt  = k["ativos_cnt"]
    excl_cnt    = k["excl_cnt"]
    fin_cnt     = k["fin_cnt"]
    fluxo_cnt   = k["fluxo_cnt"]
    proc_cnt    = k["proc_cnt"]
    nai_cnt     = k["nai_cnt"]
    avanco_pct  = k["avanco_pct"]
    peso_tot    = k["peso_tot"]
    docs_cpeso  = k["docs_cpeso"]
    sem_peso    = k["sem_peso_cnt"]
    atras_cnt   = k["atras_cnt"]
    semb_cnt    = k["semb_cnt"]
    npz_cnt     = k["npz_cnt"]
    n_discs     = k["n_discs"]
    rf          = k["ret_fin"]
    rx          = k["ret_fluxo"]

    ativos_pct = pct_str(ativos_cnt, total_all)
    excl_pct   = pct_str(excl_cnt,  total_all)
    fin_pct    = pct_str(fin_cnt,   ativos_cnt)
    fluxo_pct  = pct_str(fluxo_cnt, ativos_cnt)
    proc_pct   = pct_str(proc_cnt,  fluxo_cnt)
    nai_pct    = pct_str(nai_cnt,   fluxo_cnt)
    atras_pct  = pct_str(atras_cnt, fluxo_cnt)
    semb_pct   = pct_str(semb_cnt,  fluxo_cnt)
    npz_pct    = pct_str(npz_cnt,   fluxo_cnt)
    pb_w       = min(100.0, avanco_pct)
    restante   = max(0.0, 100.0 - avanco_pct)
    npz_val    = npz_cnt if npz_cnt > 0 else 0.01
    no_prazo_sub = "Nenhum em dia" if npz_cnt == 0 else "Em dia com o cronograma"

    ret_fin_html   = ret_table_rows(rf, False)
    ret_fluxo_html = ret_table_rows(rx, True)

    # INDICADORES table rows
    disc_rows = ""
    for d in k["disc_data"]:
        pct       = d["avanco"]
        col       = pbar_color(pct)
        bar_w     = round(pct)
        excl_col  = "#C0392B" if d["excluidos"] > 0 else "#7F8C8D"
        atras_cls = "b-red" if d["atrasados"] > 0 else "b-green"
        fluxo_col = "#CA6F1E" if d["em_fluxo"] > 0 else "#95A5A6"
        disc_rows += (
            '<tr>'
            '<td>{disc}</td><td>{total_all}</td>'
            '<td style="color:{excl_col}">{excluidos}</td>'
            '<td>{ativos}</td>'
            '<td style="color:#1E8449">{finalizados}</td>'
            '<td style="color:{fluxo_col}">{em_fluxo}</td>'
            '<td><span class="badge {atras_cls}">{atrasados}</span></td>'
            '<td><div class="pb">'
            '<div class="pb-bar" style="width:{bar_w}px;background:{col}"></div>'
            '<span class="pb-txt" style="color:{col}">{pct:.1f}%</span>'
            '</div></td></tr>\n'
        ).format(
            disc=d["disc"], total_all=d["total_all"], excl_col=excl_col,
            excluidos=d["excluidos"], ativos=d["ativos"],
            finalizados=d["finalizados"], fluxo_col=fluxo_col,
            em_fluxo=d["em_fluxo"], atras_cls=atras_cls,
            atrasados=d["atrasados"], bar_w=bar_w, col=col, pct=pct,
        )
    tot_atras = sum(d["atrasados"] for d in k["disc_data"])
    disc_rows += (
        '<tr class="t-total">'
        '<td>TOTAL</td><td>{}</td><td>{}</td><td>{}</td>'
        '<td>{}</td><td>{}</td><td>{}</td>'
        '<td>{:.2f}%</td></tr>\n'
    ).format(total_all, excl_cnt, ativos_cnt, fin_cnt, fluxo_cnt, tot_atras, avanco_pct)

    disc_labels_js = json.dumps([d["disc"] for d in k["disc_data"]], ensure_ascii=False)
    disc_vals_js   = json.dumps([round(d["avanco"], 1) for d in k["disc_data"]])

    # ── Template HTML ─────────────────────────────────────────────────────────
    parts = []
    parts.append("""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Dashboard LD — ASU Jundiaí | {ld_data}</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/chartjs-plugin-datalabels/2.2.0/chartjs-plugin-datalabels.min.js"></script>
<style>
*{margin:0;padding:0;box-sizing:border-box;}
body{font-family:Arial,sans-serif;background:#EAECEF;color:#1a1a1a;}
.header{background:#C0392B;color:white;padding:14px 32px;display:flex;justify-content:space-between;align-items:center;box-shadow:0 2px 6px rgba(0,0,0,0.25);}
.header-left h1{font-size:18px;font-weight:700;}
.header-left h2{font-size:11px;opacity:.85;margin-top:3px;}
.header-right{display:flex;align-items:center;gap:12px;}
.logo-box{background:white;padding:5px 10px;border-radius:3px;display:flex;align-items:center;}
.date-badge{background:rgba(0,0,0,0.2);padding:5px 14px;border-radius:3px;font-size:11px;font-weight:700;}
.subheader{background:#004562;padding:6px 32px;display:flex;justify-content:space-between;font-size:10px;color:rgba(255,255,255,0.7);}
.subheader strong{color:white;}
.content{padding:22px 32px 8px;}
.sec{font-size:10px;font-weight:700;color:#C0392B;letter-spacing:2px;text-transform:uppercase;margin:20px 0 12px;padding-left:10px;border-left:3px solid #C0392B;}
.row{display:flex;gap:14px;margin-bottom:16px;flex-wrap:wrap;}
.row3{display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:14px;margin-bottom:16px;}
.row2{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:16px;}
.card{background:white;border-radius:5px;padding:18px 20px 14px;box-shadow:0 1px 4px rgba(0,0,0,0.08);border-top:3px solid #BDC3C7;flex:1;min-width:120px;}
.card.navy{border-top-color:#004562;}.card.blue{border-top-color:#0057A8;}.card.red{border-top-color:#C0392B;}.card.green{border-top-color:#1E8449;}.card.orange{border-top-color:#CA6F1E;}.card.gray{border-top-color:#7F8C8D;}
.c-label{font-size:9px;color:#7f8c8d;text-transform:uppercase;letter-spacing:1.2px;font-weight:700;margin-bottom:6px;}
.c-val{font-size:38px;font-weight:700;line-height:1;color:#2C3E50;}
.c-sub{font-size:11px;color:#7f8c8d;margin-top:6px;}
.c-pct{font-weight:700;}
.c-subs{display:flex;margin-top:14px;padding-top:12px;border-top:1px solid #f0f0f0;}
.c-si{flex:1;text-align:center;border-right:1px solid #f0f0f0;}
.c-si:last-child{border-right:none;}
.c-si .sv{font-size:20px;font-weight:700;color:#2C3E50;}
.c-si .sl{font-size:9px;color:#95A5A6;text-transform:uppercase;margin-top:2px;}
.avanco{background:linear-gradient(120deg,#004562 0%,#0057A8 100%);border-radius:5px;padding:26px 32px;color:white;display:flex;align-items:center;justify-content:space-between;box-shadow:0 2px 8px rgba(0,69,98,0.35);margin-bottom:16px;}
.av-left .av-lbl{font-size:10px;text-transform:uppercase;letter-spacing:2px;opacity:.8;margin-bottom:4px;}
.av-left .av-val{font-size:72px;font-weight:700;line-height:1;}
.av-left .av-sub{font-size:11px;opacity:.65;margin-top:6px;}
.av-right{width:320px;}
.pb-outer{background:rgba(255,255,255,0.2);border-radius:8px;height:12px;}
.pb-inner{background:#27AE60;border-radius:8px;height:12px;}
.av-note{font-size:10px;opacity:.6;margin-top:6px;text-align:right;}
.cc{background:white;border-radius:5px;padding:18px 20px;box-shadow:0 1px 4px rgba(0,0,0,0.08);}
.cc h3{font-size:10px;font-weight:700;color:#2C3E50;text-transform:uppercase;letter-spacing:.8px;margin-bottom:14px;}
.tc{background:white;border-radius:5px;padding:18px 20px;box-shadow:0 1px 4px rgba(0,0,0,0.08);margin-bottom:16px;}
.tc h3{font-size:10px;font-weight:700;color:#2C3E50;text-transform:uppercase;letter-spacing:.8px;margin-bottom:14px;}
table{width:100%;border-collapse:collapse;font-size:11.5px;}
th{background:#004562;color:white;padding:9px 12px;text-align:center;font-size:9.5px;letter-spacing:.5px;font-weight:700;}
th:first-child{text-align:left;}
td{padding:8px 12px;text-align:center;border-bottom:1px solid #f2f2f2;}
td:first-child{text-align:left;font-weight:600;color:#2C3E50;}
tr:hover td{background:#FAFBFC;}
tr.t-total td{background:#004562;color:white;font-weight:700;border:none;}
tr.t-total td:first-child{background:#004562;}
.rt th{background:#0057A8;}.rt .t-total td{background:#0057A8;}
.rt .t-max td{background:#C0392B;color:white;font-style:italic;font-size:11px;}
.pb{display:flex;align-items:center;gap:6px;}
.pb-bar{height:6px;border-radius:3px;min-width:2px;}
.pb-txt{font-size:11px;font-weight:600;white-space:nowrap;}
.badge{display:inline-block;padding:2px 9px;border-radius:10px;font-size:10px;font-weight:700;}
.b-red{background:#FADBD8;color:#922B21;}.b-green{background:#D5F5E3;color:#1E8449;}.b-gray{background:#EAECEE;color:#566573;}
.footer{background:#1C2833;color:#7F8C8D;text-align:center;padding:11px;font-size:10px;margin-top:10px;}
.footer .accent{color:#C0392B;font-weight:700;}
</style>
</head>
<body>""".replace("{ld_data}", LD_DATA))

    parts.append("""
<div class="header">
  <div class="header-left">
    <h1>ASU JUNDIAÍ &nbsp;|&nbsp; DASHBOARD — LISTA DE DOCUMENTOS DE ENGENHARIA</h1>
    <h2>Project Manager &rarr; Eduardo Vessoni &nbsp;&nbsp;&nbsp; Project Leader &rarr; Antonio Julião</h2>
  </div>
  <div class="header-right">
    <div class="logo-box">{logo_img}</div>
    <div class="date-badge">STATUS: {ld_data}</div>
  </div>
</div>
<div class="subheader">
  <span>LD: <strong>P-LD-E-179-PLA34-000-001</strong> &nbsp;|&nbsp; Supervisor de Planejamento: <strong>Ilson do Santos Azevedo</strong></span>
  <span>Disciplinas: <strong>{n_discs}</strong> &nbsp;|&nbsp; Elaborado pelo Painel de Controle GPLAN — OTZ Engenharia</span>
</div>""".format(logo_img=logo_img, ld_data=LD_DATA, n_discs=n_discs))

    parts.append("""
<div class="content">
  <div class="sec">VISÃO GERAL</div>
  <div class="row">
    <div class="card navy" style="flex:1.1">
      <div class="c-label">Total de Documentos</div>
      <div class="c-val">{total_all}</div>
      <div class="c-sub">LD completa</div>
    </div>
    <div class="card green" style="flex:1.1">
      <div class="c-label">Documentos Ativos</div>
      <div class="c-val" style="color:#1E8449">{ativos_cnt}</div>
      <div class="c-sub"><span class="c-pct" style="color:#1E8449">{ativos_pct}</span> do total</div>
    </div>
    <div class="card red" style="flex:1.1">
      <div class="c-label">Documentos Excluídos</div>
      <div class="c-val" style="color:#C0392B">{excl_cnt}</div>
      <div class="c-sub"><span class="c-pct" style="color:#C0392B">{excl_pct}</span> do total</div>
    </div>
  </div>

  <div class="sec">STATUS DOS DOCUMENTOS ATIVOS</div>
  <div class="row">
    <div class="card blue" style="flex:1.5">
      <div class="c-label">DOC. FINALIZADO</div>
      <div class="c-val" style="color:#0057A8">{fin_cnt}</div>
      <div class="c-sub"><span class="c-pct" style="color:#0057A8">{fin_pct}</span> dos documentos ativos</div>
    </div>
    <div class="card orange" style="flex:2.5">
      <div class="c-label">EM FLUXO — em elaboração ou não iniciados</div>
      <div class="c-val" style="color:#CA6F1E">{fluxo_cnt}</div>
      <div class="c-sub"><span class="c-pct" style="color:#CA6F1E">{fluxo_pct}</span> dos documentos ativos</div>
      <div class="c-subs">
        <div class="c-si"><div class="sv" style="color:#CA6F1E">{proc_cnt}</div><div class="sl">Em Processo ({proc_pct})</div></div>
        <div class="c-si"><div class="sv" style="color:#95A5A6">{nai_cnt}</div><div class="sl">Não Iniciados ({nai_pct})</div></div>
      </div>
    </div>
  </div>

  <div class="avanco">
    <div class="av-left">
      <div class="av-lbl">Avanço Físico Ponderado — Documentos Ativos</div>
      <div class="av-val">{avanco_pct:.2f}%</div>
      <div class="av-sub">Base: {docs_cpeso} documentos ativos com peso cadastrado &nbsp;|&nbsp; Peso total: {peso_tot:.2f} &nbsp;|&nbsp; {sem_peso} doc(s) sem peso excluído(s) do cálculo</div>
    </div>
    <div class="av-right">
      <div style="display:flex;justify-content:space-between;font-size:10px;opacity:.7;margin-bottom:6px"><span>0%</span><span>Progresso</span><span>100%</span></div>
      <div class="pb-outer"><div class="pb-inner" style="width:{pb_w:.1f}%"></div></div>
      <div class="av-note">{restante:.1f}% restante para conclusão</div>
    </div>
  </div>

  <div class="sec">ADERÊNCIA AO BASELINE — universo: {fluxo_cnt} documentos EM FLUXO</div>
  <div class="row">
    <div class="card red">
      <div class="c-label">ATRASADOS</div>
      <div class="c-val" style="color:#C0392B">{atras_cnt}</div>
      <div class="c-sub"><span class="c-pct" style="color:#C0392B">{atras_pct}</span> do EM FLUXO</div>
    </div>
    <div class="card gray">
      <div class="c-label">SEM BASELINE</div>
      <div class="c-val" style="color:#7F8C8D">{semb_cnt}</div>
      <div class="c-sub"><span class="c-pct" style="color:#7F8C8D">{semb_pct}</span> sem data cadastrada</div>
    </div>
    <div class="card green">
      <div class="c-label">NO PRAZO</div>
      <div class="c-val" style="color:#1E8449">{npz_cnt}</div>
      <div class="c-sub">{no_prazo_sub}</div>
    </div>
  </div>

  <div class="row3">
    <div class="cc"><h3>G1 — Ativos vs Excluídos ({total_all})</h3><canvas id="c1" height="210"></canvas></div>
    <div class="cc"><h3>G2 — Status dos Ativos ({ativos_cnt})</h3><canvas id="c2" height="210"></canvas></div>
    <div class="cc"><h3>G3 — EM FLUXO: Detalhe ({fluxo_cnt})</h3><canvas id="c3" height="210"></canvas></div>
    <div class="cc"><h3>G4 — Aderência ao Baseline ({fluxo_cnt} EM FLUXO)</h3><canvas id="c4" height="210"></canvas></div>
  </div>""".format(
        total_all=total_all, ativos_cnt=ativos_cnt, excl_cnt=excl_cnt,
        ativos_pct=ativos_pct, excl_pct=excl_pct,
        fin_cnt=fin_cnt, fin_pct=fin_pct,
        fluxo_cnt=fluxo_cnt, fluxo_pct=fluxo_pct,
        proc_cnt=proc_cnt, proc_pct=proc_pct, nai_cnt=nai_cnt, nai_pct=nai_pct,
        avanco_pct=avanco_pct, docs_cpeso=docs_cpeso, peso_tot=peso_tot, sem_peso=sem_peso,
        pb_w=pb_w, restante=restante,
        atras_cnt=atras_cnt, atras_pct=atras_pct,
        semb_cnt=semb_cnt, semb_pct=semb_pct,
        npz_cnt=npz_cnt, npz_pct=npz_pct, no_prazo_sub=no_prazo_sub,
    ))

    parts.append("""
  <div class="sec">RETRABALHO — NÍVEL DE REVISÃO</div>
  <div class="row2">
    <div class="tc" style="margin-bottom:0">
      <h3>Finalizados ({rf_total} documentos)</h3>
      <table class="rt">
        <thead><tr><th>Categoria</th><th>Qtd</th><th>%</th></tr></thead>
        <tbody>{ret_fin_html}</tbody>
      </table>
    </div>
    <div class="tc" style="margin-bottom:0">
      <h3>EM FLUXO ({rx_total} documentos)</h3>
      <table class="rt">
        <thead><tr><th>Categoria</th><th>Qtd</th><th>%</th></tr></thead>
        <tbody>{ret_fluxo_html}</tbody>
      </table>
    </div>
  </div>

  <div class="cc" style="margin-top:16px;margin-bottom:16px">
    <h3>Avanço Físico por Disciplina (%)</h3>
    <canvas id="c7" height="75"></canvas>
  </div>

  <div class="sec">INDICADORES POR DISCIPLINA</div>
  <div class="tc">
    <table>
      <thead><tr>
        <th>DISCIPLINA</th><th>TOTAL</th><th>EXCLUÍDOS</th><th>ATIVOS</th>
        <th>FINALIZADOS</th><th>EM FLUXO</th><th>ATRASADOS</th>
        <th style="min-width:130px">% AVANÇO</th>
      </tr></thead>
      <tbody>{disc_rows}</tbody>
    </table>
  </div>
</div>""".format(
        rf_total=rf["total"], rx_total=rx["total"],
        ret_fin_html=ret_fin_html, ret_fluxo_html=ret_fluxo_html,
        disc_rows=disc_rows,
    ))

    parts.append("""
<div class="footer">
  <span class="accent">Part of the Messer World</span>
  &nbsp;|&nbsp; ASU Jundiaí — Dashboard Lista de Documentos de Engenharia
  &nbsp;|&nbsp; Status: {ld_data} &nbsp;|&nbsp; OTZ Engenharia / GPlan Consultoria
  &nbsp;|&nbsp; Gerado pelo Painel de Controle GPLAN
</div>""".format(ld_data=LD_DATA))

    # ── Chart.js script ───────────────────────────────────────────────────────
    script = """
<script>
Chart.register(ChartDataLabels);
Chart.defaults.font.family='Arial'; Chart.defaults.font.size=11;
const R='#C0392B',B='#0057A8',N='#004562',G='#1E8449',O='#CA6F1E',GR='#7F8C8D';
function donut(id,labels,data,colors,total){
  new Chart(document.getElementById(id),{type:'doughnut',
    data:{labels,datasets:[{data,backgroundColor:colors,borderWidth:0,hoverOffset:6}]},
    options:{cutout:'60%',plugins:{
      legend:{position:'bottom',labels:{boxWidth:12,padding:10,font:{size:10}}},
      datalabels:{color:'white',font:{weight:'bold',size:11},textAlign:'center',
        formatter:(v,ctx)=>{if(v<0.5)return'';const p=((v/total)*100).toFixed(1);return v+'\\n'+p+'%';},
        display:(ctx)=>ctx.dataset.data[ctx.dataIndex]>0.5
      }
    }}
  });
}
donut('c1',['Ativos (AT_CNT)','Excluídos (EX_CNT)'],[AT_CNT,EX_CNT],[N,R],TOT_ALL);
donut('c2',['Finalizado (FIN_CNT)','Em Fluxo (FLX_CNT)'],[FIN_CNT,FLX_CNT],[B,O],AT_CNT);
donut('c3',['Em Processo (PRC_CNT)','Não Iniciado (NAI_CNT)'],[PRC_CNT,NAI_CNT],[O,GR],FLX_CNT);
donut('c4',['Atrasados (ATR_CNT)','Sem Baseline (SBL_CNT)','No Prazo (NPZ_CNT)'],[ATR_CNT,SBL_CNT,NPZ_VAL],[R,GR,G],FLX_CNT);

const discLabels=DISC_LABELS;
const discVals=DISC_VALS;
const discColors=discVals.map(v=>v>=95?N:v>=85?O:R);
new Chart(document.getElementById('c7'),{type:'bar',
  data:{labels:discLabels,datasets:[{data:discVals,backgroundColor:discColors,borderRadius:4,borderWidth:0}]},
  options:{
    plugins:{legend:{display:false},
      datalabels:{anchor:'end',color:'#2C3E50',font:{weight:'bold',size:9},
        formatter:v=>v>0?v.toFixed(1)+'%':'0%',align:'end',offset:2}},
    layout:{padding:{top:25}},
    scales:{
      y:{min:0,max:115,grid:{color:'#F0F0F0'},ticks:{callback:v=>v+'%',font:{size:10}}},
      x:{grid:{display:false},ticks:{font:{size:10},maxRotation:25}}
    }
  }
});
</script>
</body>
</html>"""

    script = (script
        .replace("AT_CNT", str(ativos_cnt))
        .replace("EX_CNT", str(excl_cnt))
        .replace("TOT_ALL", str(total_all))
        .replace("FIN_CNT", str(fin_cnt))
        .replace("FLX_CNT", str(fluxo_cnt))
        .replace("PRC_CNT", str(proc_cnt))
        .replace("NAI_CNT", str(nai_cnt))
        .replace("ATR_CNT", str(atras_cnt))
        .replace("SBL_CNT", str(semb_cnt))
        .replace("NPZ_CNT", str(npz_cnt))
        .replace("NPZ_VAL", str(npz_val))
        .replace("DISC_LABELS", disc_labels_js)
        .replace("DISC_VALS", disc_vals_js)
    )
    parts.append(script)

    return "".join(parts)

# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    print("=" * 60)
    print("DASHBOARD LD — E-179 ASU Jundiaí | OTZ × Messer")
    print("=" * 60)
    print("\n[1] Lendo Excel …")
    docs = read_ld()
    print("    {} documentos lidos".format(len(docs)))

    print("\n[2] Computando KPIs …")
    kpis = compute_all(docs)
    print("    Total={} | Ativos={} | Finalizados={}".format(
        kpis["total_all"], kpis["ativos_cnt"], kpis["fin_cnt"]))
    print("    Avanço={:.2f}% | Atrasados={}".format(
        kpis["avanco_pct"], kpis["atras_cnt"]))

    print("\n[3] Gerando HTML …")
    html = generate_html(kpis)
    with open(HTML_OUT, "w", encoding="utf-8") as f:
        f.write(html)
    kb = os.path.getsize(HTML_OUT) / 1024
    print("    {}  ({:.0f} KB)".format(HTML_OUT, kb))

    print("\n✓ Dashboard LD concluído — estilo corporativo red/white")

if __name__ == "__main__":
    main()
