#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import date
from collections import defaultdict

today = date(2026, 5, 21)

def calc_status(nec, conc):
    if nec is None: return "—"
    if conc is not None: return "CONCLUÍDO" if conc <= nec else "CONCLUÍDO COM ATRASO"
    if nec < today: return "ATRASADO"
    if nec == today: return "ALERTA"
    return "NO PRAZO"

def calc_dias(nec, conc):
    if nec is None: return "—"
    if conc is not None: return max(0, (conc - nec).days)
    if nec < today: return (today - nec).days
    return 0

def fmt_date(d):
    return d.strftime("%d/%m/%Y") if d else "—"

# Tupla: (disc, elab, proj, emp, resp, desc, imp, id_imp, nec, obs, conc)
dados = [
    ("[CIVIL]", date(2026,5,11),"CISTO","KROOM",
     "Diego (Gerente de Projetos da Kroom) / Leobino (Eng. Civil Abelv)",
     "Mobilização da Krrom para realização da Tarefa do Dique no Piso Técnico",
     None,None,date(2026,5,20),None,date(2026,5,11)),

    ("[CIVIL]", date(2026,5,8),"CISTO","KROOM",
     "Diego (Gerente de Projetos da Kroom) / Leobino (Eng. Civil Abelv)",
     "Recebimento de Materiais do Dique no Piso Técnico",
     None,None,date(2026,5,11),None,date(2026,5,11)),

    ("[CIVIL]", date(2026,5,8),"CISTO","CRISTÁLIA",
     "Edson (Cristália) / Leobino (Eng. Civil Abelv)",
     "Retirada de 2 Peças de Vidro da Sala Limpa, pois está impedindo a continuidade da Marcação das Bases que serão construídas.",
     "Impede a continuação da Locação das Bases que serão construídas na Sala Limpa.",
     None,date(2026,5,19),None,None),

    ("[MEC/TUB]", date(2026,5,5),"CISTO","ABELV",
     "Leobino (Eng. Civil Abelv)",
     "Chegada de Materiais para Fabricação da Tubulação do Trap",
     None,None,date(2026,5,7),"19/05: Pendente a entrega dos materiais",None),

    ("[CIVIL]", date(2026,5,14),"CISTO","CRISTÁLIA",
     "Edson (Cristália) / Leobino (Eng. Civil Abelv)",
     "Cobrar Definição da Cristália a respeito da Locação da Plataforma dos Reatores em Função da Instalação da Nova Linha Hidrossanitária.",
     "Impacta o início do Corte do Piso para confecção das Bases da Plataforma dos Reatores "
     "(Início Previsto: 21/05 - Atividade do Cronograma: ID 22). E Demolição do Piso para "
     "Instalação da Rede Hidrossanitária (Início Previsto: 18/05 - Atividade do Cronograma: ID 58).",
     None,date(2026,5,18),None,None),

    ("[MEC/TUB]", date(2026,5,12),"CISTO","ABELV",
     "Tiago (Gestor de Projetos Abelv)",
     "Acompanhamento / Recebimento das Conexões de Aço Carbono",
     "Impacta na Fabricação da Tubulação de Aço Carbono "
     "(Início Previsto: 25/05/26 - Atividade do Cronograma: ID 54 e ID 317).",
     None,date(2026,5,19),None,None),

    ("[MEC/TUB]", date(2026,5,12),"CISTO","ABELV",
     "Tiago (Gestor de Projetos Abelv)",
     "Acompanhamento / Recebimento da Tubulação de Aço Carbono",
     "Impacta na Fabricação da Tubulação de Aço Carbono "
     "(Início Previsto: 25/05/26 - Atividade do Cronograma: ID 54 e ID 317).",
     None,date(2026,5,15),None,date(2026,5,15)),

    ("[PROC]", date(2026,5,15),"CISTO","ABELV",
     "Uehara (Engenheiro Mecânico do HVAC Abelv)",
     "Validar a Mudança Dimensional da Base do Lavador de Gases",
     "Impacta no Início da Demolição do Piso do Radier do Lavador de Gases a Título de Área "
     "caso aconteça alguma mudança significativa. "
     "(Início Previsto: 25/05/26 - Atividade do Cronograma: ID 466).",
     None,date(2026,5,20),None,None),

    ("[PROC][SUP]", date(2026,5,12),"CISTO","ABELV",
     "Uehara (Engenheiro Mecânico do HVAC Abelv)",
     "Contratação Lavador de Gases",
     None,None,date(2026,5,15),
     "19/05: Aguardando o Setor de Suprimentos da Abelv Fechar o Pedido.",None),

    ("[SUP]", date(2026,5,19),"CISTO","ABELV",
     "Ana Assis (Gerente do Suprimentos Abelv)",
     "Fechamento do Pedido de Compra do Lavador de Gases",
     "Impacta na identificação real do Dimensional da Base do Lavador de Gases, "
     "consequentemente também impactando o Início da Demolição do Piso do Radier do Lavador de Gases "
     "a Título de Área caso aconteça alguma mudança significativa. "
     "(Início Previsto: 25/05/26 - Atividade do Cronograma: ID 466).",
     None,date(2026,5,19),None,date(2026,5,20)),

    ("[CIVIL]", date(2026,5,12),"FARMO","KROOM",
     "Diego (Gerente de Projetos da Kroom) / Leobino (Eng. Civil Abelv)",
     "Definição do Tipo de Fundação do Prédio",
     "Impacta no início da Fundação do Prédio "
     "(Início Previsto: 20/08/26 - Atividade do Cronograma: ID 431).",
     431,date(2026,5,13),None,None),

    ("[CIVIL]", date(2026,5,12),"FARMO","CRISTÁLIA",
     "Edson (Cristália) / Leobino (Eng. Civil Abelv)",
     "Recebimento do Projeto da Base do Lavador de Gases Existente.",
     "Impacta na Formalização da Nova Locação que foi combinada IN LOCO para execução da base do "
     "Lavador existente. Início da Confecção da Nova Base (Radier) do Lavador de Gases Existente "
     "(Início Previsto: 05/06/26 - Atividade do Cronograma: ID 251).",
     None,date(2026,5,15),None,None),

    ("[MEC/TUB]", date(2026,5,7),"FARMO","MGC",
     "Yohanna (Engenheira Mecânica Abelv)",
     "Solicitação e Recebimento dos Projetos do Farmoquímico da Empresa MGC, e envio para Cristália para aprovação",
     "Impacta na Compra dos Materiais e Subcontratações para realização dos materiais.",
     None,date(2026,5,19),None,date(2026,5,20)),

    ("[CIVIL]", date(2026,5,19),"FARMO","ABELV",
     "Leobino (Eng. Civil Abelv)",
     "Enviar para a MGC as cotas de elevação do Lavador de Gases",
     "Impacta na confecção do Projeto do Radier do Lavador de Gases",
     None,date(2026,5,19),None,None),

    ("[ELET]", date(2026,5,19),"FARMO","ABELV",
     "Leobino (Eng. Civil Abelv)",
     "Enviar para a MGC as cotas de elevação da Sala Elétrica",
     "Impacta na confecção do Projeto da Sala Elétrica",
     None,date(2026,5,20),None,None),

    ("[CIVIL]", date(2026,5,19),"FARMO","KROOM",
     "Diego (Gerente de Projetos da Kroom) / Leobino (Eng. Civil Abelv)",
     "A Krrom precisa informar a Data em que irão apresentar o Tipo de Fundação que será aplicada no Farmoquímico.",
     "Impacta na Contratação da Empresa para realização da Estaca, por ventura impactando na compra "
     "de materiais da estaca (Início Previsto: 08/06 - Atividade do Cronograma: ID 118).",
     None,date(2026,5,19),None,None),

    ("[CIVIL]", date(2026,5,19),"CISTO","KROOM",
     "Diego (Gerente de Projetos da Kroom) / Leobino (Eng. Civil Abelv)",
     "A Krrom precisa apresentar a Metodologia de Corte que será aplicado para avaliar a resistência "
     "do piso onde poderá ser construída a base da Plataforma dos Reatores, em função da Interferência "
     "da Instalação da Nova Rede Hidrossanitária.",
     "Impacta o início do Corte do Piso para confecção das Bases da Plataforma dos Reatores "
     "(Início Previsto: 21/05 - Atividade do Cronograma: ID 22). E Demolição do Piso para "
     "Instalação da Rede Hidrossanitária (Início Previsto: 18/05 - Atividade do Cronograma: ID 58).",
     None,date(2026,5,20),
     "20/05: A Krrom apresentou a alternativa de realização de um Ensaio Não Destrutivo de Esclerometria, "
     "pois seria mais rápido o método de avaliação da Resistência Mecânica.",
     date(2026,5,20)),

    ("[CIVIL]", date(2026,5,19),"FARMO","KROOM",
     "Diego (Gerente de Projetos da Kroom) / Leobino (Eng. Civil Abelv)",
     "Elaboração do Pedido da Tubulação de Água Pluvial",
     "Impacta a Compra da Tubulação de Água Pluvial",
     None,date(2026,5,27),None,None),

    ("[DOC]", date(2026,5,19),"FARMO","KROOM",
     "Rodrigo (Téc. Planej. da Kroom) / Leobino (Eng. Civil Abelv)",
     "A Kroom precisa enviar os Pedidos de Faturamento Direto",
     "Impacto na Medição",
     None,date(2026,5,19),None,date(2026,5,19)),

    ("[SUP]", date(2026,5,19),"CISTO","KROOM",
     "Tiago (Gestor de Projetos Abelv) / Celso (Gestor de Projetos Abelv)",
     "Verificação do Efetivo de Andaime para atendimento das Obras (Farmoquímico e Citostático).",
     "Impacto de acesso para realização das Frentes de Montagem",
     None,date(2026,5,20),None,date(2026,5,20)),

    ("[MEC/TUB]", date(2026,5,19),"CISTO","ABELV",
     "Leobino (Eng. Civil Abelv)",
     "Montagem do Pipe-Shop de Aço Carbono no Canteiro de Obra Abelv.",
     "Impacta na Fabricação da Tubulação de Aço Carbono "
     "(Início Previsto: 25/05/26 - Atividade do Cronograma: ID 54 e ID 317).",
     None,date(2026,5,20),None,date(2026,5,20)),

    ("[DOC][SUP]", date(2026,5,19),"CISTO","ABELV",
     "Erik Massola (Comprador Abelv) / Tiago Tiago (Gestor de Projetos Abelv)",
     "O Setor de Compras precisa enviar o Efetivo (Nomes e Cpfs dos colaboradores) da empresa "
     "contratada Açoplast (Estrutura Metálica) para Tiago Matos, para posterior envio para Cristália "
     "realizar a avaliação social dos mesmos.",
     "Impacto: Caso os mesmos não forem aprovados, eles não poderão adentrar ao site, podendo "
     "impactar o prazo da obra.",
     None,date(2026,5,20),None,None),

    ("[SUP]", date(2026,5,19),"CISTO","ABELV",
     "Edimar Cunha (Supervisor de Suprimentos Abelv) / Tiago Tiago (Gestor de Projetos Abelv)",
     "Contratação do Fornecedor de Andaime.",
     "Impacto de acesso para realização das Frentes de Montagem",
     None,date(2026,5,22),None,None),

    ("[DOC][SMS]", date(2026,5,19),"FARMO","ABELV",
     "Diego (Gerente de Projetos da Kroom) / Leobino (Eng. Civil Abelv)",
     "A empresa Krrom precisa Regularizar a Documentação da Empresa Recicla (Bota Fora).",
     "Impacto: Caso aconteça alguma auditoria ou acidente, estamos descobertos por documentação "
     "legal de subcontratação.",
     None,date(2026,5,21),None,None),

    ("[MEC/TUB]", date(2026,5,19),"CISTO","ABELV",
     "Yohanna (Engenheira Mecânica Abelv)",
     "Verificação da readequação do Projeto da Plataforma dos Reatores por base do nosso fornecedor "
     "que vai fabricar, pois os reatores adquiridos pela Cristália não cabem no mesmo.",
     "Impacto: Atraso na Fabricação do Projeto da Plataforma dos Reatores, por necessidade de "
     "elaboração do Novo Projeto para readequação do novo lay-out "
     "(Início e Término Previsto: 14/05/26 e 13/07/26 - Atividade do Cronograma: ID 650).",
     650,date(2026,5,20),None,None),

    ("[MEC/TUB]", date(2026,5,19),"CISTO","CRISTÁLIA",
     "Yohanna (Engenheira Mecânica Abelv)",
     "O Filtro Secador adquirido pela Cristália não cabe na base do Projeto Fornecido, logo a Cristália "
     "ficou de elaborar um Novo Projeto da Base do Filtro Secador para essa nova realidade.",
     "Impacto: Atraso na Construção da Nova Base do Filtro Secador "
     "(Início Previsto: 20/05/26 - Atividade do Cronograma: ID 9).",
     9,date(2026,5,20),None,None),

    ("[CIVIL]", date(2026,5,19),"CISTO","CRISTÁLIA",
     "Yohanna (Engenheira Mecânica Abelv)",
     "A Cristália tem que apresentar o Projeto da Nova Locação do Ralo do Sistema Hidrossanitário, "
     "pois o Projeto Atual da Base da Plataforma dos Reatores está na mesma coordenada dos Ralos.",
     "Impacto: Atraso na Conclusão do Corte do Piso para Novo Sistema Hidrossanitário. "
     "(Término Previsto: 18/05/26 - Atividade do Cronograma: ID 59).",
     59,date(2026,5,20),None,None),

    ("[CIVIL]", date(2026,5,20),"CISTO","CRISTÁLIA",
     "Leobino (Eng. Civil Abelv)",
     "Confirmação do Cliente da Aplicação de Tinta Asfáltica nos Diques do Piso Técnico, conforme orientado no Projeto.",
     None,None,date(2026,5,20),
     "20/05: Sr. Edson da Cristália na Reunião de Planejamento no Canteiro, orientou continuarmos segundo o Projeto.",
     date(2026,5,20)),

    ("[DOC]", date(2026,5,20),"CISTO","ABELV",
     "Ilson (Planejador Abelv) / Victor (Planejador Abelv)",
     "Elaboração do Estudo de HH aplicado até a data 19/05/26, conforme solicitado em reunião.",
     None,None,date(2026,5,25),None,None),

    ("[SMS]", date(2026,5,20),"CISTO","KROOM",
     "Diego (Gerente de Projetos da Kroom) / Leobino (Eng. Civil Abelv)",
     "Compra ou Projeção de Compra do Pluviômetro, com objetivo de medir a quantidade de chuva (precipitação) na Obra, e registrar os impactos das atividades.",
     "Impacto: Registro de Comprovação de Impactos de Chuvas a nível de RDO.",
     None,date(2026,5,20),None,None),

    ("[MEC/TUB][SUP]", date(2026,5,21),"CISTO","ABELV",
     "Celso (Gestor de Projetos Abelv)",
     "Emissão de Solicitação de Compra (SC) para Fabricação da Linha do Dreno do TRAP",
     "Impacto: Fabricação da Linha do Trap (Início Previsto: 25/05 - Atividade do Cronograma: ID 169).",
     169,date(2026,5,21),None,None),

    ("[CIVIL]", date(2026,5,21),"CISTO","ABELV",
     "Leobino (Eng. Civil Abelv)",
     "Elaboração de CT (Consulta Técnica) a respeito da Aplicação da Tinta Asfáltica que segundo o Projeto está orientando aplicar nos Diques do Pavimento Técnico.",
     "Impacto: Pintura Asfáltica nos Diques do Primeiro Pavimento (Início Previsto: 02/06 - Atividade do Cronograma: ID 279).",
     279,date(2026,5,21),None,None),

    ("[CIVIL]", date(2026,5,21),"CISTO","ABELV",
     "Leobino (Eng. Civil Abelv)",
     "Solicitação de Visita Técnica e envio de documentação dos Colaboradores da empresa GEOCOM (Empresa de Ensaio de Esclerometria).",
     "Impacto: Atraso do início da confecção da base dos reatores, atividade que estava prevista para o "
     "dia 21/05/26 (ID: 22), em virtude do Projeto Fornecido pela Cristália, a base da Plataforma do "
     "Reator está localizada no Local do Ralo.",
     22,date(2026,5,21),None,None),

    ("[CIVIL][SMS]", date(2026,5,21),"CISTO","ABELV",
     "Celso (Gestor de Projetos Abelv) / Leobino (Eng. Civil Abelv)",
     "Confecção de Andaime de Proteção contra quedas de Materiais para Atividade de Furação da Laje no Prédio do Citostático, solicitado pela Krrom.",
     "Impacto: Atraso no Início da Furação da Laje do Citostático (Início Previsto: 15/06 - Atividade do Cronograma: ID 284).",
     284,date(2026,6,8),None,None),

    ("[CIVIL]", date(2026,5,21),"CISTO","ABELV",
     "Leobino (Eng. Civil Abelv)",
     "Elaboração de CT para Definição do Projeto dos Diques Técnicos, pois o Projeto Civil orienta a "
     "construção de 2 Diques, e o Projeto Mecânico orienta apenas 1 Dique para todos os equipamentos.",
     "Impacto: Retrabalho nos Diques de Contenção do Piso Técnico, pois já foi iniciado essa atividade. "
     "(Início Previsto: 21/05 - Atividade do Cronograma: ID 276).",
     276,date(2026,5,21),None,None),

    ("[SUP]", date(2026,5,21),"CISTO","ABELV",
     "Yohanna (Engenheira Mecânica Abelv)",
     "Levantamento Inicial do Quantitativo de Tintas para Obra.",
     None,None,date(2026,5,29),None,None),

    ("[CIVIL]", date(2026,5,21),"CISTO","CRISTÁLIA",
     "Leobino (Eng. Civil Abelv)",
     "Solicitar a Cristália a Definição da Tinta Externa que será Aplicada nos Diques de Contenção do Piso Técnico",
     None,None,date(2026,5,22),None,None),
]

STATUS_EMOJI = {
    "ATRASADO": "🔴",
    "ALERTA": "🟡",
    "NO PRAZO": "🟢",
    "CONCLUÍDO": "✅",
    "CONCLUÍDO COM ATRASO": "⚠️",
    "—": "⚪",
}

# Ordem de exibição das disciplinas
DISC_ORDER = ["[CIVIL]","[MEC/TUB]","[PROC]","[ELET]","[SUP]","[SMS]","[DOC]",
              "[PROC][SUP]","[MEC/TUB][SUP]","[DOC][SUP]","[DOC][SMS]","[CIVIL][SMS]"]

grouped = defaultdict(list)
for idx, row in enumerate(dados, 1):
    disc = row[0]
    grouped[disc].append((idx, row))

from collections import Counter
st_list = [calc_status(d[8], d[10]) for d in dados]
st_count = Counter(st_list)

lines = []
lines.append("# Restrições CONECTOR — Cristália 25098 + 25103")
lines.append(f"**Data:** 21/05/2026 | **Total:** {len(dados)} itens\n")

# Resumo de status
lines.append("## Resumo de Status\n")
lines.append("| Status | Qtde |")
lines.append("|--------|------|")
for s in ["ATRASADO","ALERTA","CONCLUÍDO COM ATRASO","CONCLUÍDO","NO PRAZO","—"]:
    n = st_count.get(s, 0)
    if n:
        em = STATUS_EMOJI.get(s, "")
        lines.append(f"| {em} {s} | {n} |")
lines.append(f"| **TOTAL** | **{len(dados)}** |")
lines.append("")

# Itens por disciplina
lines.append("---\n")

disc_keys = DISC_ORDER + [d for d in grouped if d not in DISC_ORDER]

for disc in disc_keys:
    if disc not in grouped:
        continue
    items = grouped[disc]
    lines.append(f"## {disc}\n")
    for idx, row in items:
        disc_val, elab, proj, emp, resp, desc, imp, id_imp, nec, obs, conc = row
        st = calc_status(nec, conc)
        da = calc_dias(nec, conc)
        em = STATUS_EMOJI.get(st, "")

        lines.append(f"### Item {idx:02d} — {proj} | {emp}")
        lines.append(f"**Status:** {em} {st}  ")
        lines.append(f"**Elaboração:** {fmt_date(elab)}  ")
        lines.append(f"**Responsável:** {resp}  ")
        if nec:
            lines.append(f"**Necessidade:** {fmt_date(nec)}  ")
        if conc:
            lines.append(f"**Conclusão Real:** {fmt_date(conc)}  ")
        if isinstance(da, int) and da > 0:
            lines.append(f"**Dias Atrasado:** {da}  ")
        if id_imp:
            lines.append(f"**ID Impact:** {id_imp}  ")
        lines.append("")
        lines.append(f"**Descrição:** {desc}")
        lines.append("")
        if imp:
            lines.append(f"**Impacto:** {imp}")
            lines.append("")
        if obs:
            lines.append(f"**Observação:** {obs}")
            lines.append("")
        lines.append("---")
        lines.append("")

out = "/home/user/meu-planejamento/Restricoes_CONECTOR_21052026.md"
with open(out, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"✅ MD gerado: {out}")
print(f"   Total: {len(dados)} itens")
