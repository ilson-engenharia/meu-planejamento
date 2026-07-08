# /atualizar-push-list — Ciclo de Atualização Push List REV3

## Projeto
**ASU Jundiaí (26001) | OTZ Engenharia × Messer Gases for Life**
Subcontratada: Andrade e Rocha (DAENG) | Contrato CLM-216

---

## O que Ilson envia

Um Excel atualizado do Lucas (DAENG):
- Nomeação típica: `DAENG_PUSH_LIST_ASU_JUNDIAI_5__ATUALIZADO_DD.MM.xlsx`
- Aba ativa: **Push List REV3** | Cabeçalho linha 3 | Dados a partir linha 4
- Colunas: A=#Card · B=Área · C=Local Nº · D=Nome do Local · E=Foto · F=#Ativ · G=Disciplina · H=Atividade/Descrição · I=Peso · J=Status · K=Conclusão · L=Avanço(%)

---

## O que o Claude faz automaticamente

1. Salva o arquivo em `/root/.claude/uploads/<session-id>/`
2. Atualiza `EXCEL_IN` no script com o novo caminho
3. Atualiza `TODAY`, `TODAY_IDX` e `DIAS_ABERTO` conforme a data da atualização
4. Roda `gerar_push_list_rev3.py`
5. Valida KPIs no terminal (Cards, Atividades, Concluídas, Avanço%)
6. Commita + push para `claude/onedrive-access-permissions-WeExM`
7. Entrega os **3 arquivos definitivos**:
   - `DAENG_PUSH_LIST_ASU_JUNDIAI.html` — dashboard interativo dark navy
   - `DAENG_PUSH_LIST_ASU_JUNDIAI.xlsx` — planilha de controle (tema claro)
   - `DAENG_PUSH_LIST_ASU_JUNDIAI.pdf` — versão impressa tema claro Messer

---

## Arquivos do projeto Push List

| Arquivo | Função |
|---------|--------|
| `projetos/OTZ_ASU_JUNDIAI/push_list/gerar_push_list_rev3.py` | Script gerador — **padrão vigente** |
| `projetos/OTZ_ASU_JUNDIAI/push_list/DAENG_PUSH_LIST_ASU_JUNDIAI.html` | Dashboard HTML — **modelo definitivo** |
| `projetos/OTZ_ASU_JUNDIAI/push_list/DAENG_PUSH_LIST_ASU_JUNDIAI.xlsx` | Planilha XLS — **modelo definitivo** |
| `projetos/OTZ_ASU_JUNDIAI/push_list/DAENG_PUSH_LIST_ASU_JUNDIAI.pdf` | PDF impresso — **modelo definitivo** |
| `projetos/OTZ_ASU_JUNDIAI/push_list/cftv_photos/` | Fotos dos 12 pontos CFTV (cftv_01.jpg … cftv_11.jpg) |
| `projetos/OTZ_ASU_JUNDIAI/push_list/CLAUDE.md` | Briefing técnico completo desta disciplina |

---

## Constantes a atualizar no script

```python
EXCEL_IN  = os.path.join(UPLOAD, "<novo-arquivo>.xlsx")
TODAY     = date(YYYY, M, D)       # data da atualização recebida
# LEVAN_DATE = date(2026, 7, 2)    # manter fixo — levantamento Caio 02/07
# WORKING_DAYS mantém fixo (04/07→17/07) salvo instrução de Ilson
DIAS_ABERTO = sum(1 for d in WORKING_DAYS if d <= TODAY)
```

---

## Calendário de acompanhamento (fixo — não alterar)

12 dias úteis seg–sáb: **04/07 → 17/07/2026** (sem domingos)
```
Dia  1: Sáb 04/07 | Dia  2: Seg 06/07 | Dia  3: Ter 07/07
Dia  4: Qua 08/07 | Dia  5: Qui 09/07 | Dia  6: Sex 10/07
Dia  7: Sáb 11/07 | Dia  8: Seg 13/07 | Dia  9: Ter 14/07
Dia 10: Qua 15/07 | Dia 11: Qui 16/07 | Dia 12: Sex 17/07
```
Entrega: **17/07/2026** — Data Book completo da obra

---

## Regras de negócio permanentes

### 1. Células mescladas — carry-forward
O Excel da DAENG mescla a coluna A nas linhas de atividade do mesmo card:
```python
current_key = None
if row[0] is not None:
    current_key = (lnum, fstr)  # nova linha de card
if current_key is None: continue
# processa atividade usando current_key
```

### 2. DISC_FIX — reclassificação
```python
DISC_FIX = {"Macrodrenagem / 5S": "Macrodrenagem"}
```

### 3. Conclusão = 100%
Quando `status.lower().startswith("conclu")` → campo Conclusão exibe **100%** (ignora data).

### 4. Cards CFTV (C01–C12)
- Lnum começa com "C" → processado como CFTV
- Fotos em `cftv_photos/` com crop landscape (center-crop 4:3)
- C12 sem foto → placeholder

### 5. Foto (col E) — parsing tolerante
```python
if isinstance(f_val, (int, float)): fstr = str(int(f_val))
elif f_val is None: fstr = "S/F"
```

### 6. Data de Tendência
```python
vel = done_atv / DIAS_ABERTO
trend_date = project_working_days(TODAY, ceil(pend_atv / vel))  # seg-sáb, sem domingo
# vermelho se trend_date > 17/07/2026
```

### 7. Curva-S — rótulos do gráfico
- Título linha 1: `Curva-S — Previsto × Realizado | 04/07 → 17/07/2026`
- Título linha 2: `Data Book` (vermelho negrito — entregável da obra)

### 8. Data Book no Excel
Linha extra ao final do XLS: peso=0, campo entregável = 17/07/2026.

---

## Modelos definitivos — layout IMUTÁVEL

> **Não alterar o layout visual sem aprovação do Supervisor Ilson do Santos Azevedo.**

### HTML (dark navy — interativo)
| Elemento | Detalhe |
|----------|---------|
| Fundo | `#06101E` (navy escuro) |
| Gauge | Velocímetro SVG 268×215 (global) + mini 158×122 (por card) |
| Filtros | Disciplina · Área · Status · busca texto |
| Cards | Grid `minmax(700px,1fr)` · 2 fotos side-by-side (ANTES/PÓS) · tabela atividades |
| Curva-S | SVG 560×260 · Previsto(tracejado azul) × Realizado(sólido verde) · defasagem triangulada · subtítulo "Data Book" em vermelho |
| Tendência | Card extra: Data de Tendência por velocidade/pendências |

### PDF (tema claro Messer — impressão)
Gerado via Playwright + Chromium (`/opt/pw-browsers/chromium`).
LIGHT_CSS injetado antes de `</style>` no HTML temporário — HTML original inalterado.

| Elemento | Cor PDF |
|----------|---------|
| Fundo | `#F0F4FA` |
| Header | `linear-gradient(135deg,#1A3680,#2050A0)` + `#CC2020` |
| Sec-header | `display:none` |
| Filter-bar | `display:none` |
| Fotos | `height:150px` (ANTES+PÓS cabem na largura A4) |
| Gauge | Classes `g-val`, `g-track`, `g-sublbl`, `g-needle`, `g-done`, etc. |
| Curva-S | `.cs-bg → #EDF2FB` · `.cs-lbl → #3A5070` · `.cs-grid → claro` |
| Disc. chart | `.dc-lbl → #1A2A40` · `.dc-pct → #3A5070` |

### XLS
- Sheet "Push List REV3" · cabeçalho linha 1 azul `#1A3680` · fundo branco
- 12 colunas: #Card · Área · Local Nº · Nome · Foto · #Ativ · Disciplina · Atividade · Peso · Status · Conclusão · Avanço%
- Linha final: Entrega Data Book (peso 0, entregável 17/07/2026)

---

## Fotos ANTES / PÓS

### ANTES (levantamento Caio — 02/07/2026)
- Fotos regulares: diretório `UPLOAD` (arquivos enviados por Ilson)
- Fotos CFTV: `cftv_photos/cftv_01.jpg` … `cftv_11.jpg`

### PÓS (conclusão — aguardando)
- Placeholder: "Aguardando Conclusão"
- Quando Ilson enviar: informar **Local Nº** e arquivo → Claude adiciona em `AREA_META` e reembarca

---

## Referências de consistência (08/07/2026 — modelos definitivos)

| Indicador | Valor |
|-----------|-------|
| Cards | 49 |
| Atividades | 225 |
| Concluídas | 48 |
| Avanço físico | 21.3% |
| Previsto (dia 4/12) | 33.3% |
| Defasagem | −12.0 pp |
| Data de Tendência | 25/07/2026 (vermelho) |

Se Cards ≠ 49 ou Atividades ≠ 225 após próxima atualização → verificar com Ilson antes de publicar.

---

## Informações fixas do projeto

| Campo | Valor |
|-------|-------|
| Projeto | ASU Jundiaí — 26001 |
| Contrato | CLM-216 |
| Contratada | Andrade e Rocha (DAENG) |
| Gerenciadora | OTZ Engenharia — GPLAN |
| Supervisor GPLAN | Ilson do Santos Azevedo |
| Responsável campo | Lucas (DAENG) — avanços e Excel |
| Levantamento CFTV | Caio Silva — 07/07/2026 |
| Prazo | 17/07/2026 |
| Branch Git | `claude/onedrive-access-permissions-WeExM` |

---

## O que o Claude NÃO muda automaticamente

- Layout dos cards (fotos, GPS, endereço, horário, estrutura visual)
- Nomes dos locais (exceto `NOME_FIX`)
- Padrão visual HTML (cores, fontes, gauge, filtros, Curva-S)
- Tema PDF Messer (LIGHT_CSS fixo)
- Fotos ANTES já embarcadas
- Calendário de dias úteis (04/07→17/07/2026)
- Cards CFTV e metadados
