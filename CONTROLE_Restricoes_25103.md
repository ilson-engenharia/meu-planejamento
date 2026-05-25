---
projeto: "[[25103]]"
tipo: CONTROLE_RESTRICOES
responsavel_escrita: "Claude Conector"
regra: "Somente o Conector escreve. Operador lê para gerar dashboards."
ultima_atualizacao: "2026-05-25"
semana: S21
total: 9
atrasado: 6
concluido: 1
concluido_com_atraso: 1
no_prazo: 1
---

# CONTROLE DE RESTRIÇÕES — 25103 FARMOQUÍMICA
## Fonte única de verdade | Atualizado pelo Conector a cada sessão

> **Regra:** Somente o Conector escreve aqui. O Operador lê para gerar o GESTAO.xlsx.
> **Wikilinks:** [[25103]] [[ABELV]] [[KRROM]] [[Cristália]]

---

## Tabela de Restrições

| ID | Projeto | Disc. | Elaboração | Empresa | Responsável | Descrição | Impacto | Necessidade | Observação | Conclusão Real | Dias Atraso | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 11 | [[25103]] | [CIVIL] | 12/05/26 | KRROM | Diego (KRROM) / Leobino (ABELV) | Definição do Tipo de Fundação do Prédio | Impacta início Fundação do Prédio (ID Cron 431). Início previsto 20/08/26 | 13/05/26 | — | — | 9 | ⚠️ ATRASADO |
| 12 | [[25103]] | [CIVIL] | 12/05/26 | CRISTÁLIA | Edson (Cristália) / Leobino (ABELV) | Recebimento do Projeto da Base do Lavador de Gases Existente | Impacta início Confecção Nova Base (Radier) Lavador Gases Existente (ID 251). Início previsto 05/06/26 | 15/05/26 | — | — | 7 | ⚠️ ATRASADO |
| 13 | [[25103]] | [MEC/TUB] | 07/05/26 | MGC | Yohanna (ABELV) | Solicitação e Recebimento dos Projetos do Farmoquímico da MGC e envio para aprovação da Cristália | Impacta Compra de Materiais e Subcontratações | 19/05/26 | — | 20/05/26 | 1 | ⚠️ CONCLUÍDO COM ATRASO |
| 14 | [[25103]] | [CIVIL] | 19/05/26 | ABELV | Leobino (ABELV) | Enviar para a MGC as cotas de elevação do Lavador de Gases | Impacta confecção do Projeto do Radier do Lavador de Gases | 19/05/26 | — | — | 3 | ⚠️ ATRASADO |
| 15 | [[25103]] | [ELET] | 19/05/26 | ABELV | Leobino (ABELV) | Enviar para a MGC as cotas de elevação da Sala Elétrica | Impacta confecção do Projeto da Sala Elétrica | 20/05/26 | — | — | 2 | ⚠️ ATRASADO |
| 16 | [[25103]] | [CIVIL] | 19/05/26 | KRROM | Diego (KRROM) / Leobino (ABELV) | A Krrom precisa informar a data em que irá apresentar o Tipo de Fundação do Farmoquímico | Impacta Contratação empresa para Estaca e compra materiais (ID 118). Início previsto 08/06 | 19/05/26 | — | — | 3 | ⚠️ ATRASADO |
| 18 | [[25103]] | [CIVIL] | 19/05/26 | KRROM | Diego (KRROM) / Leobino (ABELV) | Elaboração do Pedido da Tubulação de Água Pluvial | Impacta Compra da Tubulação de Água Pluvial | 27/05/26 | — | — | 0 | 🔵 NO PRAZO |
| 19 | [[25103]] | [DOC] | 19/05/26 | KRROM | [[Rodrigo]] (KRROM) / Leobino (ABELV) | A Krrom precisa enviar os Pedidos de Faturamento Direto | Impacto na Medição | 19/05/26 | — | 19/05/26 | 0 | ✅ CONCLUÍDO |
| 20 | [[25103]] | [CIVIL] | 19/05/26 | ABELV | Diretoria Comercial ABELV | Emissão do Sinal Financeiro de Mobilização ABELV→KRROM para expansão do efetivo civil de 3 para 8 MOD | Impacta início Área Externa (nova estrutura civil) previsto 05/06/26 e gate Liberação Escavações em 06/08/26 (ID Cron 1.4.4). Onboarding ~4 semanas — sinal após 30/05 compromete agosto | 22/05/26 | 22/05: Reunião Governança 19/05 aprovou integração de 8 pessoas. Requisição liberada. Sinal financeiro NÃO emitido. KRROM permanece com 3 MOD até 05/06/26 | — | 3 | ⚠️ ATRASADO |

---

## ⚠️ ALERTA — Restrições KRROM pendentes de confirmação de projeto (Operador)
> O Operador identificou nos RDOs (comunicado via INBOX_PARA_CONECTOR 24/05):
> - Elevação do radier (RDOs 37-39, 06-08/05) — aguardando projetista
> - Técnico de segurança KRROM fora de campo desde 04/05 (RDO 35)
>
> **Aguardando resposta do Operador no DIALOGO_AGENTES** para saber se são do 25098 ou 25103.
> Quando confirmado, serão adicionadas neste CONTROLE com IDs 21 e 22.

---

## Legenda de Status

| Status | Significado |
|---|---|
| ✅ CONCLUÍDO | Resolvido no prazo |
| ⚠️ CONCLUÍDO COM ATRASO | Resolvido, mas após prazo |
| ⚠️ ATRASADO | Prazo vencido, ainda aberto |
| 🔴 CRÍTICO | Atrasado e impacto direto no cronograma |
| 🟡 ALERTA | Vence hoje ou amanhã |
| 🔵 NO PRAZO | Aberto, dentro do prazo |

---

## Histórico de Atualizações

| Data | Sessão | O que mudou |
|---|---|---|
| 25/05/26 | S21 | Arquivo criado. Dados migrados da Planilha_de_Restricoes_210526.xlsx + nova restrição ID 20 (sinal financeiro KRROM). Dias de atraso recalculados para 22/05/26. |

---

*Escrito por Claude Conector | [[25103]] | DEC-16 + DEC-17*
*Operador: leia, não escreva aqui.*
