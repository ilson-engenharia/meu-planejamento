#!/usr/bin/env python3
"""Gerador GESTAO_RESTRICOES — script canônico. Atualizar DADOS in-place a cada sessão. Não renomear."""

from openpyxl import Workbook
from openpyxl.styles import PatternFill, Font, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from datetime import date

HOJE = date(2026, 5, 28)

# ─── Paleta de cores ──────────────────────────────────────────────────────────
COR = {
    'ATRASADO':   {'bg':'FFC7CE','fg':'9C0006','row':'FFE0E0'},
    'ALERTA':     {'bg':'FFEB9C','fg':'7F6000','row':'FFEB9C'},
    'CC ATRASO':  {'bg':'FFF2CC','fg':'7F4F00','row':'FFF2CC'},
    'CONCLUIDO':  {'bg':'DAEEF3','fg':'17375E','row':'DAEEF3'},
    'NO PRAZO':   {'bg':'C6EFCE','fg':'375623','row':'C6EFCE'},
}
CISTO_ROW = 'EBF3FB'
FARMO_ROW = 'FFF8E7'

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
    # ══════ CISTO 25098 ══════
    (1,  '25098','CIVIL',    'KRROM',     'Diego / Leobino',     'Mobilização da Krrom para Tarefa do Dique no Piso Técnico',                             '—',                                                                        '20/05/26','—',         '11/05/26', 0, 'CONCLUÍDO'),
    (2,  '25098','CIVIL',    'KRROM',     'Diego / Leobino',     'Recebimento de Materiais do Dique no Piso Técnico',                                      '—',                                                                        '11/05/26','—',         '11/05/26', 0, 'CONCLUÍDO'),
    (3,  '25098','CIVIL',    'CRISTÁLIA', 'Edson / Leobino',     'Retirada de 2 Peças de Vidro da Sala Limpa — impede continuidade da Marcação das Bases', 'Impede Locação das Bases na Sala Limpa',                                    '19/05/26','Equipe Abelv removeu o vidro.','28/05/26', 9, 'CONCLUÍDO COM ATRASO'),
    (4,  '25098','MEC/TUB',  'ABELV',     'Leobino',             'Chegada de Materiais para Fabricação da Tubulação do Trap',                              '—',                                                                        '07/05/26','MC elaborado, PC gerado. Material ainda não chegou ao canteiro.','—', 21,'ATRASADO'),
    (5,  '25098','CIVIL',    'CRISTÁLIA', 'Edson / Leobino',     'Definição da Cristália sobre Locação da Plataforma dos Reatores',                        'Impacta Corte do Piso Bases Plataforma Reatores e Demolição Piso Hidrossanitária','18/05/26','Locação definida como original em reunião 22/05.','22/05/26', 4, 'CONCLUÍDO COM ATRASO'),
    (6,  '25098','MEC/TUB',  'ABELV',     'Tiago',               'Acompanhamento / Recebimento das Conexões de Aço Carbono',                               'Impacta Fabricação Tubulação Aço Carbono (IDs 54 e 317). Início previsto 25/05/26','19/05/26','Conexões ainda não chegaram. Fabricação AC bloqueada desde 26/05.','—', 9, 'ALERTA'),
    (7,  '25098','MEC/TUB',  'ABELV',     'Tiago',               'Acompanhamento / Recebimento da Tubulação de Aço Carbono',                               'Impacta Fabricação Tubulação Aço Carbono (IDs 54 e 317)',                   '15/05/26','—',         '15/05/26', 0, 'CONCLUÍDO'),
    (8,  '25098','MEC/TUB',  'ABELV',     'Uehara / Leobino',    'Validar Mudança Dimensional da Base do Lavador de Gases',                                'Impacta Demolição Piso Radier Lavador (ID 466). Início previsto 25/05/26',   '20/05/26','Leobino: elevar base. KRROM liberada desde 22/05.','22/05/26', 2, 'CONCLUÍDO COM ATRASO'),
    (9,  '25098','PROC/SUP', 'ABELV',     'Uehara',              'Contratação Lavador de Gases',                                                           '—',                                                                        '15/05/26','Contratação finalizada confirmada em Reunião de Bom dia 27/05.','27/05/26',12,'CONCLUÍDO COM ATRASO'),
    (10, '25098','SUP',      'ABELV',     'Ana Assis / Tiago',   'Fechamento do Pedido de Compra do Lavador de Gases',                                     'Impacta identificação real do Dimensional da Base (ID 466)',                 '19/05/26','—',         '20/05/26', 1, 'CONCLUÍDO COM ATRASO'),
    (17, '25098','CIVIL',    'KRROM',     'Diego / Leobino',     'Metodologia de Corte do Piso para avaliar resistência',                                  'Impacta Corte do Piso Bases Plataforma Reatores e Demolição',                '20/05/26','KRROM apresentou Ensaio de Esclerometria.','20/05/26', 0, 'CONCLUÍDO'),
    (20, '25098','SUP/SMS',  'ABELV',     'Tiago / Celso',       'Verificação do Efetivo de Andaime para atendimento das Obras',                           'Impacto de acesso para realização das Frentes de Montagem',                  '20/05/26','—',         '20/05/26', 0, 'CONCLUÍDO'),
    (21, '25098','MEC/TUB',  'ABELV',     'Leobino',             'Montagem do Pipe-Shop de Aço Carbono no Canteiro de Obra ABELV',                         'Impacta Fabricação Tubulação Aço Carbono (IDs 54 e 317). Início previsto 25/05/26','20/05/26','—','20/05/26', 0, 'CONCLUÍDO'),
    (22, '25098','DOC/SUP',  'ABELV',     'Erik Massola / Tiago','Envio do Efetivo (Nomes e CPFs) da Açoplast para avaliação social da Cristália',          'Caso não aprovados, colaboradores não entram no site',                       '20/05/26','Setor de Compras enviou Efetivo Açoplast em 28/05.','28/05/26', 8, 'CONCLUÍDO COM ATRASO'),
    (23, '25098','SUP',      'ABELV',     'Edimar Cunha / Tiago','Contratação do Fornecedor de Andaime',                                                    'Impacto de acesso para realização das Frentes de Montagem',                  '22/05/26','—',         '—',        6, 'ATRASADO'),
    (25, '25098','MEC',      'ABELV',     'Yohanna',             'Verificação da readequação do Projeto da Plataforma dos Reatores',                        'Atraso na Fabricação do Projeto da Plataforma dos Reatores (ID 650)',         '20/05/26','Definido que Abelv assumirá elaboração do novo projeto.','22/05/26', 2, 'CONCLUÍDO COM ATRASO'),
    (26, '25098','MEC/CIVIL','CRISTÁLIA', 'Yohanna',             'Cristália elaborar Novo Projeto da Base do Filtro Secador',                               'Atraso na Construção da Nova Base do Filtro Secador (ID 9). Início previsto 20/05/26','20/05/26','—','—', 8, 'ATRASADO'),
    (27, '25098','CIVIL',    'CRISTÁLIA', 'Yohanna',             'Cristália apresentar Projeto da Nova Locação do Ralo do Sistema Hidrossanitário',         'Atraso na Conclusão do Corte do Piso para Novo Sistema Hidrossanitário (ID 59)','20/05/26','—','—', 8, 'ATRASADO'),
    (28, '25098','CIVIL',    'CRISTÁLIA', 'Leobino',             'Confirmação do Cliente sobre Aplicação de Tinta Asfáltica nos Diques do Piso Técnico',   '—',                                                                        '20/05/26','Edson orientou continuar conforme Projeto.','20/05/26', 0, 'CONCLUÍDO'),
    (29, '25098','DOC',      'ABELV',     'Ilson / Victor',      'Elaboração do Estudo de HH aplicado até 19/05/26',                                       '—',                                                                        '25/05/26','Prazo vencido em 25/05. Aguardando conclusão.','—', 3, 'ATRASADO'),
    (30, '25098','SMS/SUP',  'KRROM',     'Diego / Leobino',     'Compra/Projeção de Compra do Pluviômetro para medir precipitação na Obra',                'Registro de comprovação de impactos de chuvas no RDO',                       '20/05/26','Pluviômetro chegou ao site em 25/05/26.','25/05/26', 5, 'CONCLUÍDO COM ATRASO'),
    (31, '25098','MEC/TUB',  'ABELV',     'Celso',               'Emissão de Solicitação de Compra (SC) para Fabricação da Linha do Dreno do TRAP',         'Impacta Fabricação Linha do Trap (ID 169). Início previsto 25/05/26',         '21/05/26','MC elaborado, PC gerado (28/05).','28/05/26', 7, 'CONCLUÍDO COM ATRASO'),
    (32, '25098','CIVIL',    'ABELV',     'Leobino',             'Elaboração de CT sobre Aplicação da Tinta Asfáltica nos Diques do Pavimento Técnico',    'Impacta Pintura Asfáltica nos Diques do 1º Pavimento (ID 279). Início previsto 02/06/26','21/05/26','CT elaborada — confirmado 26/05.','25/05/26', 4, 'CONCLUÍDO COM ATRASO'),
    (33, '25098','CIVIL',    'ABELV',     'Leobino',             'Solicitação de Visita Técnica e documentação da GEOCOM para Ensaio de Esclerometria',     'Atraso no início da confecção das bases dos reatores (ID 22)',                '21/05/26','GEOCOM realizou o Ensaio de Esclerometria.','22/05/26', 1, 'CONCLUÍDO COM ATRASO'),
    (34, '25098','CIVIL',    'ABELV',     'Celso / Leobino',     'Confecção de Andaime de Proteção contra quedas para Furação da Laje do Citostático',      'Atraso no Início da Furação da Laje do Citostático (ID 284). Início previsto 15/06/26','08/06/26','—','—', 0, 'NO PRAZO'),
    (35, '25098','CIVIL/MEC','ABELV',     'Leobino',             'Elaboração de CT para Definição do Projeto dos Diques Técnicos',                          'Retrabalho nos Diques de Contenção do Piso Técnico (ID 276)',                 '21/05/26','Cancelada — Cristália enviou novo projeto em 22/05 resolvendo divergência.','22/05/26', 1, 'CONCLUÍDO COM ATRASO'),
    (36, '25098','MEC/CIVIL','ABELV',     'Yohanna',             'Levantamento Inicial do Quantitativo de Tintas para a Obra',                              '—',                                                                        '29/05/26','—',         '—',        0, 'NO PRAZO'),
    (37, '25098','CIVIL',    'CRISTÁLIA', 'Leobino',             'Solicitar à Cristália a Definição da Tinta Externa nos Diques de Contenção do Piso Técnico','Atraso na aplicação da Tinta Externa — Projeto Civil diverge do Mecânico',  '22/05/26','—',         '—',        6, 'ATRASADO'),
    (40, '25098','MEC',      'CRISTÁLIA', 'Edson / Yohanna',     'Cristália enviar Projetos dos Banhos Térmicos dos Reatores (BT-008,BT-009,BT-010)',       'Caso atrase, nova mudança no Projeto do Dique (ID 276), implicando retrabalho','28/05/26','—','—', 0, 'NO PRAZO'),
    (46, '25098','DOC/SUP',  'ABELV',     'Celso',               'Solicitar à Açoplast o preenchimento da Planilha Nominal para avaliação social Cristália', 'Impossibilidade de entrada no site — atraso na Fabricação dos Dutos de HVAC', '26/05/26','Planilha Nominal concluída e enviada em 27/05.','27/05/26', 1, 'CONCLUÍDO COM ATRASO'),
    (47, '25098','MEC/TUB',  'ABELV',     'Tiago',               'Chegada de material de tubulação de aço inox ao canteiro do Citostático',                 'Impacta início da fabricação de tubulação de aço inox',                      '26/05/26','Nenhum material de aço inox chegou ao canteiro (confirmado 28/05).','—', 2, 'ATRASADO'),
    (48, '25098','ELET',     'ABELV',     'Alexandre',           'Chegada das conexões de eletroduto ao canteiro — somente dutos retos chegaram em 27/05',  'Impacta instalação de eletroduto no Citostático',                            '27/05/26','Dutos retos chegaram. Conexões não chegaram.','—', 1, 'ATRASADO'),
    (49, '25098','MEC/TUB',  'ABELV',     'Tiago / Yohanna',     'Emissão de CT sobre incompatibilidade entre Isométrico AG e Maquete 3D',                 'Risco de retrabalho e perda de material caso divergência seja confirmada',    '28/05/26','Yohanna identificou incompatibilidade. Tiago emitindo CT. Aguardando resposta.','—', 0, 'NO PRAZO'),
    (50, '25098','MEC/TUB',  'ABELV',     'Yohanna',             'Adequação do Projeto da Linha de AG que conecta com a Linha TRAP (Isométrico)',           'Atraso na fabricação da Linha de Água Gelada',                               '27/05/26','Item em aberto. Aguardando resolução da CT (ID 49).','—', 1, 'ATRASADO'),
    (51, '25098','MEC/TUB',  'ABELV',     'Yohanna',             'Elaboração de MC para compra dos materiais faltantes do suporte de tubulação',            'Atraso na fabricação dos suportes. Início previsto 20/05, término 16/06/26',  '29/05/26','—',         '—',        0, 'NO PRAZO'),
    (52, '25098','ELET',     'ABELV',     'Yohanna',             'Emissão de CT para especificação de pintura das tubulações',                              'Atraso impedirá início do processo de suprimentos de tinta para tubulações',  '28/05/26','—',         '—',        0, 'NO PRAZO'),
    (53, '25098','CIVIL',    'ABELV',     'Yohanna / Leobino',   'Envio à Cristália da CT elaborada pelo Leobino sobre Tinta Asfáltica nos Diques',          'Impacta Pintura Asfáltica nos Diques do 1º Pavimento. Início previsto 02/06/26','28/05/26','CT já elaborada por Leobino em 26/05.','25/05/26', 0, 'CONCLUÍDO'),
    (54, '25098','MEC/TUB',  'CRISTÁLIA', 'Edson / Yohanna',     'Cristália emitir parecer técnico referente à CT de incompatibilidade geométrica Isométrico AG × Maquete 3D','Risco de retrabalho e perda de material','03/06/26','—','—', 0, 'NO PRAZO'),
    (55, '25098','ELET',     'CRISTÁLIA', 'Edson / Yohanna',     'Cristália fornecer especificação técnica homologada para esquema de pintura das tubulações','Atraso impedirá início processo de suprimentos de tinta',                   '03/06/26','—',         '—',        0, 'NO PRAZO'),
    (56, '25098','CIVIL',    'CRISTÁLIA', 'Edson / Yohanna',     'Cristália validar revisão de projeto via CT sobre tinta asfáltica nos diques',             'Impacta Pintura Asfáltica nos Diques do 1º Pavimento. Início previsto 02/06/26','03/06/26','—','—', 0, 'NO PRAZO'),
    (57, '25098','SMS/DOC',  'ABELV',     'Keite / Paula',       'Criação e liberação das credenciais de acesso no portal Abelv Parceiros para a Açoplast', 'Impedirá cadastro prévio da documentação da Açoplast para homologação',       '28/06/26','—',         '—',        0, 'NO PRAZO'),
    (58, '25098','SMS',      'KRROM',     'Diego / Leobino',     'Envio pela KRROM da documentação do novo Técnico de Segurança do Trabalho',                'Descumprimento do prazo inviabilizará homologação do Técnico SMS',            '08/06/26','—',         '—',        0, 'NO PRAZO'),
    # ══════ FARMO 25103 ══════
    (11, '25103','CIVIL',    'KRROM',     'Diego / Leobino',     'Definição do Tipo de Fundação do Prédio',                                                  'Impacta início Fundação do Prédio (ID Cron 431). Início previsto 20/08/26',   '13/05/26','—',         '—',       15, 'ATRASADO'),
    (12, '25103','CIVIL',    'CRISTÁLIA', 'Edson / Leobino',     'Recebimento do Projeto da Base do Lavador de Gases Existente',                             'Impacta início Confecção Nova Base (Radier) Lavador Gases Existente (ID 251). Início previsto 05/06/26','15/05/26','—','—',13,'ATRASADO'),
    (13, '25103','MEC/TUB',  'MGC',       'Yohanna',             'Solicitação e Recebimento dos Projetos do Farmoquímico da MGC e envio para aprovação Cristália','Impacta Compra de Materiais e Subcontratações',                        '19/05/26','—',         '20/05/26', 1, 'CONCLUÍDO COM ATRASO'),
    (14, '25103','CIVIL',    'ABELV',     'Leobino',             'Enviar para a MGC as cotas de elevação do Lavador de Gases',                               'Impacta confecção do Projeto do Radier do Lavador de Gases',                  '19/05/26','—',         '21/05/26', 2, 'CONCLUÍDO COM ATRASO'),
    (15, '25103','ELET',     'ABELV',     'Leobino',             'Enviar para a MGC as cotas de elevação da Sala Elétrica',                                  'Impacta confecção do Projeto da Sala Elétrica',                              '20/05/26','—',         '—',        8, 'ATRASADO'),
    (16, '25103','CIVIL',    'KRROM',     'Diego / Leobino',     'A Krrom precisa informar a data em que irá apresentar o Tipo de Fundação do Farmoquímico',  'Impacta Contratação empresa para Estaca e compra materiais (ID 118). Início previsto 08/06','19/05/26','—','—', 9, 'ATRASADO'),
    (18, '25103','CIVIL',    'KRROM',     'Diego / Leobino',     'Elaboração do Pedido da Tubulação de Água Pluvial',                                        'Impacta Compra da Tubulação de Água Pluvial',                                '27/05/26','—',         '—',        1, 'ATRASADO'),
    (19, '25103','DOC',      'KRROM',     'Rodrigo / Leobino',   'A Krrom precisa enviar os Pedidos de Faturamento Direto',                                  'Impacto na Medição',                                                         '19/05/26','—',         '19/05/26', 0, 'CONCLUÍDO'),
    (24, '25103','DOC',      'ABELV',     'Diego / Leobino',     'A empresa Krrom precisa Regularizar a Documentação da Empresa Recicla (Bota Fora)',         'Caso ocorra auditoria ou acidente, falta documentação legal de subcontratação','21/05/26','—','—', 7, 'ATRASADO'),
    (38, '25103','CIVIL',    'ABELV',     'Leobino',             'CT para identificar posição e trajetória da Linha de Incêndio encontrada na escavação',    'Possibilidade de atraso início da Fundação (ID 431) ou Drenagem Pluvial (ID 381)','26/05/26','Cristália não entregou o Projeto da Linha de Incêndio no prazo. Vencida há 2 dias.','—', 2, 'ATRASADO'),
    (39, '25103','MEC/TUB',  'ABELV',     'Uehara',              'CT sobre Lavadores de Gases que compartilham 1 Caixa de Ar — como realizar primeira manobra sem comprometer operação atual','Poderá atrasar operação (ID 262, Montagem Lavador de Gases 01 (Reserva)). Início previsto 14/07/26','25/05/26','—','—', 3, 'ATRASADO'),
    (41, '25103','MEC',      'CRISTÁLIA', 'Edson / Ilson',       'Comunicar à Cristália que os Elevadores (EL-001 e EL-002) são de Fornecimento e Instalação da Cristália','Impacta Instalação dos Elevadores (EL-001 e EL-002)',              '25/05/26','Informado Lucas e Edson da Cristália via celular em 25/05.','25/05/26', 0, 'CONCLUÍDO'),
    (42, '25103','CIVIL',    'ABELV',     'Diretoria Comercial',  'Emissão do Sinal Financeiro de Mobilização ABELV→KRROM para expansão do efetivo civil 3→8 MOD','Impacta início Área Externa (nova estrutura civil) previsto 05/06/26 e gate Liberação Escavações 06/08/26','22/05/26','Reunião Governança 19/05 aprovou integração de 8 pessoas. Requisição liberada. Sinal NÃO emitido.','—', 6, 'ATRASADO'),
    (43, '25103','CIVIL',    'KRROM',     'Diego / Leobino',     'Identificação de interferência entre elevação do radier e a tubulação',                   'Comprometia o prosseguimento do serviço civil de elevação do radier',         '—',         '—',        '22/05/26', 0, 'CONCLUÍDO'),
    (45, '25103','SMS',      'KRROM',     'Diego / Leobino',     'Técnico de segurança da KRROM ausente de campo desde 04/05/2026',                          'Não conformidade ativa em SMS — obra sem cobertura técnica de segurança da subcontratada civil','07/05/26','—','—',21,'ATRASADO'),
    (59, '25103','MEC/TUB',  'ABELV',     'Uehara',              'Elaboração do layout de posicionamento do lavador de gases existente do Farmoquímico',      'Afeta a subcontratada MGC na elaboração do projeto do radier do lavador de gases','27/05/26','Layout elaborado e fornecido à MGC em 27/05.','27/05/26', 0, 'CONCLUÍDO'),
    (60, '25103','CIVIL',    'KRROM',     'Diego / Leobino',     'Finalização da escavação na região da construção da sala elétrica para identificar interferências na fundação','Atraso na remoção de eventuais interferências e necessidade de avaliação pelo cliente','27/05/26','—','—', 1, 'ATRASADO'),
    (61, '25103','MEC/TUB',  'ABELV',     'Yohanna',             'Envio à Cristália da CT sobre o revestimento Gail para as 2 Caixas de Drenagem',           'Atraso impedirá início do processo de suprimentos — compra do revestimento Gail','28/05/26','—','—', 0, 'NO PRAZO'),
    (62, '25103','MEC/TUB',  'CRISTÁLIA', 'Edson / Yohanna',     'Cristália emitir parecer técnico conclusivo e homologar especificação do revestimento Gail para as 2 caixas de drenagem','Sem homologação, não é possível iniciar suprimentos do revestimento','03/06/26','Depende do recebimento da CT (ID 61).','—', 0, 'NO PRAZO'),
    (63, '25103','SMS',      'ABELV',     'Leobino',             'Emissão e envio de notificação formal por e-mail à Recicla solicitando regularização de documentação','Descarte de resíduos no estacionamento — risco de auditoria e acidente',  '29/05/26','Recicla identificada descartando resíduos em estacionamento fora da área de obra.','—', 0, 'NO PRAZO'),
]

# ─── WORKBOOK ─────────────────────────────────────────────────────────────────
wb = Workbook()
ws = wb.active
ws.title = 'GESTAO_S24b'

# ─── BLOCO 1: Título ──────────────────────────────────────────────────────────
ws.merge_cells('A1:M1')
ws['A1'] = '⚙️  GESTÃO DE RESTRIÇÕES — CRISTÁLIA FARMACÊUTICA — S24 | 28/05/2026'
ws['A1'].fill = fill('1F3864')
ws['A1'].font = Font(color='FFFFFF', bold=True, size=14)
ws['A1'].alignment = center()
ws.row_dimensions[1].height = 30

ws.merge_cells('A2:M2')
ws['A2'] = 'Citostático (25098) + Farmoquímica (25103) | Conector: Claude | Operador: Ministro'
ws['A2'].fill = fill('2E4057')
ws['A2'].font = Font(color='CCCCCC', bold=False, size=11)
ws['A2'].alignment = center()
ws.row_dimensions[2].height = 20

# ─── BLOCO 2: Totais Gerais ───────────────────────────────────────────────────
row = 4
ws.merge_cells(f'A{row}:M{row}')
ws[f'A{row}'] = '📊  TOTAIS CONSOLIDADOS — AMBOS OS PROJETOS'
ws[f'A{row}'].fill = fill('17375E')
ws[f'A{row}'].font = Font(color='FFFFFF', bold=True, size=12)
ws[f'A{row}'].alignment = center()

row += 1
totals_hdr = ['TOTAL','ATRASADO','ALERTA','CC ATRASO','CONCLUÍDO','NO PRAZO']
totals_val = [62, 20, 1, 15, 12, 14]
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

# ─── BLOCO 3: Breakdown por Projeto ──────────────────────────────────────────
row += 2
ws.merge_cells(f'A{row}:M{row}')
ws[f'A{row}'] = '🏗️  BREAKDOWN POR PROJETO'
ws[f'A{row}'].fill = fill('17375E')
ws[f'A{row}'].font = Font(color='FFFFFF', bold=True, size=12)
ws[f'A{row}'].alignment = center()

row += 1
bp_hdrs = ['PROJETO','TOTAL','ATRASADO','ALERTA','CC ATRASO','CONCLUÍDO','NO PRAZO']
bp_cols = [('A','B'),('C','D'),('E','F'),('G','G'),('H','I'),('J','K'),('L','M')]
for i,(cs,ce) in enumerate(bp_cols):
    ws.merge_cells(f'{cs}{row}:{ce}{row}')
    ws[f'{cs}{row}'] = bp_hdrs[i]
    ws[f'{cs}{row}'].fill = fill('2E4057')
    ws[f'{cs}{row}'].font = Font(color='FFFFFF', bold=True, size=10)
    ws[f'{cs}{row}'].alignment = center()

bp_data = [
    ('25098 CISTO',  42, 9,  1, 13, 8,  11, CISTO_ROW),
    ('25103 FARMO',  20, 11, 0,  2, 4,   3, FARMO_ROW),
]
for proj, tot, at, al, cc, conc, np_, row_c in bp_data:
    row += 1
    vals = [proj, tot, at, al, cc, conc, np_]
    for i,(cs,ce) in enumerate(bp_cols):
        ws.merge_cells(f'{cs}{row}:{ce}{row}')
        ws[f'{cs}{row}'] = vals[i]
        ws[f'{cs}{row}'].fill = fill(row_c)
        ws[f'{cs}{row}'].font = font(bold=(i==0), sz=11)
        ws[f'{cs}{row}'].alignment = center()
    ws.row_dimensions[row].height = 22

# ─── BLOCO 4: Atrasados por Empresa ──────────────────────────────────────────
row += 2
ws.merge_cells(f'A{row}:M{row}')
ws[f'A{row}'] = '🏢  ATRASADOS POR EMPRESA (abertos)'
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

# ─── BLOCO 5: Top 5 mais atrasados ───────────────────────────────────────────
row += 2
ws.merge_cells(f'A{row}:M{row}')
ws[f'A{row}'] = '🔥  TOP 5 — MAIS ATRASADOS (dias, abertos)'
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
    bg = CISTO_ROW if proj == '25098' else FARMO_ROW
    vals = [rid, proj, resp, desc, dias]
    for i,(cs,ce) in enumerate(top_cols):
        ws.merge_cells(f'{cs}{row}:{ce}{row}')
        ws[f'{cs}{row}'] = vals[i]
        ws[f'{cs}{row}'].fill = fill(bg)
        ws[f'{cs}{row}'].font = font(bold=(i==4), sz=11 if i<4 else 14)
        ws[f'{cs}{row}'].alignment = left(wrap=True) if i==3 else center()
    ws.row_dimensions[row].height = 24

# ─── BLOCO 6: Vencendo hoje e amanhã ─────────────────────────────────────────
row += 2
ws.merge_cells(f'A{row}:M{row}')
ws[f'A{row}'] = '⏰  VENCENDO HOJE (28/05) E AMANHÃ (29/05) — EM ABERTO'
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
        if d and d <= date(2026,5,29):
            venc.append((r[0],r[1],r[4],r[5],r[7]))

row += 1
for i,(cs,ce) in enumerate(top_cols):
    ws.merge_cells(f'{cs}{row}:{ce}{row}')
    ws[f'{cs}{row}'] = ['ID','PROJ','RESPONSÁVEL','DESCRIÇÃO','NECESSIDADE'][i]
    ws[f'{cs}{row}'].fill = fill('2E4057')
    ws[f'{cs}{row}'].font = Font(color='FFFFFF', bold=True, size=10)
    ws[f'{cs}{row}'].alignment = center()

for rid, proj, resp, desc, nec in venc:
    row += 1
    bg = CISTO_ROW if proj == '25098' else FARMO_ROW
    for i,(cs,ce) in enumerate(top_cols):
        ws.merge_cells(f'{cs}{row}:{ce}{row}')
        ws[f'{cs}{row}'] = [rid, proj, resp, desc, nec][i]
        ws[f'{cs}{row}'].fill = fill('FFEB9C')
        ws[f'{cs}{row}'].font = font(sz=11)
        ws[f'{cs}{row}'].alignment = left(wrap=True) if i==3 else center()
    ws.row_dimensions[row].height = 22

# ─── ABA DETALHAMENTO ─────────────────────────────────────────────────────────
ws2 = wb.create_sheet('DETALHAMENTO')

HDR = ['ID','PROJETO','DISC.','EMPRESA','RESPONSÁVEL','DESCRIÇÃO','IMPACTO','NECESSIDADE','OBSERVAÇÃO','CONCLUSÃO','DIAS ATRASO','STATUS']
ws2.freeze_panes = 'A2'

# header
for c, h in enumerate(HDR, 1):
    cell = ws2.cell(row=1, column=c, value=h)
    cell.fill = fill('1F3864')
    cell.font = Font(color='FFFFFF', bold=True, size=10)
    cell.alignment = center(wrap=True)
    cell.border = thin()

# col widths
widths = [5, 8, 8, 10, 18, 55, 45, 10, 50, 10, 8, 20]
for i, w in enumerate(widths, 1):
    ws2.column_dimensions[get_column_letter(i)].width = w

for r_idx, r in enumerate(RESTRICOES, 2):
    rid, proj, disc, emp, resp, desc, imp, nec, obs, conc, dias, status_raw = r
    sk = status_key(status_raw)
    row_bg = COR.get(sk,{}).get('row','FFFFFF')
    if sk == 'CONCLUIDO': row_bg = COR['CONCLUIDO']['row']
    # Override with project color for NO PRAZO / CC ATRASO
    if proj == '25098' and sk in ('NO PRAZO',): row_bg = CISTO_ROW
    if proj == '25103' and sk in ('NO PRAZO',): row_bg = FARMO_ROW

    vals = [rid, proj, disc, emp, resp, desc, imp, nec, obs, conc, dias, status_raw]
    for c_idx, v in enumerate(vals, 1):
        cell = ws2.cell(row=r_idx, column=c_idx, value=v)
        cell.fill = fill(row_bg)
        cell.font = font(sz=10)
        cell.alignment = left(wrap=True) if c_idx in (6,7,9) else center(wrap=True)
        cell.border = thin()
    # Color status cell
    st_cell = ws2.cell(row=r_idx, column=12)
    st_cell.fill = fill(COR.get(sk,{}).get('bg','FFFFFF'))
    st_cell.font = Font(color=COR.get(sk,{}).get('fg','000000'), bold=True, size=10)
    ws2.row_dimensions[r_idx].height = 30

# ─── Salvar ───────────────────────────────────────────────────────────────────
out = '/tmp/GESTAO_RESTRICOES_Cristalia_280526.xlsx'
wb.save(out)
print(f'Salvo em: {out}')
print(f'Total de restrições: {len(RESTRICOES)}')
at = sum(1 for r in RESTRICOES if status_key(r[11])=='ATRASADO')
al = sum(1 for r in RESTRICOES if status_key(r[11])=='ALERTA')
cc = sum(1 for r in RESTRICOES if status_key(r[11])=='CC ATRASO')
co = sum(1 for r in RESTRICOES if status_key(r[11])=='CONCLUIDO')
np_ = sum(1 for r in RESTRICOES if status_key(r[11])=='NO PRAZO')
print(f'AT:{at} AL:{al} CC:{cc} CONC:{co} NP:{np_}  => Total: {at+al+cc+co+np_}')
