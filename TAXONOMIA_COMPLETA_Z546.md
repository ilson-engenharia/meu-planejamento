---
tipo: especificacao_tecnica
titulo: Taxonomia Completa e Mapa de Dados — RNEST Z-546 / UGH U-36
projeto: RNEST UGH U-36 — Z-546 / Lote D — contrato 00025129
arquivo_base: LD-5290.00-22311-911-C1U-001 rev. F_0 (260819)
data_base_dados: 2026-08-18
gerado_em: 2026-08-21
autor: Claude Opus — para Eng. Ilson dos Santos Azevedo, Planejamento OTZ
finalidade: base de engenharia para substituir o pipeline Power Query por um sistema autônomo
complementa: METODOLOGIA_VELOCIDADE_Z546.md · GLOSSARIO_NOMENCLATURA_PW_RNEST.md
cobertura: taxonomia · pipeline · cross-reference PW↔LD · financeiro PPU · riscos · histórico do projeto · arquitetura-alvo
---

# Taxonomia Completa e Mapa de Dados — Z-546

Este documento é a **planta baixa do dado** do projeto Z-546. Ele existe para que um sistema
automatizado possa reconstruir, sem intervenção humana, tudo o que hoje a LD faz com Power Query,
fórmulas e tabelas dinâmicas.

Tudo aqui foi extraído dos arquivos reais — inclusive o **código-fonte M do Power Query**, que foi
recuperado de dentro do `.xlsx` (`customXml/item1.xml` → `DataMashup` → `Formulas/Section1.m`).
Nada é suposição: onde houve inferência, está marcado.

> **Como ler:** ✅ = verificado contra os dados · ⚠️ = risco/erro encontrado · ❓ = precisa decisão do Ilson.

---

## 1. Sumário executivo — o que a análise revelou

| # | Achado | Impacto |
|---|---|---|
| 1 | **As colunas "PW" da LD não vêm do ProjectWise.** Vêm do E-CLIC (`RL_DOCS` + `RL_EMISSAO`). A aba `RL_PW` **não é referenciada por nenhuma fórmula nem por nenhuma tabela dinâmica** | 🔴 Conceitual. "Emitido no PW" na LD significa *"GRD saiu do E-CLIC"*, não *"consta no ProjectWise"* |
| 2 | **6 das 8 tabelas dinâmicas usam intervalos fixos truncados.** A `Docs p_semana` enxerga só até a linha 3264 — **131 documentos ficam fora**; a `Memoria Calculo BM09` até 3320 — **75 fora** | 🔴 Números publicados estão errados por omissão |
| 3 | `Csv.Document(..., Columns=69)` no `RL_PW`, mas **o CSV do PW tem 70 colunas** | 🟠 Coluna 70 (`DataAlteracaoState`) é descartada silenciosamente |
| 4 | O marcador `EXCLUIR` precisa ser digitado em **duas colunas** (J *ESCOPO* e K *ATIVIDADE*). Metade das fórmulas testa J, a outra metade testa K | 🔴 Preencher só uma delas produz LD meio-excluída, sem erro visível |
| 5 | O filtro real do `RL_PW` é `nomeEmpresa ∉ {CONSAG, CONSAG QUALIDADE}` — **mantém os fornecedores**, não é `∈ {ENG OBRA, OTZ PROJETISTA}` | 🟠 Divergência entre a regra documentada e a implementada |
| 6 | `LD UGH Trem 2` = **OTZ PROJETISTA** e `LD Trem 2 -ICs` = **ENG OBRA**: 2.705/2.705 e 1.585/1.585, **zero cruzamento** | ✅ Regra do Ilson confirmada com 100% de precisão |
| 7 | Existe uma chave canônica de disciplina melhor que todas as usadas hoje: o **6º campo do `CÓDIGO CONSAG`** (`TUB`, `INS`, `MEC`…) | ✅ Resolve a Torre de Babel das 5 taxonomias |
| 8 | `Última emissão = "Previsto"` isola exatamente os 3.226 documentos nunca emitidos — mais simples e mais seguro que a regra de dois campos | ✅ Refinamento do conceito "Documento Emitido" |
| 9 | 6 colunas de `Previsto/Excluído`, `Status` e datas ficam em **posições diferentes** nas duas abas LD (`DL` vs `CG`) | 🟠 Todo script que usar letra de coluna quebra |
| 10 | **O histórico do projeto é integralmente reconstruível** desde 24/11/2025. O custo caiu de 68,7 para 18,6 HH/documento entre jan e jul | ✅ Não há lacuna anterior à chegada do Ilson (§11) |
| 11 | **Saldo de PPU está em −446 documentos** (−853 só em isométricos): a LD já prevê mais do que o contrato paga | 🔴 Exposição contratual, decisão de gerência |
| 12 | Lançamento de HH de agosto está ~45% incompleto e 1.168 lançamentos seguem sem aprovação | 🟠 Alvo imediato de cobrança automatizada |

---

## 2. Inventário do arquivo LD

`LD-5290.00-22311-911-C1U-001` rev. F_0 — 18 abas, 18,7 MB, 6,8 MB só de `calcChain.xml`.

| Aba | Visível | Linhas × Col | Cab. | Papel |
|---|---|---|---|---|
| `CAPA` | ✅ | 451 × 12 | — | Folha de rosto N-1710 |
| `Memoria Calculo BM09` | 🚫 oculta | 66 × 10 | 2 | Fechamento financeiro do BM 09 (pivot) |
| **`LD UGH Trem 2`** | ✅ | **3.396 × 118** | **8** | **Master OTZ PROJETISTA — 3.387 docs** |
| **`LD Trem 2 -ICs`** | ✅ | **2.472 × 88** | **8** | **Master ENG OBRA (isométricos) — 2.464 docs** |
| `Prev (tipo) x Mês` | ✅ | 139 × 13 | 3 | 4 pivots: previsão por tipo × mês |
| `Docs p_semana` | 🚫 oculta | 138 × 74 | 4 | Pivot disciplina × semana (S017…S083) |
| `RL DOCS` | ✅ | 4.914 × 29 | 1 | **Bruto E-CLIC** — relatório de documentos |
| `RL_MARKUP` | ✅ | 1.769 × 12 | 1 | **Bruto E-CLIC** — markups recebidos |
| `RL_EMISSAO` | 🚫 oculta | 5.833 × 12 | 1 | **Bruto E-CLIC** — emissões/GRD |
| `RL_PW` | ✅ | 6.688 × 49 | 1 | **Bruto ProjectWise — ÓRFÃO (⚠️ item 1)** |
| `RL_Sigem` | ✅ | 1.186 × 21 | 1 | **Bruto SIGEM** — documentos cadastrados |
| `RL_Emissão_SIT` | 🚫 oculta | 2 × 9 | 1 | Respostas de SIT da Petrobras (1 registro) |
| `RL_Previsto_Sigem` | ✅ | 5.746 × 19 | 1 | **Bruto SIGEM** — previstos (tabela `RL_Sigem_PREV`) |
| `CONSUMO PPU` | ✅ | 28 × 15 | 5 | Saldo contratual por item de PPU |
| `Rundown SGM` | ✅ | 724 × 81 | 9 | Curva S de emissão no SIGEM (7 pivots) |
| `Prev_Fat` | 🚫 oculta | 65 × 50 | 4 | Previsão de faturamento R$ × mês |
| `PADRÃO` | 🚫 oculta | 697 × 39 | 2 | **Tabelas mestre v1** — feriados, calendário, de-para |
| `PADRÃO (2)` | ✅ | 793 × 16 | 2 | **Tabelas mestre v2** — calendário de medição |

---

## 3. As sete fontes de dados e como entram

### 3.1 Consultas Power Query (código M recuperado)

Todas apontam para o **mesmo diretório de rede**:

```
K:\DDE\05-Projetos\Projeto Z-546 - RNEST - UGH\01- Planejamento\011_Relatório Query\
```

| Query | Arquivo fonte | Sistema | Filtro principal implementado | → Aba |
|---|---|---|---|---|
| `RL_DOCS` | `Z-546 - RELATÓRIO DOCUMENTO.xlsx` | E-CLIC | `Diretório` começa com `03.04`/`03.05`/`04. DO`/`05. SU` | `RL DOCS` |
| `RL_EMISSAO` | `Z-546 - RELATÓRIO EMISSÃO.xlsx` | E-CLIC | exclui **38 diretórios** de ATAS/contrato/referência, um a um, por igualdade literal | `RL_EMISSAO` |
| `RL_MARKUP` | `Z-546 - RELATÓRIO MARKUP.xlsx` | E-CLIC | `Diretório_1 ≠ "10. GRD"`; monta chave `Código+"="+Revisão` | `RL_MARKUP` |
| `RL_Sigem` | `Z-546 - RELATÓRIO SIGEM.xlsx` | SIGEM | pula 4 linhas; `Nível 2 = "04.ENGENHARIA"`; disciplina = `Nível 3` a partir do 6º caractere | `RL_Sigem` |
| `RL_Sigem (2)` | `...SIGEM DOCUMENTOS PREVISTOS.xlsx` | SIGEM | `CAMINHO` contém `\|IMPLANTAÇÃO DO PROJETO RNEST - TREM 2\|UGH U-36\|04.ENGENHARIA\|` | `RL_Previsto_Sigem` |
| `RL_Emissão_SIT` | `Z-546 - RELATÓRIO EMISSÃO.xlsx` | E-CLIC | `Diretório = "03. PLANEJAMENTO / 03.08. ... SIT / RESPOSTAS CLIENTE"` | `RL_Emissão_SIT` |
| `RL_PW` | `Z-546 - RELATÓRIO PW.csv` | ProjectWise | **`nomeEmpresa ∉ {CONSAG, CONSAG QUALIDADE}`** | `RL_PW` |

### 3.2 ⚠️ O filtro do PW implementado ≠ o filtro documentado

O M code faz **exclusão da CONSAG**, não inclusão da OTZ. Diferença medida:

| Regra | Linhas mantidas |
|---|---|
| `nomeEmpresa ∉ {CONSAG, CONSAG QUALIDADE}` (implementada) | 6.490 |
| `nomeEmpresa ∈ {ENG OBRA, OTZ PROJETISTA}` (documentada) | 6.281 |
| **Diferença** | **209 documentos de fornecedor** (ENGEMASA 116, ASVOTEC 83, WEG 6, INCASE 2, VIBROPAC 2) |

E **nenhum** dos dois outros filtros obrigatórios (`DisciplinaDesc ∉ {GESTÃO, PLANEJAMENTO, PROJETOS}`
e `TipoDocumento ≠ ATA`) existe no Power Query — eles são aplicados manualmente depois, fora do
arquivo. Custo de os esquecer: **683 + 68 = 751 linhas** a mais na contagem.

### 3.3 ⚠️ `Columns=69` contra um CSV de 70 colunas

```m
Fonte = Csv.Document(File.Contents("...Z-546 - RELATÓRIO PW.csv"),
        [Delimiter=";", Columns=69, Encoding=65001, QuoteStyle=QuoteStyle.Csv])
```

O CSV `Z546__RELAT_RIO_PW_18_08_26_8h.csv` tem **70 colunas**. A coluna 70,
`DataAlteracaoState`, é descartada sem aviso. Se o PW acrescentar mais uma coluna no meio do
export, o parse desalinha inteiro e **as datas passam a ser lidas na coluna errada** — sem erro.

---

## 4. Taxonomia definitiva de disciplinas

### 4.1 O problema: cinco vocabulários simultâneos

| Fonte | Campo | Valores distintos | Exemplo |
|---|---|---|---|
| LD (Petrobras) | col. H `DISCIPLINA PETROBRAS` | **21** | `Instr&Aut`, `Processo On Site`, `Fornos` |
| LD (OTZ) | col. BO `DISCIPLINA OTZ` | **22** | mistura maiúsc./minúsc.: `PROCESSO` (51) e `Processo` (49) |
| PW | col. O `DisciplinaDesc` | **16** | `SAFETY`, `SISTEMA DE MODELO 3D`, `TELECOMUNICAÇÕES` |
| PW | col. BB `DisciplinaResposta` | 11 siglas | `TUB`, `MET`, `SAF`, `M3D` |
| E-CLIC | `Disciplina` (RL_DOCS/MARKUP/EMISSAO) | 13–15 | `CAE - CAD`, `ESTRUTURA METÁLICA` |
| SIGEM | `RL_Sigem.Disciplina` | **18** | `MÁQUINAS`, `TRANSFERÊNCIA DE CALOR`, `SIT-CT` |
| Cadastro HH | col. B `DISCIPLINA` | **13** | `CDA`, `CAE - CAD`, `MECÂNICA` |

### 4.2 ✅ A chave canônica: 6º campo do `CÓDIGO CONSAG`

O `CÓDIGO CONSAG` (LD col. D) tem a forma:

```
RUGH - ICF - ENG - EX - U036 - TUB - PT - 0001
  1     2     3    4     5     [6]    7     8
                                └── disciplina, 3 letras
```

Esse campo tem **14 valores**, é preenchido em 100% das linhas da LD e coincide com a
`DisciplinaResposta` do PW. **É o identificador canônico recomendado.**

### 4.3 Tabela de-para DEFINITIVA

Construída por *join real* documento-a-documento (LD `Nº N-1710` ↔ PW `NumeroDocumentoCliente`),
não por semelhança de nome. A coluna "conf." é a taxa de concordância medida.

| # | **NOME DEFINITIVO** | **Sigla** | LD col. H (Petrobras) | PW `DisciplinaDesc` | conf. | Cadastro HH | SIGEM | N-1710 (grupo 4) |
|---|---|---|---|---|---|---|---|---|
| 01 | **Tubulação** | `TUB` | `Tubulação` (2.171) | `TUBULAÇÃO` | 100% | `TUBULAÇÃO` | `TUBULAÇÃO` | `200`, `955` |
| 02 | **Mecânica — Estáticos/Caldeiraria** | `MEC` | `Caldeiraria` (93) | `MECÂNICA` | 100% | `MECÂNICA` ⚠️ | `CALDEIRARIA` | `7xx`, `8xx` |
| 02 | **Mecânica — Dinâmicos** | `MEC` | `Dinâmicos` (56) | `MECÂNICA` | 100% | `MECÂNICA` ⚠️ | `MÁQUINAS` | `24x`, `25x` |
| 02 | **Mecânica — Fornos** | `MEC` | `Fornos` (90) | `MECÂNICA` | 100% | `MECÂNICA` ⚠️ | `TRANSF. DE CALOR` | `72x`, `73x` |
| 03 | **Instrumentação e Automação** | `INS` | `Instr&Aut` (305) | `INSTRUMENTAÇÃO` | 100% | `INSTRUMENTAÇÃO` | `INSTRUMENTAÇÃO` | `8xx` |
| 04 | **Elétrica** | `ELE` | `Elétrica` (198) | `ELÉTRICA` | 100% | `ELÉTRICA` | `ELÉTRICA` | `5xx`, `6xx` |
| 05 | **Processo — On Site** | `PRO` | `Processo On Site` (67) | `PROCESSO` | 93% | `PROCESSO` | `PROCESSO ON SITE` | `94x`, `98x` |
| 05 | **Processo — Off Site** | `PRO` | `Processo Off Site` (15) | `PROCESSO` | 100% | `PROCESSO` | `PROCESSO OFF SITE` | `94x` |
| 05 | **Processo (genérico)** ❓ | `PRO` | `Processo` (21) | *sem par no PW* | — | `PROCESSO` | — | `944` |
| 06 | **Civil** 🔵 | `CIV` | `Civil` (32) | `CIVIL` | 89% | *ausente* 🔵 | `CIVIL` | `12x` |
| 06 | **Drenagem** 🔵 | `CIV` | `Drenagem` (1) | `CIVIL` | 100% | *ausente* 🔵 | — | `131` |
| 06 | **Arruamento e Pavimentação** 🔵 | `CIV` | `Arruamento e Pav.` (1) | `CIVIL` | 100% | *ausente* 🔵 | — | `121` |
| 06 | **Arquitetura** 🔵 | `ARQ` | `Arquitetura` (1) | `ARQUITETURA` | 100% | *ausente* 🔵 | `ARQUIT. E URBANISMO` | `140` |
| 07 | **Estrutura Metálica** | `MET` | `Estrutura Metálica` (185) | `ESTRUTURA METÁLICA` | 100% | *via* `MECÂNICA` | `ESTRUTURA METÁLICA` | `183` |
| 08 | **Segurança** | `SAF` | `Segurança` (57) | **`SAFETY`** | 100% | `SEGURANÇA` | `SEGURANÇA` | `94x`, `947` |
| 09 | **Telecomunicações** | `TEL` | `Telecom` (34) | **`TELECOMUNICAÇÕES`** | 100% | `TELECOM` | `TELECOM` | `39x` |
| 10 | **Automação de Projetos** | `AUT` | *(1 doc em Instr&Aut)* | `AUTOMAÇÃO` | — | `CAE - CAD` | — | — |
| 11 | **Qualidade** | `QUA` | *não existe na LD* | `QUALIDADE` | — | `QUALIDADE` | — | — |
| 12 | **Modelo 3D / Eng. Digital** ⛔ | `M3D` | `Eng. Digital (E3D)` (25)<br>`Eng. Digital (COMOS)` (25) | `SISTEMA DE MODELO 3D` | 100% | `CDA` + `CAE - CAD` | `ENGENHARIA DIGITAL` | `98V`, `98X` |
| 13 | **Riscos** ❓ | `RIS` | `Riscos` (5) | *sem par no PW* | — | — | — | `98V`,`98X`,`983` |
| — | **Coordenação** ⛔ | `PLA` | `Coordenação` (4) | `PLANEJAMENTO` | 100% | `GESTÃO` | `PLANEJAMENTO` | `940`,`942` |
| — | **Planejamento** ⛔ | `PLA` | — | `PLANEJAMENTO` | — | `PLANEJAMENTO` | `PLANEJAMENTO` | `911` |
| — | **Gestão / Projetos** ⛔ | — | — | `GESTÃO`, `PROJETOS` | — | `GESTÃO`, `GERAL` | `GERAL` | — |

**Legenda:** 🔵 vem da 2ª planilha de HH (gerência DPC) · ⛔ excluída da contagem de escopo
· ⚠️ agregação muitos-para-um · ❓ ver §9.

### 4.4 Regras de normalização obrigatórias

```python
# 1) Sempre normalizar caixa e acentos antes de comparar
#    (DISCIPLINA OTZ tem "PROCESSO"(51) e "Processo"(49); "SEGURANÇA"(49) e "Segurança"(13))
# 2) A sigla canônica vem do código, não do rótulo:
SIGLA = CODIGO_CONSAG.split('-')[5]      # 100% preenchido, 14 valores
# 3) Colapsos muitos-para-um confirmados:
MEC = {'Caldeiraria', 'Dinâmicos', 'Fornos', 'Mecânica'}
PRO = {'Processo', 'Processo On Site', 'Processo Off Site'}
CIV = {'Civil', 'Drenagem', 'Arruamento e Pavimentação'}   # + Arquitetura -> ARQ
M3D = {'Engenharia Digital (E3D)', 'Engenharia Digital (COMOS)'}
# 4) Fora do escopo OTZ:
FORA = {'Coordenação', 'Engenharia Digital (E3D)', 'Engenharia Digital (COMOS)'}   # LD col. H
FORA_PW = {'GESTÃO', 'PLANEJAMENTO', 'PROJETOS'}                                    # PW col. O
```

### 4.5 ⚠️ O valor `CONSAG` na coluna `DISCIPLINA OTZ`

5 linhas trazem `CONSAG` como disciplina. A tabela mestre `PADRÃO!W:X` mapeia `CONSAG → CONSAG`
(uma "diretoria"), então a fórmula da coluna BW não erra — mas **para efeito de KPI por
disciplina esses 5 documentos ficam num balde que não existe em nenhuma outra fonte.**

### 4.6 Disciplina → Diretoria (`PADRÃO!W3:X34`, usada pela coluna BW)

| Diretoria | Disciplinas |
|---|---|
| **DDE** | Caldeiraria, Dinâmicos, Elétrica, Fornos, Instr&Aut, Segurança, Telecom, Tubulação, Coordenação, HVAC, Processo (On/Off Site), Transferência de Calor, Mecânica, Eng. Digital (E3D/COMOS), Riscos, Máquinas, Equipamento Térmico |
| **DPC** 🔵 | Civil, Arquitetura, Drenagem, Infraestrutura, **Estrutura Metálica**, Instalações Prediais, Geotecnia, Arruamento e Pavimentação, Pavimentação |
| **CONSAG** | CONSAG |

> ⚠️ **Estrutura Metálica está em DPC**, não em DDE. Se a 2ª planilha de HH é "tudo que é DPC",
> ela deve trazer também os 185 documentos de Estrutura Metálica — não só Civil.

### 4.7 Cadastro de HH — 7.764 lançamentos, 40.268 h

| Disciplina HH | Lançamentos | Horas | Mapeia para |
|---|---|---|---|
| `TUBULAÇÃO` | 1.203 | 7.250,5 | `TUB` |
| `ELÉTRICA` | 664 | 5.065,0 | `ELE` |
| `PROCESSO` | 686 | 4.636,1 | `PRO` |
| `INSTRUMENTAÇÃO` | 637 | 4.584,0 | `INS` |
| `PLANEJAMENTO` | 730 | 3.970,0 | ⛔ overhead |
| `CDA` | 682 | 3.464,4 | `M3D` (Centro de Dados/Modelagem) |
| `CAE - CAD` | 468 | 3.225,0 | `M3D` / `AUT` |
| `GESTÃO` | 633 | 3.011,5 | ⛔ overhead |
| `MECÂNICA` | 1.722 | 2.940,2 | `MEC` — **agrega Caldeiraria + Dinâmicos + Fornos + Est. Metálica** |
| `QUALIDADE` | 179 | 1.258,6 | `QUA` |
| `SEGURANÇA` | 128 | 751,0 | `SAF` |
| `GERAL` | 22 | 75,5 | ⛔ overhead |
| `TELECOM` | 9 | 36,0 | `TEL` |

✅ **`CIVIL` não aparece** — confirma que Civil vem de outra gerência (DPC), como o Ilson indicou.

**Estrutura do campo `ITEM`** (268 valores): três formatos convivem —
`TUB - TUBULAÇÃO` (sigla-prefixo), `01. PROJ. REMANESCENTE - TUB` (sigla-sufixo, ligado à EAP) e
`MC-5290.00-22311-700-C1U-101` (número de documento). Um parser de HH precisa tratar os três.

Campos de controle: `TIPO` ∈ {`Horas Previstas` (7.598), `Serviços Adicionais` (165)};
`APROVAÇÃO` ∈ {`Sim` (6.595), `Não` (1.168)}. **1.168 lançamentos ainda não aprovados** — é aqui
que a cobrança automática por e-mail tem o alvo mais óbvio.

---

## 5. Pipeline de dados — o caminho completo

### 5.1 Diagrama de fluxo real

```
E-CLIC (OTZ)                      SIGEM (Petrobras)              ProjectWise (CONSAG)
    │                                    │                              │
    ├─ RELATÓRIO DOCUMENTO.xlsx          ├─ RELATÓRIO SIGEM.xlsx        └─ RELATÓRIO PW.csv
    ├─ RELATÓRIO EMISSÃO.xlsx            └─ ...DOCS PREVISTOS.xlsx              │
    └─ RELATÓRIO MARKUP.xlsx                       │                            │
              │                                    │                            │
        [Power Query]                        [Power Query]                [Power Query]
              ↓                                    ↓                            ↓
   RL DOCS · RL_EMISSAO · RL_MARKUP     RL_Sigem · RL_Previsto_Sigem         RL_PW
              │                                    │                            │
              └──────── XLOOKUP por Nº N-1710 ─────┘                    ✗ ÓRFÃO ✗
                                │                                    (nenhuma fórmula,
                                ↓                                     nenhum pivot)
                    ┌───────────────────────┐
                    │   LD UGH Trem 2       │  ← 118 colunas, 57 com fórmula
                    │   (OTZ PROJETISTA)    │
                    └───────────┬───────────┘
                                │ XLOOKUP CH → C  (IS-955 ← IS-200)
                    ┌───────────┴───────────┐
                    │   LD Trem 2 -ICs      │  ← 88 colunas, 22 com fórmula
                    │   (ENG OBRA)          │
                    └───────────┬───────────┘
                                │
        ┌───────────┬───────────┼───────────┬─────────────┬──────────────┐
        ↓           ↓           ↓           ↓             ↓              ↓
  Prev(tipo)×Mês  Docs      CONSUMO      Rundown      Prev_Fat    Memoria Calc.
                 p_semana     PPU          SGM                       BM09
     cache 297    cache 303   cache 308   cache 334    cache 340    cache 344
     ⚠️ −4 docs   ⚠️ −131     col. até CK    ok           ok        ⚠️ −75 docs
```

**Tabelas mestre transversais** (`PADRÃO` e `PADRÃO (2)`) alimentam tudo por *defined names*:
`FERIADOS`, `FERIADO_2`, `CALENDÁRIO_2`, `SEMANA_2`, `Per_21_a_20`, `Per_MêsCheio`,
`Mês_medição`, `IS_medição`, `Tabela1`.

### 5.2 Rastreamento campo a campo (LD UGH Trem 2)

| Col | Campo na LD | Origem real | Transformação | Alimenta |
|---|---|---|---|---|
| `C` | **Nº N-1710** | digitado | chave primária de todos os XLOOKUP | tudo |
| `D` | CÓDIGO CONSAG | digitado | 6º campo = sigla de disciplina | taxonomia canônica |
| `H` | DISCIPLINA PETROBRAS | digitado | — | filtro de todos os pivots |
| `J` | ESCOPO (REVISÃO/NOVO) | digitado | `EXCLUIR` ⇒ dispara exclusão | `BT`, `DL`, `AH`, `AI`, `AM`, `BU`, `X`, `BB` |
| `K` | ATIVIDADE | digitado | `EXCLUIR` ⇒ dispara exclusão | `BV`, `BW`, `CM`, `CP`, `CW`, `CX`, `DA`, `DG` |
| `AB` | Data real 1ª Emissão PW | **`RL_DOCS[Data Primeira Emissão]`** (E-CLIC) | XLOOKUP; `0` → `""` | `CT`, `CU`, `CV`, `CW` |
| `AD` | Data Emissão Real PW | **`RL_EMISSAO[Data Emissão]`** (E-CLIC) | XLOOKUP | `AH`, `AI`, `BV` |
| `AE` | Rev. Atual - PW | `RL_EMISSAO[Revisão]` | XLOOKUP | `AH` (detecta `_` → CONSAG) |
| `AF` | Propósito Emissão - PW | `RL_EMISSAO[Finalidade]` | XLOOKUP | — |
| `AH` | ORIGEM DA REVISÃO | derivada | `FIND("_", AE)` ⇒ `CONSAG`, senão `PETROBRAS` | análise |
| `AI` | DATA PREVISTA MARKUP CONSAG | derivada | `WORKDAY(AD; 3; FERIADOS)` — **SLA 3 DU** | cobrança |
| `AM` | DATA PREV. ATENDIMENTO MARKUP | derivada | `WORKDAY(AJ; 2 ou 3; FERIADOS)` (2 se aprovado) | cobrança |
| `AT` | DATA REPROG 1ª EMISSÃO SIGEM | derivada | `WORKDAY(W; 2 se IS senão 7; FERIADO_2)` | `AU` |
| `AV`–`BA` | bloco SIGEM | **`RL_Sigem[…]`** | XLOOKUP por `Documento` | `BB`, `BG`, `BV` |
| `BB` | DATA PREVISTA RESPOSTA PB | derivada | `WORKDAY.INTL(AX; 10; 1; PADRÃO!A3:A109)` — **SLA 10 DU** | cobrança |
| `BG` | Data Prev. atendimento Markup PB | derivada | `WORKDAY.INTL(BD; 5; 1; PADRÃO!A3:A58)` — **SLA 5 DU** | cobrança |
| `BN` | Tipo do Doc | derivada de `C` | `LEFT(C;2)`, ou `MID(C;3;2)` se começa com `I-`, ou `SIT` | `BT`, `AT`, `DI` |
| `BS` | PRÉ CADASTRADO NO SIGEM? | `RL_Sigem` **com fallback** `RL_Sigem_PREV` | XLOOKUP aninhado, default `NÃO` | KPI cadastro |
| `BT` | **CONSUMO PPU** | derivada | `BN & " - " & J` → `"DE - NOVO"` | pivot `CONSUMO PPU` |
| `BU` | STATUS DOCUMENTO E-CLIC | `RL_DOCS[Status do Documento]` | XLOOKUP; erro → `VER CADASTRO NO E-CLIC` | auditoria |
| `BV` | **STATUS DO DOCUMENTO** | **derivada — o coração da LD** | máquina de estados de 9 valores (§5.3) | `CI`, pivots, dashboard |
| `BW` | EQ. INTERNA RESPONSÁVEL | `PADRÃO!W:X` via `BO` | XLOOKUP disciplina→diretoria | alocação |
| `BY`–`CF` | bloco financeiro | `BY` peso EAP; `CA` R$/doc | `CB=CA*BZ`; `CD=CC*CA`; `CE=CB+CD`; `CF=CA−CE` | `Memoria Calculo BM09` |
| `CI` | % AVANÇO FÍSICO (período) | **derivada de `BV`** | 1 / 0,7 / 0,5 / 0 conforme status, **menos `CH`** | curva física |
| `CM`–`DF` | calendarização | `CALENDÁRIO_2` + `SEMANA_2` + `Per_21_a_20` | XLOOKUP de data → semana/mês de medição | `Docs p_semana`, `Rundown SGM` |
| `CW`,`DG` | 1ª emissão no prazo? (PW/SIGEM) | derivada | compara real × programada usando **`TODAY()`** ⚠️ | KPI de aderência |
| `DH`,`DI` | data e mês de medição | derivada | `IS` usa `IS_medição` (corte dia 19); demais usam `Mês_medição` (corte dia 6) | `Prev_Fat` |
| `DL` | **Previsto / Excluído** | derivada | `IF(J="EXCLUIR"; "EXCLUÍDO"; "PREVISTO")` | filtro-mestre |

### 5.3 A máquina de estados — coluna `BV` `STATUS DO DOCUMENTO`

Este é o campo mais importante da LD: define o avanço físico, a cor do dashboard e quem deve ser
cobrado. Lógica exata (traduzida do Excel):

```python
def status_documento(row):
    if row.K == "EXCLUIR":                      return "EXCLUÍDO"
    if row.AD == "":                            return "EMITIR EMISSÃO INICIAL"   # nunca emitiu
    if is_number(row.AX) and row.AX >= row.AD:                    # já está no SIGEM
        if row.BA in {"Sem Comentários","Para Compra","Para Construção"}:
                                                return "DOC. FINALIZADO"
        if row.BA in {"COM COMENTÁRIOS","RECUSADO"}:
                                                return "ATENDER MARKUP PB"
        if row.BA == "CANCELADO":               return "DOCUMENTO CANCELADO"
        if row.BF == "N/A":                     return "N/A"
        return                                         "AGUARDANDO MARKUP PB"
    # emitiu para a CONSAG mas ainda não chegou ao SIGEM
    if row.AL == "APROVADO":                    return "EMITIR NO SIGEM"
    if row.AL in {"APROVADO COM COMENTÁRIOS","RECUSADO"}:
                                                return "ATENDER MARKUP CONSAG"
    if row.AL == "N/A":                         return "N/A"
    if row.AE != "":                            return "AGUARDANDO MARKUP CONSAG"
    return                                             "EMITIR EMISSÃO INICIAL"
```

Onde `AD` = data de emissão E-CLIC, `AX` = data emissão SIGEM, `BA` = status SIGEM,
`AL` = status markup CONSAG, `AE` = revisão atual E-CLIC, `BF` = status markup PB.

**Distribuição atual (2.777 docs ativos da LD UGH):**

| Status | Qtd | % Avanço físico (`CI`) | Quem deve agir |
|---|---|---|---|
| `EMITIR EMISSÃO INICIAL` | 1.634 | 0,0 | **OTZ (disciplina)** |
| `DOC. FINALIZADO` | 1.006 | 1,0 | — |
| `AGUARDANDO MARKUP CONSAG` | 50 | 0,5 | **CONSAG** |
| `EMITIR NO SIGEM` | 29 | 0,7 | **OTZ (documentação)** |
| `ATENDER MARKUP CONSAG` | 20 | 0,5 | **OTZ (disciplina)** |
| `AGUARDANDO MARKUP PB` | 18 | 0,7 | **Petrobras** |
| `DOCUMENTO CANCELADO` | 11 | 1,0 | — |
| `ATENDER MARKUP PB` | 9 | 0,7 | **OTZ (disciplina)** |

> Essas 8 linhas são, literalmente, **a lista de cobrança do robô**: 97 documentos com
> responsável identificável e prazo calculado (`AI`, `AM`, `BB`, `BG`).

---

## 6. Cross-reference PW ↔ LD

### 6.1 ✅ Validação da correspondência de abas

| Aba LD | Docs | Encontrados no PW | sob `OTZ PROJETISTA` | sob `ENG OBRA` | Cruzamento |
|---|---|---|---|---|---|
| `LD UGH Trem 2` | 2.777 ativos | 2.705 | **2.705** | 0 | **zero** |
| `LD Trem 2 -ICs` | 1.600 ativos | 1.585 | 0 | **1.585** | **zero** |

**A regra do Ilson está 100% correta.** Não há um único documento fora do lugar.

### 6.2 Por disciplina — `LD UGH Trem 2` (OTZ PROJETISTA)

| DISCIPLINA PETROBRAS | LD total | LD ativos¹ | No PW | Emitidos PW² | GAP³ | Baseline BL0 médio |
|---|---|---|---|---|---|---|
| Tubulação | 2.011 | 1.392 | 1.999 | 572 | 12 | 2026-10-12 |
| Instr&Aut | 227 | 163 | 209 | 73 | **18** | 2026-08-03 |
| Estrutura Metálica | 140 | 2 | 140 | 140 | 0 | 2026-03-27 |
| Elétrica | 137 | 62 | 123 | 75 | **14** | 2026-06-20 |
| Processo On Site | 66 | 35 | 66 | 41 | 0 | 2026-06-21 |
| Fornos | 47 | 36 | 47 | 14 | 0 | 2026-05-11 |
| Segurança | 36 | 17 | 31 | 22 | 5 | 2026-06-11 |
| Telecom | 29 | 9 | 26 | 24 | 3 | 2026-05-29 |
| Dinâmicos | 23 | 6 | 19 | 17 | 4 | 2026-05-20 |
| Civil | 17 | 9 | 17 | 8 | 0 | 2026-04-06 |
| Caldeiraria | 15 | 9 | 8 | **7** | 7 | 2026-08-21 |
| Processo Off Site | 14 | 6 | 14 | 8 | 0 | 2026-07-11 |
| **Processo** ❓ | 9 | 9 | **0** | 0 | **9** | 2026-12-30 (todos) |
| Riscos ❓ | 3 | 3 | 3 | 0 | 0 | 2026-10-09 |
| Arquitetura | 1 | 1 | 1 | 0 | 0 | 2026-06-30 |
| Drenagem | 1 | 1 | 1 | 1 | 0 | 2026-06-12 |
| Arruamento e Pav. | 1 | 0 | 1 | 1 | 0 | 2026-06-05 |
| **TOTAL** | **2.777** | **1.760** | **2.705** | **1.002** | **72** | — |

¹ exclui `DOC. FINALIZADO`, `DOCUMENTO CANCELADO`, `EXCLUÍDO`, `N/A`, `NÃO NECESSÁRIO`
² `RevisaoCompleta` sem `_` **e** `DataAceiteGRD` preenchida
³ documentos da LD sem nenhuma linha correspondente no PW

### 6.3 `LD Trem 2 -ICs` (ENG OBRA)

| Disciplina | LD total | LD ativos | No PW | Emitidos PW | GAP |
|---|---|---|---|---|---|
| Tubulação | 1.600 | 1.600 | 1.585 | 241 | 15 |

### 6.4 🔴 Análise dos 87 documentos de GAP

Os 87 (72 UGH + 15 ICs) têm um padrão perfeito:

- **100% estão em `EMITIR EMISSÃO INICIAL`** — é backlog puro, não erro de join;
- **0 aparecem no PW sob outra empresa** — não é problema de classificação;
- **86 de 87 estão marcados `PRÉ CADASTRADO NO PW? = SIM`** na LD, **mas não existem no export do PW**.

> ⚠️ **Contradição de dado real.** A LD afirma um pré-cadastro que o ProjectWise não confirma.
> Ou o cadastro não foi feito, ou foi feito com número diferente. São 86 documentos que ninguém
> vai conseguir emitir até que alguém abra o cadastro. **Este é o achado mais acionável do
> relatório** — vale um e-mail nesta semana.

Concentração: Instr&Aut 18 · Elétrica 14 · Tubulação 12+15 · Processo 9 · Caldeiraria 7.

### 6.5 ✅ Refinamento do conceito "Documento Emitido"

A regra atual (revisão sem `_` **+** `DataAceiteGRD` preenchida) foi testada contra as 6.281 linhas
do escopo OTZ:

| | sem `DataAceiteGRD` | com `DataAceiteGRD` |
|---|---|---|
| **`RevisaoCompleta` com `_`** | 0 | 1.497 (ciclos de comentário CI/CC) |
| **`RevisaoCompleta` sem `_`** | **3.226** | **1.431 ← emitidos** |

✅ A regra funciona. Mas existe uma equivalente **de campo único e mais robusta**:

| `Última emissão` | Linhas | Significado |
|---|---|---|
| `Previsto` | **3.226** | nunca emitido — *idêntico* ao quadrante sem GRD |
| `Sim` | 1.396 | revisão corrente do documento |
| `Não` | 1.532 | histórico de revisões anteriores |

**Recomendação:** usar `Última emissão` como filtro primário —
`Previsto` = backlog, `Sim` = estado atual (dedupe automático), `Não` = histórico.
Isso elimina a necessidade de `drop_duplicates` e é imune a mudanças no formato da revisão.

**Números de referência:** 1.431 linhas emitidas · **1.272 documentos únicos** ·
1.278 com `Última emissão = Sim`.

⚠️ Atenção: 146 documentos `Superado` e 11 `Cancelado` contam como "emitidos". Para KPI de
*estoque atual* filtre `Última emissão = "Sim"`; para KPI de *produção acumulada*, mantenha todos.

---

## 7. Análise financeira

### 7.1 O que é PPU

**PPU = Planilha de Preços Unitários.** O contrato não paga por hora nem por documento genérico:
paga por **evento de emissão de um tipo de documento**, a preço unitário fechado. A unidade
comercial é o par `TIPO_DOC - ESCOPO`:

```
Item da PPU  =  Tipo do Doc (BN)  +  " - "  +  ESCOPO (J)
                      ↓                            ↓
                 DE, IS, RM, FD…            NOVO | REVISÃO
```

É exatamente o que a coluna **`BT` CONSUMO PPU** calcula. Cada item tem `Valor Unitário` fixo
(`CONSUMO PPU!N`), e `R$ POR DOC.` (col. `CA`) é esse valor herdado para a linha do documento.

### 7.2 Saldo contratual — aba `CONSUMO PPU`

| Item PPU | Docs na LD | Qtde PPU (contrato) | **Saldo** | Valor unitário | Valor total do item |
|---|---|---|---|---|---|
| DE - NOVO | 20 | 121 | +101 | R$ 17.773,67 | R$ 2.150.613,67 |
| DE - REVISÃO | 483 | 544 | +61 | R$ 7.821,73 | R$ 4.255.019,67 |
| ET - NOVO | 3 | 55 | +52 | R$ 12.879,53 | R$ 708.374,09 |
| ET - REVISÃO | 7 | 62 | +55 | R$ 6.164,96 | R$ 382.227,60 |
| FD - NOVO | 18 | 42 | +24 | R$ 11.301,02 | R$ 474.642,95 |
| FD - REVISÃO | 18 | 114 | +96 | R$ 6.526,55 | R$ 744.026,16 |
| **IS - NOVO** | **533** | **46** | **−487** 🔴 | R$ 5.744,54 | R$ 264.249,03 |
| **IS - REVISÃO** | **1.245** | **879** | **−366** 🔴 | R$ 2.010,59 | R$ 1.767.308,97 |
| LI - NOVO | 9 | 29 | +20 | R$ 9.483,45 | R$ 275.020,05 |
| LI - REVISÃO | 46 | 51 | +5 | R$ 5.148,27 | R$ 262.561,57 |
| MC - NOVO | 37 | 40 | +3 | R$ 16.838,69 | R$ 673.547,79 |
| **MC - REVISÃO** | 46 | 44 | **−2** 🟠 | R$ 8.307,56 | R$ 365.532,52 |
| MD - NOVO | 2 | 6 | +4 | R$ 14.899,91 | R$ 89.399,47 |
| MD - REVISÃO | 2 | 2 | 0 🟠 | R$ 4.146,84 | R$ 8.293,69 |
| **RL - NOVO** | 17 | 5 | **−12** 🔴 | R$ 14.361,36 | R$ 71.806,80 |
| **TOTAL** | **2.486** | **2.040** | **−446** | — | **R$ 13.674.438,28** |

> 🔴 **A LD já prevê 446 documentos a mais do que o contrato comporta**, concentrados em
> isométricos (**−853 entre IS-NOVO e IS-REVISÃO**) e relatórios (−12).
> Isso não é erro de planilha: é **exposição contratual**. Ou entra aditivo, ou 446 documentos
> serão produzidos sem receita. Nota da própria aba: *"RMs e PTs não são contabilizados"*.

### 7.3 Como a previsão de faturamento se liga ao avanço — aba `Prev_Fat`

A cadeia é direta e inteiramente determinística:

```
BV (STATUS)  ─┐
              ├─→  AX / W / AS   →  DH (data de medição)  →  DI (mês de medição)
BR (na LD PB?)┘         │                                          │
                        │                            ┌─────────────┘
                        │                            ↓
                   BT (Item PPU) ──────→  pivot Qtde_Docs_Mediçao  (qtd por item × mês)
                                                     │
                                                     ↓
              CONSUMO PPU!N (valor unitário) → T  →  PREV FAT = SUMPRODUCT(qtd; valor)
```

Fórmula literal da linha 27 de `Prev_Fat`: `=SUMPRODUCT(B5:B20; $T$5:$T$20)`
onde `T` = `XLOOKUP(item; 'CONSUMO PPU'!L; 'CONSUMO PPU'!N)`.

**Curva de faturamento prevista (R$):**

| Mês medição | 03/26 | 04/26 | 05/26 | 06/26 | 07/26 | **08/26** | 09/26 | 10/26 | 11/26 | 12/26 | 01/27 | 02/27 | 03/27 | 04/27 | 05/27 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Docs** | 5 | 30 | 152 | 137 | 134 | **448** | 323 | 217 | 282 | 187 | 130 | 174 | 149 | 43 | 56 |
| **R$ mil** | 10 | 209 | 1.126 | 756 | 643 | **1.557** | 1.431 | 1.144 | 1.076 | 782 | 488 | 729 | 753 | 357 | 435 |

Total previsto: **R$ 11.496.662** (contra R$ 13.674.438 de teto de PPU).

### 7.4 Calendário de medição — a regra dos dois cortes

Em `PADRÃO (2)`, três janelas diferentes convivem:

| Regra | Coluna | Corte | Aplica a |
|---|---|---|---|
| Período de emissão | `I` `Per_21_a_20` | dia **20** | agrupamento geral (21 a 20) |
| Medição padrão | `L` `Mês_medição` | dia **6** | todos os tipos exceto IS |
| Medição de isométrico | `O` `IS_medição` | dia **19** | apenas `Tipo do Doc = IS` |

A coluna `DI` escolhe entre `IS_medição` e `Mês_medição` conforme `BN = "IS"`. **Errar esse
desvio joga ~1.800 isométricos no mês errado de faturamento.**

### 7.5 Avanço físico × financeiro

- **Financeiro** (`BZ`→`CF`): `R$ acumulado = CA×BZ + CC×CA`; `SALDO = CA − CE`. Base: peso EAP.
- **Físico** (`CI`): função escada do `STATUS DO DOCUMENTO` — 0 → 0,5 → 0,7 → 1,0.
- **Eventos de medição** (`PADRÃO!AA:AB`): `EMISSÃO LIBERADO - APROVADO PB` = 100%;
  `RM EMITIDA NO SIGEM` / `PT EMITIDO SIGEM` / `ADF 1ª EMISSÃO` = 70%;
  `RM APROVADA PB` / `PT APROVADO PB` / `ADF CERTIFICADO` = 30%.

✅ Os 70/30 da PPU e os 0,7/1,0 do avanço físico são **a mesma régua** — coerência confirmada.

---

## 8. Riscos do pipeline atual

Ordenados por probabilidade × impacto.

### 🔴 R1 — Tabelas dinâmicas com intervalo fixo truncado

| Cache | Consumidor | Intervalo gravado | Docs fora | Colunas |
|---|---|---|---|---|
| 303 | **`Docs p_semana`** | `B8:DG3264` | **131** | até DG |
| 344 | **`Memoria Calculo BM09`** | `A8:DM3320` | **75** | até DM |
| 297 | `Prev (tipo) x Mês` | `C8:DG3391` | 4 | até DG |
| 308 | **`CONSUMO PPU`** | `C8:CK3395` | 0 | ⚠️ **para em CK** — não alcança `DL` `Previsto/Excluído` nem `DM` `Item da PPU` |
| 316 | `Prev (tipo) x Mês` (ICs) | `B8:AF2471` | 1 | até AF |
| 334 / 340 / 351 | Rundown SGM / Prev_Fat / ICs | até linha 3395 / 2472 | 0 | ok |

**Por que é grave:** são intervalos fixos, não Tabelas do Excel. "Atualizar Tudo" **não os
expande**. Cada linha nova da LD nasce invisível para esses pivots, e o erro cresce em silêncio.
Hoje: até **131 documentos** (4,7% da carteira ativa) ausentes de um relatório publicado.

### 🔴 R2 — `EXCLUIR` precisa ser digitado em duas colunas

| Testa `J` (ESCOPO) | Testa `K` (ATIVIDADE) |
|---|---|
| `X`, `AH`, `AI`, `AM`, `BB`, `BT`, `BU`, `DL` | `AM`(1ª cond.), `BV`, `BW`, `CM`, `CP`, `CT`, `CW`, `CX`, `DA`, `DG` |

Hoje os 562 excluídos têm `EXCLUIR` nas duas colunas e tudo bate (`DL` e `BV` = 562/562 ✅).
Mas **nada garante isso**: preencher só `J` deixa `BV` com status ativo — o documento sai do
relatório de escopo e continua na fila de cobrança. Falha silenciosa, sem célula de erro.

### 🔴 R3 — Fórmulas com deslocamento de coluna

Na coluna `AP`/`AR`/`AS` da `LD UGH Trem 2` existe a **mesma fórmula em três variantes deslocadas**:

| Célula | Testa exclusão em | Testa tipo em | Data base | Ocorrências |
|---|---|---|---|---|
| `AP246` | `H` | `I` | `S` | 8 |
| `AR10` | `J` ✅ | `K` ✅ | `U` | 199 |
| `AS160` | `K` | `L` | `V` | 12 |

Assinatura clássica de **inserção de coluna com fórmulas não propagadas**. Só a variante `AR`
está alinhada com o layout atual. As outras 20 linhas calculam datas programadas a partir das
colunas erradas.

### 🟠 R4 — Sete caminhos absolutos em `K:\`

```
K:\DDE\05-Projetos\Projeto Z-546 - RNEST - UGH\01- Planejamento\011_Relatório Query\
```

Quebra se: a letra do drive mudar, o nome da pasta mudar (tem acento e espaços), o usuário estiver
fora da rede, ou o arquivo for aberto por outra pessoa. **Nenhum parâmetro, nenhum fallback.**
Além disso, os nomes de arquivo (`Z-546 - RELATÓRIO PW.csv`) precisam ser reescritos manualmente a
cada export — o arquivo real baixado chama-se `Z546__RELATÓRIO_PW_18_08_26_8h.csv`.

### 🟠 R5 — `Columns=69` × CSV de 70 colunas
Ver §3.3. Perde `DataAlteracaoState` e desalinha se o PW mudar o layout.

### 🟠 R6 — Filtros de escopo aplicados fora do arquivo
`DisciplinaDesc ∉ {GESTÃO, PLANEJAMENTO, PROJETOS}` e `TipoDocumento ≠ ATA` não existem no Power
Query. São 751 linhas que dependem de alguém lembrar de filtrar. Idem `nomeEmpresa` (§3.2).

### 🟠 R7 — Dependência de nomes de aba e item
`Fonte{[Item="Relatório", Kind="Sheet"]}` e `Fonte{[Item="Sheet1", Kind="Sheet"]}`: se o E-CLIC
ou o SIGEM renomear a aba do export, a query morre com erro obscuro.
Idem `Table.Skip(..., 4)` — número de linhas de cabeçalho do SIGEM **hard-coded**.

### 🟠 R8 — `TODAY()` volátil nas colunas de aderência
`CW` e `DG` (`EMITIDO NO PRAZO` / `EM ATRASO`) usam `TODAY()`. O mesmo arquivo aberto em dois dias
diferentes produz KPIs diferentes, e **arquivos históricos se reescrevem sozinhos** ao abrir.
Impossível auditar um número publicado no passado.

### 🟠 R9 — Feriados em quatro intervalos diferentes
`FERIADOS` = `PADRÃO!A3:A36` · `FERIADO_2` = `PADRÃO (2)!A3:A41` ·
`PADRÃO!A3:A55` · `PADRÃO!A3:A58` · `PADRÃO!A3:A109` (usados literalmente dentro das fórmulas).
**Cinco calendários de feriado** para o mesmo projeto. Um novo feriado inserido fora do intervalo
certo altera uns SLAs e não altera outros.

### 🟡 R10 — Layout divergente entre as duas abas LD
`Previsto/Excluído` = `DL` na UGH e `CG` nos ICs; `STATUS DO DOCUMENTO` = `BV` / `BO`;
`Tipo do Doc` = `BN` / `BJ`. Qualquer código que use letra de coluna precisa de dois mapas.
**Sempre indexar por nome de cabeçalho (linha 8).**

### 🟡 R11 — Caixa inconsistente em `DISCIPLINA OTZ`
`PROCESSO`/`Processo`, `SEGURANÇA`/`Segurança`, `MECÂNICA`/`Mecânica`, `ELÉTRICA`, `TUBULAÇÃO`.
O Excel ignora caixa no XLOOKUP; **Python e SQL não**. Normalizar na entrada.

### 🟡 R12 — `calcChain.xml` de 6,8 MB
Sintoma de ~200 mil fórmulas vivas. Recalcular a pasta é caro e o arquivo é frágil a corrupção.

---

## 9. Pontos que precisam de decisão do Ilson

| # | Questão | O que os dados mostram | Sugestão |
|---|---|---|---|
| Q1 | **`Processo` genérico (21 docs, 9 ativos)** — é disciplina própria ou erro de digitação de `Processo On Site`? | Nenhum dos 9 ativos existe no PW; **todos com baseline 2026-12-30** (data-balde) | Provável placeholder. Reclassificar ou marcar `EXCLUIR` |
| Q2 | **`Riscos` (5 docs)** | Sigla CONSAG `RIS`; sem par no PW; N-1710 `98V`/`98X`/`983` (mesma família de Eng. Digital) | Confirmar se entra no escopo contável |
| Q3 | **`CONSAG` como disciplina (5 docs)** | Existe em `PADRÃO!W:X` como diretoria própria | Definir disciplina real ou excluir dos KPIs |
| Q4 | **Filtro do PW: incluir fornecedores?** | O PQ mantém 209 docs de ENGEMASA/ASVOTEC/WEG/INCASE/VIBROPAC; a regra escrita os exclui | Decidir e **unificar** — hoje o número muda conforme quem calcula |
| Q5 | **Estrutura Metálica é DPC** | `PADRÃO!W:X` põe MET em DPC, junto com Civil | A 2ª planilha de HH deve incluir MET? São 185 docs |
| Q6 | **Saldo negativo de PPU (−446 docs)** | IS-NOVO −487, IS-REVISÃO −366, RL-NOVO −12 | Aditivo contratual ou revisão de escopo — decisão de gerência |
| Q7 | **86 docs "pré-cadastrados no PW" que não estão no PW** | §6.4 | Verificar com a CONSAG esta semana |
| Q8 | **Qual data manda no "emitido"?** | LD usa E-CLIC (`RL_EMISSAO`); o PW tem `DataAceiteGRD` própria | Definir a fonte da verdade antes de automatizar |
| Q9 | **`Engenharia Digital` conta ou não?** | Hoje excluída do escopo, mas o Ilson quer manter "Modelo 3D" na contagem | São 50 docs (E3D 25 + COMOS 25) |

---

## 10. Recomendações para a automação

### 10.1 Arquitetura-alvo

```
                    ┌──────────────────────────────────────┐
   Exports diários  │  ingest/  — leitura tolerante        │
   (E-CLIC, SIGEM,  │  • detecta cabeçalho por conteúdo    │
    PW, HH)  ──────▶│  • valida schema, não posição        │
                    │  • registra hash + timestamp         │
                    └──────────────┬───────────────────────┘
                                   ▼
                    ┌──────────────────────────────────────┐
                    │  normalize/ — taxonomia canônica     │
                    │  • sigla = CÓDIGO_CONSAG[5]          │
                    │  • de-para §4.3 como YAML versionado │
                    │  • upper/unaccent em todo rótulo     │
                    └──────────────┬───────────────────────┘
                                   ▼
                    ┌──────────────────────────────────────┐
                    │  core.documento  (SQLite/Parquet)    │
                    │  1 linha por Nº N-1710, com estado,  │
                    │  datas dos 3 sistemas e SLAs         │
                    └───┬────────────┬──────────┬──────────┘
                        ▼            ▼          ▼
                    KPI/dash     cobranca/    financeiro/
                                (e-mail +      (PPU, Prev_Fat)
                                 registro)
```

### 10.2 Regras de ouro (extraídas dos erros encontrados)

1. **Nunca indexar por letra de coluna.** Ler o cabeçalho da linha 8 e mapear por nome.
   Os riscos R1, R3 e R10 são todos variações desse pecado.
2. **Nunca usar intervalo fixo.** Todo agregado se recalcula sobre o dataset inteiro.
3. **`EXCLUIR` em um único lugar.** Uma coluna `escopo` com domínio fechado
   `{NOVO, REVISÃO, EXCLUIR, N/A}` e validação na entrada.
4. **Congelar a data de referência.** Substituir `TODAY()` por `DATA_BASE` recebida como
   parâmetro e gravada no output. Sem isso não existe auditoria (R8).
5. **Um único calendário de feriados**, versionado, com um único conjunto de SLAs nomeados:
   `SLA_MARKUP_CONSAG=3DU` · `SLA_ATENDIMENTO_CONSAG=2/3DU` · `SLA_RESPOSTA_PB=10DU` ·
   `SLA_ATENDIMENTO_PB=5DU` · `SLA_SIGEM_IS=2DU` · `SLA_SIGEM_OUTROS=7DU`.
6. **Caminhos por configuração**, com *glob* por padrão de nome e data
   (`Z546*RELAT*PW*.csv` → pega o mais recente), nunca literal.
7. **Portão de qualidade a cada ingestão** — abortar e avisar se:
   contagem de colunas mudar · disciplina desconhecida aparecer · `GAP` crescer >10% ·
   soma de `CONSUMO PPU` divergir do último ciclo · `DL` ≠ `BV` em qualquer linha.

### 10.3 Ordem de implementação sugerida

| Fase | Entrega | Por quê primeiro |
|---|---|---|
| **1** | `normalize/` + de-para YAML + leitor dos 4 exports | Base de tudo; já rende o relatório de GAP (§6.4) que dá visibilidade imediata |
| **2** | `core.documento` + máquina de estados `BV` reimplementada e **validada contra as 2.777 linhas atuais** | Teste de regressão objetivo: tem que bater 100% |
| **3** | KPI/dashboard sem intervalo fixo | Corrige R1 — os 131 docs invisíveis reaparecem |
| **4** | `cobranca/` — fila a partir de `BV` + `AI`/`AM`/`BB`/`BG`, e-mail e log | O valor visível para a gerência |
| **5** | `financeiro/` — PPU, Prev_Fat, curva de medição com os dois cortes (§7.4) | Maior valor, maior risco: só depois de 1–4 estáveis |

### 10.4 Teste de aceitação

O sistema só substitui a planilha quando reproduzir, **a partir dos brutos**, estes nove números:

| Métrica | Valor esperado (base 18/08/2026) |
|---|---|
| LD UGH — documentos | 3.387 |
| LD UGH — `EXCLUÍDO` | 562 |
| LD ICs — documentos | 2.464 (863 excluídos) |
| LD UGH ativos, fora Coord/Eng.Digital | 2.777 |
| `DOC. FINALIZADO` (UGH ativos) | 1.006 |
| PW escopo OTZ, pós 3 filtros | 6.281 linhas |
| PW documentos emitidos | 1.431 linhas / 1.272 únicos |
| GAP LD↔PW | 87 (72 + 15) |
| Saldo PPU total | −446 |

---

## 11. Reconstrução do histórico do projeto

Os três sistemas guardam datas suficientes para reconstruir o que aconteceu **antes da chegada do
Ilson**. Não há lacuna: o registro começa em **24/11/2025** (primeiro lançamento de HH) e o
primeiro documento aceito é de **18/12/2025**.

### 11.1 Linha do tempo mestre

| Mês | Docs emitidos (PW) | Ciclos de comentário | Horas (HH) | Efetivo | **HH / doc** |
|---|---|---|---|---|---|
| 2025-11 | 0 | 0 | 96,5 | 5 | — *(mobilização)* |
| 2025-12 | 1 | 5 | 1.723,5 | 20 | *(ramp-up)* |
| 2026-01 | 55 | 104 | 3.781,0 | 34 | **68,7** |
| 2026-02 | 76 | 80 | 4.003,6 | 35 | **52,7** |
| 2026-03 | 104 | 155 | 5.535,0 | 42 | **53,2** |
| 2026-04 | 108 | 200 | 5.192,0 | 41 | **48,1** |
| 2026-05 | 214 | 162 | 5.397,3 | 40 | **25,2** |
| 2026-06 | 255 | 165 | 5.700,8 | 43 | **22,4** |
| 2026-07 | **362** | **341** | **6.735,2** | **52** | **18,6** |
| 2026-08* | 256 | 285 | 2.102,9* | 40 | — |

\* agosto parcial (dados até 18/08).

### 11.2 O que a curva conta

**1. Curva de aprendizado real e forte.** O custo por documento caiu de **68,7 HH/doc (jan)** para
**18,6 HH/doc (jul)** — uma **redução de 73%** com efetivo crescendo apenas 53% (34 → 52). O ganho
não veio de gente: veio de maturidade. A inflexão está entre **abril e maio** (48,1 → 25,2), quando
a Tubulação entra em produção em escala (32 → 105 docs/mês).

**2. O projeto é uma máquina de isométricos.** Tubulação salta de 32 (abr) para 105 (mai), 189
(jun), 277 (jul), 220 (ago parcial). Em julho, **77% de tudo que saiu era tubulação**. Qualquer
KPI que trate todas as disciplinas com o mesmo peso vai ser dominado por esse ruído.

**3. Ordem de entrada em produção das disciplinas:**

| Disciplina | 1ª emissão | Docs emitidos | Leitura |
|---|---|---|---|
| Estrutura Metálica | 18/12/2025 | 166 | abriu o projeto; **encerrou em 31/07** — escopo praticamente concluído |
| Mecânica | 21/01/2026 | 75 | idem, última emissão 31/07 |
| Tubulação | 23/01/2026 | 864 | **ativa até hoje** — é o caminho crítico |
| Elétrica / Instrumentação | 26/01/2026 | 92 / 89 | ativas |
| Telecom | 06/02/2026 | 26 | ativa |
| Safety | 06/03/2026 | 30 | ativa |
| Modelo 3D | 09/03/2026 | 18 | ativa |
| Civil | 18/03/2026 | 8 | volume baixíssimo — confirma que é outra gerência |
| Processo | 13/04/2026 | 56 | entrou tarde, ativa |
| Qualidade | 27/05/2026 | 6 | marginal |

> ⚠️ **Estrutura Metálica e Mecânica pararam de emitir em 31/07/2026.** Na LD, Estrutura Metálica
> tem 140 docs e apenas **2 ativos** — coerente com escopo concluído. Mecânica ainda tem 9+36+6
> ativos entre Caldeiraria/Fornos/Dinâmicos. Vale confirmar se é conclusão ou parada.

**4. Retrabalho é maior que produção.** Em julho: 362 emissões contra **341 ciclos de comentário**.
Cada documento emitido gera quase um ciclo de markup. Acumulado: 1.431 emissões × 1.497 ciclos.
**Razão ≈ 1,05 ciclo por emissão** — é aqui que a cobrança automática rende mais.

**5. Rotatividade mapeada.** 14 pessoas sem lançamento há mais de 45 dias (≈ 4.010 h investidas).
As saídas relevantes concentram-se em **Gestão** (Gustavo Lima, Valério Sanches, Aline Ferreira —
todos até abril) e **CDA** (Filipe Brandão, até 30/04). Sinal de uma troca de time de coordenação
no 2º trimestre — provavelmente o contexto da contratação do próprio Ilson.

**6. 🔴 Lançamento de HH está atrasado.** Agosto registra 2.102,9 h para 40 pessoas em 12 dias
úteis. O esperado seria ~3.800 h. **Faltam ~45% dos lançamentos** — e 1.168 lançamentos (15%)
seguem com `APROVAÇÃO = Não`. Alvo imediato e trivialmente automatizável de cobrança.

### 11.3 Equipe reconstruída — top 10 por horas

| Responsável | Horas | Disciplina dominante | Desde | Até |
|---|---|---|---|---|
| RICARDO.AMORIM | 1.392,0 | Tubulação | 01/12/2025 | ativo |
| LUIZ.NERY | 1.304,0 | Gestão | 24/11/2025 | 23/07/2026 |
| JOSIMAR.SILVA | 1.287,0 | CDA | 08/12/2025 | ativo |
| SAMUEL.SOUZA | 1.255,1 | Qualidade | 22/12/2025 | ativo |
| FABIO.KRELLING | 1.244,0 | Planejamento | 15/12/2025 | ativo |
| ENILSON.CRUZ | 1.233,1 | Processo | 08/12/2025 | ativo |
| ALDO.OLIVEIRA | 1.232,0 | Elétrica | 05/01/2026 | ativo |
| LEONARDO.FERREIRA | 1.216,0 | CAE - CAD | 05/01/2026 | ativo |
| BRUNO.LEE | 1.206,7 | Mecânica | 08/12/2025 | ativo |
| CARLOS.LORENA | 1.200,0 | Instrumentação | 12/01/2026 | ativo |

> Esta tabela é também **a lista de destinatários da cobrança automática**, cruzada com
> `EQ. INTERNA RESPONSÁVEL` (col. BW) e `DisciplinaResposta` do PW.

### 11.4 Como estender a reconstrução

Os campos abaixo permitem detalhar ainda mais e **não estão sendo usados por ninguém hoje**:

| Campo | Onde | O que reconstrói |
|---|---|---|
| `datacriacao` / `datacriacaoCI` / `datacriacaoCC` | PW | data exata de cadastro, 1º comentário interno e comentário do cliente |
| `DataAlteracaoState` | PW col. 70 | **descartada pelo `Columns=69`** — é o carimbo de cada mudança de estado |
| `Data Início Fluxo` / `Data Fim Fluxo` | `RL DOCS` (E-CLIC) | duração real do fluxo interno OTZ |
| `QTD_DIA_UTIL_DOC_ESTEVE_WF` | `RL_Previsto_Sigem` | dias úteis que o doc passou no workflow SIGEM |
| `Modificado em` | `RL_Sigem` | último toque da Petrobras no documento |
| `Destinatários` | `RL_EMISSAO` | grafo de quem recebe o quê — base do e-mail automático |

---

## 12. Arquitetura do sistema autônomo

### 12.1 Princípio operacional — o portão humano

> **Regra de ouro:** toda ação externa (e-mail, registro, cobrança) passa pelo aval do Ilson
> **antes** de sair. Autonomia total só depois de o padrão estar comprovado.

Isso não é uma limitação temporária: é a arquitetura correta. Sistemas que agem em nome de uma
pessoa precisam de um **estado explícito de aprovação**, gravado, reversível e auditável.

```
detecta → redige → ENFILEIRA (pendente_aprovacao) → Ilson aprova/edita/rejeita → envia → registra
                          │                                    │
                          └── expira em 48 h ──────────────────┘
                              (não envia; volta para a fila)
```

Cada item da fila carrega: documento, destinatário, prazo violado, número de cobranças anteriores,
texto proposto e **o cálculo que justificou a cobrança**. A aprovação é um clique; a rejeição
alimenta o ajuste do critério.

**Modo sombra primeiro.** Antes de qualquer envio, rodar 2–4 semanas gerando a fila **sem enviar
nada**. Ilson compara o que o sistema teria feito com o que ele efetivamente fez. Quando a
concordância passar de ~90%, liga-se o envio com aprovação; depois, autonomia por categoria — nunca
tudo de uma vez. Comece pelo mais seguro (lembrete interno de HH), termine pelo mais sensível
(cobrança à Petrobras).

### 12.2 Camadas

| Camada | Responsabilidade | Estado |
|---|---|---|
| `ingest/` | ler os 4 exports, validar schema, versionar com hash+timestamp | sem estado |
| `normalize/` | taxonomia canônica (§4), calendário, SLAs | de-para em YAML versionado |
| `core/` | 1 linha por `Nº N-1710`; máquina de estados `BV`; SLAs calculados | **fonte da verdade** |
| `history/` | série temporal append-only — nunca sobrescreve | ✅ resolve o risco R8 |
| `kpi/` | agregações e dashboard, sempre sobre o dataset inteiro | ✅ resolve R1 |
| `outreach/` | detecta violação, redige, **enfileira**, registra | portão humano |
| `finance/` | PPU, Prev_Fat, curva de medição com os dois cortes | — |

### 12.3 O que torna isto melhor que o Power Query

| Power Query hoje | Sistema autônomo |
|---|---|
| 7 caminhos fixos em `K:\` | *glob* por padrão + configuração |
| `Columns=69` contra CSV de 70 | schema validado, falha ruidosa |
| Intervalos de pivot congelados | agregação sobre o dataset inteiro |
| `TODAY()` reescreve o passado | `DATA_BASE` congelada e gravada |
| `EXCLUIR` em duas colunas | domínio fechado, validado na entrada |
| 5 calendários de feriado | um só, versionado |
| Disciplina em 5 vocabulários | sigla canônica do `CÓDIGO CONSAG` |
| Silencioso quando erra | portão de qualidade aborta e avisa |

### 12.4 Onde a IA agrega de verdade (e onde não)

**Não use modelo de linguagem para:** contar documentos, calcular SLA, agregar horas, aplicar
filtro. Isso é código determinístico, e precisa ser **reproduzível bit a bit** — é o que sustenta
a credibilidade do número diante da gerência.

**Use modelo de linguagem para:**
- **redigir a cobrança** no tom do Ilson, com o contexto certo (quantas vezes já cobrou, qual o
  histórico daquele documento, qual a relação com aquele interlocutor);
- **classificar o inclassificável** — os casos `Processo` genérico, `CONSAG` como disciplina, os
  86 pré-cadastros fantasma (§6.4): propor a classificação com justificativa, para o Ilson aprovar;
- **ler o texto livre** — `OBSERVAÇÃO - PENDÊNCIAS E RESTRIÇÕES` (col. Y) e `NOTA` (col. AA) são
  campos que hoje ninguém agrega e que contêm a explicação real dos atrasos;
- **escrever a narrativa do período** — transformar a variação dos KPIs em um parágrafo que a
  gerência lê em 30 segundos. É isso que desperta a curiosidade que o Ilson quer despertar.

### 12.5 Nota sobre infraestrutura

Com VPS própria, o desenho natural é: um *cron* diário puxa os exports, roda `ingest→core`, grava o
snapshot em `history/`, regenera o dashboard estático e **enfileira** as cobranças. O volume real é
modesto — ~18 mil linhas de PW, ~7,8 mil de HH. Isso roda em segundos e cabe em SQLite.

O custo de API é irrelevante nesse desenho, porque o modelo só é chamado no que não é
determinístico: redação de e-mail (dezenas por dia), classificação de exceções (dezenas por
semana) e a narrativa (uma por semana). **Não há necessidade de plano maior** — o gargalo do
projeto nunca foi computação, foi a fragilidade do pipeline.

### 12.6 Primeira entrega que a gerência vai notar

Antes de qualquer automação, existe um relatório de uma página que já pode ser produzido hoje com
os dados desta análise, e que ninguém na OTZ tem:

1. **86 documentos marcados como pré-cadastrados no PW que não existem no PW** (§6.4) — bloqueio
   concreto, nominal, por disciplina.
2. **131 documentos invisíveis no relatório semanal** por causa do intervalo congelado da
   `Docs p_semana` (§8/R1) — o número publicado está errado e agora se sabe por quê.
3. **Saldo de PPU em −446 documentos**, sendo −853 só em isométricos (§7.2) — exposição contratual.

Os três são verificáveis, específicos e não dependem de nenhum sistema novo. São a credencial
para propor o resto.

---

## 13. Referência rápida — códigos

**Emissor (grupo 5 do N-1710)** — validado contra `nomeEmpresa` no PW:

| Código | Empresa | Docs na LD | Observação |
|---|---|---|---|
| `C1U` | **OTZ (produção própria)** | 3.632 | também usado pela CONSAG em docs próprios |
| `CHZ` | CHEINTEC (acervo herdado) | 1.202 | 100% `OTZ PROJETISTA` no PW |
| `JEI` | Jaguará (acervo herdado) | 850 | 100% `OTZ PROJETISTA` no PW |
| `ATI` | ASVOTEC | — | fornecedor |
| `EDF` | ENGEMASA | — | fornecedor |
| `WDD` | WEG | — | fornecedor |
| `UAG`,`UOP`,`GBR`,`SWM`,`JCC`,`EVY`,`SJA`,`VBP`,`RD7`,`GAA`,`H7A`,`LUB`,`MIE`,`PEI`,`RND`,`RSF`,`CIU` | diversos/legado | 1–32 cada | ver GLOSSÁRIO §7 |

**Tipos de documento na LD** (prefixo de 2 letras do `Nº N-1710`):
`IS` 4.387 · `DE` 598 · `RM` 158 · `FD` 136 · `I-` 118 (prefixo de importado — tipo real em
`MID(C;3;2)`) · `PT` 109 · `MC` 106 · `RL` 86 · `LI` 63 · `SI` 55 · `ET` 13 · `MD` 10 · `LD` 7 ·
`MA` 2 · `LM` 1.

**Status de markup CONSAG** (`AL`): `APROVADO` · `APROVADO COM COMENTÁRIOS` · `RECUSADO` · `N/A`
**Status SIGEM** (`BA`): `Para Construção` · `Para Compra` · `Sem Comentários` · `Com Comentários`
· `Recusado` · `Cancelado`
**`o_statename` no PW**: `Emitir para Cliente` · `Em Analise Engenharia` · `Emitido para Cliente` ·
`Liberado para Construcao` · `Liberado para Compra` · `Aprovado` · `Aprovado com Comentarios` ·
`Superado` · `Cancelado` · `Reprovado` (+ variantes `pelo Cliente`)

---

*Documento gerado por análise direta dos arquivos-fonte, incluindo o código M do Power Query
extraído de `customXml/item1.xml`. Todos os números são reprodutíveis a partir dos exports de
18/08/2026.*
