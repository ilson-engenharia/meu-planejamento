#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Modelo GESTAO — formato do arquivo original do usuário
46 itens | 27/05/2026 | 1 aba "GESTAO" | PROJETO = "25098 CISTO" | STATUS com emoji
"""
import openpyxl
from openpyxl.styles import PatternFill, Font, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from datetime import date

def pf(h): return PatternFill(start_color=h, end_color=h, fill_type="solid")
def ft(bold=False, color="000000", size=10): return Font(bold=bold, color=color, size=size, name="Calibri")
def al(h="center", v="center", wrap=False): return Alignment(horizontal=h, vertical=v, wrap_text=wrap)
def bt():
    s = Side(style="thin", color="BFBFBF")
    return Border(left=s, right=s, top=s, bottom=s)

C_HDR_BG="1F4E79"; C_HDR_FG="FFFFFF"
C_NP_BG="C6EFCE";  C_NP_FG="375623"
C_AL_BG="FFEB9C";  C_AL_FG="7F6000"
C_AT_BG="FFC7CE";  C_AT_FG="9C0006"
C_CO_BG="DAEEF3";  C_CO_FG="17375E"
C_CA_BG="FFF2CC";  C_CA_FG="7F4F00"
C_CI_BG="EBF3FB";  C_FA_BG="FFF2CC"

today = date(2026, 5, 27)

def fmt_d(d):
    return d.strftime("%d/%m/%y") if d else "—"

def calc_status(nec, conc):
    if nec is None: return "— SEM PRAZO"
    if conc is not None: return "✅ CONCLUÍDO" if conc <= nec else "⚠️ CONCLUÍDO COM ATRASO"
    if nec < today: return "⚠️ ATRASADO"
    if nec == today: return "🟡 ALERTA"
    return "🟢 NO PRAZO"

def status_colors(st):
    m = {
        "🟢 NO PRAZO":           (C_NP_BG, C_NP_FG),
        "🟡 ALERTA":             (C_AL_BG, C_AL_FG),
        "⚠️ ATRASADO":          (C_AT_BG, C_AT_FG),
        "✅ CONCLUÍDO":          (C_CO_BG, C_CO_FG),
        "⚠️ CONCLUÍDO COM ATRASO": (C_CA_BG, C_CA_FG),
        "— SEM PRAZO":           ("F2F2F2", "808080"),
    }
    return m.get(st, ("F2F2F2", "808080"))

def calc_dias(nec, conc):
    if nec is None: return "—"
    if conc is not None: return max(0, (conc - nec).days)
    if nec < today: return (today - nec).days
    return 0

def proj_fmt(p):
    return "25098 CISTO" if p == "CISTO" else "25103 FARMO"

# (disc, elab, proj, emp, resp, desc, imp, id_imp, nec, obs, conc)
dados = [
    ("[CIVIL]",date(2026,5,11),"CISTO","KROOM","Diego (Gerente de Projetos da Kroom) / Leobino (Eng. Civil Abelv)","Mobilização da Krrom para realização da Tarefa do Dique no Piso Técnico",None,None,date(2026,5,20),"25/05: Não foi mobilizada a equipe da Krrom (no momento 3 colaboradores), pois a Krrom não recebeu o sinal.",date(2026,5,11)),
    ("[CIVIL]",date(2026,5,8),"CISTO","KROOM","Diego (Gerente de Projetos da Kroom) / Leobino (Eng. Civil Abelv)","Recebimento de Materiais do Dique no Piso Técnico",None,None,date(2026,5,11),None,date(2026,5,11)),
    ("[CIVIL]",date(2026,5,8),"CISTO","CRISTÁLIA","Edson (Cristália) / Leobino (Eng. Civil Abelv)","Retirada de 2 Peças de Vidro da Sala Limpa, pois está impedindo a continuidade da Marcação das Bases que serão construídas.","Impede a continuação da Locação das Bases que serão construídas na Sala Limpa.",None,date(2026,5,19),None,None),
    ("[MEC/TUB]",date(2026,5,5),"CISTO","ABELV","Leobino (Eng. Civil Abelv)","Chegada de Materiais para Fabricação da Tubulação do Trap",None,None,date(2026,5,7),"19/05: Pendente a entrega dos materiais.",None),
    ("[CIVIL]",date(2026,5,14),"CISTO","CRISTÁLIA","Edson (Cristália) / Leobino (Eng. Civil Abelv)","Cobrar Definição da Cristália a respeito da Locação da Plataforma dos Reatores em Função da Instalação da Nova Linha Hidrossanitária.","Impacta o início do Corte do Piso para confecção das Bases da Plataforma dos Reatores (Início Previsto: 21/05 - Atividade do Cronograma: ID 22). E Demolição do Piso para Instalação da Rede Hidrossanitária (Início Previsto: 18/05 - Atividade do Cronograma: ID 58).",None,date(2026,5,18),None,None),
    ("[MEC/TUB]",date(2026,5,12),"CISTO","ABELV","Tiago (Gestor de Projetos Abelv)","Acompanhamento / Recebimento das Conexões de Aço Carbono","Impacta na Fabricação da Tubulação de Aço Carbono (Início Previsto: 25/05/26 - Atividade do Cronograma: ID 54 e ID 317).",None,date(2026,5,19),None,None),
    ("[MEC/TUB]",date(2026,5,12),"CISTO","ABELV","Tiago (Gestor de Projetos Abelv)","Acompanhamento / Recebimento da Tubulação de Aço Carbono","Impacta na Fabricação da Tubulação de Aço Carbono (Início Previsto: 25/05/26 - Atividade do Cronograma: ID 54 e ID 317).",None,date(2026,5,15),None,date(2026,5,15)),
    ("[PROC]",date(2026,5,15),"CISTO","ABELV","Uehara (Engenheiro Mecânico do HVAC Abelv)","Validar a Mudança Dimensional da Base do Lavador de Gases","Impacta no Início da Demolição do Piso do Radier do Lavador de Gases a Título de Área caso aconteça alguma mudança significativa. (Início Previsto: 25/05/26 - Atividade do Cronograma: ID 466).",None,date(2026,5,20),None,None),
    ("[PROC][SUP]",date(2026,5,12),"CISTO","ABELV","Uehara (Engenheiro Mecânico do HVAC Abelv)","Contratação Lavador de Gases",None,None,date(2026,5,15),"19/05: Aguardando o Setor de Suprimentos da Abelv fechar o pedido.",None),
    ("[SUP]",date(2026,5,19),"CISTO","ABELV","Ana Assis (Gerente do Suprimentos Abelv)","Fechamento do Pedido de Compra do Lavador de Gases","Impacta na identificação real do Dimensional da Base do Lavador de Gases, consequentemente também impactando o Início da Demolição do Piso do Radier do Lavador de Gases a Título de Área caso aconteça alguma mudança significativa. (Início Previsto: 25/05/26 - Atividade do Cronograma: ID 466).",None,date(2026,5,19),None,date(2026,5,20)),
    ("[CIVIL]",date(2026,5,12),"FARMO","KROOM","Diego (Gerente de Projetos da Kroom) / Leobino (Eng. Civil Abelv)","Definição do Tipo de Fundação do Prédio","Impacta no início da Fundação do Prédio (Início Previsto: 20/08/26 - Atividade do Cronograma: ID 431).",431,date(2026,5,13),None,None),
    ("[CIVIL]",date(2026,5,12),"FARMO","CRISTÁLIA","Edson (Cristália) / Leobino (Eng. Civil Abelv)","Recebimento do Projeto da Base do Lavador de Gases Existente.","Impacta na Formalização da Nova Locação que foi combinada IN LOCO para execução da base do Lavador existente. Início da Confecção da Nova Base (Radier) do Lavador de Gases Existente (Início Previsto: 05/06/26 - Atividade do Cronograma: ID 251).",None,date(2026,5,15),None,None),
    ("[MEC/TUB]",date(2026,5,7),"FARMO","MGC","Yohanna (Engenheira Mecânica Abelv)","Solicitação e Recebimento dos Projetos do Farmoquímico da Empresa MGC, e envio para Cristália para aprovação","Impacta na Compra dos Materiais e Subcontratações para realização dos materiais.",None,date(2026,5,19),None,date(2026,5,20)),
    ("[CIVIL]",date(2026,5,19),"FARMO","ABELV","Leobino (Eng. Civil Abelv)","Enviar para a MGC as cotas de elevação do Lavador de Gases","Impacta na confecção do Projeto do Radier do Lavador de Gases.",None,date(2026,5,19),None,date(2026,5,21)),
    ("[ELET]",date(2026,5,19),"FARMO","ABELV","Leobino (Eng. Civil Abelv)","Enviar para a MGC as cotas de elevação da Sala Elétrica","Impacta na confecção do Projeto da Sala Elétrica.",None,date(2026,5,20),None,None),
    ("[CIVIL]",date(2026,5,19),"FARMO","KROOM","Diego (Gerente de Projetos da Kroom) / Leobino (Eng. Civil Abelv)","A Krrom precisa informar a Data em que irão apresentar o Tipo de Fundação que será aplicada no Farmoquímico.","Impacta na Contratação da Empresa para realização da Estaca, por ventura impactando na compra de materiais da estaca (Início Previsto: 08/06 - Atividade do Cronograma: ID 118).",None,date(2026,5,19),None,None),
    ("[CIVIL]",date(2026,5,19),"CISTO","KROOM","Diego (Gerente de Projetos da Kroom) / Leobino (Eng. Civil Abelv)","A Krrom precisa apresentar a Metodologia de Corte que será aplicada para avaliar a resistência do piso onde poderá ser construída a base da Plataforma dos Reatores, em função da Interferência da Instalação da Nova Rede Hidrossanitária.","Impacta o início do Corte do Piso para confecção das Bases da Plataforma dos Reatores (Início Previsto: 21/05 - Atividade do Cronograma: ID 22). E Demolição do Piso para Instalação da Rede Hidrossanitária (Início Previsto: 18/05 - Atividade do Cronograma: ID 58).",None,date(2026,5,20),"20/05: A Krrom apresentou a alternativa de realização de um Ensaio Não Destrutivo de Esclerometria, pois seria mais rápido o método de avaliação da Resistência Mecânica.",date(2026,5,20)),
    ("[CIVIL]",date(2026,5,19),"FARMO","KROOM","Diego (Gerente de Projetos da Kroom) / Leobino (Eng. Civil Abelv)","Elaboração do Pedido da Tubulação de Água Pluvial","Impacta a Compra da Tubulação de Água Pluvial.",None,date(2026,5,27),None,None),
    ("[DOC]",date(2026,5,19),"FARMO","KROOM","Rodrigo (Téc. Planej. da Kroom) / Leobino (Eng. Civil Abelv)","A Kroom precisa enviar os Pedidos de Faturamento Direto","Impacto na Medição.",None,date(2026,5,19),None,date(2026,5,19)),
    ("[SUP]",date(2026,5,19),"CISTO","KROOM","Tiago (Gestor de Projetos Abelv) / Celso (Gestor de Projetos Abelv)","Verificação do Efetivo de Andaime para atendimento das Obras (Farmoquímico e Citostático).","Impacto de acesso para realização das Frentes de Montagem.",None,date(2026,5,20),None,date(2026,5,20)),
    ("[MEC/TUB]",date(2026,5,19),"CISTO","ABELV","Leobino (Eng. Civil Abelv)","Montagem do Pipe-Shop de Aço Carbono no Canteiro de Obra Abelv.","Impacta na Fabricação da Tubulação de Aço Carbono (Início Previsto: 25/05/26 - Atividade do Cronograma: ID 54 e ID 317).",None,date(2026,5,20),None,date(2026,5,20)),
    ("[DOC][SUP]",date(2026,5,19),"CISTO","ABELV","Erik Massola (Comprador Abelv) / Tiago Matos (Gestor de Projetos Abelv)","O Setor de Compras precisa enviar o Efetivo (Nomes e CPFs dos colaboradores) da empresa contratada Açoplast (Estrutura Metálica) para Tiago Matos, para posterior envio para Cristália realizar a avaliação social dos mesmos.","Impacto: Caso os mesmos não forem aprovados, eles não poderão adentrar ao site, podendo impactar o prazo da obra. (Início Previsto: 21/05 - Atividade do Cronograma (Fabricação dos Dutos): ID 561).",561,date(2026,5,20),None,None),
    ("[SUP]",date(2026,5,19),"CISTO","ABELV","Edimar Cunha (Supervisor de Suprimentos Abelv) / Tiago Matos (Gestor de Projetos Abelv)","Contratação do Fornecedor de Andaime.","Impacto de acesso para realização das Frentes de Montagem.",None,date(2026,5,22),None,None),
    ("[DOC][SMS]",date(2026,5,19),"FARMO","ABELV","Diego (Gerente de Projetos da Kroom) / Leobino (Eng. Civil Abelv)","A empresa Krrom precisa Regularizar a Documentação da Empresa Recicla (Bota Fora).","Impacto: Caso aconteça alguma auditoria ou acidente, estamos descobertos por documentação legal de subcontratação.",None,date(2026,5,21),None,None),
    ("[MEC/TUB]",date(2026,5,19),"CISTO","ABELV","Yohanna (Engenheira Mecânica Abelv)","Verificação da readequação do Projeto da Plataforma dos Reatores por base do nosso fornecedor que vai fabricar, pois os reatores adquiridos pela Cristália não cabem no mesmo.","Impacto: Atraso na Fabricação do Projeto da Plataforma dos Reatores, por necessidade de elaboração do Novo Projeto para readequação do novo lay-out (Início e Término Previsto: 14/05/26 e 13/07/26 - Atividade do Cronograma: ID 650).",650,date(2026,5,20),None,None),
    ("[MEC/TUB]",date(2026,5,19),"CISTO","CRISTÁLIA","Yohanna (Engenheira Mecânica Abelv)","O Filtro Secador adquirido pela Cristália não cabe na base do Projeto Fornecido, logo a Cristália ficou de elaborar um Novo Projeto da Base do Filtro Secador para essa nova realidade.","Impacto: Atraso na Construção da Nova Base do Filtro Secador (Início Previsto: 20/05/26 - Atividade do Cronograma: ID 9).",9,date(2026,5,20),None,None),
    ("[CIVIL]",date(2026,5,19),"CISTO","CRISTÁLIA","Yohanna (Engenheira Mecânica Abelv)","A Cristália tem que apresentar o Projeto da Nova Locação do Ralo do Sistema Hidrossanitário, pois o Projeto Atual da Base da Plataforma dos Reatores está na mesma coordenada dos Ralos.","Impacto: Atraso na Conclusão do Corte do Piso para Novo Sistema Hidrossanitário. (Término Previsto: 18/05/26 - Atividade do Cronograma: ID 59).",59,date(2026,5,20),None,None),
    ("[CIVIL]",date(2026,5,20),"CISTO","CRISTÁLIA","Leobino (Eng. Civil Abelv)","Confirmação do Cliente da Aplicação de Tinta Asfáltica nos Diques do Piso Técnico, conforme orientado no Projeto.",None,None,date(2026,5,20),"20/05: Sr. Edson da Cristália na Reunião de Planejamento no Canteiro orientou continuarmos segundo o Projeto.",date(2026,5,20)),
    ("[DOC]",date(2026,5,20),"CISTO","ABELV","Ilson (Planejador Abelv) / Victor (Planejador Abelv)","Elaboração do Estudo de HH aplicado até a data 19/05/26, conforme solicitado em reunião.",None,None,date(2026,5,25),None,None),
    ("[SMS]",date(2026,5,20),"CISTO","KROOM","Diego (Gerente de Projetos da Kroom) / Leobino (Eng. Civil Abelv)","Compra ou Projeção de Compra do Pluviômetro, com objetivo de medir a quantidade de chuva (precipitação) na Obra, e registrar os impactos das atividades.","Impacto: Registro de Comprovação de Impactos de Chuvas a nível de RDO.",None,date(2026,5,20),"26/05: Chegou o Pluviômetro no site.",date(2026,5,25)),
    ("[MEC/TUB][SUP]",date(2026,5,21),"CISTO","ABELV","Celso (Gestor de Projetos Abelv)","Emissão de Solicitação de Compra (SC) para Fabricação da Linha do Dreno do TRAP","Impacto: Fabricação da Linha do Trap (Início Previsto: 25/05 - Atividade do Cronograma: ID 169).",169,date(2026,5,21),None,None),
    ("[CIVIL]",date(2026,5,21),"CISTO","ABELV","Leobino (Eng. Civil Abelv)","Elaboração de CT (Consulta Técnica) a respeito da Aplicação da Tinta Asfáltica que segundo o Projeto está orientando aplicar nos Diques do Pavimento Técnico.","Impacto: Pintura Asfáltica nos Diques do Primeiro Pavimento (Início Previsto: 02/06 - Atividade do Cronograma: ID 279).",279,date(2026,5,21),"26/05: Leobino, na Reunião de Bom Dia, informou que já elaborou a CT.",date(2026,5,25)),
    ("[CIVIL]",date(2026,5,21),"CISTO","ABELV","Leobino (Eng. Civil Abelv)","Solicitação de Visita Técnica e envio de documentação dos Colaboradores da empresa GEOCOM (Empresa de Ensaio de Esclerometria).","Impacto: Atraso do início da confecção da base dos reatores, atividade que estava prevista para o dia 21/05/26 (ID: 22), em virtude do Projeto Fornecido pela Cristália, a base da Plataforma do Reator está localizada no Local do Ralo.",22,date(2026,5,21),"22/05: A GEOCOM realizou o Ensaio de Esclerometria.",date(2026,5,22)),
    ("[CIVIL][SMS]",date(2026,5,21),"CISTO","ABELV","Celso (Gestor de Projetos Abelv) / Leobino (Eng. Civil Abelv)","Confecção de Andaime de Proteção contra quedas de Materiais para Atividade de Furação da Laje no Prédio do Citostático, solicitado pela Krrom.","Impacto: Atraso no Início da Furação da Laje do Citostático (Início Previsto: 15/06 - Atividade do Cronograma: ID 284).",284,date(2026,6,8),None,None),
    ("[CIVIL]",date(2026,5,21),"CISTO","ABELV","Leobino (Eng. Civil Abelv)","Elaboração de CT para Definição do Projeto dos Diques Técnicos, pois o Projeto Civil orienta a construção de 2 Diques, e o Projeto Mecânico orienta apenas 1 Dique para todos os equipamentos.","Impacto: Retrabalho nos Diques de Contenção do Piso Técnico, pois já foi iniciada essa atividade. (Início Previsto: 21/05 - Atividade do Cronograma: ID 276).",276,date(2026,5,21),None,None),
    ("[SUP]",date(2026,5,21),"CISTO","ABELV","Yohanna (Engenheira Mecânica Abelv)","Levantamento Inicial do Quantitativo de Tintas para Obra.",None,None,date(2026,5,29),None,None),
    ("[CIVIL]",date(2026,5,21),"CISTO","CRISTÁLIA","Leobino (Eng. Civil Abelv)","Solicitar a Cristália a Definição da Tinta Externa que será Aplicada nos Diques de Contenção do Piso Técnico.","Impacto: Atraso na aplicação da Tinta Externa, porém sabendo que no dia 20/05, o Projeto Civil de Construção dos Diques não está de acordo com o apresentado pela Mecânica para a contenção dos equipamentos, já caracterizando retrabalho.",None,date(2026,5,22),None,None),
    ("[CIVIL]",date(2026,5,22),"FARMO","ABELV","Leobino (Eng. Civil Abelv)","Elaboração de Consulta Técnica (CT) para identificar a posição e trajetória da Linha de Incêndio encontrada na escavação, pois existe a possibilidade de topar com nova Rede de Drenagem Pluvial ou com a posição atual do Prédio que será construído. E saber qual será a tratativa de correção estrutural da mesma, tendo em vista que ela apresenta pontos de corrosão (diversos pontos), aparente baixa espessura e vazamento em vários pontos.","Impacto: Possibilidade de atraso no início da Fundação ou da Linha de Drenagem, caso haja demora no retorno do cliente. (Início Previsto: 21/08 - Fundações - ID 431; e Início Previsto: 22/12 - Drenagem Pluvial - ID 381).","381;431",date(2026,5,25),"25/05: Leobino informou que o Edson da Cristália já possuía o Projeto da Linha de Incêndio Aéreo e o forneceria até o dia 26/05/26.",None),
    ("[MEC/TUB]",date(2026,5,22),"FARMO","ABELV","Uehara (Engenheiro Mecânico do HVAC Abelv)","Elaboração de Consulta Técnica (CT) para saber qual tratativa a ser executada, tendo em vista que os Lavadores de Gases apresentam 1 Caixa de Ar que se comunica aos 2 Equipamentos do Farmoquímico. Para fazer a primeira manobra de instalar o primeiro e possibilitar a desativação e remoção do segundo do estado inicial, precisamos antes condicionar o primeiro removido com uma Caixa de Ar.","Impacto: Caso não haja disponibilidade de 1 Caixa de Ar para a realização da primeira mudança do Lavador de Gases para a nova posição, poderá atrasar essa operação (Início Previsto: 14/07 - ID 262).",262,date(2026,5,25),None,None),
    ("[CIVIL]",date(2026,5,25),"CISTO","CRISTÁLIA","Edson (Cristália) / Yohanna (Engenheira Mecânica Abelv)","A Cristália deve enviar os Projetos dos Equipamentos (Banhos Térmicos dos Reatores: BT-008, BT-009 e BT-010), para que a Abelv possa verificar se os mesmos cabem dentro do Novo Dique Técnico. Essa informação foi solicitada por e-mail.","Impacto: Caso atrase, e haja novamente a necessidade de mudança no Projeto do Dique de Contenção do Piso Técnico, teremos que novamente retrabalhar na confecção do Dique (Início Previsto: 21/05 - ID 276).",276,date(2026,5,28),None,None),
    ("[DOC]",date(2026,5,25),"FARMO","CRISTÁLIA","Edson (Cristália) / Ilson (Planejamento Abelv)","Comunicar à Cristália que os Elevadores (EL-001 e EL-002) são de Fornecimento e Instalação da Cristália, conforme o Contrato.","Impacto: Instalação dos elevadores (EL-001 e EL-002).",None,date(2026,5,25),"25/05: Já informado Lucas e Edson da Cristália via celular, dia 25/05/26.",date(2026,5,25)),
    ("[DOC][SUP]",date(2026,5,26),"CISTO","ABELV","Celso (Gestor de Projetos Abelv)","Solicitar à equipe da empresa contratada Açoplast (Estrutura Metálica) o preenchimento e envio para a Abelv da Planilha Nominal com os Dados dos Colaboradores que realmente irão ao site. O objetivo é realizar a avaliação social da Cristália.","Impacto: Necessidade de contratação de outros colaboradores de forma emergencial para adentrar o site, consequentemente atraso no início da Fabricação dos Dutos de HVAC (Início Previsto: 21/05 - ID 561).",561,date(2026,5,26),None,None),
    ("[MEC/TUB]",date(2026,5,26),"CISTO","ABELV","Yohanna (Engenheira Mecânica Abelv)","Adequação do Projeto da Linha de AG que conecta com a Linha TRAP (Isométrico).","Impacto: Atraso na fabricação da Linha de Água Gelada, já em atraso pois até o dia 26/05/26 não chegaram as conexões para iniciar a Fabricação (Início Previsto: 25/05 - ID 261).",261,date(2026,5,27),None,None),
    ("[MEC/TUB]",date(2026,5,27),"FARMO","ABELV","Uehara (Engenheiro Mecânico do HVAC Abelv)","Elaboração do layout de posicionamento do lavador de gases existente do Farmoquímico.","Impacto: Esta atividade afeta a subcontratada MGC na elaboração do projeto do radier do lavador de gases (Período previsto: 05/05 a 15/05/26 — ID 15). Como consequência, haverá um atraso posterior na construção do radier do lavador de gases existente (Início previsto: 18/06 — ID 251).","15;251",date(2026,5,27),None,None),
    ("[MEC/TUB][SUP]",date(2026,5,27),"CISTO","ABELV","Yohanna (Engenheira Mecânica Abelv)","Elaboração de MC (Mapa de Cotação) para a compra dos materiais faltantes do suporte de tubulação, devido à incompatibilidade da LPU com o projeto recebido pela Cristália.","Impacto: Atraso na fabricação dos suportes (Início previsto: 20/05 até o Término previsto: 16/06/26 — ID 254).",254,date(2026,5,29),None,None),
    ("[CIVIL]",date(2026,5,27),"FARMO","KROOM","Diego (Gerente de Projetos da Kroom) / Leobino (Eng. Civil Abelv)","Finalização da escavação na região da construção da Sala Elétrica, para identificar interferências no local da fundação.","Impacto: Atraso na remoção de eventuais interferências, devido à necessidade de avaliação pelo cliente, com consequente impacto no início dos serviços civis da Sala Elétrica e da base do radier do lavador de gases existente (Início previsto: 18/06 — ID 251).",251,date(2026,5,27),None,None),
]

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "GESTAO"

headers = ["ITEM","PROJETO","DISCIPLINA","ELABORAÇÃO","EMPRESA RESP.","RESPONSÁVEL",
           "DESCRIÇÃO","IMPACTO","ID IMPACT","NECESSIDADE","OBSERVAÇÃO",
           "CONCLUSÃO REAL","DIAS ATRASADO","STATUS"]
N = 14
col_widths = [5,12,14,13,14,35,52,38,10,13,40,14,10,22]
for i,w in enumerate(col_widths,1):
    ws.column_dimensions[get_column_letter(i)].width = w
ws.row_dimensions[1].height = 36

for col,h in enumerate(headers,1):
    c = ws.cell(row=1,column=col,value=h)
    c.fill=pf(C_HDR_BG); c.font=ft(bold=True,color=C_HDR_FG)
    c.alignment=al(wrap=True); c.border=bt()

for idx,row in enumerate(dados,1):
    r = idx+1
    disc,elab,proj,emp,resp,desc,imp,id_imp,nec,obs,conc = row
    st = calc_status(nec,conc)
    da = calc_dias(nec,conc)
    proj_bg = C_CI_BG if proj=="CISTO" else C_FA_BG
    st_bg, st_fg = status_colors(st)

    imp_v = imp if imp else "—"
    id_v  = id_imp if id_imp else "—"
    obs_v = obs if obs else "—"
    conc_v = fmt_d(conc) if conc else "—"

    values = [idx, proj_fmt(proj), disc, fmt_d(elab), emp, resp,
              desc, imp_v, id_v, fmt_d(nec), obs_v, conc_v, da, st]

    for col,val in enumerate(values,1):
        c = ws.cell(row=r,column=col,value=val)
        c.border=bt()
        c.alignment=al(h="left",v="center",wrap=True)

        if col in (1,9,13):
            c.alignment=al(h="center",v="center")
        if col==3:
            c.alignment=al(h="center",v="center"); c.font=ft(bold=True)
        if col in (4,10,12):
            c.alignment=al(h="center",v="center")

        if col==14:
            c.fill=pf(st_bg); c.font=ft(bold=True,color=st_fg)
            c.alignment=al(h="center",v="center")
        elif col==13:
            if isinstance(val,int) and val>0: c.font=ft(bold=True,color=C_AT_FG)
            elif val=="—": c.font=ft(color="808080")
            c.fill=pf(proj_bg)
        else:
            c.fill=pf(proj_bg)

    ws.row_dimensions[r].height = 30

ws.freeze_panes="A2"
ws.auto_filter.ref=f"A1:{get_column_letter(N)}{len(dados)+1}"

OUT = "/home/user/meu-planejamento/GESTAO_RESTRICOES_Cristalia_270526.xlsx"
wb.save(OUT)
print(f"✅ Salvo: {OUT} | {len(dados)} itens")
