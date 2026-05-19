#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Planilha Consolidada de Restrições — Projetos Cristália
25098 Citostático + 25103 Farmoquímico
Gerado por: Claude Conector — Ministro das Pontes Digitais
Data: 19/05/2026
"""

import openpyxl
from openpyxl.styles import PatternFill, Font, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from datetime import date
from collections import Counter

# ============================================================
# HELPERS
# ============================================================
def pf(hex_color):
    return PatternFill(start_color=hex_color, end_color=hex_color, fill_type="solid")

def ft(bold=False, color="000000", size=10, italic=False):
    return Font(bold=bold, color=color, size=size, italic=italic, name="Calibri")

def al(h="center", v="center", wrap=False):
    return Alignment(horizontal=h, vertical=v, wrap_text=wrap)

def border_thin():
    s = Side(style="thin", color="BFBFBF")
    return Border(left=s, right=s, top=s, bottom=s)

# ============================================================
# CORES
# ============================================================
C_HEADER_BG   = "1F4E79"
C_HEADER_FG   = "FFFFFF"
C_NO_PRAZO_BG = "C6EFCE"
C_NO_PRAZO_FG = "375623"
C_ALERTA_BG   = "FFEB9C"
C_ALERTA_FG   = "7F6000"
C_ATRASADO_BG = "FFC7CE"
C_ATRASADO_FG = "9C0006"
C_CONC_BG     = "DAEEF3"
C_CONC_FG     = "17375E"
C_CONC_ATR_BG = "FFF2CC"
C_CONC_ATR_FG = "7F4F00"
C_CISTO_BG    = "EBF3FB"
C_FARMO_BG    = "FFF2CC"
C_ALT_CISTO   = "D6E8F7"
C_ALT_FARMO   = "FFE8A1"

# ============================================================
# CALCULOS
# ============================================================
today = date(2026, 5, 19)

def calc_status(prazo, conclusao):
    if conclusao is not None:
        return "CONCLUÍDO" if conclusao <= prazo else "CONCLUÍDO COM ATRASO"
    if prazo < today:
        return "ATRASADO"
    if prazo == today:
        return "ALERTA"
    return "NO PRAZO"

def calc_dias(prazo, conclusao):
    if conclusao is not None:
        return max(0, (conclusao - prazo).days)
    if prazo < today:
        return (today - prazo).days
    return 0

# ============================================================
# DADOS — 51 REGISTROS
# ============================================================
# (data_reuniao, projeto, disciplina, empresa_resp, responsavel,
#  atividade, impacto, prazo, conclusao, observacao)

dados = [
    # ── 07/05/2026 — Citostático ──────────────────────────
    ("07/05/2026","Citostático","[DOC]","ABELV",
     "Victor / Ilson",
     "Apresentação do Mapa de Restrições da Obra",
     "—",
     date(2026,5,7), date(2026,5,11), ""),

    ("07/05/2026","Citostático","[CIVIL]","Cristália",
     "Edson / Leobino",
     "Definição das Interferências para Execução de Bota Fora",
     "Processo contínuo — novas interferências podem ser identificadas ao longo da obra",
     date(2026,5,7), date(2026,5,7), "Processo vivo no projeto"),

    ("07/05/2026","Citostático","[CIVIL]","ABELV",
     "Leobino / Celso",
     "Resolução das Interferências — Execução de Bota Fora",
     "—",
     date(2026,5,7), date(2026,5,11), ""),

    ("07/05/2026","Citostático","[ELET]","ABELV",
     "Leobino",
     "Levantamento de Material para o Sistema de Hidrante",
     "—",
     date(2026,5,7), date(2026,5,11), ""),

    ("07/05/2026","Citostático","[CIVIL][MEC/TUB]","ABELV",
     "Leobino",
     "Base do Filtro Secador — Topografia Divergente do Projeto",
     "Pode travar o posicionamento e a fundação do equipamento",
     date(2026,5,8), date(2026,5,8),
     "Registrado no INTEGRA em 08/05/2026. Divergência topográfica pendente de resolução pela engenharia"),

    ("07/05/2026","Citostático","[ELET][SUP]","ABELV",
     "Yohanna",
     "Compra de Material para o Sistema de Hidrante",
     "—",
     date(2026,5,8), date(2026,5,11), ""),

    ("07/05/2026","Citostático","[MEC/TUB]","ABELV",
     "Elson",
     "Recebimento da Tenda do Pipe Shop",
     "—",
     date(2026,5,8), date(2026,5,8), ""),

    ("07/05/2026","Citostático","[MEC/TUB][SUP]","ABELV",
     "Elson",
     "Recebimento de Ferramentas para o Pipe Shop",
     "—",
     date(2026,5,8), date(2026,5,11), ""),

    ("07/05/2026","Citostático","[MEC/TUB]","ABELV",
     "Leobino",
     "Chegada de Materiais para Fabricação da Tubulação do Trap",
     "Impacta o início da fabricação da tubulação do Trap",
     date(2026,5,8), None,
     "19/05: Material ainda não entregue"),

    ("07/05/2026","Citostático","[MEC/TUB][SUP]","ABELV",
     "Leobino",
     "Recebimento de Materiais de Inox para Fabricação de Suportes",
     "—",
     date(2026,5,8), date(2026,5,8),
     "Materiais de inox recebidos para fabricação dos suportes"),

    ("07/05/2026","Citostático","[ELET][DOC]","ABELV",
     "Leobino",
     "Confecção da MC de Aterramento",
     "—",
     date(2026,5,8), date(2026,5,11), ""),

    ("07/05/2026","Citostático","[DOC][CIVIL]","Krrom",
     "Diego / Leobino",
     "Envio da Documentação do Topógrafo",
     "—",
     date(2026,5,11), date(2026,5,15), ""),

    ("07/05/2026","Citostático","[CIVIL][SUP]","ABELV",
     "Leobino",
     "Chegada de Materiais para os Diques do Piso Técnico",
     "—",
     date(2026,5,11), date(2026,5,11),
     "Pendente remoção de vidros da Sala Limpa, porém não é mais crítico para paralisação da obra"),

    ("07/05/2026","Citostático","[MEC/TUB]","ABELV",
     "Leobino",
     "Montagem do Pipe Shop de Aço Carbono no Canteiro de Obra",
     "Impacta o início da fabricação de tubulação de aço carbono",
     date(2026,5,11), None,
     "Prazo de conclusão revisado para 11/08/2026 — obra em andamento"),

    ("07/05/2026","Citostático","[MEC/TUB][SUP]","ABELV",
     "Elson",
     "Contratação do Munk",
     "—",
     date(2026,5,11), date(2026,5,11), ""),

    ("07/05/2026","Citostático","[PROC][SUP]","ABELV",
     "Uehara",
     "Contratação da Empresa Lavador de Gases",
     "—",
     date(2026,5,14), None,
     "19/05: Aguardando o Setor de Suprimentos da ABELV fechar o pedido"),

    ("07/05/2026","Citostático","[PROC][DOC]","ABELV",
     "Leobino",
     "Recebimento do Projeto do Radier do Lavador de Gases",
     "—",
     date(2026,5,15), date(2026,5,18), ""),

    ("07/05/2026","Citostático","[CIVIL][SUP]","Krrom",
     "Diego / Leobino",
     "Mobilização da Krrom para Execução dos Diques do Piso Técnico",
     "—",
     date(2026,5,20), date(2026,5,11),
     "Concluído 9 dias antes do prazo"),

    # ── 08/05/2026 — Citostático ──────────────────────────
    ("08/05/2026","Citostático","[SUP][SMS]","ABELV",
     "Vladimir / Keite",
     "Instalação de Placas de Identificação nas Frentes de Serviço",
     "—",
     date(2026,5,8), date(2026,5,11), ""),

    ("08/05/2026","Citostático","[CIVIL][MEC/TUB]","ABELV",
     "Mateus",
     "Verificação de Interferência nas Bases da Sala do Citostático",
     "—",
     date(2026,5,8), date(2026,5,8), ""),

    ("08/05/2026","Citostático","[CIVIL][SUP]","Krrom",
     "Leobino",
     "Movimentação dos Containers da Krrom",
     "—",
     date(2026,5,8), date(2026,5,8), ""),

    ("08/05/2026","Citostático","[SUP]","Krrom",
     "Elson / Leobino",
     "Confirmação da Data de Entrega do Banheiro da Krrom com Edimar",
     "—",
     date(2026,5,8), date(2026,5,11),
     "Data confirmada com Edimar (Mestre de Obras Krrom)"),

    ("08/05/2026","Citostático","[SUP][DOC]","ABELV",
     "Tiago",
     "Instalação da Placa de Identificação da Obra",
     "—",
     date(2026,5,8), date(2026,5,11), ""),

    ("08/05/2026","Citostático","[CIVIL][SUP]","ABELV",
     "Leobino / Keite",
     "Contratação de Empresa para Bota Fora (MC)",
     "—",
     date(2026,5,11), date(2026,5,11), ""),

    ("08/05/2026","Citostático","[MEC/TUB][SUP]","ABELV",
     "Elson",
     "Contratação do Munk (novo serviço)",
     "—",
     date(2026,5,11), date(2026,5,11), ""),

    ("08/05/2026","Farmoquímico","[CIVIL]","Krrom",
     "Leobino",
     "Instalação dos Portões na Vedação de Tapume — Farmoquímico",
     "—",
     date(2026,5,15), None,
     "19/05: Aguardando complemento de efetivo — apenas 1 soldador disponível"),

    ("08/05/2026","Farmoquímico","[ELET]","ABELV",
     "Diego / Leobino / Alexandre",
     "Instalação da Iluminação do Farmoquímico",
     "—",
     date(2026,5,15), date(2026,5,18), ""),

    ("08/05/2026","Citostático","[PROC][SMS]","ABELV",
     "Keite",
     "Definição do PAE — Plano de Atendimento de Emergência",
     "—",
     date(2026,5,15), None,
     "19/05: Aguardando avaliação do GP Tiago"),

    ("08/05/2026","Citostático","[ELET]","ABELV",
     "Tiago",
     "Solicitação de Terrômetro para Laudo de Aterramento",
     "—",
     date(2026,5,15), date(2026,5,18), ""),

    ("08/05/2026","Citostático","[CIVIL][SUP]","Krrom",
     "Diego / Leobino",
     "Elaboração do Layout do Canteiro da Krrom",
     "—",
     date(2026,5,15), None, ""),

    # ── 12/05/2026 ────────────────────────────────────────
    ("12/05/2026","Citostático","[MEC/TUB][SUP]","ABELV",
     "Tiago",
     "Acompanhamento do Recebimento da Tubulação de Aço Carbono",
     "Impacta a Fabricação da Tubulação de Aço Carbono (Início Previsto: 25/05 — ID 54 e ID 317)",
     date(2026,5,15), date(2026,5,15), ""),

    ("12/05/2026","Citostático","[PROC][SUP]","ABELV",
     "Uehara",
     "Contratação da Empresa Lavador de Gases",
     "Impacta o processo crítico do Citostático",
     date(2026,5,15), None,
     "19/05: Aguardando o Setor de Suprimentos da ABELV fechar o pedido"),

    ("12/05/2026","Citostático","[MEC/TUB][SUP]","ABELV",
     "Tiago",
     "Acompanhamento do Recebimento das Conexões de Aço Carbono",
     "Impacta a Fabricação da Tubulação de Aço Carbono (Início Previsto: 25/05 — ID 54 e ID 317)",
     date(2026,5,19), None, ""),

    ("12/05/2026","Farmoquímico","[CIVIL][SUP]","Krrom",
     "Diego / Leobino",
     "Definição do Tipo de Fundação do Prédio — Farmoquímico",
     "Impacta a contratação de empresa para execução de estacas (Início Previsto: 08/06 — ID 118)",
     date(2026,5,13), None, ""),

    ("12/05/2026","Farmoquímico","[CIVIL][DOC]","Cristália",
     "Edson / Leobino",
     "Recebimento do Projeto da Base do Lavador de Gases Existente — Farmoquímico",
     "Impacta a formalização da nova locação e a confecção do Radier da Base (Início Previsto: 05/06 — ID 251)",
     date(2026,5,15), None, ""),

    # ── 14/05/2026 ────────────────────────────────────────
    ("14/05/2026","Citostático","[CIVIL][DOC]","Cristália",
     "Edson / Leobino",
     "Definição da Locação da Plataforma dos Reatores para a Nova Linha Hidrossanitária",
     "Impacta o Corte do Piso para a Plataforma dos Reatores (Início Previsto: 21/05 — ID 22) "
     "e a Demolição do Piso para a Rede Hidrossanitária (Início Previsto: 18/05 — ID 58)",
     date(2026,5,18), None, ""),

    # ── 15/05/2026 ────────────────────────────────────────
    ("15/05/2026","Citostático","[PROC][DOC]","ABELV",
     "Uehara",
     "Validação da Mudança Dimensional da Base do Lavador de Gases",
     "Impacta a Demolição do Piso do Radier do Lavador de Gases em caso de mudança significativa "
     "(Início Previsto: 25/05 — ID 466)",
     date(2026,5,20), None, ""),

    # ── 19/05/2026 — Citostático ──────────────────────────
    ("19/05/2026","Citostático","[CIVIL][DOC]","Cristália",
     "Edson / Leobino",
     "Retirada de 2 Peças de Vidro da Sala Limpa para Liberação da Marcação das Bases",
     "Impede a continuação da Locação das Bases da Sala Limpa",
     date(2026,5,19), None, ""),

    ("19/05/2026","Citostático","[SUP]","ABELV",
     "Ana Assis",
     "Fechamento do Pedido de Compra do Lavador de Gases",
     "Impacta a identificação do dimensional da base do Lavador e a Demolição do Radier "
     "(Início Previsto: 25/05 — ID 466)",
     date(2026,5,19), None, ""),

    ("19/05/2026","Citostático","[CIVIL][DOC]","Krrom",
     "Diego / Leobino",
     "Apresentação da Metodologia de Corte do Piso para Execução da Plataforma dos Reatores",
     "Impacta o Corte do Piso (Início Previsto: 21/05 — ID 22) e a Demolição do Piso para "
     "Rede Hidrossanitária (Início Previsto: 18/05 — ID 58)",
     date(2026,5,20), None, ""),

    ("19/05/2026","Citostático","[SUP]","Krrom",
     "Tiago / Celso",
     "Verificação do Efetivo de Andaime para as Obras",
     "Impacta o acesso para realização das Frentes de Montagem",
     date(2026,5,20), None, ""),

    ("19/05/2026","Citostático","[MEC/TUB]","ABELV",
     "Leobino",
     "Montagem do Pipe Shop de Aço Carbono no Canteiro de Obra",
     "Impacta a Fabricação da Tubulação de Aço Carbono (Início Previsto: 25/05 — ID 54 e ID 317)",
     date(2026,5,20), None, ""),

    ("19/05/2026","Citostático","[SUP][DOC]","ABELV",
     "Erik Massola / Tiago",
     "Envio do Efetivo da Açoplast (Nomes e CPFs) para Aprovação Social pela Cristália",
     "Sem aprovação social, os colaboradores não poderão acessar o canteiro, "
     "podendo impactar o prazo da obra",
     date(2026,5,20), None, ""),

    ("19/05/2026","Citostático","[SUP]","ABELV",
     "Edimar Cunha / Tiago",
     "Contratação do Fornecedor de Andaime",
     "Impacta o acesso para realização das Frentes de Montagem",
     date(2026,5,22), None, ""),

    # ── 19/05/2026 — Farmoquímico ─────────────────────────
    ("19/05/2026","Farmoquímico","[DOC]","MGC",
     "Yohanna",
     "Solicitação e Recebimento dos Projetos do Farmoquímico da MGC para Aprovação pela Cristália",
     "Impacta a Compra de Materiais e as Subcontratações para execução",
     date(2026,5,19), None, ""),

    ("19/05/2026","Farmoquímico","[DOC]","ABELV",
     "Leobino",
     "Envio das Cotas de Elevação do Lavador de Gases para a MGC",
     "Impacta a confecção do Projeto do Radier do Lavador de Gases",
     date(2026,5,19), None, ""),

    ("19/05/2026","Farmoquímico","[DOC][SUP]","Krrom",
     "Diego / Leobino",
     "Informar à ABELV a Data em que a Krrom Irá Apresentar o Tipo de Fundação do Farmoquímico",
     "Impacta a contratação de empresa para execução de estacas (Início Previsto: 08/06 — ID 118)",
     date(2026,5,19), None, ""),

    ("19/05/2026","Farmoquímico","[SUP]","Krrom",
     "Rodrigo / Leobino",
     "Envio dos Pedidos de Faturamento Direto pela Krrom",
     "Impacta a Medição",
     date(2026,5,19), None, ""),

    ("19/05/2026","Farmoquímico","[DOC]","ABELV",
     "Leobino",
     "Envio das Cotas de Elevação da Sala Elétrica para a MGC",
     "Impacta a confecção do Projeto da Sala Elétrica",
     date(2026,5,20), None, ""),

    ("19/05/2026","Farmoquímico","[SUP][DOC]","Krrom",
     "Diego / Leobino",
     "Regularização da Documentação da Empresa Recicla (Bota Fora)",
     "Risco legal: subcontratação sem documentação adequada em caso de auditoria ou acidente",
     date(2026,5,21), None, ""),

    ("19/05/2026","Farmoquímico","[MEC/TUB][SUP]","Krrom",
     "Diego / Leobino",
     "Elaboração do Pedido de Compra da Tubulação de Água Pluvial",
     "Impacta a Compra da Tubulação de Água Pluvial",
     date(2026,5,27), None, ""),
]

# ============================================================
# WORKBOOK
# ============================================================
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Restrições"

# ── Cabeçalhos ───────────────────────────────────────────────
headers = [
    "#", "Data\nReunião", "Projeto", "Disciplina",
    "Empresa\nResponsável", "Responsável",
    "Atividade", "Impacto",
    "Prazo", "Data\nConclusão",
    "Dias de\nAtraso", "Status", "Observação"
]
COL_STATUS = 12   # L
COL_DIAS   = 11   # K
COL_PRAZO  = 9    # I
COL_CONC   = 10   # J
N_COLS     = 13

# Larguras
col_widths = [5, 12, 13, 18, 16, 22, 50, 45, 12, 14, 10, 22, 40]

for i, w in enumerate(col_widths, 1):
    ws.column_dimensions[get_column_letter(i)].width = w

ws.row_dimensions[1].height = 36

# Escrever cabeçalhos
for col, h in enumerate(headers, 1):
    c = ws.cell(row=1, column=col, value=h)
    c.fill   = pf(C_HEADER_BG)
    c.font   = ft(bold=True, color=C_HEADER_FG, size=10)
    c.alignment = al(h="center", v="center", wrap=True)
    c.border = border_thin()

# ── Dados ────────────────────────────────────────────────────
for idx, row in enumerate(dados, 1):
    r = idx + 1  # linha Excel
    data_reu, projeto, disc, empresa, resp, ativ, imp, prazo, conc, obs = row

    status    = calc_status(prazo, conc)
    dias_atr  = calc_dias(prazo, conc)

    # Cor de fundo da linha por projeto
    proj_bg = C_CISTO_BG if projeto == "Citostático" else C_FARMO_BG

    values = [
        idx, data_reu, projeto, disc, empresa, resp,
        ativ, imp, prazo, conc,
        dias_atr, status, obs
    ]

    for col, val in enumerate(values, 1):
        c = ws.cell(row=r, column=col, value=val)
        c.border    = border_thin()
        c.alignment = al(h="left", v="center", wrap=True)

        # Formatação de datas
        if col in (COL_PRAZO, COL_CONC) and isinstance(val, date):
            c.number_format = "DD/MM/YYYY"
            c.alignment = al(h="center", v="center")

        # Número centrado
        if col in (1, COL_DIAS):
            c.alignment = al(h="center", v="center")

        # Cor dos dias de atraso
        if col == COL_DIAS:
            if dias_atr > 0:
                c.font = ft(bold=True, color=C_ATRASADO_FG)
            else:
                c.font = ft(color="375623")

        # Cor do status
        if col == COL_STATUS:
            if status == "NO PRAZO":
                c.fill = pf(C_NO_PRAZO_BG)
                c.font = ft(bold=True, color=C_NO_PRAZO_FG)
            elif status == "ALERTA":
                c.fill = pf(C_ALERTA_BG)
                c.font = ft(bold=True, color=C_ALERTA_FG)
            elif status == "ATRASADO":
                c.fill = pf(C_ATRASADO_BG)
                c.font = ft(bold=True, color=C_ATRASADO_FG)
            elif status == "CONCLUÍDO":
                c.fill = pf(C_CONC_BG)
                c.font = ft(bold=True, color=C_CONC_FG)
            elif status == "CONCLUÍDO COM ATRASO":
                c.fill = pf(C_CONC_ATR_BG)
                c.font = ft(bold=True, color=C_CONC_ATR_FG)

        # Cor de fundo da linha (exceto status)
        elif col != COL_STATUS:
            if status == "ATRASADO":
                c.fill = pf("FFE0E0") # vermelho bem claro para linha
            else:
                c.fill = pf(proj_bg)

    ws.row_dimensions[r].height = 30

# ── Congelar linha 1 + auto-filtro ────────────────────────────
ws.freeze_panes = "A2"
ws.auto_filter.ref = f"A1:{get_column_letter(N_COLS)}{len(dados)+1}"

# ── Legenda de status (canto superior direito) ───────────────
legenda_col = N_COLS + 2  # coluna O
ws.cell(row=1, column=legenda_col, value="LEGENDA DE STATUS").fill = pf(C_HEADER_BG)
ws.cell(row=1, column=legenda_col).font = ft(bold=True, color="FFFFFF")
ws.cell(row=1, column=legenda_col).alignment = al()
ws.column_dimensions[get_column_letter(legenda_col)].width = 24

legendas = [
    ("NO PRAZO",             C_NO_PRAZO_BG, C_NO_PRAZO_FG),
    ("ALERTA (vence hoje)",  C_ALERTA_BG,   C_ALERTA_FG),
    ("ATRASADO",             C_ATRASADO_BG, C_ATRASADO_FG),
    ("CONCLUÍDO",            C_CONC_BG,     C_CONC_FG),
    ("CONCLUÍDO COM ATRASO", C_CONC_ATR_BG, C_CONC_ATR_FG),
]
for i, (lbl, bg, fg) in enumerate(legendas, 2):
    c = ws.cell(row=i, column=legenda_col, value=lbl)
    c.fill = pf(bg)
    c.font = ft(bold=True, color=fg)
    c.alignment = al(h="center")
    c.border = border_thin()

# ============================================================
# ABA RESUMO / DASHBOARD
# ============================================================
wd = wb.create_sheet("Dashboard")
wd.sheet_view.showGridLines = False

def dash_title(ws, row, col, text, bg=C_HEADER_BG):
    c = ws.cell(row=row, column=col, value=text)
    c.fill  = pf(bg)
    c.font  = ft(bold=True, color="FFFFFF", size=11)
    c.alignment = al(h="center")
    c.border = border_thin()
    return c

def dash_cell(ws, row, col, val, bg="FFFFFF", bold=False, color="000000", h="left"):
    c = ws.cell(row=row, column=col, value=val)
    c.fill = pf(bg)
    c.font = ft(bold=bold, color=color)
    c.alignment = al(h=h)
    c.border = border_thin()
    return c

# Larguras
for i, w in enumerate([3, 30, 14, 3, 22, 10, 3, 22, 10], 1):
    wd.column_dimensions[get_column_letter(i)].width = w

# Título geral
wd.merge_cells("B1:I1")
c = wd.cell(row=1, column=2, value="DASHBOARD — RESTRIÇÕES | Cristália 25098 + 25103 | 19/05/2026")
c.fill = pf(C_HEADER_BG)
c.font = ft(bold=True, color="FFFFFF", size=13)
c.alignment = al(h="center")
wd.row_dimensions[1].height = 30

# ── Bloco 1: Por Status ───────────────────────────────────────
status_list = [calc_status(d[7], d[8]) for d in dados]
status_count = Counter(status_list)
order_status = ["ATRASADO", "ALERTA", "CONCLUÍDO COM ATRASO", "CONCLUÍDO", "NO PRAZO"]
status_colors = {
    "ATRASADO":             (C_ATRASADO_BG, C_ATRASADO_FG),
    "ALERTA":               (C_ALERTA_BG,   C_ALERTA_FG),
    "CONCLUÍDO COM ATRASO": (C_CONC_ATR_BG, C_CONC_ATR_FG),
    "CONCLUÍDO":            (C_CONC_BG,     C_CONC_FG),
    "NO PRAZO":             (C_NO_PRAZO_BG, C_NO_PRAZO_FG),
}

wd.merge_cells("B3:C3")
dash_cell(wd, 3, 2, "POR STATUS — QTDE", bg=C_HEADER_BG, bold=True, color="FFFFFF", h="center")

for i, s in enumerate(order_status, 4):
    bg, fg = status_colors[s]
    dash_cell(wd, i, 2, s,                   bg=bg, bold=True, color=fg)
    dash_cell(wd, i, 3, status_count.get(s,0), bg=bg, bold=True, color=fg, h="center")

total_row = 4 + len(order_status)
dash_cell(wd, total_row, 2, "TOTAL", bg="1F4E79", bold=True, color="FFFFFF")
dash_cell(wd, total_row, 3, len(dados), bg="1F4E79", bold=True, color="FFFFFF", h="center")

# ── Bloco 2: Por Projeto ─────────────────────────────────────
proj_count = Counter(d[1] for d in dados)
wd.merge_cells("E3:F3")
dash_cell(wd, 3, 5, "POR PROJETO — QTDE", bg=C_HEADER_BG, bold=True, color="FFFFFF", h="center")

proj_colors = {"Citostático": (C_CISTO_BG, "17375E"), "Farmoquímico": (C_FARMO_BG, "7F4F00")}
for i, (proj, cnt) in enumerate(sorted(proj_count.items()), 4):
    bg, fg = proj_colors.get(proj, ("FFFFFF","000000"))
    dash_cell(wd, i, 5, proj, bg=bg, bold=True, color=fg)
    dash_cell(wd, i, 6, cnt,  bg=bg, bold=True, color=fg, h="center")

# ── Bloco 3: Por Disciplina ───────────────────────────────────
# Extrair disciplinas individuais
from collections import defaultdict
disc_count = defaultdict(int)
for d in dados:
    tags = d[2].replace("][","],[").split(",")
    for t in tags:
        t = t.strip().strip("[]")
        if t:
            disc_count[t] += 1

wd.merge_cells("H3:I3")
dash_cell(wd, 3, 8, "POR DISCIPLINA — QTDE", bg=C_HEADER_BG, bold=True, color="FFFFFF", h="center")

disc_order = ["CIVIL","MEC/TUB","ELET","SUP","PROC","DOC","SMS"]
disc_colors = {
    "CIVIL":   ("E2EFDA","375623"), "MEC/TUB": ("D9E1F2","17375E"),
    "ELET":    ("FFF2CC","7F4F00"), "SUP":     ("FCE4D6","843C0C"),
    "PROC":    ("E2EFDA","375623"), "DOC":     ("EDEDED","404040"),
    "SMS":     ("FFE0CC","7F3F00"),
}
for i, disc in enumerate(disc_order, 4):
    bg, fg = disc_colors.get(disc, ("FFFFFF","000000"))
    dash_cell(wd, i, 8, disc,              bg=bg, bold=True, color=fg)
    dash_cell(wd, i, 9, disc_count.get(disc,0), bg=bg, bold=True, color=fg, h="center")

# ── Bloco 4: Atrasados por responsável ───────────────────────
resp_atr = Counter(d[4] for d in dados if calc_status(d[7],d[8]) == "ATRASADO")
wd.row_dimensions[12].height = 8

wd.merge_cells("B13:C13")
dash_cell(wd, 13, 2, "RESPONSÁVEIS COM MAIS ITENS ATRASADOS", bg=C_HEADER_BG, bold=True, color="FFFFFF", h="center")

for i, (resp, cnt) in enumerate(resp_atr.most_common(8), 14):
    dash_cell(wd, i, 2, resp, bg=C_ATRASADO_BG, color=C_ATRASADO_FG)
    dash_cell(wd, i, 3, cnt,  bg=C_ATRASADO_BG, bold=True, color=C_ATRASADO_FG, h="center")

# ── Bloco 5: Alerta — vence hoje ─────────────────────────────
alertas = [(d[4], d[6], d[7]) for d in dados if calc_status(d[7],d[8]) == "ALERTA"]
wd.merge_cells("E13:F13")
dash_cell(wd, 13, 5, "⚠ ALERTA — VENCE HOJE (19/05)", bg=C_ALERTA_BG, bold=True, color=C_ALERTA_FG, h="center")
for i, (resp, ativ, prazo) in enumerate(alertas, 14):
    dash_cell(wd, i, 5, resp, bg=C_ALERTA_BG, color=C_ALERTA_FG)
    c = wd.cell(row=i, column=6, value=ativ[:60]+"…" if len(ativ)>60 else ativ)
    c.fill = pf(C_ALERTA_BG)
    c.font = ft(color=C_ALERTA_FG)
    c.border = border_thin()
    c.alignment = al(h="left", wrap=True)
    wd.row_dimensions[i].height = 28

# ============================================================
# SALVAR
# ============================================================
output_path = "/home/user/meu-planejamento/Restricoes_Consolidadas_Cristalia_19052026.xlsx"
wb.save(output_path)
print(f"✅ Arquivo salvo: {output_path}")
print(f"   Total de registros: {len(dados)}")
print(f"   Status summary: {dict(Counter(status_list))}")
