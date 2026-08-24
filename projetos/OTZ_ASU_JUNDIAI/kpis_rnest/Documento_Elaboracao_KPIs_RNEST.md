# Documento de Elaboração de KPIs — RNEST Z-546 Lote D
**OTZ Engenharia · Supervisão GPLAN: Ilson dos Santos Azevedo**
Versão 2.0 · Agosto 2026

---

> **Como usar este documento**
> Este procedimento foi escrito para que **qualquer pessoa — inclusive sem experiência prévia no projeto** — consiga entender de onde vem cada número, cada variável e cada planilha que alimenta os KPIs. Um outro analista, um novo colaborador ou outro sistema de IA deve conseguir reproduzir os cálculos do zero lendo apenas este documento.
>
> Siga a ordem das seções. Cada seção depende das anteriores.

---

## 1. Propósito e Governança

Este documento registra **como cada KPI é construído**: quais planilhas alimentam, quais colunas são lidas, quais regras de negócio se aplicam, e qual é a lógica de cálculo. Deve ser atualizado a cada novo KPI criado ou a cada mudança de regra aprovada.

**Regra de Ouro do projeto:** OTZ **nunca** se comunica diretamente com Petrobras. Toda comunicação passa pela CONSAG via GRD. Os dados que alimentam os KPIs refletem exatamente essa cadeia.

| Campo | Valor |
|-------|-------|
| Responsável pela atualização | Supervisor GPLAN — Ilson dos Santos Azevedo |
| Branch Git | `claude/onedrive-access-permissions-WeExM` |
| Repositório | `ilson-engenharia/meu-planejamento` |
| Contrato | Z-546 · Lote D · RNEST (Refinaria Abreu e Lima) |
| Subcontratada | OTZ Engenharia |
| Contratante principal | CONSAG |
| Cliente final | Petrobras |

---

## 2. Definições Essenciais

> Leia esta seção antes de qualquer outra. Os termos aqui definidos são usados em todo o documento.

### 2.1 O que é HH (Homem-Hora)?

HH = quantidade de horas trabalhadas por um profissional em uma atividade. Se 2 pessoas trabalham 4 horas, o total é 8 HH.

No projeto, HH é registrado por **disciplina** (ex.: Tubulação, Elétrica). **Não existe registro de HH por documento individual** — isso é uma limitação do sistema atual.

### 2.2 O que é um Documento de Engenharia?

É qualquer arquivo técnico produzido pela OTZ: Isométrico (IS), Desenho (DE), Especificação Técnica (ET), Folha de Dados (FD), Requisição de Materiais (RM), Memória de Cálculo (MC), etc. Cada tipo tem um código de prefixo padronizado pela Norma Petrobras N-1710.

### 2.3 O que é um Ciclo (GRD)?

Um **ciclo** é uma passagem completa de um documento pelo fluxo de aprovação. Começa quando a OTZ entrega o documento à CONSAG e termina quando a CONSAG registra a aceitação no sistema (campo `DataAceiteGRD` preenchido no ProjectWise).

**Um documento pode ter muitos ciclos** — toda vez que há um ajuste ou uma nova revisão, um novo ciclo é aberto.

### 2.4 O que é GRD?

GRD = Gerenciamento de Revisão de Documentos. É o processo formal pelo qual os documentos circulam entre OTZ → CONSAG → Petrobras. Cada GRD aceita = 1 ciclo.

### 2.5 O que é o ProjectWise (PW)?

Sistema de gerenciamento de documentos da CONSAG (software Bentley). É onde todos os documentos e seus históricos de aprovação ficam registrados. A OTZ acessa via exportação CSV.

### 2.6 O que é a LD (Lista de Documentos)?

Planilha Excel mantida pela OTZ com o status de cada documento do projeto: se está ativo, em qual fase, qual o avanço percentual, etc.

### 2.7 Tipos de documento: Tipo A vs Tipo B

| Tipo | O que é | Quem elabora | Fluxo |
|------|---------|--------------|-------|
| **Tipo A** | Documento de projeto (Engenharia) | OTZ | OTZ elabora → CONSAG revisa → Petrobras aprova |
| **Tipo B** | Documento de fornecedor (ADF) | Fornecedor externo | OTZ apenas coordena e analisa |

> **Atenção:** Tipo A e Tipo B têm HH, fluxos e taxas completamente diferentes. **Nunca misturar** no mesmo cálculo de taxa.

### 2.8 O que é uma Taxa (HH/ciclo)?

Taxa = quantidade média de horas necessárias para completar um ciclo de aprovação.

```
Taxa (HH/ciclo) = HH total gasto (disciplina) ÷ nº de ciclos concluídos (disciplina)
```

Esta taxa é usada para **prever o HH futuro**: se ainda restam 100 ciclos e a taxa é 5h/ciclo, o HH futuro previsto é 500h.

### 2.9 O que é EWMA?

EWMA = Exponentially Weighted Moving Average (Média Móvel Exponencialmente Ponderada).

Em vez de uma média simples dos últimos N meses, o EWMA dá **mais peso para os meses recentes** e menos para os mais antigos. O peso decai ~21% a cada mês passado.

**Por que usar EWMA e não média simples?**
- A produtividade da equipe muda ao longo do tempo (curva de aprendizado)
- A taxa caiu de ~68 h/ciclo (início do projeto) para ~18 h/ciclo (julho/2026)
- Usar a média acumulada total subestimaria a produtividade real atual em ~2×
- EWMA com meia-vida de 3 meses captura o nível atual sem descartar o histórico

---

## 3. Fontes de Dados

São três fontes. Todas devem ser atualizadas na mesma data de referência.

### 3.1 Planilhas de HH (Homem-Hora)

| ID | Nome | Escopo | Disciplinas |
|----|------|--------|-------------|
| **Z-546** | Planilha Principal | Lote D | TUB, ELE, PRO, INS, MEC, SAF, ARQ, QUA, OVH |
| **Z-546.1** | Planilha DPC | Lote D | EST, CIV, TEL, M3D (somente CAE-CAD — CDA é OVH, não M3D) |

**Regra fundamental:** SOMAR Z-546 + Z-546.1. Nunca usar uma sem a outra.

**Como obter:** Acessar o sistema interno da OTZ. Cada aba da planilha = uma disciplina.

**O que extrair:** Totais de HH por disciplina por mês/período.

**Limitação crítica:** O HH está disponível apenas no nível de **disciplina**. Não é possível saber quantas horas foram gastas em cada documento individual.

### 3.2 Exportação PW (ProjectWise)

**O que é:** Arquivo CSV exportado diretamente do sistema da CONSAG. Contém o histórico completo de todos os ciclos de aprovação (GRDs) do projeto.

**Como obter:** Solicitar exportação ao gestor do PW na CONSAG, ou exportar diretamente se tiver acesso.

**Dois arquivos distintos:**

| Export | O que contém |
|--------|--------------|
| **UGH Trem 2** | Documentos do Trem 2 principal (UGH U-36) |
| **Trem 2 - ICs** | Documentos de Itens de Contrato do Trem 2 |

**Regra:** Sempre usar os dois exports combinados. Nunca um sem o outro.

**Tamanho de referência:** Base 18/08/2026 = 18.198 linhas, 70 colunas.

### 3.3 LD — Lista de Documentos

**O que é:** Planilha Excel da OTZ com status de cada documento do projeto.

**Formato do arquivo:**
- Extensão: `.xlsx`
- Cabeçalho: **linha 8**
- Dados: a partir da **linha 9**
- Aba de dados: `LD`

**Nome padrão do arquivo:**
```
PLDE179PLA340000001_AAAA.MM.DD_*.xlsx
```

**Como obter:** Gerada internamente pela equipe GPLAN da OTZ.

---

## 4. KPI 1 — HH Utilizado e Previsto por Disciplina

**Status:** Publicado · Base 18/08/2026 · Elaboração agosto/2026

---

### 4.1 O que este KPI mede

O KPI 1 responde a duas perguntas:

1. **Quantas horas a OTZ já gastou** em cada disciplina até hoje?
2. **Quantas horas ainda vai gastar** para concluir os documentos restantes?

Com isso, calculamos:
- O **% de conclusão** de cada disciplina (em HH)
- O **HH total estimado** do projeto (realizado + previsto)
- O **forecast de HH por mês** para os meses seguintes

---

### 4.2 O fluxo de aprovação (de onde vêm os ciclos)

```
OTZ elabora documento
        ↓
OTZ entrega à CONSAG via GRD  ← código: 0_0 (primeira entrega)
        ↓
CONSAG analisa internamente
        ↓
[Se comentários internos]
        → OTZ ajusta e reentrega  ← código: 0_1, 0_2... (ajustes)
[Se ok internamente]
        ↓
CONSAG encaminha à Petrobras  ← código: 0 (sem sufixo = emissão formal)
        ↓
[Se Petrobras comenta]
        → OTZ revisa para nova rodada  ← código: A_0, A_1... → A
[Se Petrobras aprova]
        ↓
DOC. FINALIZADO
```

**DataAceiteGRD preenchida** = OTZ entregou e a CONSAG registrou a aceitação = **1 ciclo concluído**.

---

### 4.3 Passo a Passo — Como Calcular o KPI 1

#### PASSO 1 — Abrir e consolidar as planilhas de HH

1. Abrir Z-546 (planilha principal)
2. Para cada aba (= cada disciplina), anotar o total de HH acumulado
3. Abrir Z-546.1 (planilha DPC)
4. Para as disciplinas MET, CIV, TEL, M3D: anotar o total de HH acumulado
5. **Somar** os valores das duas planilhas quando a disciplina aparecer nas duas

#### PASSO 2 — Abrir e processar o CSV do PW

1. Abrir os dois CSVs (UGH Trem 2 + Trem 2-ICs)
2. Para cada linha: verificar se `DataAceiteGRD` está preenchida
3. Se preenchida → é um ciclo válido
4. Aplicar regras de exclusão (ver 4.7)
5. Extrair a sigla da disciplina do campo `CÓDIGO CONSAG` (ver 4.5)
6. Contar ciclos válidos por disciplina e por mês

#### PASSO 3 — Calcular a Taxa EWMA

Para cada disciplina, calcular a taxa EWMA com meia-vida de 3 meses (ver 4.9 para o procedimento completo).

#### PASSO 4 — Abrir e processar a LD

1. Abrir a planilha LD (aba `LD`, cabeçalho linha 8, dados linha 9+)
2. Filtrar documentos pendentes (ver 4.6 — regra de docs pendentes)
3. Contar documentos pendentes por disciplina

#### PASSO 5 — Calcular HH Previsto e % Concluído

```
HH Previsto (disciplina) = Docs Pendentes × Taxa EWMA (disciplina)
% Concluído (central)   = HH Real ÷ (HH Real + HH Previsto com EWMA)
% Concluído (piso)      = HH Real ÷ (HH Real + HH Previsto com taxa acumulada)
```

Publicar o `% Concluído` como faixa: **[piso% — central%]**

---

### 4.4 Mapeamento de Colunas — Planilha HH (Z-546 e Z-546.1)

> A planilha HH não tem índice de coluna fixo universal. A disciplina é identificada pelo **nome da aba** (sheet). Cada aba = uma disciplina.

| O que ler | Onde está | O que extrair |
|-----------|-----------|---------------|
| Nome da aba | Tab da planilha Excel | Identifica a disciplina (ver De-Para seção 4.14) |
| Linha de totais | Última linha de dados da aba | Total de HH da disciplina no período |
| Período (mês/ano) | Colunas de cabeçalho | Explosão mensal para o gráfico de taxa |

**Regra:** Somar todos os períodos para obter o HH **acumulado** de cada disciplina.

---

### 4.5 Mapeamento de Colunas — CSV PW (ProjectWise)

> Índice 0-baseado. As colunas podem variar entre exports — sempre verificar o cabeçalho real antes de indexar.

| Índice | Nome da Coluna | Tipo | Para que serve |
|--------|---------------|------|----------------|
| [0] | CÓDIGO CONSAG | Texto | Identificação do documento. O 6º campo (split por `-`) = sigla da disciplina |
| [9] | ESCOPO | Texto | Regra de exclusão (ver 4.7 — Regra 1) |
| [10] | ATIVIDADE | Texto | Regra de exclusão (ver 4.7 — Regra 1) |
| [18] | BL 0 (Baseline 0) | Data | Data planejada — fallback para Data Prevista quando reprogramada está vazia |
| [20] | Reprogramada Trem 2-ICs | Data | Data Prevista para ICs — usar em primeiro lugar |
| [22] | Reprogramada UGH Trem 2 | Data | Data Prevista para UGH — usar em primeiro lugar |
| — | DataAceiteGRD | Data | **Campo principal.** Preenchida = 1 ciclo válido concluído |
| — | TipoDocumento | Texto | Tipo A (projeto) ou Tipo B (fornecedor) |
| — | fornecimento | Texto | Campo auxiliar para distinguir Tipo A/B |

**Como extrair a sigla da disciplina do CÓDIGO CONSAG:**

```python
sigla = str(CODIGO_CONSAG).split('-')[5]
# Exemplo: "5290.00-22311-940-TUB-00123-DE" → split('-')[5] = "TUB"
```

**Regra de Data Prevista:**

```python
# Export UGH Trem 2:
data_prevista = row[22] or row[18]   # reprogramada primeiro, BL0 como fallback

# Export Trem 2 - ICs:
data_prevista = row[20] or row[18]   # reprogramada primeiro, BL0 como fallback
```

---

### 4.6 Mapeamento de Colunas — LD (Lista de Documentos)

> Índice 0-baseado. Cabeçalho na linha 8. Dados a partir da linha 9.

| Índice | Campo | Descrição | Para que serve |
|--------|-------|-----------|----------------|
| 0 | disc | Disciplina | Identificação da linha |
| 3 | num_doc | Número do documento | Identificação única (pode ser cruzado com PW no futuro) |
| 4 | titulo | Título do documento | Exibição |
| 5 | rev | Revisão (número inteiro) | Controle de retrabalho |
| 11 | base_ult | Baseline última emissão | Aderência ao baseline |
| 19 | peso | Peso ponderado | Avanço físico ponderado |
| 20 | avanco | Avanço % (0–100) | Avanço por disciplina |
| 21 | status_doc | Status no escopo | `ATIVO` ou `EXCLUÍDO` |
| 23 | status | Status de fluxo | Classificação de status (ver 4.7 — Regra 3) |

**Definição de Documentos Pendentes** (usados para calcular HH Previsto):

```
Docs Pendentes = linhas onde:
  status_doc = "ATIVO"
  E status ≠ "DOC. FINALIZADO"
  E status ≠ "NÃO NECESSÁRIO"
```

---

### 4.7 Regras de Negócio

#### Regra 1 — Exclusão de documentos do PW (operador AND obrigatório)

```python
# Um documento é EXCLUÍDO do KPI somente quando AMBAS as condições forem verdadeiras:
excluido = (
    str(row[9]).strip().upper() == "EXCLUIR"    # coluna ESCOPO
    AND
    str(row[10]).strip().upper() == "EXCLUIR"   # coluna ATIVIDADE
)
```

> **ATENÇÃO:** O operador é `AND`, não `OR`. Se apenas UMA coluna tiver "EXCLUIR", o documento **NÃO** é excluído.

#### Regra 2 — NÃO NECESSÁRIO é sempre excluído

```python
nao_necessario = str(row[23]).strip().upper() == "NÃO NECESSÁRIO"
# Excluído do escopo ativo, independente do valor de status_doc
```

#### Regra 3 — Classificação de status

| Valor do campo `status` (col 23) | Categoria KPI |
|----------------------------------|---------------|
| `DOC. FINALIZADO` | Finalizado |
| `AGUARDANDO MARKUP` | EM FLUXO — Em Processo |
| `ATENDER MARKUP` | EM FLUXO — Em Processo |
| `PATEC EMITIDO` | EM FLUXO — Em Processo |
| `EMITIR EMISSÃO INICIAL` | EM FLUXO — Não Iniciados |
| `NÃO NECESSÁRIO` | **Excluído** (mesmo que status_doc = ATIVO) |

#### Regra 4 — CDA = OVH (confirmado por Luiz Sobreira, 21/08/2026)

- **CDA** (Controle de Documentação e Acervo) → classificar como **OVH (Overhead)**
- **CDA ≠ CAE-CAD** — são atividades completamente distintas
- **CAE-CAD = M3D** (modelagem 3D / COMOS) → **excluído** do KPI de produtividade

#### Regra 5 — MEC e EST são SEPARADOS (confirmado por Luiz Sobreira, 21/08/2026)

- **MEC** — Mecânica. HH na planilha **Principal (Z-546)**.
- **EST** — Estrutura Metálica. HH na planilha **DPC (Z-546.1)**.
- Nunca agrupar em pool. São disciplinas distintas com taxas distintas.

#### Regra 6 — TEL é profissional externo

- **TEL** (Telecomunicações) = terceirizado.
- O HH de TEL representa apenas a **coordenação interna da OTZ**, não a execução.
- Taxa 0,63 h/ciclo é correta — não investigar, não ajustar.
- TEL **não entra** na base de cálculo de produtividade geral.

#### Regra 7 — CIV é provisório

- CIV entrou no projeto em 18/03/2026. Base de 18/08/2026: apenas **18 ciclos**.
- Taxa de 172 h/ciclo é **estatisticamente inválida** (mínimo: 30 ciclos; ideal: 50+).
- Marcar sempre como "⚠ provisório" no slide e no relatório.
- Substituir pela taxa análoga de disciplina similar até atingir 30 ciclos.

#### Regra 8 — Premissa do Forecast

- **1 documento pendente (LD) = 1 ciclo futuro** (cenário conservador).
- O HH Previsto pode ser subestimado se houver retrabalho adicional (Rev 2+).
- Documentar sempre como premissa, não como fato.

#### Regra 9 — Tipo A e Tipo B nunca se misturam

- Calcular taxas, forecasts e análises **separadamente** para Tipo A e Tipo B.
- Tipo B: HH = coordenação OTZ apenas (muito menor que Tipo A).

#### Regra 10 — Razão de Somas (nunca média de razões)

```python
# CORRETO — razão de somas:
taxa = sum(HH_por_mes) / sum(ciclos_por_mes)

# ERRADO — média de razões (distorce quando n é pequeno em algum mês):
taxa = mean([HH_mes / ciclos_mes for cada mes])
```

---

### 4.8 Definição: Revisão × Emissão de Documentos

> Verificado contra MD-903 (item 7.4) e PPU do contrato em 23/08/2026.

| Termo KPI | O que significa | Campo no PW | Exemplos de código |
|-----------|----------------|-------------|-------------------|
| **REVISÃO** | Qualquer ciclo de trabalho com `DataAceiteGRD` preenchida. Todo evento no PW é uma revisão, independente do sufixo. | `DataAceiteGRD` preenchida | `0_0`, `0_1`, `0`, `A_0`, `A_1`, `A`, `B`... |
| **EMISSÃO / DOCUMENTO** | Versão formal aceita pela Petrobras, registrada no SIGEM. Código **sem** sufixo `_N`. | Código sem sufixo | `0`, `A`, `B`, `C`... |

**O que cada sufixo representa:**

| Sufixo | Significado | Fase | Revisão (KPI)? | Emissão (KPI)? |
|--------|-------------|------|:-:|:-:|
| `_0` | Início de ciclo — OTZ entrega à CONSAG para análise interna | OTZ → CONSAG | Sim | Não |
| `_1`, `_2`... | Ajuste interno — OTZ reemite após markup CONSAG | OTZ → CONSAG | Sim | Não |
| sem sufixo (`0`, `A`, `B`...) | Emissão formal — CONSAG encaminha à Petrobras (SIGEM) | CONSAG → Petrobras | Sim | Sim |

> **Conclusão:** toda Emissão é também uma Revisão. Mas nem toda Revisão é uma Emissão.

> **Exceção:** Isométricos (MET) têm convenção de numeração própria — verificar individualmente.

---

### 4.9 Taxa EWMA — Metodologia de Cálculo

#### Por que EWMA e não média acumulada?

A produtividade da equipe evolui ao longo do projeto. No início, os ciclos eram mais lentos (equipe aprendendo, processos sendo definidos). Com o tempo, a taxa caiu significativamente. A taxa acumulada total reflete esse passado mais lento e **superestima o HH futuro em ~2×**.

O EWMA com meia-vida de 3 meses dá peso maior ao presente e menor ao passado, capturando a produtividade real atual sem desperdiçar o histórico.

#### Parâmetro EWMA

- **Meia-vida:** 3 meses
- **Fator de decaimento mensal (λ):** `λ = 0,5^(1/3) ≈ 0,794`
- Isso significa: o mês anterior vale 79,4% do atual; 2 meses atrás valem 63,0%; 3 meses atrás valem 50%; e assim por diante.

#### Fórmula EWMA — passo a passo

```
Dados mensais (do mês mais recente para o mais antigo):
  Mês t=0 (atual):    HH₀ ciclos, N₀ ciclos
  Mês t=1 (anterior): HH₁ ciclos, N₁ ciclos
  Mês t=2:            HH₂ ciclos, N₂ ciclos
  ...

Peso de cada mês:
  peso(t) = λ^t  onde λ = 0,794

Taxa EWMA = Σ [peso(t) × HH(t)] / Σ [peso(t) × N(t)]
```

#### Exemplo numérico (TUB, dados fictícios para ilustração):

| Mês | HH | Ciclos | Peso (λ^t) | HH × peso | Ciclos × peso |
|-----|-----|--------|-----------|-----------|---------------|
| ago/26 (t=0) | 480 | 42 | 1,000 | 480,0 | 42,0 |
| jul/26 (t=1) | 380 | 35 | 0,794 | 301,7 | 27,8 |
| jun/26 (t=2) | 420 | 39 | 0,630 | 264,6 | 24,6 |
| mai/26 (t=3) | 350 | 31 | 0,500 | 175,0 | 15,5 |
| **Soma** | | | | **1.221,3** | **109,9** |

```
Taxa EWMA (TUB) = 1.221,3 ÷ 109,9 = 11,11 h/ciclo
```

#### Janela mínima por disciplina

| Disciplina | Ciclos/mês (aprox.) | Janela mínima para n≥30 |
|------------|--------------------|-----------------------|
| TUB | ~35 | 1–2 meses |
| MEC | ~18 | 2–3 meses |
| ELE, INS, PRO, SAF | 5–9 | 5–6 meses |
| MET | ~32 | 1–2 meses |
| CIV | <3 | ⚠ provisório — usar proxy |
| TEL | variável | externo — não usar |

> **Regra:** Nunca publicar uma taxa com menos de 10 ciclos na janela. Menos de 10 → herdar do nível acima. Menos de 30 → sinalizar como provisório.

---

### 4.10 Fórmulas Completas do KPI 1

```
─────────────────────────────────────────────────────────────────
ENTRADAS:
  HH_real(d)     = HH acumulado da disciplina d (planilha Z-546/Z-546.1)
  N_ciclos(d,t)  = nº de ciclos válidos da disciplina d no mês t (PW CSV)
  Docs_pend(d)   = documentos pendentes da disciplina d (LD)

─────────────────────────────────────────────────────────────────
TAXA EWMA (disciplina d):
  peso(t) = 0,794^t   (t = meses atrás; t=0 = mês atual)
  Taxa_EWMA(d) = Σ[peso(t) × HH(d,t)] / Σ[peso(t) × N_ciclos(d,t)]

TAXA ACUMULADA (disciplina d):
  Taxa_acum(d) = HH_real(d) / N_ciclos_total(d)

─────────────────────────────────────────────────────────────────
HH PREVISTO:
  HH_prev_EWMA(d) = Docs_pend(d) × Taxa_EWMA(d)
  HH_prev_acum(d) = Docs_pend(d) × Taxa_acum(d)

─────────────────────────────────────────────────────────────────
% CONCLUÍDO (publicar como faixa):
  % central (EWMA)  = HH_real(d) / [HH_real(d) + HH_prev_EWMA(d)]
  % piso (acumulado)= HH_real(d) / [HH_real(d) + HH_prev_acum(d)]

  Publicar: "X% – Y%"  (piso – central)

─────────────────────────────────────────────────────────────────
HH TOTAL ESTIMADO:
  HH_total(d) = HH_real(d) + HH_prev_EWMA(d)

─────────────────────────────────────────────────────────────────
```

---

### 4.11 Pesos por Tipo de Documento e Severidade

#### Para que servem os pesos?

Como o HH só existe no nível disciplina (não por documento), os pesos permitem calcular **ciclos equivalentes** — ajustando o peso de cada documento pendente conforme sua complexidade esperada.

**Pesos de severidade** (do MD-903 §7.10 — contrato Petrobras):

| Severidade | Descrição | Peso |
|------------|-----------|------|
| NOVO | Documento criado do zero pela OTZ | 1,00 |
| ALTO | 60–100% de modificações | 0,80 |
| MÉDIO | 30–60% de modificações | 0,45 |
| BAIXO | Até 30% de modificações | 0,15 |

> **Atenção:** A coluna SEVERIDADE na LD está atualmente **vazia (100% sem preenchimento)**.
> Usar os pesos abaixo por tipo de documento (derivados do MD-903 §7.11) como proxy:

| Prefixo (N-1710) | Tipo de documento | Peso estimado |
|---|---|---|
| IS | Isométrico | 0,19 |
| DE | Desenho | 0,36 |
| FD | Folha de Dados | 0,54 |
| ET | Especificação Técnica | 0,60 |
| MC | Memória de Cálculo | 0,55 |
| RM | Requisição de Materiais | 0,40 |
| LI | Lista | 0,35 |
| RL | Relatório | 0,45 |
| LD | Lista de Documentos | 0,30 |
| PT | Parecer Técnico | 0,50 |
| MD | Memorial Descritivo | 0,60 |

> Estes pesos são proxy do MD-903 e devem ser **calibrados com dados reais** quando houver histórico suficiente por tipo de documento.

---

### 4.12 Hierarquia de Fallback (quando não há dados suficientes)

Quando uma célula de taxa não tem dados históricos suficientes, usar a seguinte cascata:

```
1. Disciplina × Tipo de Documento × Etapa (_0/_1+/sem sufixo)
   n ≥ 30 ciclos → usar taxa própria
   10 ≤ n < 30  → mistura com nível acima (credibilidade parcial)
   n < 10       → descer para nível 2

2. Disciplina × Tipo de Documento
   Mesmas regras de n acima

3. Disciplina (nível atual do KPI 1)
   Mesmas regras de n acima

4. Global (média de todas as disciplinas)
   Usar somente como último recurso

5. Proxy pelo máximo (fator de segurança)
   = max(taxas conhecidas para aquela dimensão)
   Usar quando não há nenhum dado histórico
   Documentar sempre como estimativa conservadora
```

---

### 4.13 Gráficos do KPI 1

#### Gráfico A — Evolução da Taxa (HH/ciclo ao longo do tempo)

**O que mostra:** Como a produtividade da equipe evoluiu mês a mês. Revela a curva de aprendizado — se a equipe está ficando mais rápida ou mais lenta.

| Eixo | O que colocar |
|------|---------------|
| X | Meses (formato MM/AAAA) |
| Y | HH/ciclo = HH_mês ÷ ciclos_mês |
| Linhas | Uma por disciplina |
| Overlay | Linha EWMA de cada disciplina |
| Barras de fundo | nº de ciclos do mês (n baixo = ponto ruidoso) |

**O que consegue revelar que outros gráficos não conseguem:**
- Se a queda de taxa é aprendizado permanente ou mudança de mix de documentos
- Qual disciplina está ficando mais lenta (precisa de atenção)
- Se a EWMA está convergindo (estabilidade) ou ainda descendo (aprendizado ativo)

#### Gráfico B — Mix de Tipo de Ciclo (retrabalho)

**O que mostra:** Qual proporção dos ciclos de cada mês foi `_0` (primeira entrega), `_1+` (retrabalho CONSAG) ou sem sufixo (emissão formal). O retrabalho aparece visualmente aqui.

| Eixo | O que colocar |
|------|---------------|
| X | Meses |
| Y | % (barra 100% empilhada) |
| Segmentos | `_0` (azul), `_1+` (laranja/vermelho), sem sufixo (verde) |

**O que consegue revelar:**
- Se o retrabalho (`_1+`) está crescendo → CONSAG está devolvendo mais vezes
- Se a proporção de emissões formais (sem sufixo) está aumentando → projeto avançando
- Sazonalidade de tipos de ciclo

#### Gráfico C — Duração de Ciclo em Dias (futuro — quando PW CSV tiver datas completas)

**O que mostra:** Mediana de dias corridos por tipo de ciclo por disciplina. Velocidade de resposta da equipe, sem precisar de HH.

---

### 4.14 Metodologia de Duração de Ciclo

#### Definição

**Duração de ciclo** = intervalo em dias corridos entre dois eventos consecutivos de `DataAceiteGRD` para o mesmo documento. Mede quanto tempo a OTZ levou para responder a cada GRD recebida.

#### Fórmula

```
Duração ciclo N = DataAceiteGRD(revisão N) − DataAceiteGRD(revisão N−1)

Exemplos:
  Duração ciclo 0_1 = DataAceiteGRD(0_1) − DataAceiteGRD(0_0)
  Duração ciclo A_0 = DataAceiteGRD(A_0) − DataAceiteGRD(0)
  Duração ciclo A_1 = DataAceiteGRD(A_1) − DataAceiteGRD(A_0)
```

#### Regra do Primeiro Ciclo — Proxy pelo Máximo

O ciclo `0_0` (primeira entrega) não tem `DataAceiteGRD` anterior. Portanto:

```
Duração estimada do ciclo 0_0 = max(durações de todos os ciclos conhecidos do mesmo documento)
```

> **Justificativa:** Estimativa conservadora — assume que o primeiro ciclo demorou pelo menos tanto quanto o pior ciclo observado. Documentar sempre como estimativa, não como valor medido.

#### Cuidados

| Situação | Ação |
|----------|------|
| Duração negativa | Erro nos dados — excluir e investigar |
| Duração > 90 dias | Sinalizar como outlier antes de incluir na média |
| Isométricos (MET) | Convenção de numeração diferente — verificar antes de aplicar |

---

### 4.15 De-Para: Aba da Planilha HH → Sigla Canônica

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

### 4.16 De-Para: Sigla no PW → Sigla Canônica

| Sigla no PW (campo [5] do CÓDIGO CONSAG) | Sigla KPI |
|------------------------------------------|-----------|
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

### 4.17 Valores de Referência — Base 18/08/2026

> Estes são os valores históricos fechados na base de 18/08/2026. Usar apenas como referência para validação. A cada nova exportação, recalcular.

| Disciplina | Sigla | HH Real | Ciclos PW | HH/ciclo acum. | Categoria | Observação |
|------------|-------|---------|-----------|----------------|-----------|------------|
| Tubulação | TUB | 2.861h | 597 | 4,79h | Forecast | Maior base — taxa sólida |
| Elétrica | ELE | 2.482h | 100 | 24,83h | Forecast | Boa amostra |
| Processo | PRO | 3.281h | 138 | 23,77h | Forecast | 82,6% concluído |
| Instrumentação | INS | 2.595h | 103 | 25,19h | Forecast | Taxa mais alta |
| Mecânica | MEC | 2.940h | 218 | 13,49h | Forecast | Separado de EST |
| Est. Metálica | EST | 390h | 388 | 1,01h | Forecast | DPC. Sem pendentes → ~100% |
| Segurança | SAF | 1.193h | 148 | 8,08h | Forecast | SAF no PW = SEGURANÇA no HH |
| Civil | CIV | 3.096h | 18 | 172h ⚠ | Provisório | Apenas 18 ciclos — inválido estatisticamente |
| Arquitetura | ARQ | 284h | 0 | N/A | N/A | 1 doc RM bloqueado · reprog. 27/11/26 |
| Telecom | TEL | 36h | 57 | 0,63h | Externo | Só coordenação OTZ — não entra na produtividade |
| Qualidade | QUA | 1.259h | — | — | Custo | Sem forecast de GRD |
| Overhead | OVH | 11.492h | — | — | Overhead | Inclui CDA |
| Modelo 3D | M3D | 3.225h | — | — | Excluído | CAE-CAD/COMOS |

---

### 4.18 Totais do KPI 1 — Base 18/08/2026

| Métrica | Valor | Como foi calculado |
|---------|-------|--------------------|
| HH Realizado (disciplinas com forecast) | 19.158h | Soma de TUB+ELE+PRO+INS+MEC+EST+SAF+CIV+TEL |
| HH Escopo estimado | ~40.175h | HH real (19.158) + HH previsto (21.017) |
| Ciclos PW (GRD aceita) | 1.767 | Soma de todos os ciclos válidos nas duas exports |
| HH Total (planilha bruta) | 34.874h | Valor direto da planilha — inclui ~260h sem categoria |
| Docs Pendentes (LD) | 3.024 | Ativos, não finalizados, não "NÃO NECESSÁRIO" |
| Docs Formalizados (LD) | 1.353 | Status = "DOC. FINALIZADO" |

> **Nota sobre o GAP de ~260h:** A diferença entre o HH Total (34.874h) e a soma das categorias (~35.134h) corresponde a registros sem categoria definida na planilha bruta. Exibir no dashboard com nota explicativa.

---

### 4.19 Referência de Consistência (histórico para validação)

Use esta tabela para verificar se um novo cálculo está consistente com o histórico:

| Data base | Total LD | Ativos LD | Excluídos | Finalizados | Avanço |
|-----------|----------|-----------|-----------|-------------|--------|
| 30/06/2026 | 524 | 419 | 105 | 353 | 94,22% |
| 07/07/2026 | 524 | 419 | 105 | 358 | 94,46% |

> Se Excluídos ≠ 105 ou Total ≠ 524, verificar a Regra NÃO NECESSÁRIO (Regra 2) antes de publicar.

---

## 5. KPIs Futuros — Estrutura Reservada

| KPI | Título | Status | Dependência |
|-----|--------|--------|-------------|
| KPI 1 | HH Utilizado e Previsto por Disciplina | ✅ Publicado | — |
| KPI 2 | Duração de Ciclo por Tipo e Disciplina | 🔲 Planejado | PW CSV com datas completas |
| KPI 3 | Headcount por Disciplina (Realizado e Previsto) | 🔲 Planejado | Z-546 estrutura completa |
| KPI 4 | (a definir) | 🔲 Planejado | — |

> À medida que novos KPIs forem criados, adicionar uma seção `## N. KPI N — Título` seguindo a mesma estrutura do KPI 1.

---

## 6. Controle de Versões

| Versão | Data | Alteração | Responsável |
|--------|------|-----------|-------------|
| 1.0 | 21/08/2026 | Criação do documento. KPI 1 completo: regras, colunas, de-para, valores base 18/08/2026. | Ilson / Claude |
| 1.1 | 23/08/2026 | Adicionadas seções 3.5-A (Revisão × Emissão) e 3.5-B (Metodologia de Duração de Ciclo). KPI 2 e KPI 3 registrados como planejados. | Ilson / Claude |
| 1.2 | 23/08/2026 | Correção da seção 3.5-A: definição correta de REVISÃO e EMISSÃO/DOCUMENTO. Verificação de coerência com MD-903 e PPU do contrato. | Ilson / Claude |
| 2.0 | 23/08/2026 | Reescrita completa como procedimento definitivo. Adicionado: EWMA, % Concluído como faixa, Gráficos A/B/C, pesos por tipo de documento (MD-903 §7.11), hierarquia de fallback, Tipo A/B, Regra da Razão de Somas, Janela mínima por disciplina, exemplos numéricos. Consolidação de todas as definições e regras anteriores. | Ilson / Claude |

---

*Documento interno OTZ Engenharia — uso restrito à equipe GPLAN.*
*Não compartilhar com CONSAG ou terceiros sem aprovação do Supervisor de Planejamento.*
