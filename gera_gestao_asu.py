#!/usr/bin/env python3
"""Gerador GESTAO_RESTRICOES_ASU_JUNDIAI — script canônico do projeto 26001.
Mesmo padrão visual aprovado em S24b (ver MAPA_INSTRUCOES_CONECTOR.md seção 11).
Atualizar DADOS in-place a cada sessão. Não renomear."""

from openpyxl import Workbook
from openpyxl.styles import PatternFill, Font, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from datetime import date

HOJE = date(2026, 6, 22)

COR = {
    'ATRASADO':   {'bg':'FFC7CE','fg':'9C0006','row':'FFE0E0'},
    'ALERTA':     {'bg':'FFEB9C','fg':'7F6000','row':'FFE0E0'},
    'CC ATRASO':  {'bg':'FFF2CC','fg':'7F4F00','row':'FFF2CC'},
    'CONCLUIDO':  {'bg':'DAEEF3','fg':'17375E','row':'DAEEF3'},
    'NO PRAZO':   {'bg':'C6EFCE','fg':'375623','row':'EBF3FB'},
}

def fill(hex_c):
    return PatternFill('solid', fgColor=hex_c) if hex_c else None

def font(hex_c=None, bold=False, sz=11):
    return Font(color=hex_c or '000000', bold=bold, size=sz)

def thin():
    s = Side(style='thin', color='AAAAAA')
    return Border(left=s, right=s, top=s, bottom=s)

def center(wrap=False):
    return Alignment(horizontal='center', vertical='center', wrap_text=wrap)

def left(wrap=False):
    return Alignment(horizontal='left', vertical='center', wrap_text=wrap)

def status_key(s):
    su = s.upper()
    if 'CONCLU' in su and 'ATRASO' in su: return 'CC ATRASO'
    if 'ATRASADO' in su: return 'ATRASADO'
    if 'ALERTA' in su: return 'ALERTA'
    if 'CONCLU' in su: return 'CONCLUIDO'
    return 'NO PRAZO'

# ─── DADOS ────────────────────────────────────────────────────────────────────
# Colunas: id, proj, disc, empresa, responsavel, descricao, impacto, nec, obs, conc, dias, status_raw
RESTRICOES = [
    (1, '26001', 'Elétrica', 'CPFL', 'Sem nome',
     'Chegada da linha de transmissão (LT) no canteiro de obras por parte da concessionária de energia elétrica, para atendimento à nova planta da ASU Messer Jundiaí',
     'Fornecimento de energia para a nova subestação elétrica da nova base; o não atendimento impede a partida da planta',
     '15/09/26', '—', '—', 0, 'NO PRAZO'),
    (2, '26001', 'Civil', 'Prefeitura de Jundiaí', 'Sem nome',
     'Obtenção e emissão da Licença de Construção (Alvará de Construção) junto aos órgãos municipais competentes, para autorização de início das atividades físicas em campo no canteiro de obras da ASU Messer Jundiaí',
     'Não libera o início das atividades de Civil (fase posterior do projeto); após a emissão, a Messer ainda precisa de 2 semanas para finalizar a contratação da empresa de Civil e mais 1 mês para mobilização dessa empresa, atrasando o início efetivo da obra',
     '10/08/26', '12/06/26: a solicitação da Licença de Construção foi protocolada em maio/2025. Em maio/2026 a Prefeitura enviou uma diligência à Messer; 2 semanas depois a Messer atendeu novamente o que a Prefeitura solicitava. Prazo até 10/08/26 para emissão da licença, caso não haja nova diligência.',
     '—', 0, 'NO PRAZO'),
]

# ─── WORKBOOK ─────────────────────────────────────────────────────────────────
wb = Workbook()
ws = wb.active
ws.title = 'GESTAO_ASU'

# ─── BLOCO 1: Título ──────────────────────────────────────────────────────────
ws.merge_cells('A1:M1')
ws['A1'] = '⚙️  GESTÃO DE RESTRIÇÕES — ASU JUNDIAÍ (OTZ × MESSER) | 22/06/2026 | Semana S28'
ws['A1'].fill = fill('1F3864')
ws['A1'].font = Font(color='FFFFFF', bold=True, size=14)
ws['A1'].alignment = center()
ws.row_dimensions[1].height = 30

ws.merge_cells('A2:M2')
ws['A2'] = 'Projeto 26001 ASUOTZGERAP0020 | Conector: Claude | Operador: Ministro'
ws['A2'].fill = fill('2E4057')
ws['A2'].font = Font(color='CCCCCC', bold=False, size=11)
ws['A2'].alignment = center()
ws.row_dimensions[2].height = 20

# ─── BLOCO 2: Totais Gerais ───────────────────────────────────────────────────
row = 4
ws.merge_cells(f'A{row}:M{row}')
ws[f'A{row}'] = '📊  TOTAIS CONSOLIDADOS — PROJETO 26001'
ws[f'A{row}'].fill = fill('17375E')
ws[f'A{row}'].font = Font(color='FFFFFF', bold=True, size=12)
ws[f'A{row}'].alignment = center()

row += 1
totals_hdr = ['TOTAL','ATRASADO','ALERTA','CC ATRASO','CONCLUÍDO','NO PRAZO']
total = len(RESTRICOES)
at = sum(1 for r in RESTRICOES if status_key(r[11]) == 'ATRASADO')
al = sum(1 for r in RESTRICOES if status_key(r[11]) == 'ALERTA')
cc = sum(1 for r in RESTRICOES if status_key(r[11]) == 'CC ATRASO')
co = sum(1 for r in RESTRICOES if status_key(r[11]) == 'CONCLUIDO')
npz = sum(1 for r in RESTRICOES if status_key(r[11]) == 'NO PRAZO')
totals_val = [total, at, al, cc, co, npz]
totals_col = ['DDDDDD','FFC7CE','FFEB9C','FFF2CC','DAEEF3','C6EFCE']
totals_fg  = ['000000','9C0006','7F6000','7F4F00','17375E','375623']
col_span = [('A','B'),('C','D'),('E','F'),('G','H'),('I','J'),('K','M')]
for i,(cs,ce) in enumerate(col_span):
    ws.merge_cells(f'{cs}{row}:{ce}{row}')
    ws[f'{cs}{row}'] = totals_hdr[i]
    ws[f'{cs}{row}'].fill = fill('17375E')
    ws[f'{cs}{row}'].font = Font(color='FFFFFF', bold=True, size=11)
    ws[f'{cs}{row}'].alignment = center()

row += 1
for i,(cs,ce) in enumerate(col_span):
    ws.merge_cells(f'{cs}{row}:{ce}{row}')
    ws[f'{cs}{row}'] = totals_val[i]
    ws[f'{cs}{row}'].fill = fill(totals_col[i])
    ws[f'{cs}{row}'].font = Font(color=totals_fg[i], bold=True, size=18)
    ws[f'{cs}{row}'].alignment = center()
ws.row_dimensions[row].height = 36

# ─── BLOCO 3: Atrasados/Alerta por Empresa (FORTUNE / MESSER) ───────────────
row += 2
ws.merge_cells(f'A{row}:M{row}')
ws[f'A{row}'] = '🏢  ATRASADOS/ALERTA POR EMPRESA (abertos)'
ws[f'A{row}'].fill = fill('17375E')
ws[f'A{row}'].font = Font(color='FFFFFF', bold=True, size=12)
ws[f'A{row}'].alignment = center()

empresas = {}
for r in RESTRICOES:
    st = status_key(r[11])
    if st in ('ATRASADO','ALERTA'):
        emp = r[3]
        empresas[emp] = empresas.get(emp,0) + 1

row += 1
emp_hdr = ['EMPRESA','QTDE ATRASADOS/ALERTA']
col_span2 = [('A','E'),('F','M')]
for i,(cs,ce) in enumerate(col_span2):
    ws.merge_cells(f'{cs}{row}:{ce}{row}')
    ws[f'{cs}{row}'] = emp_hdr[i]
    ws[f'{cs}{row}'].fill = fill('2E4057')
    ws[f'{cs}{row}'].font = Font(color='FFFFFF', bold=True, size=10)
    ws[f'{cs}{row}'].alignment = center()

for emp in sorted(empresas, key=lambda x: -empresas[x]):
    row += 1
    ws.merge_cells(f'A{row}:E{row}')
    ws[f'A{row}'] = emp
    ws[f'A{row}'].fill = fill('FFF2CC')
    ws[f'A{row}'].font = font(bold=True)
    ws[f'A{row}'].alignment = center()
    ws.merge_cells(f'F{row}:M{row}')
    ws[f'F{row}'] = empresas[emp]
    ws[f'F{row}'].fill = fill('FFC7CE')
    ws[f'F{row}'].font = Font(color='9C0006', bold=True, size=13)
    ws[f'F{row}'].alignment = center()

# ─── BLOCO 4: Top urgentes (maior dias de atraso) ────────────────────────────
row += 2
ws.merge_cells(f'A{row}:M{row}')
ws[f'A{row}'] = '🔥  MAIS URGENTES — MAIOR DIAS DE ATRASO (abertos)'
ws[f'A{row}'].fill = fill('17375E')
ws[f'A{row}'].font = Font(color='FFFFFF', bold=True, size=12)
ws[f'A{row}'].alignment = center()

abertos_at = [(r[0],r[1],r[4],r[5],r[10]) for r in RESTRICOES if status_key(r[11]) in ('ATRASADO','ALERTA')]
abertos_at.sort(key=lambda x:-x[4])

row += 1
top_hdrs = ['ID','PROJ','RESPONSÁVEL','DESCRIÇÃO','DIAS ATRASO']
top_cols = [('A','A'),('B','B'),('C','D'),('E','J'),('K','M')]
for i,(cs,ce) in enumerate(top_cols):
    ws.merge_cells(f'{cs}{row}:{ce}{row}')
    ws[f'{cs}{row}'] = top_hdrs[i]
    ws[f'{cs}{row}'].fill = fill('2E4057')
    ws[f'{cs}{row}'].font = Font(color='FFFFFF', bold=True, size=10)
    ws[f'{cs}{row}'].alignment = center()

for rid, proj, resp, desc, dias in abertos_at[:5]:
    row += 1
    vals = [rid, proj, resp, desc, dias]
    for i,(cs,ce) in enumerate(top_cols):
        ws.merge_cells(f'{cs}{row}:{ce}{row}')
        ws[f'{cs}{row}'] = vals[i]
        ws[f'{cs}{row}'].fill = fill('EBF3FB')
        ws[f'{cs}{row}'].font = font(bold=(i==4), sz=11 if i<4 else 14)
        ws[f'{cs}{row}'].alignment = left(wrap=True) if i==3 else center()
    ws.row_dimensions[row].height = 24

# ─── BLOCO 5: Vencendo hoje ───────────────────────────────────────────────────
row += 2
ws.merge_cells(f'A{row}:M{row}')
ws[f'A{row}'] = '⏰  VENCENDO HOJE (22/06) — EM ABERTO'
ws[f'A{row}'].fill = fill('17375E')
ws[f'A{row}'].font = Font(color='FFFFFF', bold=True, size=12)
ws[f'A{row}'].alignment = center()

def parse_date(s):
    if not s or s == '—': return None
    try:
        p = s.split('/')
        return date(int('20'+p[2]), int(p[1]), int(p[0]))
    except: return None

venc = []
for r in RESTRICOES:
    st = status_key(r[11])
    if st in ('NO PRAZO','ALERTA'):
        d = parse_date(r[7])
        if d and d == HOJE:
            venc.append((r[0],r[1],r[4],r[5],r[7]))

row += 1
for i,(cs,ce) in enumerate(top_cols):
    ws.merge_cells(f'{cs}{row}:{ce}{row}')
    ws[f'{cs}{row}'] = ['ID','PROJ','RESPONSÁVEL','DESCRIÇÃO','NECESSIDADE'][i]
    ws[f'{cs}{row}'].fill = fill('2E4057')
    ws[f'{cs}{row}'].font = Font(color='FFFFFF', bold=True, size=10)
    ws[f'{cs}{row}'].alignment = center()

if venc:
    for rid, proj, resp, desc, nec in venc:
        row += 1
        for i,(cs,ce) in enumerate(top_cols):
            ws.merge_cells(f'{cs}{row}:{ce}{row}')
            ws[f'{cs}{row}'] = [rid, proj, resp, desc, nec][i]
            ws[f'{cs}{row}'].fill = fill('FFEB9C')
            ws[f'{cs}{row}'].font = font(sz=11)
            ws[f'{cs}{row}'].alignment = left(wrap=True) if i==3 else center()
        ws.row_dimensions[row].height = 22
else:
    row += 1
    ws.merge_cells(f'A{row}:M{row}')
    ws[f'A{row}'] = 'Nenhum item vence hoje ✅'
    ws[f'A{row}'].fill = fill('C6EFCE')
    ws[f'A{row}'].font = Font(color='375623', bold=True, size=11)
    ws[f'A{row}'].alignment = center()

# ─── ABA DETALHAMENTO ─────────────────────────────────────────────────────────
ws2 = wb.create_sheet('DETALHAMENTO')

HDR = ['ID','PROJETO','DISC.','EMPRESA','RESPONSÁVEL','DESCRIÇÃO','IMPACTO','NECESSIDADE','OBSERVAÇÃO','CONCLUSÃO','DIAS ATRASO','STATUS']
ws2.freeze_panes = 'A2'

for c, h in enumerate(HDR, 1):
    cell = ws2.cell(row=1, column=c, value=h)
    cell.fill = fill('1F3864')
    cell.font = Font(color='FFFFFF', bold=True, size=10)
    cell.alignment = center(wrap=True)
    cell.border = thin()

widths = [5, 8, 10, 10, 18, 55, 45, 10, 50, 10, 8, 20]
for i, w in enumerate(widths, 1):
    ws2.column_dimensions[get_column_letter(i)].width = w

for r_idx, r in enumerate(RESTRICOES, 2):
    rid, proj, disc, emp, resp, desc, imp, nec, obs, conc, dias, status_raw = r
    sk = status_key(status_raw)
    row_bg = COR.get(sk,{}).get('row','FFFFFF')

    vals = [rid, proj, disc, emp, resp, desc, imp, nec, obs, conc, dias, status_raw]
    for c_idx, v in enumerate(vals, 1):
        cell = ws2.cell(row=r_idx, column=c_idx, value=v)
        cell.fill = fill(row_bg)
        cell.font = font(sz=10)
        cell.alignment = left(wrap=True) if c_idx in (6,7,9) else center(wrap=True)
        cell.border = thin()
    st_cell = ws2.cell(row=r_idx, column=12)
    st_cell.fill = fill(COR.get(sk,{}).get('bg','FFFFFF'))
    st_cell.font = Font(color=COR.get(sk,{}).get('fg','000000'), bold=True, size=10)
    ws2.row_dimensions[r_idx].height = 30

# ─── Salvar ───────────────────────────────────────────────────────────────────
out = '/tmp/GESTAO_RESTRICOES_ASU_JUNDIAI_220626.xlsx'
wb.save(out)
print(f'Salvo em: {out}')
print(f'Total de restrições: {len(RESTRICOES)}')
print(f'AT:{at} AL:{al} CC:{cc} CONC:{co} NP:{npz}  => Total: {at+al+cc+co+npz}')
