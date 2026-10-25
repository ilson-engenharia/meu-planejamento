# CLAUDE.md — Caixa Preta do Operador
> Arquivo de memória persistente. Leia sempre no início de cada sessão.
> Última atualização: 25/10/2026

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

## 🛠️ SKILLS INSTALADAS — REGRA PARA TODOS OS CLAUDE

> **REGRA:** Todo Claude que trabalhar neste projeto DEVE ter todas as skills abaixo instaladas.
> Instalar com: `npx skills add <repo>` (requer Node.js) ou copiar para `~/.claude/skills/`
> Instalação em lote: execute o bloco de comandos abaixo no terminal.

### Instalar todas de uma vez:
```bash
npx skills add tt-a1i/archify
npx skills add OthmanAdi/planning-with-files
npx skills add cathrynlavery/diagram-design
npx skills add virgiliojr94/book-to-skill
npx skills add eugeniughelbur/obsidian-second-brain
npx skills add 0xpili/simplified-technical-english
npx skills add QingYunA/answer-me-with-html
npx skills add mathiaschu/watch
npx skills add zarazhangrui/frontend-slides
npx skills add kharmanskyi/open-steps
npx skills add DreambigOu/ELI5
npx skills add op7418/guizang-social-card-skill
```

### Catálogo de Skills Instaladas (out/2026):

| Skill | Comando | Para que serve |
|-------|---------|----------------|
| `/archify` | tt-a1i/archify ⭐89k | Transforma qualquer ideia, plano ou processo em diagrama interativo |
| `/planning-with-files` | OthmanAdi/planning-with-files ⭐28k | Planejamento persistente entre sessões — não perde o plano ao reiniciar |
| `/diagram-design` | cathrynlavery/diagram-design ⭐61k | 45 tipos de diagramas editoriais: fluxo, cronograma, org, processo |
| `/book-to-skill` | virgiliojr94/book-to-skill ⭐36k | Converte livro/manual/norma PDF em skill para uso contínuo |
| `/obsidian-second-brain` | eugeniughelbur/obsidian-second-brain ⭐5k | Memória persistente em Obsidian — todos os Claude compartilham |
| `/simplified-technical-english` | 0xpili/simplified-technical-english ⭐1k | Escreve documentos técnicos no padrão ASD-STE100 (industrial) |
| `/answer-me-with-html` | QingYunA/answer-me-with-html ⭐4k | Responde perguntas complexas como página HTML bonita |
| `/watch` | mathiaschu/watch ⭐143 | Assiste vídeos (YouTube/Instagram/local) e analisa o conteúdo |
| `/frontend-slides` | zarazhangrui/frontend-slides ⭐31k | Cria apresentações HTML profissionais via agente |
| `/os-step-by-step` etc | kharmanskyi/open-steps ⭐1.2k | 8 sub-skills de linguagem clara: passo a passo, riscos, próximos passos |
| `/eli5` | DreambigOu/ELI5 ⭐1.8k | Explica qualquer coisa para qualquer público (técnico, leigo, gestor) |
| `/guizang` | op7418/guizang-social-card-skill ⭐7.7k | Gera cards visuais profissionais e carrosséis de apresentação |

---

## 🎬 SKILL: WATCH (claude-video)

**Repositório instalado:** `~/.claude/skills/watch/` (bradautomates/claude-video v0.3.2)
**Engine:** local (yt-dlp + ffmpeg) — sem custo de API
**Dependências:** yt-dlp ✅ · ffmpeg ✅ · python3 ✅

**Como usar:**
- `/watch https://youtube.com/...` → Claude assiste o vídeo e responde perguntas
- `/watch /caminho/para/video.mp4` → funciona com arquivo local também
- Após o `/watch`, pergunte qualquer coisa: "Quais ações foram definidas?" / "O que está errado nessa instalação?"

**Casos de uso confirmados para obras:**
- Gravar reunião/inspeção → Claude resume e extrai ações
- Vídeo de treinamento de sistema (RPAs, ERP, plataformas) → Claude aprende o fluxo e replica
- Filmar não-conformidade → Claude analisa e descreve

**Para instalar em outro computador:**
1. Claude Code instalado
2. `/plugin marketplace add bradautomates/claude-video`
3. `/plugin install watch@claude-video`

---

## ✅ CHECKLIST DE ENTREGA — RESTRIÇÕES

A cada atualização da planilha de restrições, entregar:
- [ ] `GESTAO_RESTRICOES_Cristalia_DDMMYY.xlsx`
- [ ] `GESTAO_RESTRICOES_Cristalia_DDMMYY.md`
- [ ] `Carta_para_Conector_DDMMYY.md`
- [ ] `Relatorio_Operador_DDMMYY.md`
- [ ] Commit + push no git
- [ ] Upload no Drive Vault (pasta a confirmar com usuário)
