# PROTOCOLO KPI — Z-546 RNEST UGH
**OTZ Engenharia × CONSAG × Petrobras**  
**Responsável:** Ilson dos Santos Azevedo — Eng. Planejamento  
**Versão:** 21/08/2026 — inclui Civil (DPC) + tabela de-para + correção MEC/MET + problemas de qualidade de dados

---

## 1. FONTES DE DADOS E FILTROS OBRIGATÓRIOS

### 1.1 Relatório PW (ProjectWise — CONSAG)

| Filtro | Operação | Valor |
|--------|----------|-------|
| `nomeEmpresa` | MANTER | `ENG OBRA` ou `OTZ PROJETISTA` |
| `DisciplinaDesc` | REMOVER | `GESTÃO`, `PLANEJAMENTO`, `PROJETOS` |
| `TipoDocumento` | REMOVER | `ATA` |

> **Atenção:** o Power Query atual faz exclusão (`nomeEmpresa ∉ {CONSAG, CONSAG QUALIDADE}`), não inclusão. Isso mantém 209 documentos de fornecedores (ENGEMASA 116, ASVOTEC 83, WEG 6…). O script autônomo deve usar inclusão explícita.

### 1.2 Lista de Documentos (LD Excel — OTZ)

**Duas abas mestras — estruturas diferentes:**

| Aba | Equivale a | Linhas | Colunas | Cabeçalho |
|-----|------------|--------|---------|-----------|
| `LD UGH Trem 2` | OTZ PROJETISTA | 3.396 | 118 | linha 8, dados a partir linha 9 |
| `LD Trem 2 -ICs` | ENG OBRA (isométricos) | 2.472 | 88 | linha 8, dados a partir linha 9 |

> **Crítico:** as colunas de Status e datas estão em posições diferentes nas duas abas (DL vs CG). Nunca usar letra de coluna hard-coded — usar o nome do cabeçalho.

**Filtros obrigatórios da LD:**

| Campo | Operação | Valor | Coluna |
|-------|----------|-------|--------|
| `DISCIPLINA PETROBRAS` | REMOVER | `Coordenação` · `Engenharia Digital (E3D)` · `Engenharia Digital (COMOS)` | col. H |
| `ESCOPO` | REMOVER | `EXCLUIR` | col. J |
| `ATIVIDADE` | REMOVER | `EXCLUIR` | col. K |

> **Regra EXCLUIR — crítica:** o marcador EXCLUIR deve estar nas **duas colunas J e K**. Preencher só uma cria um documento "meio-excluído" sem erro visível. O script deve testar `J == "EXCLUIR" OR K == "EXCLUIR"` para remover.

**Sigla canônica de disciplina:**
```python
SIGLA = str(row["CÓDIGO CONSAG"]).split("-")[5].strip()
# Exemplo: "5290-002-231-19-40-TUB-001" → "TUB"
# 100% preenchido em todas as linhas da LD
```

### 1.3 Cadastro de Horas (HH)

**Duas planilhas — somar, nunca substituir:**

| Planilha | Projeto | Aba | Cabeçalho |
|----------|---------|-----|-----------|
| Principal | Z-546 - RNEST - UGH | `cadastro horas` | linha 4, dados a partir linha 5 |
| DPC (Civil) | Z-546.1 - RNEST - UGH | `cadastro horas` | linha 4, dados a partir linha 5 |

**Colunas relevantes (0-indexado):**

| Índice | Campo |
|--------|-------|
| 1 | DISCIPLINA |
| 4 | DATA |
| 5 | HORAS |
| 11 | TIPO (`Horas Previstas` / `Serviços Adicionais`) |

---

## 2. DEFINIÇÕES FUNDAMENTAIS

### 2.1 CICLO (unidade de medida do HH)

> **Ciclo** = cada passagem completa de um documento pelo fluxo, identificada por uma linha no PW com `DataAceiteGRD` preenchida.
>
> Um documento com 3 `DataAceiteGRD` diferentes = 3 ciclos.

**Data âncora de todos os KPIs de tempo:** `DataAceiteGRD` — data em que a GRD foi aceita, momento oficial de envio ao próximo ator do fluxo.

### 2.2 EMISSÃO vs REVISÃO

| Conceito | Campo PW | Regra | Exemplo |
|----------|----------|-------|---------|
| **Emissão de desenho** | `RevisaoCompleta` | Sem sufixo (`_A`, `_B`, `_1`…) | `"0"`, `"1"`, `"2"` |
| **Revisão de desenho** | `RevisaoCompleta` | Com sufixo letra | `"0_A"`, `"1_B"` |
| **Documento emitido** | `RevisaoCompleta` + `DataAceiteGRD` | Sem sufixo + data preenchida | Aprovado pela Petrobras |

**Filtro "emissão pura":**
```python
sem_sufixo = not bool(re.search(r'_[A-Za-z]', str(row["RevisaoCompleta"])))
com_grd    = pd.notna(row["DataAceiteGRD"]) and row["DataAceiteGRD"] != ""
emissao_pura = sem_sufixo and com_grd
```

**Para o forecast HH (KPI 1):** usar **ciclos totais** (emissões + revisões) — o HH é consumido em cada ciclo independente de tipo.

### 2.3 Normalização obrigatória antes de qualquer comparação

```python
import unicodedata, re

def normalizar(s):
    s = str(s).strip().upper()
    s = unicodedata.normalize('NFKD', s)
    s = s.encode('ascii', errors='ignore').decode()
    return s

# Colapsos muitos-para-um (HH e LD usam nomes granulares; PW e sigla usam agrupado):
MEC_LD  = {"CALDEIRARIA", "DINAMICOS", "FORNOS", "MECANICA"}
PRO_LD  = {"PROCESSO", "PROCESSO ON SITE", "PROCESSO OFF SITE"}
CIV_LD  = {"CIVIL", "DRENAGEM", "ARRUAMENTO E PAVIMENTACAO"}
M3D_HH  = {"CDA", "CAE - CAD"}
OVH_HH  = {"GESTAO", "PLANEJAMENTO", "GERAL"}  # overhead — só custo real
```

---

## 3. TABELA DE-PARA DEFINITIVA (HH ↔ PW ↔ LD)

Construída por join documento-a-documento (LD `Nº N-1710` ↔ PW `NumeroDocumentoCliente`). Concordância medida por cruzamento real.

| Sigla | Nome definitivo | HH (planilha) | PW `DisciplinaDesc` | LD col. H (Petrobras) | Status KPI 1 |
|-------|----------------|---------------|--------------------|-----------------------|--------------|
| `TUB` | Tubulação | `TUBULAÇÃO` | `TUBULAÇÃO` | `Tubulação` | ✅ Forecast completo |
| `ELE` | Elétrica | `ELÉTRICA` | `ELÉTRICA` | `Elétrica` | ✅ Forecast completo |
| `PRO` | Processo | `PROCESSO` | `PROCESSO` | `Processo On Site` · `Processo Off Site` · `Processo` | ✅ Forecast completo |
| `INS` | Instrumentação | `INSTRUMENTAÇÃO` | `INSTRUMENTAÇÃO` | `Instr&Aut` | ✅ Forecast completo |
| `MEC` | Mecânica | `MECÂNICA` | `MECÂNICA` | `Caldeiraria` · `Dinâmicos` · `Fornos` · `Mecânica` | ✅ Forecast completo |
| `CIV` | Civil 🔵 | *(DPC)* | `CIVIL` | `Civil` · `Drenagem` · `Arruamento e Pav.` | ✅ Forecast completo |
| `MET` | Estrutura Metálica 🔵 | *(DPC, via MEC)* | `ESTRUTURA METÁLICA` | `Estrutura Metálica` | ✅ Forecast completo |
| `ARQ` | Arquitetura 🔵 | *(DPC)* | `ARQUITETURA` | `Arquitetura` | ✅ Forecast completo |
| `SAF` | Segurança | `SEGURANÇA` | `SAFETY` ⚠️ | `Segurança` | ✅ Forecast completo |
| `TEL` | Telecomunicações | `TELECOM` | `TELECOMUNICAÇÕES` ⚠️ | `Telecom` | ✅ Forecast completo |
| `QUA` | Qualidade | `QUALIDADE` | `QUALIDADE` | *(não existe na LD)* | 📊 Só custo real |
| `M3D` | Modelo 3D / Eng. Digital ⛔ | `CDA` + `CAE - CAD` | `SISTEMA DE MODELO 3D` · `AUTOMAÇÃO` | `Eng. Digital (E3D/COMOS)` | 🔮 Inferência estatística |
| `OVH` | Overhead gerencial ⛔ | `GESTÃO` · `PLANEJAMENTO` · `GERAL` | *(filtrado)* | *(não existe)* | 📊 Só custo real |

> 🔵 = vem da planilha DPC (Civil)  
> ⚠️ = nome diferente entre fontes — tradução necessária  
> ⛔ = excluído do escopo de documentos técnicos

---

## 4. METODOLOGIA DO FORECAST HH (KPI 1)

### 4.1 Cálculo do HH/ciclo histórico

```python
# Por disciplina (sigla) × tipo de documento
hh_real   = hh_df.groupby(["sigla"])["horas"].sum()
ciclos_pw = pw_df[pw_df["DataAceiteGRD"].notna()].groupby(["sigla"])["NumeroDocumentoCliente"].count()

hh_por_ciclo = (hh_real / ciclos_pw).dropna()
```

### 4.2 Forecast de HH futuro

```python
# Ciclos futuros = documentos na LD que ainda não emitidos × revisões esperadas
ciclos_futuros = ld_df[ld_df["ultima_emissao"] == "Previsto"].groupby("sigla")["num_doc"].count()

hh_previsto = ciclos_futuros * hh_por_ciclo
```

### 4.3 Classificação de HH por categoria

| Categoria | HH total | Linha no gráfico |
|-----------|----------|-----------------|
| Previsível (10 disciplinas) | ~30.293h | Linha sólida — forecast determinístico |
| Modelo 3D (CDA + CAE-CAD) | 6.689h | Linha tracejada — inferência estatística (se r > 0,7) |
| Overhead (GESTÃO, PLAN, GERAL) | ~8.028h | Barra cinza — só custo real, sem projeção |
| **Total geral** | **~45.010h** | — |

### 4.4 Números atuais (base 18/08/2026)

| Número | Valor | Nota |
|--------|-------|------|
| HH realizado (previsível) | 30.293h | 10 disciplinas com forecast |
| HH modelo 3D (CDA+CAE) | 6.689h | Sem forecast determinístico |
| HH overhead | 8.028h | Gestão + Planejamento + Geral |
| Total geral | 45.010h | Soma das duas planilhas |
| Pico set/26 | 9.563h | 3,6× a média histórica — coerente com LD |

---

## 5. REGRAS DA LD — RESUMO EXECUTIVO

```python
# ── FILTROS OBRIGATÓRIOS DA LD ──────────────────────────────────────
DISC_REMOVER_LD = {
    "COORDENACAO",
    "ENGENHARIA DIGITAL (E3D)",
    "ENGENHARIA DIGITAL (COMOS)"
}
# Testar coluna H normalizada

# ── EXCLUÍDOS ────────────────────────────────────────────────────────
# Regra: excluir se col J == "EXCLUIR" OU col K == "EXCLUIR"
# CRÍTICO: preencher só uma delas cria "meio-excluído" sem erro visível
excluido = (row["ESCOPO"] == "EXCLUIR") or (row["ATIVIDADE"] == "EXCLUIR")

# ── DOCUMENTO NUNCA EMITIDO ──────────────────────────────────────────
# Última emissão == "Previsto" → documento ainda não entrou no fluxo GRD
nao_emitido = row["ultima_emissao"] == "Previsto"  # 3.226 documentos

# ── SIGLA CANÔNICA ───────────────────────────────────────────────────
sigla = str(row["CÓDIGO CONSAG"]).split("-")[5].strip()
```

---

## 6. FILTROS DO PW — RESUMO EXECUTIVO

```python
# ── FILTROS OBRIGATÓRIOS DO PW ───────────────────────────────────────
EMPRESA_MANTER  = {"ENG OBRA", "OTZ PROJETISTA"}
DISC_REMOVER_PW = {"GESTÃO", "PLANEJAMENTO", "PROJETOS",
                   "SISTEMA DE MODELO 3D", "AUTOMAÇÃO", "QUALIDADE"}
TIPO_REMOVER_PW = {"ATA"}

pw_filtrado = pw_df[
    pw_df["nomeEmpresa"].isin(EMPRESA_MANTER) &
    ~pw_df["DisciplinaDesc"].isin(DISC_REMOVER_PW) &
    ~pw_df["TipoDocumento"].isin(TIPO_REMOVER_PW)
]
```

---

## 7. SLAs DO FLUXO §9.2

| Ator | SLA | Base | Status |
|------|-----|------|--------|
| CONSAG — 1ª análise | 3 DU | Fluxograma §9.2 | ✅ Confirmado |
| CONSAG — reanálise | 2 DU | Fluxograma §9.2 | ✅ Confirmado |
| OTZ — resposta comentários | 5 DU | Texto §9.2 | ⚠️ Decisão pendente (vs 3du do fluxograma) |
| Petrobras | 10 DU | Contrato | ✅ Confirmado |
| SIGEM — upload | 0 DU (mesmo dia do PW) | Fluxograma §9.2 | ❌ Nenhum KPI mede |

---

## 8. ACHADOS CRÍTICOS

1. **RL_PW é aba órfã:** "Emitido no PW" na LD = GRD saiu do E-CLIC, não consta no ProjectWise.
2. **86 documentos pré-cadastrados no PW que não existem** no export PW. Todos em `EMITIR EMISSÃO INICIAL`.
3. **6 tabelas dinâmicas com ranges truncados:** `Docs p_semana` perde 131 documentos, `Memoria Calculo BM09` perde 75.
4. **3 campos contratuais 100% vazios:** `SEVERIDADE` · `Rede de Precedência` · `FLUXOGRAMA (REF. Isométrico)` — Anexo VII.
5. **Curva de aprendizado:** 68,7 HH/doc (jan/25) → 18,6 HH/doc (jul/26) — 3,7× mais eficiente com 53% mais pessoas.
6. **1.153 ICs bloqueados:** dependentes de IS-200 pai não emitido.
7. **Saldo PPU negativo:** −446 documentos (−853 em isométricos) — LD prevê mais do que o contrato paga.

---

---

## 9. PROBLEMAS DE QUALIDADE DE DADOS — HH × PW (CRÍTICO PARA O OUTRO CLAUDE)

Os problemas abaixo foram descobertos pelo cruzamento real HH × PW. **Nenhum dado deve ser publicado no dashboard sem verificar estas seções.**

### 9.1 MEC + MET — Problema de granularidade no cadastro de HH (CORRIGIDO por pooling)

**Causa:** O cadastro de HH da planilha principal não separa MECÂNICA de ESTRUTURA METÁLICA. Todo o trabalho do time principal (inclusive EME) é lançado como `MECÂNICA`. Apenas a planilha DPC tem uma linha separada `ESTRUTURA METÁLICA` (390h).

**Consequência sem correção:**
- MECÂNICA: 2.940h ÷ 218 ciclos = **13,49h/ciclo** (inflado — inclui trabalho EME)
- ESTRUTURA METÁLICA: 390h ÷ 388 ciclos = **1,01h/ciclo** (deflado — só DPC)

**Correção aplicada — pooling:**
```
HH pool  = 2.940h (principal) + 390h (DPC) = 3.330h
Ciclos   = 218 (MEC) + 388 (MET) = 606
HH/ciclo = 3.330 ÷ 606 = 5,50h/ciclo → aplicado a MEC e MET no forecast
```

**Status:** PROVISÓRIO. Correto definitivamente quando o cadastro de HH começar a separar as duas disciplinas.

**Ação futura:** pedir para a equipe de HH criar linha separada `ESTRUTURA METÁLICA` na planilha principal.

---

### 9.2 ARQ — Sem ciclos no PW (sem solução possível agora)

**Causa:** Arquitetura tem 284h de HH mas **0 ciclos no PW**. A disciplina ainda não iniciou emissão de documentos no ProjectWise.

**Ação:** Marcar como N/A no forecast do KPI 1. Atualizar automaticamente quando os primeiros documentos forem emitidos.

---

### 9.3 CIV — Amostra insuficiente (provisório)

**Causa:** Civil tem apenas 18 ciclos (8 documentos únicos) no PW. Entrou em 18/03/2026 — volume muito baixo.

**Consequência:** HH/ciclo = 3.097h ÷ 18 = **172h/ciclo** — estatisticamente inválido para forecast.

**Ação:** Marcar no dashboard com flag ⚠️ "provisório". Revisar quando Civil tiver > 50 ciclos no PW.

---

### 9.4 TEL — HH suspeito (verificar com equipe)

**Causa:** Telecomunicações tem 36h de HH para 57 ciclos = **0,63h/ciclo = 38 minutos por documento**. Irreal para documentos de engenharia.

**Hipótese:** O HH de Telecom está sendo lançado em outra disciplina (possivelmente Elétrica ou Instrumentação).

**Ação:** Verificar com a equipe antes de usar o número no forecast.

---

### 9.5 Tabela HH/ciclo final — com status de confiança

| Sigla | Disciplina | HH real | Ciclos PW | HH/ciclo | Confiança |
|-------|-----------|--------:|----------:|----------:|-----------|
| TUB | Tubulação | 7.250h | 1.514 | **4,79h** | ✅ Alta |
| ELE | Elétrica | 5.065h | 204 | **24,83h** | ✅ Alta |
| PRO | Processo | 4.636h | 195 | **23,77h** | ✅ Alta |
| INS | Instrumentação | 4.584h | 182 | **25,19h** | ✅ Alta |
| MEC | Mecânica (pool) | 3.330h | 606 | **5,50h** | 🟡 Média — pool MEC+MET |
| MET | Est. Metálica (pool) | (pool c/ MEC) | (pool c/ MEC) | **5,50h** | 🟡 Média — pool MEC+MET |
| SAF | Segurança | 751h | 93 | **8,08h** | ✅ Alta |
| CIV | Civil | 3.097h | 18 | 172h ⚠️ | 🔴 Baixa — 18 ciclos |
| ARQ | Arquitetura | 284h | 0 | — N/A | ❌ Sem ciclos no PW |
| TEL | Telecomunicações | 36h | 57 | 0,63h ⚠️ | 🔴 Suspeito — verificar HH |

---

*Protocolo gerado em: 21/08/2026 — baseado em todas as análises da sessão Z-546. Para o outro Claude: este documento substitui qualquer versão anterior.*
