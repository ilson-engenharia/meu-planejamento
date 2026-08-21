# PROTOCOLO KPI — Z-546 RNEST UGH
**OTZ Engenharia × CONSAG × Petrobras**  
**Responsável:** Ilson dos Santos Azevedo — Eng. Planejamento  
**Versão:** 21/08/2026  

---

## 1. FONTES DE DADOS E FILTROS OBRIGATÓRIOS

### 1.1 Relatório PW (ProjectWise — CONSAG)
| Filtro | Valor |
|--------|-------|
| `nomeEmpresa` | `ENG OBRA` ou `OTZ PROJETISTA` — apenas |
| `DisciplinaDesc` | Remover: GESTÃO, PLANEJAMENTO, PROJETOS |
| `TipoDocumento` | Remover: ATA |

### 1.2 Lista de Documentos (LD Excel — OTZ)
| Filtro | Valor |
|--------|-------|
| Coluna H (Disciplina) | Remover: Coordenação, Engenharia Digital |
| Coluna DL (Status) | Remover: EXCLUÍDO |

**Correspondência LD ↔ PW:**
- `LD Trem 2 - ICs` = `ENG OBRA` (isométricos)
- `LD UGH Trem 2` = `OTZ PROJETISTA` (demais disciplinas)

### 1.3 Cadastro de Horas (HH)
Duas planilhas — devem ser **somadas**, não substituídas:

| Planilha | Projeto | Disciplinas |
|----------|---------|-------------|
| Principal | Z-546 - RNEST - UGH | TUBULAÇÃO, ELÉTRICA, PROCESSO, INSTRUMENTAÇÃO, CDA, MECÂNICA, QUALIDADE, SEGURANÇA, TELECOM + GESTÃO, PLANEJAMENTO, GERAL, CAE-CAD |
| DPC | Z-546.1 - RNEST - UGH | CIVIL, ARQUITETURA, ESTRUTURA METÁLICA + GESTÃO, GERAL |

---

## 2. DEFINIÇÕES FUNDAMENTAIS

### 2.1 CICLO (unidade de medida do HH)
> **Ciclo** = cada passagem completa de um documento pelo fluxo de aprovação, identificada pela existência de `DataAceiteGRD` preenchida no PW.
>
> Um documento com 3 DataAceiteGRD diferentes = 3 ciclos (1 emissão + 2 revisões).

**Data âncora de todos os KPIs de tempo:** `DataAceiteGRD` = data em que a GRD (Guia de Remessa de Documentos) foi aceita — é a data oficial em que o documento foi formalizado e enviado para o próximo ator do fluxo.

### 2.2 EMISSÃO vs REVISÃO

| Conceito | Definição | Campo PW | Exemplo |
|----------|-----------|----------|---------|
| **Emissão de desenho** | Documento entrando pela 1ª vez no fluxo | `RevisaoCompleta` **sem sufixo** (sem _A, _B, _1...) | `Rev 0`, `0` |
| **Revisão de desenho** | Documento retornando ao fluxo após comentários | `RevisaoCompleta` **com sufixo** | `0_A`, `1_B`, `Rev 1_C` |
| **Documento emitido (aprovado)** | Revisão sem sufixo + DataAceiteGRD preenchida | Sem sufixo + DataAceiteGRD | Aprovado pela Petrobras |

**Regra do filtro "Emissão pura":**
```
RevisaoCompleta NÃO contém _ (underscore) ou letra após o número
DataAceiteGRD NÃO é vazio
```

**Para o forecast de HH (KPI 1):** trabalhamos com **ciclos totais** (emissões + revisões), pois o HH é consumido em cada ciclo independente de ser primeira emissão ou revisão.

---

## 3. CLASSIFICAÇÃO DE DISCIPLINAS (HH)

### 3.1 Disciplinas previsíveis (aparecem no PW + LD)
Entram no **forecast** e na curva HH previsto vs realizado:

| Disciplina | Fonte | HH Realizado |
|------------|-------|-------------:|
| TUBULAÇÃO | Principal | 7.250,5h |
| ELÉTRICA | Principal | 5.065,0h |
| PROCESSO | Principal | 4.636,1h |
| INSTRUMENTAÇÃO | Principal | 4.584,0h |
| CDA | Principal | 3.464,4h |
| MECÂNICA | Principal | 2.940,2h |
| QUALIDADE | Principal | 1.258,6h |
| SEGURANÇA | Principal | 751,0h |
| CIVIL | DPC | 3.097,0h |
| ESTRUTURA METÁLICA | DPC | 390,0h |
| ARQUITETURA | DPC | 284,5h |
| TELECOM | Principal | 36,0h |
| **TOTAL PREVISÍVEL** | | **33.757,3h** |

### 3.2 Disciplinas não previsíveis (não estão no PW nem na LD)
Aparecem no total real de HH gasto, mas **sem curva de forecast**:

| Disciplina | Fonte | HH Realizado | Motivo |
|------------|-------|-------------:|--------|
| GESTÃO | Principal + DPC | 3.959,5h | Overhead gerencial — não entra no fluxo GRD |
| PLANEJAMENTO | Principal | 3.970,0h | Overhead gerencial — não entra no fluxo GRD |
| GERAL | Principal + DPC | 98,5h | Overhead geral — não está no PW/LD |
| **TOTAL NÃO PREVISÍVEL** | | **8.028,0h** | |

### 3.3 Excluído do KPI 1
| Disciplina | HH | Motivo |
|------------|---:|--------|
| CAE - CAD | 3.225,0h | Sistema de Modelo 3D — não produz documentos no fluxo GRD |

### 3.4 Total consolidado
| Categoria | HH |
|-----------|---:|
| Previsível (forecast) | 33.757,3h |
| Não previsível (só real) | 8.028,0h |
| CAE-CAD (excluído) | 3.225,0h |
| **TOTAL GERAL** | **45.010,3h** |

---

## 4. METODOLOGIA DO FORECAST HH (KPI 1)

```
HH/ciclo (por disciplina × tipo) = HH real ÷ ciclos realizados no PW

HH previsto (por disciplina × tipo) = ciclos futuros (LD) × HH/ciclo

Ciclos futuros = documentos na LD com status ≠ EXCLUÍDO × revisões esperadas
```

**Pico identificado:** setembro/2026 = 9.563h previstas (3,6× a média histórica de 2.652h/mês) — coerente com o baseline da LD (outubro/26: 489 emissões).

---

## 5. SLAs DO FLUXO §9.2 (status: decisão pendente)

| Ator | SLA | Base | Status |
|------|-----|------|--------|
| CONSAG — 1ª análise | 3 DU | Fluxograma §9.2 | ✅ Confirmado |
| CONSAG — reanálise | 2 DU | Fluxograma §9.2 | ✅ Confirmado |
| OTZ — resposta loop interno | 3 DU / 2 DU | Fluxograma §9.2 | ⚠️ Decisão pendente |
| OTZ — resposta a comentários | 5 DU | Texto §9.2 | ⚠️ Decisão pendente |
| Petrobras | 10 DU | Contrato | ✅ Confirmado |
| SIGEM — upload | 0 DU (mesmo dia) | Fluxograma §9.2 | ❌ Nenhum KPI mede |

> **PONTO A ABERTO:** OTZ medida contra 5du (texto) ou 3du (fluxograma)? Decisão de Ilson.

---

## 6. ACHADOS CRÍTICOS (para atenção do outro Claude)

1. **RL_PW é aba órfã**: não alimenta nenhuma fórmula no Excel LD. "Emitido no PW" na LD = "GRD saiu do E-CLIC", **não** "consta no ProjectWise".
2. **86 documentos pré-cadastrados no PW que não existem**: LD mostra `PRÉ CADASTRADO NO PW? = SIM`, mas não aparecem no export do PW. Todos em `EMITIR EMISSÃO INICIAL`.
3. **3 campos contratuais 100% vazios**: `SEVERIDADE`, `Rede de Precedência`, `FLUXOGRAMA (REF. Isométrico)` — Anexo VII, risco de auditoria.
4. **Curva de aprendizado**: 68,7 HH/doc (jan/25) → 18,6 HH/doc (jul/26) — 3,7× mais eficiente com 53% mais pessoas.
5. **1.153 ICs bloqueados**: dependentes de IS-200 pai não emitido.

---

## 7. GARGALO PRINCIPAL — COMUNICAÇÃO ENTRE DISCIPLINAS (EM DISCUSSÃO)

O problema: as três planilhas (HH, PW, LD) usam nomenclaturas diferentes para a mesma disciplina.

| HH (planilha) | PW (DisciplinaDesc) | LD (col H) | Chave canônica |
|---------------|---------------------|------------|----------------|
| TUBULAÇÃO | TUB | Tubulação | 6º campo CÓDIGO CONSAG |
| ELÉTRICA | ELE | Elétrica | 6º campo CÓDIGO CONSAG |
| INSTRUMENTAÇÃO | INS | Instrumentação | 6º campo CÓDIGO CONSAG |
| MECÂNICA | MEC | Mecânica | 6º campo CÓDIGO CONSAG |
| PROCESSO | PRO | Processo | 6º campo CÓDIGO CONSAG |
| CIVIL | CIV | Civil | 6º campo CÓDIGO CONSAG |
| CDA | CDA | — | ⚠️ não mapeia direto no PW |
| QUALIDADE | — | — | ⚠️ não está no PW |
| SEGURANÇA | — | — | ⚠️ não está no PW |

> **Chave de tradução canônica:** 6º campo do `CÓDIGO CONSAG` no PW (ex: `5290.002.231.19.40.TUB.001` → `TUB`).
>
> **Próxima discussão:** como fazer as três planilhas conversarem automaticamente. Isso é o principal gargalo para o sistema autônomo.

---

*Protocolo gerado em: 21/08/2026 — baseado em todas as análises da sessão Z-546.*
