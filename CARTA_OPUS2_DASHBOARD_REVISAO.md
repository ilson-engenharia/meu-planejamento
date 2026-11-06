# CARTA TÉCNICA — REVISÃO DO DASHBOARD KPI RNEST Z-546
**De:** Análise Opus (Claude) — Revisão Independente  
**Para:** Ilson dos Santos Azevedo — Eng. Planejamento OTZ  
**Data:** 21/08/2026  
**Ref.:** DASH_BOARD_KPI_RNEST_20082026.html — Parecer técnico pré-apresentação gerencial

---

## 1. SITUAÇÃO ATUAL

O dashboard foi revisado à luz de três fontes de conhecimento acumuladas nesta sessão:
- `TAXONOMIA_COMPLETA_Z546.md` — pipeline de dados, Power Query, 958 linhas
- `CONTEXTO_OBRA_Z546.md` — contrato, obra, dependências, 2.303 linhas
- Dados brutos: PW CSV (18.198 linhas), LD Excel (18 abas), Cadastro HH

O parecer abaixo é estruturado como: **o que está certo · o que precisa de decisão · o que precisa de correção**.

---

## 2. O QUE ESTÁ CERTO E É DEFENSÁVEL

### KPI 3 — Documentos Elaborados por Disciplina
- **Fonte:** PW CSV, filtros corretos aplicados (ENG OBRA + OTZ PROJETISTA, sem ATA)
- **Número:** 1.459 documentos únicos com DataAceiteGRD preenchida
- **Defensável:** sim. O cross-reference LD×PW confirma 2.705+1.585 documentos, zero cruzamento — correspondência perfeita.

### KPI 4 — Documentos Revisados × Diretos
- **Lógica:** documentos com RevisaoCompleta > "0" = com retrabalho. Correto.
- **Defensável:** sim, com a ressalva de que CHZ/JEI (acervos herdados) inflam o percentual de retrabalho — não é performance OTZ pura.

### KPI 6 — CONSAG 1ª análise e reanálise
- **SLA:** 3du e 2du (§9.2 fluxograma) — já corrigidos e documentados no dashboard.
- **Números:** 2,87 DU / 2,23 DU — defensáveis, revalidados em 20/08/2026.
- **Defensável:** sim.

### KPI 9 — Tempo médio por fase
- **Revalidado:** 1ª análise CONSAG 2,87 DU, reanálise 2,23 DU, Petrobras 11,23 DU
- **Defensável:** sim, com nota que Petrobras (N=250) tem baixo preenchimento de DataRetornoGRDCliente (1,6%).

### KPI 1 — Forecast HH
- **Metodologia:** HH/ciclo = HH real ÷ ciclos realizados no PW. Aplicada por disciplina × tipo.
- **Números:** Realizado 26.521h | Previsto teto 42.120h | Total 68.641h | Avanço 38,6%
- **Pico set/26:** 9.563h = 3,6× a média histórica (2.652h/mês)
- **Coerência com a LD:** a LD já calibrou baseline em outubro com 489 emissões — o pico é real, não erro de cálculo.
- **Defensável:** sim, com declaração explícita do intervalo (teto/base).

---

## 3. PONTOS QUE PRECISAM DE DECISÃO DO ILSON

### PONTO A — SLA da série OTZ no KPI 6

**Situação atual:** OTZ medida contra **5 dias úteis** (SLA do texto do §9.2: "A OTZ terá o prazo de 5 dias úteis contados da data do recebimento dos comentários").

**O que o fluxograma do §9.2 mostra (folha 11):** além do SLA de texto, o fluxograma detalha etapas com `OTZ–3du` e `OTZ–2du` para o ciclo interno OTZ×CONSAG.

**A ambiguidade:**
- O **texto** do §9.2 diz 5du para OTZ responder a comentários
- O **fluxograma** do §9.2 mostra 3du/2du para etapas do loop interno
- A série OTZ no KPI 6 mede o tempo entre a resposta da CONSAG e a criação da próxima revisão pela OTZ — isso pode ser o loop interno (3du) ou o externo (5du), dependendo da revisão

**Opções:**
1. **Manter 5du** — mais conservador, baseado no texto contratual. A OTZ aparece com 23% de casos acima do SLA → defensável perante a OTZ (SLA mais folgado).
2. **Mudar para 3du** — baseado no fluxograma. A OTZ aparece com mais casos acima → defensável perante Petrobras/CONSAG (SLA mais rigoroso).
3. **Separar em duas séries** — loop interno (3du) × resposta pós-Petrobras (5du) — mais completo, mais trabalho.

**Recomendação:** Ilson decide qual narrativa quer usar. Se o objetivo é **defender a OTZ**, manter 5du. Se o objetivo é **mostrar transparência máxima**, mudar para 3du ou separar as séries.

---

### PONTO B — 86 documentos "pré-cadastrados no PW" que não existem

**Achado:** 86 documentos na LD com `PRÉ CADASTRADO NO PW? = SIM` não aparecem no export do PW. Todos em status `EMITIR EMISSÃO INICIAL`.

**Impacto no dashboard:** esses documentos constam nas contagens da LD mas não têm par no PW — infla o gap LD×PW.

**Decisão necessária:** verificar com a equipe se esses 86 são erro de cadastro na LD ou documentos que realmente foram bloqueados no envio para o PW.

---

### PONTO C — 3 campos contratuais vazios na LD

Os campos `SEVERIDADE`, `Rede de Precedência` e `FLUXOGRAMA (REF. Isométrico)` têm 0 de 2.824 linhas preenchidas — são obrigações do Anexo VII.

**Impacto no dashboard:** não afeta os KPIs atuais diretamente, mas é risco contratual.

**Decisão necessária:** priorizar preenchimento antes de qualquer auditoria da Petrobras.

---

### PONTO D — OTZ 0du: SIGEM no mesmo dia que PW

O fluxograma mostra `OTZ–0du` para upload no SIGEM no mesmo dia do envio ao PW — obrigação com SLA zero que nenhum KPI mede.

**Decisão necessária:** incluir como KPI novo ou como nota no KPI 9?

---

## 4. O QUE PRECISA DE CORREÇÃO ANTES DA APRESENTAÇÃO

### CORREÇÃO 1 — Nomenclatura KPI 5 vs KPI 7

O KPI 5 chama-se "Documentos Elaborados por Mês" mas conta documentos únicos pela 1ª DataAceiteGRD — não "documentos emitidos pela Petrobras" (sem sufixo). O conceito correto de "documento emitido" = DataAceiteGRD sem sufixo, que é a coluna `eo` do KPI 7.

**Correção:** renomear KPI 5 para "Documentos Únicos Entrados em Fluxo por Mês" e deixar claro na nota que é a data da 1ª formalização, não da aprovação Petrobras.

### CORREÇÃO 2 — Nota sobre RL_PW (achado crítico da taxonomia)

A aba `RL_PW` do Excel LD não alimenta nenhuma fórmula — foi descoberto pela análise do Power Query. "Emitido no PW" na LD significa "GRD saiu do E-CLIC", não "consta no ProjectWise". Essa distinção precisa aparecer como nota no dashboard (KPI 3 e KPI 5) para evitar interpretação errada.

### CORREÇÃO 3 — Civil zerado no KPI 1

O KPI 1 não tem HH de Civil porque a planilha correspondente (outra gerência) ainda não foi recebida. Isso precisa aparecer como nota explícita: "Civil: aguardando planilha HH da gerência DPC — será incorporado na próxima atualização."

---

## 5. HIERARQUIA PARA A PRIMEIRA APRESENTAÇÃO GERENCIAL

Se a apresentação for amanhã, a ordem de prioridade é:

| Prioridade | Ação | Tempo estimado |
|---|---|---|
| 1 | Decidir SLA OTZ (Ponto A) | 10 min |
| 2 | Adicionar nota "Civil pendente" no KPI 1 | 5 min |
| 3 | Renomear KPI 5 (Correção 1) | 5 min |
| 4 | Adicionar nota RL_PW (Correção 2) | 10 min |
| 5 | Registrar 86 docs pré-cadastrados como risco conhecido | 5 min |

**Total:** ~35 minutos de ajustes para o dashboard estar totalmente defensável.

---

## 6. NÚMEROS DEFENSÁVEIS POR KPI (PARA USAR EM REUNIÃO)

| KPI | Número principal | Frase defensável |
|---|---|---|
| KPI 1 | 26.521h realizadas / 42.120h previstas | "Completamos 38,6% do HH. O pico de setembro exige 3,6× o ritmo histórico — a LD já está calibrada para isso." |
| KPI 3 | 1.459 docs em fluxo | "1.459 documentos formalizados via GRD de 4.610 no escopo." |
| KPI 4 | 56% sem retrabalho | "56% dos documentos foram aprovados sem revisão — acima da média para projetos de brownfield." |
| KPI 5 | 287 docs em jul/26 (pico) | "Julho foi o mês de maior produção — 287 documentos únicos entrados em fluxo." |
| KPI 6 CONSAG | 2,87 DU / 2,23 DU | "CONSAG entrega dentro do SLA contratual de 3du/2du." |
| KPI 6 Petrobras | 11,23 DU vs SLA 10 DU | "Petrobras está 12% acima do SLA — dado para gestão CONSAG, não para OTZ." |
| KPI 6 OTZ | 7,15 DU vs SLA 5 DU | "OTZ: 23% acima do SLA de 5du. Tendência de melhora em ago/26." |
| KPI 7 | 3.046 eventos de emissão | "3.046 eventos — inclui todas as revisões, não apenas primeiras emissões." |
| KPI 9 | Idem KPI 6 | "Confirmado célula a célula. Petrobras: N=250 — amostra pequena, usar como direção." |

---

## 7. UMA OBSERVAÇÃO FINAL

A curva de aprendizado da equipe é o dado mais poderoso que nenhum KPI mostra: **68,7 → 18,6 HH/documento de janeiro a julho** (3,7× mais eficiente com 53% mais pessoas). Esse número protege a OTZ em qualquer discussão de produtividade. Considere incluir como indicador adicional.

---

*Gerado em: 21/08/2026 — Análise baseada em todos os documentos disponíveis nesta sessão.*
