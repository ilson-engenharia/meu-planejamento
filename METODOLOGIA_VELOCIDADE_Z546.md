---
tipo: memoria_de_calculo
titulo: Metodologia da Análise de Velocidade do Fluxo de Aprovação Documental
projeto: RNEST UGH U-36 — Z-546 / Lote D — contrato 00025129
data_base: 2026-08-18
gerado_em: 2026-08-19
autor: Claude (agente de análise) — para Eng. Ilson dos Santos Azevedo, Supervisor de Planejamento, OTZ Engenharia
relatorio_associado: velocidade-fluxo-z546.html
finalidade: permitir auditoria cruzada independente de cada número publicado
---

# Metodologia — Análise de Velocidade do Fluxo Documental Z-546

Este documento é a memória de cálculo do relatório `velocidade-fluxo-z546.html`. Ele existe para que
um auditor que **não viu a conversa original** possa reproduzir cada número a partir dos arquivos
brutos, verificar cada premissa e contestar cada decisão de filtro.

**Regra de leitura:** todo número publicado aparece aqui com (a) as colunas de origem, (b) o filtro
aplicado, (c) o código executado, (d) o resultado. Onde houve escolha metodológica, ela está
declarada e testada contra a alternativa.

---

## 1. Fontes de dados

Todos os arquivos em `/root/.claude/uploads/001b7fb0-8857-54b0-9eb5-28053bfc3f61/`.

| # | Arquivo | Sistema | Dono | Dimensões | Cabeçalho |
|---|---|---|---|---|---|
| F1 | `79f2bdab-Z546__RELAT_RIO_PW_18_08_26_8h.csv` | ProjectWise (PW) | **CONSAG** | 18.198 × 70 | linha 0 |
| F2 | `fe804493-Z546__RELAT_RIO_SIGEM.xlsx` | SIGEM | **PETROBRAS** | 13.463 × 28 | linha 4 (0-indexed) |
| F3 | `c33af65d-Z546__RELAT_RIO_MARKUP.xlsx` | E-CLIC (markup) | **OTZ** | 3.517 × 14 | linha 1 |
| F4 | `a438e06e-Z546__RELAT_RIO_DOCUMENTO.xlsx` | E-CLIC | **OTZ** | 27.774 × 49 | linha 0 |
| F5 | `fa3a78da-Z546__RELAT_RIO_EMISS_O.xlsx` | E-CLIC (emissões) | **OTZ** | 5.877 × 16 | linha 0 |
| F6 | `73dffbcc-...SIGEM_DOCUMENTOS_PREVISTOS.xlsx` | SIGEM | PETROBRAS | — | linha 4 |
| F7 | `4a425c0e-...SIGEM_CONSOLIDACAO...xlsx` | SIGEM | PETROBRAS | — | linha 4 |

**Documentos de referência (não são dados, são fonte de premissa):**

| Sigla | Documento | Uso nesta análise |
|---|---|---|
| PROC-COORD | `RUGH-PEX-OTZ-EX-U036-PRJ-PT-0002` — Procedimento de Coordenação OTZ × CONSAG, Rev. 0 | **§9.2 — origem dos SLAs de 10 DU e 5 DU** |
| GLOSSÁRIO | `GLOSSARIO_NOMENCLATURA_PW_RNEST.md` (19/08/2026) | significado das 70 colunas do PW; regra oficial de fila |
| N-1710 | Norma Petrobras N-1710 Rev. N — Codificação de Documentos Técnicos de Engenharia | estrutura do `NumeroDocumentoCliente` (Grupo 5 = código de origem) |
| XLSM-CONSAG | `CONSAG-PHC-ENG-DC-GERA-GES-PT-0001_20.xlsm` | confirmação de `AG` = Alexandre Germano; `DGS` = Suprimentos |

**Leitura de encoding do PW (F1):** separador `;`, encoding `utf-8-sig`, todas as colunas lidas como
`str` para evitar coerção automática de datas em formato ambíguo.

```python
pw = pd.read_csv(F1, sep=';', encoding='utf-8-sig', dtype=str)   # -> (18198, 70)
```

---

## 2. Filtros de escopo — quem é quem

### 2.1 Separação primária (usada em todos os números do PW)

Campo: `nomeEmpresa` (100% preenchido, 9 valores distintos).

```python
GRP_OTZ  = {'ENG OBRA', 'OTZ PROJETISTA'}
GRP_CONS = {'CONSAG', 'CONSAG QUALIDADE'}
pw['cls'] = np.select(
    [pw['nomeEmpresa'].isin(GRP_OTZ), pw['nomeEmpresa'].isin(GRP_CONS)],
    ['A_OTZ', 'CONSAG'], default='B_FORN')
```

| Classe | Empresas | Linhas |
|---|---|---|
| `A_OTZ` | ENG OBRA (1.794) + OTZ PROJETISTA (4.487) | **6.281** |
| `CONSAG` | CONSAG QUALIDADE (8.802) + CONSAG (2.906) | **11.708** |
| `B_FORN` | ENGEMASA (116), ASVOTEC (83), WEG (6), INCASE (2), VIBROPAC (2) | **209** |

**Fonte da regra:** GLOSSÁRIO §2.1 — `nomeEmpresa ∈ {ENG OBRA, OTZ PROJETISTA}` é o filtro oficial de
escopo OTZ (KPI-INSTR §9).

**Validação cruzada executada.** O campo `fornecimento` (pacote de compra, preenchido só em documento
de fornecedor) foi usado como classificador alternativo:

```python
pd.crosstab(pw['cls'], pw['fornecimento'].notna())
# A_OTZ   6281 False /    0 True
# B_FORN     0 False /  209 True
# CONSAG 11708 False /    0 True
```

**Resultado: consistência 100%.** Os 209 documentos classificados como fornecedor são exatamente os
209 com `fornecimento` preenchido. Reclassificar por `fornecimento` produz números idênticos
(Fase 2 Tipo B: n=113, média 12,9, 62,8% — igual).

### 2.2 Separação secundária — código de origem N-1710 (Grupo 5)

Usada **apenas** na Fase 1, para separar produção própria da OTZ do acervo herdado.

```python
pw['emissor'] = pw['NumeroDocumentoCliente'].astype(str).str.extract(
    r'^(?:[A-Z]-)?[A-Z]{2}-\d{4}\.\d{2}-\d{4,5}-[0-9A-Z]{3}-([0-9A-Z]{3})-')[0]
# extraiu em 9.313 de 18.198 linhas (51,2%)
```

As 48,8% sem extração são o **esquema de numeração dos RIR** (98,3% delas têm
`TipoDocumento == 'RIR'`), que não segue o N-1710 — ver GLOSSÁRIO §5.

**Validação executada** — cruzamento `emissor` × `nomeEmpresa`:

| emissor | ASVOTEC | CONSAG | ENG OBRA | ENGEMASA | INCASE | OTZ PROJ. | VIBROPAC | WEG |
|---|---|---|---|---|---|---|---|---|
| `ATI` | **83** | | | | | | | |
| `C1U` | | 2.902 | **1.793** | | | **1.647** | | |
| `CHZ` | | | | | | **1.727** | | |
| `JEI` | | | | | | **1.005** | | |
| `EDF` | | 1 | | **116** | | | | |
| `INH` | | | | | **2** | | | |
| `VCE` | | | | | | | **2** | |
| `WDD` | | | | | | | | **6** |

A correspondência é praticamente perfeita, o que sustenta a leitura do 5º campo como emissor
independentemente da norma.

| Código | Empresa | Papel | Fonte da identificação |
|---|---|---|---|
| `C1U` | OTZ ENGENHARIA | produção própria | GLOSSÁRIO §6 |
| `CHZ` | **CHEINTEC** | projetista anterior — acervo herdado pela OTZ | GLOSSÁRIO §12.2 (Ilson, 19/08/2026) |
| `JEI` | **Jaguará** | fornecedor/projetista anterior — acervo herdado | GLOSSÁRIO §12.2 |
| `ATI`/`EDF`/`WDD`/`INH`/`VCE` | ASVOTEC / ENGEMASA / WEG / INCASE / VIBROPAC | fornecedores | GLOSSÁRIO §6 (LD-FORN) |

> ⚠️ **Limitação declarada.** Não consegui extrair o corpo do PDF da N-1710 neste ambiente — as fontes
> são subconjuntos embutidos com codificação Identity, e as bibliotecas de PDF do ambiente estão
> quebradas (`_cffi_backend` ausente). Só a capa é legível em texto. A estrutura de 7 grupos da norma
> é citada **de segunda mão**, via GLOSSÁRIO §12. **A conclusão da Fase 1 não depende disso** — ela se
> apoia na tabela de validação acima, que é dado.

### 2.3 SIGEM — segmentação por natureza do documento

Campo: `Nível 3`. Necessária porque 80% do volume SIGEM é RIR de inspeção, que afoga a média.

```python
term = sg[sg['Status Workflow'] == 'TERMINADO']
rir  = term[term['Nível 3'] == '03.01.INSPEÇÃO RECEBIMENTO']       # n = 9.147
mob  = term[term['Nível 3'] == '01.01.MOB SERV PRELIMINARES']      # n = 1.127
eng  = term[~term['Nível 3'].isin([...os dois acima...])]          # n = 1.116
```

### 2.4 Markup — remoção das linhas de GRD

O relatório de markup tem **duas linhas por markup**: uma para o documento e uma para a GRD que o
transportou. As linhas de GRD têm `Disciplina == 'NÃO SE APLICA'`.

```python
doc = mk[mk['Disciplina'] != 'NÃO SE APLICA']    # 3.517 -> 1.753
# linhas removidas: 1.764
```

**Por que importa:** contar pendências na base bruta dá **2.057 markups pendentes / 52,1 DU**; na base
correta dá **293 / 33,2 DU**. O relatório publica os 293.

---

## 3. Definição de "dia útil"

Contagem por `numpy.busday_count` (segunda a sexta), com feriados **nacionais** brasileiros
2025–2026 excluídos. Feriados estaduais/municipais de Pernambuco **não** foram incluídos.

```python
FER = np.array([
 '2025-01-01','2025-03-03','2025-03-04','2025-04-18','2025-04-21','2025-05-01','2025-06-19',
 '2025-09-07','2025-10-12','2025-11-02','2025-11-15','2025-11-20','2025-12-25',
 '2026-01-01','2026-02-16','2026-02-17','2026-04-03','2026-04-21','2026-05-01','2026-06-04',
 '2026-09-07','2026-10-12','2026-11-02','2026-11-15','2026-11-20','2026-12-25'],
 dtype='datetime64[D]')

def du(ini, fim):
    ini = pd.to_datetime(ini).dt.floor('D').values.astype('datetime64[D]')
    fim = pd.to_datetime(fim).dt.floor('D').values.astype('datetime64[D]')
    ok  = ~(pd.isna(ini) | pd.isna(fim))
    r = np.full(len(ini), np.nan)
    r[ok] = np.busday_count(ini[ok], fim[ok], holidays=FER)
    return r
```

Convenção: `du(A, B)` conta dias úteis **de A até B, sem incluir B**. Emissão no mesmo dia = 0 DU.

### 3.1 Teste de sensibilidade executado

Recalculei tudo **sem nenhum feriado** (só seg–sex):

| Métrica | Com feriados (adotado) | Sem feriados | Δ |
|---|---|---|---|
| Fase 2 Tipo A — média | 2,37 DU | 2,52 DU | +0,15 |
| Fase 2 Tipo A — % ≤10 DU | 94,3% | 93,7% | −0,6 pp |
| Fase 2 Tipo B — média | 12,91 DU | 13,40 DU | +0,49 |
| **Fase 2 Tipo B — % ≤10 DU** | **62,8%** | **51,3%** | **−11,5 pp** ⚠️ |
| Fase 2b repasse — média | 4,47 DU | 4,71 DU | +0,24 |

**Conclusão:** as médias são robustas. O **% no prazo do Tipo B não é** — com n=113 e muitos casos
caindo exatamente em 10 DU, a escolha de feriados move o indicador em 11,5 pp. O relatório declara
isso e recomenda citar a média (12,9 DU), não o percentual.

### 3.2 Exceção: o SIGEM não foi recalculado

A coluna `Dias úteis em workflow` **já vem calculada pelo próprio SIGEM**. Foi usada como está,
sem recomputar a partir de `Inicio do workflow`. Isso é deliberado: o número que a Petrobras
reconhece é o dela. Consequência: o calendário de feriados do SIGEM pode diferir do meu, e os
números SIGEM não são estritamente comparáveis aos números PW no dígito decimal.

---

## 4. Limpeza aplicada

### 4.1 Datas fora de faixa

```python
for c in ['aceite','resp','env','ret','prev']:
    pw.loc[(pw[c] < '2024-01-01') | (pw[c] > '2029-12-31'), c] = pd.NaT
```

| Campo | Preenchidos | Fora de faixa | Efeito |
|---|---|---|---|
| `DataAceiteGRD` | 13.085 | 0 | — |
| `DataResposta` | 3.056 | 0 | — |
| `DataEnvioGRDCliente` | 1.078 | 0 | — |
| `DataRetornoGRDCliente` | 288 | 0 | — |
| `DataPrevista1Emissao` | 17.953 | **3** (até ano 6490) | só a Fase 1 |

### 4.2 Valores negativos — mantidos, com uma exceção declarada

Intervalos negativos (data-fim anterior à data-início) são **erro de cadastro**, não outlier
estatístico. Foram **mantidos** no cálculo publicado, com o impacto medido:

| Métrica | n | Negativos | Média c/ negativos | Média s/ negativos |
|---|---|---|---|---|
| Fase 2 (aceite→resposta) | 3.056 | 3 (0,10%) | 2,76 | 2,76 |
| Fase 2b (resposta→envio) | 1.077 | 2 (0,19%) | 4,47 | 4,49 |
| **Fase 3 (envio→retorno)** | **254** | **2 (0,79%)** | **9,46** | **10,53** ⚠️ |

Os dois registros negativos da Fase 3 são de −1 e **−251 DU** (data de envio lançada em 2027). Com
n=254, eles deslocam a média em 1,1 DU — o suficiente para mudar a leitura de "abaixo do SLA" para
"no limite do SLA". **O relatório publica 9,5 DU e declara 10,5 DU como o valor limpo**, recomendando
usar o segundo em discussão contratual.

### 4.3 O que NÃO foi removido

- Revisões superadas (`Última emissão == 'Não'`, 3.330 linhas) — cada revisão é um ciclo de análise
  real e conta como observação.
- Documentos cancelados (`Categoria == 'CAN'`, 17 linhas) — irrelevantes no volume.
- Outliers altos (máximos de 90, 159, 257, 372 DU) — são casos reais, não erro.

---

## 5. Cálculo de cada fase

### 5.1 Fase 1 — Elaboração / entrega vs. prazo previsto

**Pergunta:** o documento foi emitido antes ou depois da data planejada da 1ª emissão?

| Item | Valor |
|---|---|
| Campos | `DataPrevista1Emissao` → `DataAceiteGRD` |
| Sinal | positivo = atrasado; negativo = adiantado |
| SLA | 0 (o prazo é a própria data prevista) |

```python
pw['F1'] = du(pw['prev'], pw['aceite'])
pw.groupby('cls')['F1'].agg(['count','mean','median','max'])
```

| Classe | n | Média | Mediana | P90 | Máx | % ≤0 | Atraso médio dos atrasados |
|---|---|---|---|---|---|---|---|
| A_OTZ | 3.045 | **+20,0** | 0 | 232 | 372 | 50,4% | 82,6 DU |
| B_FORN | 149 | **+10,9** | 1 | 39 | 98 | 49,0% | 30,9 DU |
| CONSAG | 9.850 | +0,1 | 3 | 20 | 88 | 29,4% | 9,7 DU |

**Decomposição por código de origem** (só escopo A_OTZ):

```python
otz = pw[pw['cls']=='A_OTZ']
otz['grupo'] = np.select(
    [otz['emissor']=='C1U', otz['emissor'].isin(['CHZ','JEI'])],
    ['C1U — produção OTZ', 'CHZ/JEI — acervo herdado'], default='outros')
```

| Grupo | Docs | n c/ F1 | Média | Mediana | % ≤0 | Máx |
|---|---|---|---|---|---|---|
| `C1U` — produção OTZ | 3.440 | 1.369 | **+68,4** | +6 | 42,1% | 372 |
| `CHZ` — CHEINTEC | 1.727 | 1.075 | **−11,8** | 0 | 51,2% | 87 |
| `JEI` — Jaguará | 1.005 | 507 | **−40,0** | −35 | 75,3% | 97 |

Conferência aritmética: (1.369 × 68,4) + (1.582 × −20,9) + (94 × 1,9) = 60.755; ÷ 3.045 = **20,0** ✓
(bate com a média agregada da tabela anterior).

**Achado:** dos 397 documentos com atraso > 100 DU, **397 são `C1U`** e zero vêm do acervo herdado.

**Série mensal de `C1U` isolado** (por mês de `DataAceiteGRD`):

| Mês | n | Média | Mediana |
|---|---|---|---|
| 2026-01 | 159 | +220,4 | +236 |
| 2026-02 | 158 | +193,0 | +243 |
| 2026-03 | 97 | +100,1 | +12 |
| 2026-04 | 119 | +74,5 | +6 |
| 2026-05 | 161 | +31,8 | 0 |
| 2026-06 | 234 | +1,1 | −1 |
| 2026-07 | 311 | +9,7 | −29 |
| 2026-08 | 124 | **−0,2** | −15 |

CHZ/JEI só aparecem a partir de 2026-03 (166 docs) — antes disso o acervo ainda não tinha sido
carregado no PW. É por isso que a média do conjunto vira negativa a partir de junho.

> ⚠️ **Limitação da Fase 1.** `DataAceiteGRD` é o aceite da GRD **na CONSAG**, não a data em que a OTZ
> terminou o documento. A Fase 1 mede "atraso até o documento ser aceito", que inclui eventual espera
> de protocolo. Como `DataGRDEntrada` está 100% vazia, não é possível separar os dois trechos.

### 5.2 Fase 2 — Análise da CONSAG no PW

| Item | Valor |
|---|---|
| Campos | `DataAceiteGRD` → `DataResposta` |
| SLA | **10 DU** (PROC-COORD §9.2) |
| Justificativa do marco inicial | GLOSSÁRIO §2.6: `DataAceiteGRD` é *"o marco que inicia a contagem do SLA de 10 dias úteis da CONSAG"* |

```python
pw['F2'] = du(pw['aceite'], pw['resp'])
```

| Emissor | Tipo | n | Média | Mediana | P90 | Máx | % ≤10 DU |
|---|---|---|---|---|---|---|---|
| OTZ Projetista | A | 2.713 | 2,1 | 1 | 5 | 90 | 95,3% |
| Eng. Obra | A | 230 | 5,1 | 1 | 19 | 42 | 82,2% |
| **Subtotal A_OTZ** | A | **2.943** | **2,4** | **1** | **5** | **90** | **94,3%** |
| ENGEMASA | B | 106 | 12,9 | 10 | 24 | 76 | 65,1% |
| WEG | B | 6 | 14,5 | 16 | — | 17 | 16,7% |
| ASVOTEC | B | 1 | 3,0 | 3 | — | 3 | (n=1) |
| **Subtotal B_FORN** | B | **113** | **12,9** | **10** | **24** | **76** | **62,8%** |
| Total | A+B | 3.056 | 2,8 | 1 | 7 | 90 | 93,1% |

**Quem responde:** `ResponsavelResposta` — 3.043 de 3.056 (99,6%) são `@agnet.com.br`, domínio da
CONSAG. 2 são `cda-ugh@ottimiza.com` (CDA da OTZ) e 11 são um cadastro sem domínio
(`carlos.andrade`, média 38,7 DU). Ruído de 0,4%, sem efeito nos agregados.

**Taxa de reprovação** (campo `Resposta`):

```python
sub = pw[(pw.cls==cl) & pw['Resposta'].notna()]
rep = sub['Resposta'].str.contains('Not Approved|Reprovado', na=False).sum()
```

| Classe | Reprovados | Total c/ parecer | Taxa |
|---|---|---|---|
| A_OTZ | 7 | 2.943 | **0,2%** |
| B_FORN | 20 | 113 | **17,7%** |

### 5.3 Fase 2b — Repasse da CONSAG ao cliente

| Item | Valor |
|---|---|
| Campos | `DataResposta` → `DataEnvioGRDCliente` |
| SLA | 5 DU (referência operacional, **não contratual** — o §9.2 não prevê prazo para este trecho) |

```python
pw['F2b'] = du(pw['resp'], pw['env'])
```

**Resultado:** n=1.077 · média 4,5 · mediana 1 · P90 19 · máx 257 · 81,5% ≤5 DU.

### 5.4 Fase 3 — Petrobras

Medida por **duas vias independentes**, que não são equivalentes.

**Via A — SIGEM (relógio da Petrobras):** coluna `Dias úteis em workflow`, já calculada pelo sistema.

| Recorte | n | Média | Mediana | P90 | Máx | % ≤10 DU |
|---|---|---|---|---|---|---|
| TERMINADO — total | 11.390 | 4,8 | 3 | 10 | 159 | 90,7% |
| ↳ RIR / inspeção recebimento | 9.147 | 3,8 | 3 | 8 | 39 | 94,4% |
| ↳ Mobilização / serv. preliminares | 1.127 | 9,1 | 6 | 17 | 135 | 72,2% |
| ↳ **Engenharia e demais** | **1.116** | **8,7** | **6** | **18** | **159** | **79,1%** |
| ↳ Doc. de fornecedor (Nível 2 = 17) | 95 | 5,1 | 6 | 8 | 10 | 100% |
| EM ABERTO (INICIALIZADO) | 418 | 21,0 | 16 | 43 | 140 | 29,9% |

**Via B — GRD no PW (relógio da CONSAG):** `DataEnvioGRDCliente` → `DataRetornoGRDCliente`.

**Resultado:** n=254 · média 9,5 (10,5 sem os 2 negativos) · mediana 9 · máx 76 · 72,0% ≤10 DU.

> ⚠️ **As duas vias divergem e a divergência é informativa.** O SIGEM registra 11.390 workflows
> terminados; o PW registra retorno de cliente em apenas 254 de 1.078 GRDs enviadas. O PW **não é
> confiável para medir a Petrobras** — subpreenchimento severo do campo de retorno. Use o SIGEM para
> julgar a Petrobras e o PW só para dimensionar a fila da CONSAG.

### 5.5 Fase 4 — Atendimento de markup pela OTZ

| Item | Valor |
|---|---|
| Campos | `Data de Recebimento` → `Data Última Emissão` |
| Base | 1.753 markups de documento (linhas de GRD removidas — §2.4) |
| SLA | **5 DU** (PROC-COORD §9.2) |
| Filtro | `real >= 0` (exclui documentos cuja última emissão é anterior ao markup) |

```python
doc['real'] = du(doc['rec'], doc['emi'])
atendidos = doc.loc[doc['real'] >= 0, 'real']    # n = 1.468
```

**Resultado:** n=1.468 · média **10,1** · mediana 2 · P90 33 · máx 129 · **69,7% ≤5 DU**.

> ⚠️ **Proxy declarado.** Não existe campo "data de atendimento do markup" em nenhuma das fontes.
> `Data Última Emissão` é a emissão **mais recente** do documento, que pode ser posterior à revisão
> que respondeu ao markup. **O número tende a superestimar** o tempo real de atendimento. É a maior
> fragilidade metodológica desta análise.

**Validação empírica do SLA de 5 DU** (`Data de Recebimento` → `Data Planejada`):

| DU | −18 | −11 | −8 | −3 | 0 | 2 | 3 | 4 | **5** | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| markups | 3 | 1 | 1 | 1 | 1 | 2 | 2 | 87 | **1.334** | 286 | 20 | 7 |

Moda = 5, mediana = 5, **76,3% exatamente 5 DU**. O próprio sistema grava o SLA contratual.

### 5.6 Fluxo interno E-CLIC (contexto, não é fase do SLA)

Campos `Data Início Fluxo` → `Data Fim Fluxo`; classe por `fornecedor` preenchido.

| Classe | n | Média | Mediana | P90 | Máx | % ≤10 DU |
|---|---|---|---|---|---|---|
| A — OTZ próprio | 1.374 | 1,0 | 0 | 2 | 95 | 98,8% |
| B — doc. de fornecedor | 175 | 7,1 | 1 | 23 | 43 | 72,0% |

---

## 6. Aging das pendências

Regra geral: para cada etapa, os registros com data de início preenchida e data de fim **vazia** são
medidos contra a data-base 18/08/2026.

```python
pend = pw[pw['env'].notna() & pw['ret'].isna()]
pend['aging'] = np.busday_count(
    pend['env'].values.astype('datetime64[D]'), np.datetime64('2026-08-18'), holidays=FER)
```

| Fila | n | Aging médio | Mediana | Máx |
|---|---|---|---|---|
| Aguardando parecer CONSAG — OTZ | 103 | 17,9 | 7 | 55 |
| Aguardando parecer CONSAG — fornecedor | 39 | 18,6 | 18 | 102 |
| **Subtotal escopo OTZ+forn.** | **142** | **18,1** | **12,5** | **102** |
| Aguardando retorno do cliente — OTZ | 818 | 46,7 | 38 | 115 |
| Aguardando retorno do cliente — fornecedor | 6 | 43,5 | 52,5 | 84 |
| Workflow SIGEM aberto | 418 | 21,0 | 16 | 140 |
| Markup sem emissão de resposta | 293 | 33,2 | 24 | 130 |

Dos 142 na fila da CONSAG, **73 (51,4%) já passaram dos 10 DU**.
Dos 293 markups pendentes, **202 (68,9%) já passaram da data planejada**.

### 6.1 Validação cruzada da fila da CONSAG

O GLOSSÁRIO §13.1 dá a regra oficial de "de quem é a bola", que o PW já entrega pronta:

```python
TERMINAIS = {'Superado','Cancelado','Liberado para Construcao','Liberado para Compra',
             'Aprovado','Certificado','Para Informação'}
fila = pw[(pw['Responsável para Próxima Ação'] == 'AG') &
          (pw['Próxima Ação Esperada'] == 'Analisar Documento') &
          (~pw['o_statename'].isin(TERMINAIS)) &
          (pw['resp'].isna()) & (pw['aceite'].notna())]
fila_escopo = fila[fila['cls'] != 'CONSAG']    # -> 142
```

**Resultado: exatamente os mesmos 142 documentos** (103 OTZ + 39 fornecedor) obtidos pelo critério
simples "aceite sem resposta". Duas regras independentes, mesmo conjunto. `AG` = Alexandre Germano
(XLSM-CONSAG, aba `Doc_Setor Emissor_Verif_Aprov`, linha 59) — mas a identidade da pessoa não afeta
nenhum número, o campo é usado só como flag de roteamento.

### 6.2 Correção da fila do cliente — 178 registros suspeitos

```python
pend['RespostaCliente'].notna().sum()    # -> 178
```

**178 dos 824 documentos "pendentes" já têm `RespostaCliente` preenchida sem data de retorno.** Isso
é falha de cadastro, não atraso da Petrobras.

| Cenário | n na fila | Aging médio |
|---|---|---|
| Fila bruta | 824 | 46,6 |
| **Fila efetiva** (exclui os 178) | **646** (641 OTZ) | **32,4** |

---

## 7. E2E e o "piso com pendentes"

**Problema:** toda média de etapa concluída sofre viés de sobrevivência — documentos que voltam
rápido entram na conta, os travados há 100 dias não.

**Correção adotada:** média ponderada entre os concluídos e a idade atual da fila.

```python
piso = (n_concluidos * media_concluidos + n_pendentes * aging_medio) / (n_concluidos + n_pendentes)
```

| Etapa | Concluídos | Pendentes | Piso |
|---|---|---|---|
| Fase 2 CONSAG | 2.943 × 2,4 | 103 × 17,9 | **2,9 DU** |
| SIGEM | 11.390 × 4,8 | 418 × 21,0 | **5,4 DU** |
| Markup OTZ | 1.468 × 10,1 | 293 × 33,2 | **13,9 DU** |
| **Ciclo GRD cliente** | 254 × 9,5 | 824 × 46,6 | **37,9 DU** |
| ↳ mesma conta com a fila efetiva | 254 × 9,5 | 646 × 32,4 | **26,0 DU** |

**Nota de honestidade:** o piso não é uma estimativa do tempo final desses documentos — é um
**limite inferior**. Os pendentes ainda vão acumular mais dias. O número real será pior.

---

## 8. As duas leituras do SLA de 10 DU

**Texto contratual (PROC-COORD §9.2, literal):**

> *"Após a emissão do Projeto no GED SIGEM e no GED PW, a CONSAG e a PETROBRAS terão **10 (dez) dias
> úteis** para comentá-lo ou aprová-lo. A OTZ terá o prazo de **5 (cinco) dias úteis** contados da data
> do recebimento dos comentários para analisá-los e emitir os documentos revisados."*

A frase atribui os 10 DU a dois agentes de uma vez. Duas leituras são gramaticalmente possíveis:

| Leitura | O que se mede | n | Média | % ≤10 DU | Veredito |
|---|---|---|---|---|---|
| **A — 10 DU por elo** | CONSAG: aceite → resposta | 2.943 | 2,4 | 94,3% | CONSAG cumpre |
| | Petrobras: workflow SIGEM | 11.390 | 4,8 | 90,7% | Petrobras cumpre |
| | Ciclo GRD: envio → retorno | 254 | 9,5 | 72,0% | no limite |
| **B — 10 DU compartilhados** | Cadeia: `DataAceiteGRD` → `DataRetornoGRDCliente` | 288 | **17,4** | **42,7%** | **a cadeia estoura** |

```python
pw['cadeia'] = du(pw['aceite'], pw['ret'])
pw.dropna(subset=['cadeia']).groupby('cls')['cadeia'].agg(['count','mean','median'])
# A_OTZ : n=260  media=17,3  mediana=11  -> 42,3% <= 10 DU
# B_FORN: n= 28  media=18,4  mediana=12  -> 46,4% <= 10 DU
```

**Esta é a maior fonte de risco interpretativo do relatório.** Sob a Leitura A todos cumprem o
contrato; sob a Leitura B, 57,3% dos documentos estouram. O dado é o mesmo. **Recomendação: pedir
esclarecimento formal do §9.2 antes que o número apareça numa medição.**

---

## 9. Tabela de correspondência — número publicado → origem

| # | Número publicado | Fonte | Campos | Filtro | Reprodutível |
|---|---|---|---|---|---|
| 1 | CONSAG análise A: 2,4 / med 1 / 94,3% / n=2.943 | PW | `DataAceiteGRD`→`DataResposta` | `cls=A_OTZ` | ✅ §5.2 |
| 2 | CONSAG análise B: 12,9 / med 10 / 62,8% / n=113 | PW | idem | `cls=B_FORN` | ✅ §5.2 |
| 3 | Repasse: 4,5 / med 1 / 81,5% / n=1.077 | PW | `DataResposta`→`DataEnvioGRDCliente` | todos | ✅ §5.3 |
| 4 | SIGEM engenharia: 8,7 / med 6 / 79,1% / n=1.116 | SIGEM | `Dias úteis em workflow` | TERMINADO, exclui RIR e MOB | ✅ §5.4 |
| 5 | Markup OTZ: 10,1 / med 2 / 69,7% / n=1.468 | Markup | `Data de Recebimento`→`Data Última Emissão` | disciplina ≠ NÃO SE APLICA, real≥0 | ✅ §5.5 |
| 6 | E2E c/ fila: 37,9 DU | PW | ponderação | 254 concluídos + 824 pendentes | ✅ §7 |
| 7 | 818 GRDs / 46,7 DU / 178 suspeitos | PW | `DataEnvioGRDCliente` sem retorno | `cls=A_OTZ` | ✅ §6 |
| 8 | 293 markups pendentes / 33,2 DU / 68,9% vencidos | Markup | sem emissão posterior | base de 1.753 | ✅ §6 |
| 9 | Reprovação 17,7% vs 0,2% | PW | `Resposta` | com parecer | ✅ §5.2 |
| 10 | Fase 1 C1U +68,4 vs CHZ/JEI −11,8/−40,0 | PW | `DataPrevista1Emissao`→`DataAceiteGRD` | `cls=A_OTZ`, por `emissor` | ✅ §5.1 |
| 11 | Fila CONSAG: 142 docs, 73 estourados | PW | aceite sem resposta | `cls≠CONSAG` | ✅ §6.1 |
| 12 | Cadeia sob Leitura B: 17,4 DU / 42,7% | PW | `DataAceiteGRD`→`DataRetornoGRDCliente` | todos | ✅ §8 |

---

## 10. O que NÃO foi possível calcular

| # | O que | Por quê |
|---|---|---|
| 1 | Tempo entre protocolo da GRD e aceite | `DataGRDEntrada` **100% vazia** (0 de 18.198) |
| 2 | Data real de atendimento do markup | Campo não existe em nenhuma fonte; usado proxy `Data Última Emissão` (§5.5) |
| 3 | Prazo contratual do fornecedor | Não há data de entrega do fornecedor à OTZ. `Data Início Fluxo` do E-CLIC mede o ciclo de análise da OTZ, não o cumprimento do fornecedor |
| 4 | Separação A×B robusta no SIGEM | `Nome da contratada` **100% vazia** nas 13.463 linhas. A separação usou Nível 2 = "17.DOCUMENTOS FORNECEDOR" → só 95 documentos terminados, amostra insuficiente |
| 5 | Aderência a cronograma via E-CLIC | `Data Planejada` é derivada (emissão − 5 DU em 99,6% dos casos), não é marco de cronograma. Qualquer "% no prazo" sobre ela daria ~100% e seria falso |
| 6 | Fase 1 do acervo herdado antes de mar/2026 | CHZ/JEI não têm registros de aceite antes de 2026-03 — o acervo não estava no PW |
| 7 | Verificação direta da norma N-1710 | PDF com fontes subconjunto; bibliotecas de PDF quebradas no ambiente. Estrutura citada de segunda mão (§2.2) |
| 8 | Feriados estaduais/municipais de PE | Não incorporados. Efeito estimado: desloca médias em menos de 0,5 DU (extrapolando o teste do §3.1) |
| 9 | Fases separadas dentro do SIGEM | O relatório dá só o total de dias em workflow, não o tempo por etapa interna da Petrobras |

---

## 11. Divergências encontradas no double-check e como foram resolvidas

O relatório passou por três passes de conferência. Registro do que foi encontrado:

| # | Divergência | Diagnóstico | Resolução |
|---|---|---|---|
| D1 | "2.057 markups pendentes / 52,1 DU / 90% vencidos" circulava em nota intermediária | Número calculado sobre a base bruta de 3.517 linhas, que inclui 1.764 linhas de GRD | Publicado **293 / 33,2 DU / 68,9%**, sobre a base correta de 1.753 |
| D2 | Fase 3 média 9,5 DU | 2 registros com data de retorno anterior à de envio, um deles −251 DU | Mantido 9,5 no corpo, **declarado 10,5 DU (n=252)** como valor limpo e recomendado para uso contratual |
| D3 | "Fila efetiva ~640 documentos" | Aproximação | Corrigido para **646 (641 OTZ)**, com aging de 32,4 DU |
| D4 | "% no prazo" do Tipo B (62,8%) | Sensível à definição de dia útil: varia 51,3%–62,8% | Declarado no relatório; recomendado citar a **média de 12,9 DU** |
| D5 | SLA de 10 DU tratado como premissa não verificada | Localizado no PROC-COORD §9.2 em 19/08/2026 | Promovido a fato contratual; abriu a questão das duas leituras (§8) |
| D6 | "A OTZ emite 17 a 20 DU antes do prazo" | Efeito de mistura: o adiantamento vem do acervo CHEINTEC/Jaguará, não da produção própria | Corrigido para **"a OTZ chegou ao prazo"** (C1U: −0,2 DU em ago/26) |

**Números que passaram sem divergência nos dois primeiros passes:** 1, 2, 3, 4, 5, 7, 9 da tabela
§9 — reproduzidos dígito a dígito por código independente.

---

## 12. Como reproduzir

```python
import pandas as pd, numpy as np
U = '<caminho dos uploads>/'

# feriados e função de dias úteis: ver §3
# 1. carregar
pw = pd.read_csv(U+'79f2bdab-Z546__RELAT_RIO_PW_18_08_26_8h.csv',
                 sep=';', encoding='utf-8-sig', dtype=str)
sg = pd.read_excel(U+'fe804493-Z546__RELAT_RIO_SIGEM.xlsx', header=4)
mk = pd.read_excel(U+'c33af65d-Z546__RELAT_RIO_MARKUP.xlsx', header=1)
sg.columns = [str(c).strip() for c in sg.columns]
mk.columns = [str(c).strip() for c in mk.columns]

# 2. datas do PW (formato DD/MM/AAAA)
for col, nome in [('DataAceiteGRD','aceite'), ('DataResposta','resp'),
                  ('DataEnvioGRDCliente','env'), ('DataRetornoGRDCliente','ret'),
                  ('DataPrevista1Emissao','prev')]:
    pw[nome] = pd.to_datetime(pw[col], format='%d/%m/%Y', errors='coerce')
    pw.loc[(pw[nome] < '2024-01-01') | (pw[nome] > '2029-12-31'), nome] = pd.NaT

# 3. classes e fases: ver §2.1 e §5
# 4. markup: header=1, remover Disciplina == 'NÃO SE APLICA', datas com dayfirst=True
```

**Ambiente:** Python 3.11, pandas 3.0.5, numpy, openpyxl 3.1.5. Data-base fixa: `2026-08-18`.

---

## 13. Julgamentos metodológicos — lista para o auditor contestar

Pontos onde outra pessoa razoável poderia ter decidido diferente:

1. **Manter os negativos** na média publicada da Fase 3 (§4.2). Alternativa defensável: removê-los e
   publicar 10,5 DU direto.
2. **Não recalcular o SIGEM** a partir de `Inicio do workflow` (§3.2). Alternativa: recalcular para
   ter o mesmo calendário do PW, ao custo de divergir do número que a Petrobras reconhece.
3. **Usar `Data Última Emissão` como proxy de atendimento de markup** (§5.5). É a decisão mais frágil
   de todas. Sem ela, a Fase 4 simplesmente não existiria.
4. **Contar cada revisão como uma observação** em vez de agrupar por documento. Um documento com 5
   revisões pesa 5× na média. Alternativa: `Última emissão == 'Sim'` para pegar só a revisão corrente.
5. **Excluir feriados nacionais mas não estaduais** (§3). Recife tem feriados próprios relevantes.
6. **Adotar a Leitura A do §9.2 no corpo do relatório**, com a Leitura B em seção destacada (§8).
   Alternativa: inverter a ênfase.
7. **Ponderar o piso pela idade atual da fila** (§7). É conservador — subestima o resultado final.

---

*Documento gerado em 19/08/2026. Data-base dos dados: 18/08/2026.
Relatório associado: `velocidade-fluxo-z546.html`.*
