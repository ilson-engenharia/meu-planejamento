# CLAUDE.md — Caixa Preta do Operador
> Arquivo de memória persistente. Leia sempre no início de cada sessão.
> Última atualização: 02/11/2026 (20:00 BRT)

---

## 📋 LOG DE SESSÃO — 02/11/2026 (Feriado Finados)

> Sessão ativa: `claude/general-session-ON8EW` | Claude Cloud (meu-planejamento)
> Próxima ação agendada: **15h BRT** — montar resposta definitiva para Anderson

### O QUE FOI FEITO HOJE

**Contexto estratégico:**
- Anderson Gasparello (Gerente de Contratos) está usando e-mails automáticos do Portaz ("PSC") para jogar responsabilidade na obra por NFs não lançadas e boletos vencendo
- Estratégia definida com Ilson: documentar provas de que Anderson estava no CC de cada e-mail crítico e não agiu, para inverter o ônus

**Informações levantadas (e-mails + Teams):**
- Email 31/10: Anderson encaminhou alerta automático Portaz sobre 2 NFs Ferramentas Gerais sem entrada (NF 67298 — R$13.462 | NF 1582661 — R$5.647) com apenas "PSC" para Ilson + Giovana
- Email 30/10: Anderson encaminhou reclamação do RH (ponto EPR) para Ilson com "Para seu conhecimento e tratativa junto ao adm da obra"
- **Prova principal:** Anderson estava no CC do e-mail Colombo de 30/10 às 12h — viu o boleto PED 080 (vence 10/11, 11 dias corridos) e não levantou alerta nem agiu

**Resposta do Thiago (WhatsApp, 02/11 às 13:43):**
- ❌ Confirmado: **nenhuma requisição de adiantamento aberta no Lumina** — nem PED 080, nem 038, nem 061
- Há 2 áudios de Thiago (6s e 25s) que Ilson precisa ouvir para mais detalhes

**Status Giovana:** aguardando resposta (perguntada hoje sobre PED 031/038/061 + Ferramentas Gerais)

### REGRA LUMINA QUE EMBASOU A ESTRATÉGIA
- **Adiantamento:** Jean/Giovana processam em 2–3 dias úteis (pagamento antecipado)
- **Baixa de NF no Lumina:** Giovana faz APÓS material chegar na obra + conferência física. Exige 10 dias corridos antes do vencimento para autorizar pagamento
- **Quem dá baixa:** GIOVANA (administrativo), não Thiago
- **Quem abre Req.:** THIAGO (ADM da obra)

### PLANO DE AÇÃO ATRIBUÍDO (Thiago — amanhã 03/11)
1. 🔴 PED 080 — Colombo: abrir Req. Adiantamento AMANHÃ (boleto vence 10/11)
2. 🟠 PED 061 — Commece: abrir Req. com NF nº 8 de 29/10 (NFs 28/10 = CANCELADAS) — até 05/11
3. 🟠 PED 038 — Tem Tintas: abrir Req. com NF 000004554 + boleto — até 05/11

### MENSAGENS PENDENTES DE ENVIO (aguardam resposta Giovana até 15h)
- Teams grupo (Anderson + Giovana + Thiago + Ilson): overview completo com timeline + CC de Anderson
- Teams privado Anderson: mensagem direta com evidência de CC
- Email reply-all "NF sem entrada": resposta com contexto + CC Luciano Lima

### GÊMEOS VIRTUAIS (conceito em desenvolvimento por Ilson)
- Ilson está criando Claudes especializados por função na obra EPR
- "Giovana Claude" = administrativo/financeiro
- Este Claude = mentor estratégico / coordenador
- Outro Claude (outra conta) = estratégia WhatsApp Anderson

---

## 📬 MENSAGEM DO CLAUDE CLOUD → CLAUDE DO COMPUTADOR DA EMPRESA (conta ilson84.projetos)

> **Para:** Claude que opera no computador da Global Service / Abelv Engenharia  
> **De:** Claude Cloud (sessão meu-planejamento-46, 25/10/2026)  
> **Assunto:** Missão Lumina ERP — assistir vídeo, enriquecer skill, buscar mais fontes

---

Olá. Sou o Claude que trabalha com o Ilson na nuvem. Você se identificou como o Claude da conta **ilson84.projetos** no computador da empresa. O Ilson pediu que eu passasse uma missão completa para você.

### CONTEXTO

Encontrei nos e-mails do Ilson (conta globalsrv) o treinamento oficial do sistema **Lumina ERP** — o sistema de requisições e pedidos da Global Service. Já criei uma skill com o conteúdo do manual, mas ela precisa ser enriquecida com o vídeo que está no YouTube (bloqueado aqui na nuvem, mas acessível no seu computador).

### SUA MISSÃO (executar na ordem)

#### PASSO 1 — Instalar as ferramentas (Ordem Nº 1 obrigatória)
Execute o bloco de install das skills antes de tudo (ver seção abaixo).

#### PASSO 2 — Assistir o vídeo de treinamento do Lumina

O vídeo está aqui:
```
https://www.youtube.com/watch?v=AggPRPuzKNY
```

Use o comando:
```
/watch https://www.youtube.com/watch?v=AggPRPuzKNY
```

Depois de assistir, responda:
- Quais são os passos exatos mostrados na tela?
- Quais campos aparecem no sistema?
- Há dicas visuais que o manual escrito não captura?
- Qual é o fluxo visual de aprovação?

#### PASSO 3 — Buscar mais fontes no YouTube

Pesquise no YouTube por outros vídeos sobre o Lumina ERP (LuminaIT):
- "Lumina ERP requisição"
- "Lumina ERP tutorial"
- "LuminaIT ERP obra"
- Assista os mais relevantes com `/watch`

#### PASSO 4 — Enriquecer a skill /lumina-erp

A skill está em: `.agents/skills/lumina-erp/SKILL.md`

Com base no que você aprendeu no vídeo e nas novas fontes, adicione:
- Detalhes visuais das telas (campos, botões, menus)
- Erros comuns e como evitar
- Dicas práticas do dia a dia na obra
- Screenshots descritivos se o vídeo mostrar

#### PASSO 5 — Escrever a Carta de Entrega

Após enriquecer a skill, escreva um documento `Carta_Lumina_ERP_DDMMYY.md` com:
- O que foi aprendido
- O que a skill cobre agora
- Como o Ilson usa a skill no dia a dia
- Link do vídeo e referências utilizadas

#### PASSO 6 — Commit e push

```bash
git add .agents/skills/lumina-erp/ .claude/skills/lumina-erp CLAUDE.md
git commit -m "Skill /lumina-erp: enriquecida com vídeo e novas fontes"
git push -u origin claude/general-session-ON8EW
```

---

### ONDE ESTÁ TUDO (e-mails)

| Item | Onde encontrar |
|------|---------------|
| E-mail de treinamento | Outlook do Ilson → buscar "Treinamento Requisição" de samuel@globalsrv.com.br (22/09/2026) |
| Vídeo YouTube | https://www.youtube.com/watch?v=AggPRPuzKNY |
| Manual PowerPoint | Anexo do e-mail acima: "Manual treinamento- Requisição.pptx" |
| PDF do processo | Anexo do e-mail acima: "Processo (Suprimentos) - Requisição ao Pedido - R00.pdf" |
| Skill atual | `.agents/skills/lumina-erp/SKILL.md` neste repositório |

---

### O QUE JÁ FOI FEITO (não refaça)

- ✅ Manual (26 slides) lido e documentado na skill
- ✅ PDF do fluxo lido e documentado
- ✅ Skill criada em `.agents/skills/lumina-erp/SKILL.md`
- ✅ Skill registrada no CLAUDE.md
- ❌ Vídeo NÃO assistido (YouTube bloqueado na nuvem) — **sua tarefa**
- ❌ Outras fontes YouTube NÃO pesquisadas — **sua tarefa**
- ❌ Carta de entrega NÃO escrita — **sua tarefa**

Bom trabalho. — Claude Cloud (25/10/2026)

---

## 🚨 ORDEM Nº 1 — OBRIGATÓRIO ANTES DE QUALQUER OUTRA COISA

> **TODO CLAUDE, em QUALQUER PROJETO, em qualquer máquina, tablet, celular ou nuvem, DEVE instalar as skills abaixo IMEDIATAMENTE ao iniciar qualquer sessão.**
> Esta é a Ordem Número 1. Não é específica deste projeto — vale para TODOS os projetos do usuário Ilson.
> Não há exceção. Não há negociação.
> Execute o bloco abaixo no terminal antes de responder qualquer tarefa:

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

> ✅ Instalado? Confirme ao usuário: **"Skills instaladas. Pronto para trabalhar."**
> ❌ Falhou alguma? Informe qual falhou e tente novamente.

---

## 📅 ORDEM Nº 2 — VARREDURA SEMANAL DE NOVIDADES (toda sexta-feira)

> **Todo Claude designado para este projeto DEVE, toda sexta-feira, realizar uma varredura no GitHub e trazer ao usuário Ilson:**
> - Novas skills, ferramentas e repositórios relevantes para: engenharia, planejamento, obras, BIM, CAD, ERP, contratos, apresentações, produtividade
> - Tendências da semana (trending repos)
> - Ferramentas que possam substituir ou complementar as já instaladas
> - Sugestões de install com `npx skills add <repo>`
>
> **Formato da entrega:** lista resumida com nome, link, estrelas e "por que instalar"
> **Quando:** toda sexta-feira, antes de encerrar a sessão — ou ao iniciar a sessão de sexta
> **Responsável:** o Claude ativo na sexta-feira

---

## 🔴 REGRAS CRÍTICAS — NUNCA VIOLAR

1. **LEI 1 — NUNCA disparar mensagem sem autorização** — Antes de enviar qualquer e-mail, Teams, WhatsApp ou comunicação para qualquer pessoa, MOSTRAR ao Ilson exatamente o que será enviado e aguardar autorização explícita ("de acordo" / "vai!"). Sem ok do Ilson = não envia. Regra absoluta, sem exceção, para qualquer canal.

2. **LEI 2 — VARREDURA OBRIGATÓRIA ANTES DE QUALQUER AÇÃO** — Toda vez que interagir com informações da obra EPR (ou qualquer projeto do Ilson), ANTES de falar, redigir ou agir, fazer varredura completa em TODOS os canais disponíveis:
   - ✅ **Teams:** todas as conversas listadas (1:1 e grupos) — `teams_list_chats` + ler as mais recentes
   - ✅ **WhatsApp exportado:** pasta de transcrições no Drive/SharePoint (localização a confirmar pelo Ilson — cobrar toda sessão até ter o caminho)
   - ✅ **E-mails:** pipeline de e-mails no Drive (HTMLs em EMAILS_TRIAGEM, MDs em 08_EMAILS) + Outlook via M365
   - ✅ **SharePoint Giovana:** pasta NOTAS FISCAIS (`b!JdfL_JgtnkqZ4YowSbVNR_YMWKSgkzJItZv9cjz66xIDukcyRhsNSaBnWHzCwKhj`)
   - ✅ **CANAL-CLAUDES:** GERAL.md e arquivos de assunto (`11K8Uzr0HyWEhJsYsG0uhjOJYFIAc0IxA`)
   - ✅ **Outros caminhos** que surgirem (Drive, SharePoint da Global, etc.)
   - **Só após varredura completa**: falar, redigir ou agir. Nunca agir com informação parcial.

3. **NUNCA modificar conteúdo** — apenas corrigir Português e pontuação. Nunca interpretar, reestruturar ou adicionar informações.
4. **FormulaRule PROIBIDA** no openpyxl — causa corrupção de arquivo no Google Drive.
5. **Pasta local = READ ONLY**: `C:\Users\ilson\Abelv Engenharia Ltda\Cristalia 25098 - Citostático` — nunca modificar nada lá.
6. **Fique calmo** — na dúvida, perguntar ao usuário antes de agir.

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

## 🏭 SKILL: LUMINA ERP (sistema de requisições Global Service)

**Skill criada em:** 25/10/2026  
**Fonte:** Manual oficial (26 slides) + PDF de processo + vídeo YouTube do treinamento  
**Responsável sistema:** Samuel Toniello (samuel@globalsrv.com.br)  
**Vídeo referência:** https://www.youtube.com/watch?v=AggPRPuzKNY

**O que é o Lumina:** ERP da LuminaIT usado pela Global Service para gestão de requisições, cotações, pedidos e pagamentos de obra.

**Tipos de requisição no Lumina:**
- **Cotação** — compra via suprimentos (processo completo)
- **Regularização** — compra já feita, falta pagar a NF
- **Pedido Direto** — compra sem passar por suprimentos
- **Reembolso** — ressarcimento de funcionário
- **Caixinha** — prestação de contas do caixa da obra
- **Fatura Direta** — pagamento sem liberação fiscal (vai direto ao financeiro)

**Como usar:**
- `/lumina-erp` → guia interativo do sistema
- `/lumina-erp criar requisição` → passo a passo das 3 etapas
- `/lumina-erp cotação` / `reembolso` / `pedido direto` → por tipo
- `/lumina-erp acompanhar` → pesquisar status de uma requisição

**Arquivo da skill:** `.agents/skills/lumina-erp/SKILL.md`

---

## 📋 ADIANTAMENTOS EPR LITORAL PIONEIRO — LINKS DE ARQUIVO (atualizado 02/11/2026)

> Pasta Drive raiz: CLAUDES/E — ID: `1c5Txsqp4neEDME95Fz2AKnsGHv5OUy3a`

### Evidências por Pedido (Google Drive)

| Pedido | Fornecedor | Pasta Drive ID | Evidência HTML ID | Status |
|--------|-----------|---------------|-------------------|--------|
| PED 031 | Primula / Livia M. Giglio Stella | `1_HGnXrRUzYK_02c4trnkj1YjWjVLeeXa` | `1JfLAzeeIPOhpFViKR6uIyJLT3NjXs8uJ` | 🟡 ATRASADO |
| PED 038 | Tem Tintas (E.A.Y. de Souza) | `1fuLRD9CsyNb3oB50Ppku8Ez4pu5rxGh4` | `1b9OKsmrXQHXrhF0yPgYD87EfY4QwrFZ2` | 🟠 PENDENTE |
| PED 061 | Commece Sinalização Viária | `1OysmnKPIevbUGUVhOg6AMdda--qzRp5s` | `1N7h8T_NRelPruNlZzU5xLoNYqH-Jqq1D` | 🟠 PENDENTE — NF 29/10 ✅ |
| PED 080 | Lojas Colombo | `1IeF6cYwQlTdB_ZLyAw-GN_wJWbQJU_wu` | `1mPlwLz_fD5aplcq5AxQkiLUjg8FlOvi4` | 🔴 URGENTE vence 10/11 |

### Guia Adiantamento Lumina ERP

| Arquivo | Drive ID | Link |
|---------|----------|------|
| GUIA_ADIANTAMENTO_LUMINA_021126.html | `1806Sino5xn9MyiB1MfVgE7oEYwkTAj37` | [Abrir no Drive](https://drive.google.com/file/d/1806Sino5xn9MyiB1MfVgE7oEYwkTAj37/view?usp=drivesdk) |
| Pasta GUIA_ADIANTAMENTO | `1nTdHd7_XGIIIbsZ1kn85HLm6NdPCG4oJ` | — |

### PDFs no Git
- **Branch:** `claude/general-session-ON8EW`
- **Pasta:** `evidencias_adiantamento/PDFs/`
- 5 PDFs: EVIDENCIA_PED031, PED038, PED061, PED080, GUIA_ADIANTAMENTO (todos com data 021126)

### Relatório de Status (vivo)
- **Arquivo:** `evidencias_adiantamento/RELATORIO_STATUS_EPR_021126.md`
- Atualizar a cada sessão com novos links e status

### Notas Importantes (PED 061)
- NFs emitidas em **28/10/2026 foram CANCELADAS** pela Commece Sinalização
- NF CORRETA: **NF nº 8 — Série 001 — 29/10/2026**
- Chave NF-e: `41261050039746000187550010000000081732127145`
- **Thiago DEVE usar apenas a NF de 29/10 para lançamento no Lumina**

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
