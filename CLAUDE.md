# CLAUDE.md — Caixa Preta do Operador
> Arquivo de memória persistente. Leia sempre no início de cada sessão.
> Última atualização: 27/05/2026

---

## 🔴 REGRAS CRÍTICAS — NUNCA VIOLAR

1. **NUNCA modificar conteúdo** — apenas corrigir Português e pontuação. Nunca interpretar, reestruturar ou adicionar informações.
2. **FormulaRule PROIBIDA** no openpyxl — causa corrupção de arquivo no Google Drive.
3. **Pasta local = READ ONLY**: `C:\Users\ilson\Abelv Engenharia Ltda\Cristalia 25098 - Citostático` — nunca modificar nada lá.
4. **Fique calmo** — na dúvida, perguntar ao usuário antes de agir.

---

## 📁 PADRÃO DE NOMENCLATURA — PLANILHA DE GESTÃO DE RESTRIÇÕES

**Nome obrigatório:** `GESTAO_RESTRICOES_Cristalia_DDMMYY.xlsx`

**Exemplos:**
- `GESTAO_RESTRICOES_Cristalia_270526.xlsx` ← 27/05/2026
- `GESTAO_RESTRICOES_Cristalia_030626.xlsx` ← 03/06/2026

**Modelo:** CONECTOR
- 2 abas: `Restrições` + `Dashboard`
- Células coloridas por status (sem emoji no texto)
- Coluna DISCIPLINA em formato bracket: `[CIVIL]`, `[MEC/TUB]`, `[PROC]`, `[ELET]`, `[SUP]`, `[SMS]`, `[DOC]` e combinações
- Status calculado automaticamente via Python (`today = date(AAAA, MM, DD)`)

**⚠️ NÃO usar mais:**
- ~~`Restricoes_CONECTOR_DDMMYYYY.xlsx`~~
- ~~`Restricoes_Consolidadas_Cristalia_DDMMYYYY.xlsx`~~
- ~~`2026-MM-DD_CONTROLE_CRITICO_PLA_*.xlsx`~~

---

## 📋 PADRÃO DE NOMENCLATURA — MD DE RESTRIÇÕES

**Nome:** `GESTAO_RESTRICOES_Cristalia_DDMMYY.md`
- Mesmo padrão da planilha, extensão `.md`
- Agrupado por disciplina, com emojis de status

---

## 🏗️ PROJETOS

| Código | Nome | ID Cronograma |
|--------|------|---------------|
| CISTO | 25098 Citostático | — |
| FARMO | 25103 Farmoquímico | — |

---

## 🗂️ DISCIPLINAS (formato bracket)

| Bracket | Disciplina |
|---------|-----------|
| `[CIVIL]` | Civil |
| `[MEC/TUB]` | Mecânica / Tubulação |
| `[PROC]` | Processos / HVAC |
| `[ELET]` | Elétrica |
| `[SUP]` | Suprimentos |
| `[SMS]` | Segurança / Meio Ambiente / Saúde |
| `[DOC]` | Documentação |
| Combinações: `[CIVIL][SMS]`, `[MEC/TUB][SUP]`, `[DOC][SUP]`, `[DOC][SMS]`, `[PROC][SUP]` | — |

---

## 📊 VOCABULÁRIO DE STATUS

| Status | Condição |
|--------|----------|
| `NO PRAZO` | NEC > hoje, sem conclusão |
| `ALERTA` | NEC == hoje, sem conclusão |
| `ATRASADO` | NEC < hoje, sem conclusão |
| `CONCLUÍDO` | CONC <= NEC |
| `CONCLUÍDO COM ATRASO` | CONC > NEC |
| `—` | Sem prazo definido |

---

## ☁️ DRIVE VAULT

| Campo | Valor |
|-------|-------|
| Vault Root ID | `1jzX9l751K6oAi3SRYUrFuvcmMHIzPEC3` |
| Servidor MCP | `drivemcp.googleapis.com/mcp/v1` (novo — antigo foi desativado) |
| Pastas | `00_BASE`, `01_ENTRADA`, `02_EMPRESAS_PARCEIRAS`, `03_CONHECIMENTO`, `04_ARQUIVO_MORTO`, `05_INTELIGENCIA_ARTIFICIAL`, `06_ILSON_PESSOAL`, `99_SCRIPTS`, `99_Arquivos_Originais` |

---

## 🌿 GIT

| Campo | Valor |
|-------|-------|
| Branch de trabalho | `claude/general-session-ON8EW` |
| Repositório | `ilson-engenharia/meu-planejamento` |
| Regra | Sempre commit + push ao final de cada entrega |

---

## 📂 RDOs (pendente)

- Localização local: `C:\Users\ilson\Documents\ABELV\Planejamento\RDO e RDC Diário de Obra\MD\` (44 arquivos)
- **Não sincronizados ao Drive ainda** — cobrar do usuário a cada sessão

---

## ✅ CHECKLIST DE ENTREGA — RESTRIÇÕES

A cada atualização da planilha de restrições, entregar:
- [ ] `GESTAO_RESTRICOES_Cristalia_DDMMYY.xlsx`
- [ ] `GESTAO_RESTRICOES_Cristalia_DDMMYY.md`
- [ ] `Carta_para_Conector_DDMMYY.md`
- [ ] `Relatorio_Operador_DDMMYY.md`
- [ ] Commit + push no git
- [ ] Upload no Drive Vault (pasta a confirmar com usuário)
