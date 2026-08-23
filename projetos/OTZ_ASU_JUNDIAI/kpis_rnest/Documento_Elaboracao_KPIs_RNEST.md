# Documento de Elaboração de KPIs — RNEST Z-546 Lote D
**OTZ Engenharia · Supervisão GPLAN: Ilson dos Santos Azevedo**
Versão 1.2 · Agosto 2026

---

## 1. Propósito e Governança

Este documento registra **como cada KPI é construído**: quais planilhas alimentam, quais colunas são lidas, quais regras de negócio se aplicam, e qual é a lógica de cálculo. Deve ser atualizado a cada novo KPI criado ou a cada mudança de regra aprovada.

**Regra de Ouro:** OTZ nunca comunica diretamente com Petrobras. Toda comunicação passa pela CONSAG via GRD. Os dados que alimentam os KPIs refletem exatamente essa cadeia.

**Responsável pela atualização:** Supervisor GPLAN (Ilson dos Santos Azevedo)
**Branch Git:** `claude/onedrive-access-permissions-WeExM`
**Repositório:** `ilson-engenharia/meu-planejamento`

---

## 2. Fontes de Dados

### 2.1 Planilhas de HH (Homem-Hora)

| ID | Nome | Contrato | Disciplinas cobertas | Observação |
|----|------|----------|----------------------|------------|
| Z-546 | Planilha Principal | Lote D | TUB, ELE, PRO, INS, MEC, SAF, ARQ, QUA, OVH | Fonte primária de HH |
| Z-546.1 | Planilha DPC | Lote D | MET, CIV, TEL, M3D (CAE-CAD) | Fonte secundária — somar com principal |

**Regra:** SOMAR Z-546 + Z-546.1. Nunca substituir uma pela outra.

### 2.2 Exportação PW (ProjectWise)

Arquivo CSV exportado diretamente do ProjectWise (sistema da CONSAG). Contém o histórico de GRDs aceitas (ciclos).

**Dois exports:**
- **UGH Trem 2** — documentos do Trem 2 principal
- **Trem 2 - ICs** — documentos de Itens de Contrato do Trem 2

### 2.3 LD (Lista de Documentos)

Arquivo Excel com extensão `.xlsx`. Cabeçalho na **linha 8**, dados a partir da **linha 9**.
Nome padrão: `PLDE179PLA340000001_AAAA.MM.DD_*.xlsx`

---

## 3. KPI 1 — HH Utilizado e Previsto por Disciplina

**Status:** Publicado · Base 18/08/2026 · Elaboração 21/08/2026

### 3.1 Definição

> **KPI 1** mede as horas utilizadas (HH real acumulado) e as horas previstas (HH estimado para concluir) por disciplina, com base na taxa histórica de HH por ciclo de aprovação (GRD).

**Fórmula principal:**
```
HH/ciclo = HH real acumulado (disciplina) ÷ nº de ciclos PW com DataAceiteGRD preenchida
HH Previsto = Docs pendentes (LD) × HH/ciclo
% Concluído = HH real ÷ (HH real + HH Previsto)
```

**HH/ciclo é uma média móvel:** recalculada a cada nova exportação do PW. Não é um valor fixo.

---

### 3.2 Mapeamento de Colunas — Planilha HH (Z-546 e Z-546.1)

> Índice 0-baseado. Separador de campo: tabulação ou vírgula dependendo da exportação.

| Índice | Campo | Tipo | Uso no KPI 1 |
|--------|-------|------|--------------|
| — | Nome da aba | Texto | Identifica a disciplina (ver De-Para HH→Sigla abaixo) |
| — | Linha de totais | Numérico | Soma de HH da disciplina naquele período |
| — | Período (mês/ano) | Data | Explosão mensal de HH para o gráfico de forecast |

**Nota:** A planilha HH não tem índice de coluna fixo universal — a disciplina é identificada pelo nome da **aba** (sheet). Cada aba = uma disciplina.

---

### 3.3 Mapeamento de Colunas — CSV PW (ProjectWise)

| Índice | Campo | Tipo | Uso no KPI 1 |
|--------|-------|------|--------------|
| [0] | CÓDIGO CONSAG | Texto | Identificação do documento. O 6º campo (split por `-`) = sigla da disciplina |
| [9] | ESCOPO | Texto | Regra de exclusão (ver 3.5) |
| [10] | ATIVIDADE | Texto | Regra de exclusão (ver 3.5) |
| [18] | BL 0 (Baseline 0) | Data | Data planejada fallback para Data Prevista |
| [20] | Reprogramada Trem 2-ICs | Data | Data Prevista (Trem 2-ICs) — prioridade 1 |
| [22] | Reprogramada UGH Trem 2 | Data | Data Prevista (UGH Trem 2) — prioridade 1 |
| DataAceiteGRD | DataAceiteGRD | Data | Define início de um ciclo. Preenchida = ciclo válido |

**Regra de Data Prevista:**
```python
# UGH Trem 2:
data_prevista = row[22] or row[18]   # reprogramada primeiro, BL0 como fallback

# Trem 2 - ICs:
data_prevista = row[20] or row[18]   # reprogramada primeiro, BL0 como fallback
```

**Regra de Sigla a partir do CÓDIGO CONSAG:**
```python
sigla = str(CODIGO_CONSAG).split('-')[5]
# Exemplo: "5290.00-22311-940-TUB-00123" → split('-')[5] = "TUB"
```

---

### 3.4 Mapeamento de Colunas — LD (Lista de Documentos)

| Índice | Campo | Descrição | Uso no KPI 1 |
|--------|-------|-----------|--------------|
| 0 | disc | Disciplina | Identificação da linha |
| 3 | num_doc | Número do documento | Identificação única |
| 4 | titulo | Título | Exibição |
| 5 | rev | Revisão (inteiro) | Controle de retrabalho |
| 11 | base_ult | Baseline última emissão (data) | Aderência ao baseline |
| 19 | peso | Peso ponderado | Avanço físico ponderado |
| 20 | avanco | Avanço % (0–100) | Avanço por disciplina |
| 21 | status_doc | Status no escopo: ATIVO ou EXCLUÍDO | Filtro de documentos ativos |
| 23 | status | Status de fluxo | Classificação de status (ver 3.5) |

**Docs Pendentes** usados no KPI 1:
= documentos com status_doc = **ATIVO** + status ≠ **DOC. FINALIZADO** + status ≠ **NÃO NECESSÁRIO**

---

### 3.5 Regras de Negócio

#### Regra 1 — Exclusão de documentos (operador AND obrigatório)

```python
# Um documento é EXCLUÍDO do KPI somente quando AMBAS as condições são verdadeiras:
excluido = (
    str(row[9]).strip().upper() == "EXCLUIR"   # col ESCOPO
    AND
    str(row[10]).strip().upper() == "EXCLUIR"  # col ATIVIDADE
)
```

> **ATENÇÃO:** O operador é AND, não OR. Se apenas uma coluna tiver "EXCLUIR", o documento NÃO é excluído.

#### Regra 2 — NÃO NECESSÁRIO é sempre excluído

```python
nao_necessario = str(row[23]).strip().upper() == "NÃO NECESSÁRIO"
# NÃO NECESSÁRIO = excluído do escopo ativo, independente de status_doc
```

#### Regra 3 — Classificação de status

| status (col 23) | Categoria KPI |
|-----------------|---------------|
| DOC. FINALIZADO | Finalizado |
| AGUARDANDO MARKUP | EM FLUXO — Em Processo |
| ATENDER MARKUP | EM FLUXO — Em Processo |
| PATEC EMITIDO | EM FLUXO — Em Processo |
| EMITIR EMISSÃO INICIAL | EM FLUXO — Não Iniciados |
| NÃO NECESSÁRIO | **Excluído** (mesmo que status_doc = ATIVO) |

#### Regra 4 — CDA = OVH (confirmado por Luiz Sobreira em 21/08/2026)

- **CDA** (Controle de Documentação e Acervo) → classificar como **OVH (Overhead)**
- **CDA ≠ CAE-CAD** — são atividades distintas
- **CAE-CAD = M3D** (modelagem 3D / COMOS) → **excluído** do KPI de produtividade

#### Regra 5 — MEC e MET são SEPARADOS

- **MEC** — Mecânica. HH na planilha Principal (Z-546).
- **MET** — Estrutura Metálica. HH na planilha DPC (Z-546.1).
- Nunca agrupar em pool. Confirmado por Luiz Sobreira em 21/08/2026.

#### Regra 6 — TEL é profissional externo

- **TEL** (Telecomunicações) = terceirizado. O HH representa apenas a **coordenação da equipe OTZ**.
- Taxa 0,63h/ciclo é correta — não investigar, não ajustar.

#### Regra 7 — CIV é provisório

- CIV entrou em 18/03/2026. Base de 18/08/2026: apenas 18 ciclos.
- Taxa de 172h/ciclo é **estatisticamente inválida** até atingir 50+ ciclos.
- Marcar sempre como "⚠ provisório" no slide.

#### Regra 8 — Premissa do Forecast

- **1 documento pendente (LD) = 1 ciclo futuro** (cenário conservador).
- O HH Previsto pode ser subestimado se houver retrabalho adicional (Rev 2+).

---

### 3.5-A Definição: Revisão × Emissão de Documentos

> Referências: Fluxograma de Aprovação de Documentos RNEST — Rev. 0 · MD-5290.00-22311-940-PEI-903 (MD-903, 14 pp) verificado em 23/08/2026

#### Definições para fins dos KPIs (fixadas em 20/08/2026 — Ilson dos Santos Azevedo)

| Termo KPI | O que significa | Campo no PW | Exemplos de código |
|-----------|-----------------|-------------|-------------------|
| **REVISÃO** | **Qualquer ciclo de trabalho** entregue à CONSAG e aceito pela OTZ. Toda linha com `DataAceiteGRD` preenchida é uma revisão — independente do sufixo. | `DataAceiteGRD` preenchida | `0_0`, `0_1`, `0_2`, `0`, `A_0`, `A_1`, `A`, `B_0`, `B`... |
| **EMISSÃO / DOCUMENTO** | Versão **formal aceita pela Petrobras**, registrada no SIGEM. Código **sem sufixo numérico** (`_N`) = entregável comercial final. | Código sem sufixo | `0`, `A`, `B`, `C`, `D`... |

**Regra operacional:**
```
REVISÃO  = toda linha do PW com DataAceiteGRD preenchida  (qualquer código)
EMISSÃO  = linhas cujo código de revisão NÃO tem sufixo _N  (0, A, B, C...)
```

#### O que cada sufixo representa no fluxo (Norma N-1710 / Fluxograma RNEST):

| Sufixo | Significado no fluxo | Fase | É Revisão (KPI)? | É Emissão (KPI)? |
|--------|---------------------|------|-----------------|-----------------|
| `_0` | Início de ciclo — OTZ envia documento à CONSAG para análise interna | OTZ → CONSAG | **Sim** | Não |
| `_1`, `_2`... | Ajuste interno — OTZ reemite após markup CONSAG (CONSAG não repassa à Petrobras) | OTZ → CONSAG | **Sim** | Não |
| sem sufixo (`0`, `A`, `B`...) | Emissão formal — CONSAG aprova e encaminha à Petrobras (registrado no SIGEM) | CONSAG → Petrobras | **Sim** | **Sim** |

> **Conclusão:** toda Emissão é também uma Revisão (tem DataAceiteGRD). Mas nem toda Revisão é uma Emissão (os ciclos `_0` e `_1+` não chegam à Petrobras).

#### Verificação de coerência com o MD-903

O MD-903 (item 7.4) exige que *"as modificações e alterações de projeto sejam precedidas da emissão das revisões dos documentos originais pertinentes, respeitando o sequencial de revisão"*. A PPU do contrato tem linhas separadas para **revisão** (modificação de documento existente) e **emissão** (documento novo/formal), o que valida a distinção acima.

As definições de KPI são coerentes com o MD-903 — operam no nível rastreável dos dados (campo `DataAceiteGRD` do PW) e respeitam a hierarquia: ciclos internos (OTZ×CONSAG) → emissão formal (CONSAG→Petrobras).

> **Atenção:** Isométricos (MET) têm convenção de numeração própria e devem ser verificados individualmente antes de aplicar o padrão `_0`/`_1`.

---

### 3.5-B Metodologia de Duração de Ciclo (preparada para quando o PW CSV estiver disponível)

#### Definição

**Duração de ciclo** = intervalo entre dois eventos consecutivos de `DataAceiteGRD` para o mesmo documento. Mede quanto tempo OTZ levou para responder a cada GRD recebida.

#### Fórmula

```
Duração ciclo N = DataAceiteGRD(revisão N) − DataAceiteGRD(revisão N−1)

Exemplo:
  Duração ciclo 0_1 = DataAceiteGRD(0_1) − DataAceiteGRD(0_0)
  Duração ciclo A_0 = DataAceiteGRD(A_0) − DataAceiteGRD(0)
  Duração ciclo A_1 = DataAceiteGRD(A_1) − DataAceiteGRD(A_0)
```

#### Regra do Primeiro Ciclo — Proxy pelo Máximo

O ciclo `0_0` (primeira emissão) não tem `DataAceiteGRD` anterior — o documento nasceu sem GRD prévia. Portanto:

```
Duração estimada do ciclo 0_0 = max(durações de todos os ciclos conhecidos do mesmo documento)
```

> **Justificativa:** É a estimativa conservadora — assume que o primeiro ciclo demorou pelo menos tanto quanto o pior ciclo observado no mesmo documento. Documentar sempre como estimativa, não como valor medido.

#### O que a metodologia habilita (quando PW CSV disponível):

| Análise | Como calcular |
|---|---|
| Tempo médio de resposta por disciplina | Média das durações de todos os ciclos da disciplina |
| Documentos com ciclos mais longos | Ordenar por max(duração) por documento |
| Tendência temporal | Comparar durações médias por mês de aceitação |
| Ciclos de retrabalho vs. primeiros ciclos | Comparar duração de `_0` vs `_1+` |
| Evolução por letra (0→A→B→C) | A cada ciclo Petrobras o tempo aumenta ou diminui? |

#### Exceções e cuidados:

- **Isométricos (MET):** convenção diferente — verificar antes de aplicar
- **Duração negativa:** indica erro nos dados de DataAceiteGRD — excluir e investigar
- **Duração > 90 dias:** sinalizar como outlier antes de incluir na média

---

### 3.6 De-Para: Aba da Planilha HH → Sigla Canônica

| Nome na planilha HH | Sigla KPI |
|---------------------|-----------|
| TUBULAÇÃO | TUB |
| ELÉTRICA / ELETRICA | ELE |
| PROCESSO | PRO |
| INSTRUMENTAÇÃO / Instr&Aut | INS |
| MECÂNICA / MECANICA | MEC |
| EST. METÁLICA / METALURGIA | MET |
| SEGURANÇA / SAFETY | SAF |
| CIVIL | CIV |
| ARQUITETURA | ARQ |
| TELECOMUNICAÇÕES / TELECOM | TEL |
| QUALIDADE | QUA |
| OVERHEAD / GERAL / GESTÃO / CDA / PLANEJAMENTO | OVH |
| CAE-CAD / COMOS / MODELO 3D | M3D |

---

### 3.7 De-Para: Sigla no PW → Sigla Canônica

| Sigla no PW (campo 6 do CÓDIGO CONSAG) | Sigla KPI |
|----------------------------------------|-----------|
| TUB | TUB |
| ELE | ELE |
| PRO | PRO |
| INS | INS |
| MEC | MEC |
| MET | MET |
| SAF / SAFETY | SAF |
| CIV | CIV |
| ARQ | ARQ |
| TEL | TEL |
| TELECOMUNICAÇÕES | TEL |
| INSTRUMENTAÇÃO | INS |

---

### 3.8 Valores de HH/ciclo — Base 18/08/2026

| Disciplina | Sigla | HH Real | Ciclos PW | HH/ciclo | Categoria | Observação |
|------------|-------|---------|-----------|----------|-----------|------------|
| Tubulação | TUB | 2.861h | 597 | 4,79h | Forecast | Maior base — taxa sólida |
| Elétrica | ELE | 2.482h | 100 | 24,83h | Forecast | Boa amostra |
| Processo | PRO | 3.281h | 138 | 23,77h | Forecast | 82,6% concluído |
| Instrumentação | INS | 2.595h | 103 | 25,19h | Forecast | Taxa mais alta |
| Mecânica | MEC | 2.940h | 218 | 13,49h | Forecast | Separado de MET |
| Est. Metálica | MET | 390h | 388 | 1,01h | Forecast | DPC. Sem pendentes → ~100% |
| Segurança | SAF | 1.193h | 148 | 8,08h | Forecast | SAF no PW = SEGURANÇA no HH |
| Civil | CIV | 3.096h | 18 | 172h ⚠ | Provisório | Apenas 18 ciclos — inválido |
| Arquitetura | ARQ | 284h | 0 | N/A | N/A | 1 doc RM bloqueado |
| Telecom | TEL | 36h | 57 | 0,63h | Externo | Só coordenação OTZ |
| Qualidade | QUA | 1.259h | — | — | Custo | Sem forecast de GRD |
| Overhead | OVH | 11.492h | — | — | Overhead | Inclui CDA |
| Modelo 3D | M3D | 3.225h | — | — | Excluído | CAE-CAD/COMOS |

---

### 3.9 Totais do KPI 1 — Base 18/08/2026

| Métrica | Valor | Como calculado |
|---------|-------|----------------|
| HH Realizado (forecast) | 19.158h | Soma das 10 disciplinas com linha no ranking |
| HH Escopo estimado | ~40.175h | HH real (19.158) + HH previsto todas disciplinas (21.017) |
| Ciclos PW (GRD aceita) | 1.767 | Soma de todos os ciclos válidos no PW |
| HH Total (geral) | 34.874h | Valor direto da planilha bruta (inclui ~260h sem categ.) |
| Docs Pendentes (LD) | 3.024 | Ativos, não finalizados, não NÃO NECESSÁRIO |
| Docs Formalizados | 1.353 | DOC. FINALIZADO na LD |

---

### 3.10 Referência de Consistência (histórico)

| Data base | Total LD | Ativos LD | Excluídos | Finalizados | Avanço |
|-----------|----------|-----------|-----------|-------------|--------|
| 30/06/2026 | 524 | 419 | 105 | 353 | 94,22% |
| 07/07/2026 | 524 | 419 | 105 | 358 | 94,46% |

> Se Excluídos ≠ 105 ou Total ≠ 524, verificar a Regra NÃO NECESSÁRIO antes de publicar.

---

## 4. KPIs Futuros — Estrutura reservada

| KPI | Título | Status |
|-----|--------|--------|
| KPI 1 | HH Utilizado e Previsto por Disciplina | ✅ Publicado |
| KPI 2 | Duração de Ciclo por Disciplina / Documento | 🔲 Aguardando PW CSV |
| KPI 3 | Headcount por Disciplina (Realizado e Previsto) | 🔲 Aguardando Z-546 completa |
| KPI 4 | (a definir) | 🔲 Planejado |

> À medida que novos KPIs forem criados, adicionar uma seção `## N. KPI N — Título` seguindo a mesma estrutura do KPI 1: definição, fontes, colunas, regras, de-para, valores base, totais.

---

## 5. Controle de Versões

| Versão | Data | Alteração | Responsável |
|--------|------|-----------|-------------|
| 1.0 | 21/08/2026 | Criação do documento. KPI 1 completo com todas as regras, colunas, de-para e valores base 18/08/2026. | Ilson / Claude |
| 1.1 | 23/08/2026 | Adicionadas seções 3.5-A (Revisão × Emissão) e 3.5-B (Metodologia de Duração de Ciclo com proxy do primeiro ciclo). KPI 2 e KPI 3 registrados como planejados. | Ilson / Claude |
| 1.2 | 23/08/2026 | Correção da seção 3.5-A: redefinição correta de REVISÃO (= todo ciclo DataAceiteGRD) e EMISSÃO/DOCUMENTO (= código sem sufixo, aceito pela Petrobras). Verificação de coerência com MD-903 e PPU do contrato realizada e documentada. | Ilson / Claude |

---

*Documento interno OTZ Engenharia — uso restrito à equipe GPLAN.*
*Não compartilhar com CONSAG ou terceiros sem aprovação do Supervisor de Planejamento.*
