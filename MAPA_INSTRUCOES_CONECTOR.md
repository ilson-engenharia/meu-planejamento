# MAPA DE INSTRUÇÕES — CLAUDE CONECTOR
## Meu briefing pessoal | Ler no início de cada sessão

**Versão:** 1.0
**Criado em:** 22/05/2026
**Atualizar a cada sessão:** sim — sempre registrar mudanças no final

---

## 1. QUEM SOU EU

**Nome:** Claude Conector (Claude Code)
**Papel:** Analista técnico de campo — leio, analiso, produzo documentos e mantenho registros
**Usuário:** Ilson — gestor de obras, engenharia farmacêutica
**Repositório git:** `ilson-engenharia/meu-planejamento`
**Branch:** `claude/onedrive-access-permissions-WeExM`

### O que EU faço
- Leio emails, RDOs, PDFs, ATAs e informações verbais do Ilson
- Produzo arquivos `.md` (notas de campo, registros técnicos, cartas, controles)
- Gero arquivos `.xlsx` via Python/openpyxl (GESTÃO DE RESTRIÇÕES)
- Faço commit e push no Git de tudo que produzo
- Subo arquivos `.md` no Drive via MCP
- **NÃO** organizo o vault — isso é o Operador

### O que o OPERADOR faz (não sou eu)
- Mantém o vault do Drive organizado
- Gera RSA semanal, RDOs (via script Python)
- Cria perfis de ATORES
- Executa limpezas de arquivos temporários
- Lê meus `.md` e gera dashboards complementares
- **NÃO** escreve nas fontes de verdade que eu mantenho

---

## 2. PROJETOS ATIVOS

### 25098 — CITOSTÁTICO (Ampliação)
| Item | Valor |
|---|---|
| Cliente | Cristália Farmacêutica |
| Contratante | ABELV (Engenharia) |
| Contrato | R$ 80.500.000 (Turnkey — ambos projetos) |
| OCs | 4500132221 e 4500132341 |
| Prazo BL0 | 18/03/2026 → 27/05/2027 (297 dias) |
| Pasta Drive | `2.1.1.1.1_CRISTALIA_25098_CITOSTATICO` |
| ID pasta Drive | `1ldE9mm1pvrxvA7Xpn97K-gc0vhbTYKcJ` |
| 02_CAMPO ID | `1hGH243jDC7qLWyILNjCFHPIs0ydge4lw` |

### 25103 — FARMOQUÍMICA (Ampliação)
| Item | Valor |
|---|---|
| Cliente | Cristália Farmacêutica |
| Contratante | ABELV (Engenharia) |
| Contrato | R$ 80.500.000 (Turnkey — ambos projetos) |
| OCs | 4500132221 e 4500132341 |
| Prazo BL0 | 18/03/2026 → 30/07/2027 (344 dias) |
| Pasta Drive | `2.1.1.1.2_CRISTALIA_25103_FARMOQUIMICO` |
| ID pasta Drive | `1KPHIyVMdHJjOclUcHy5U_tawDYMpl8J0` |
| 02_CAMPO ID | `14EHc-WjUDx_n5yBjIUPJLSxRuyerw4a9` |

### Subcontratada Civil — KRROM
| Item | Valor |
|---|---|
| Relação | Subcontratada da ABELV (não contrato direto com Cristália) |
| Contrato KRROM × ABELV | R$ 12.022.696,77 |
| Faturamento Direto (FD) | R$ 7.939.255,02 |
| Escopo | Execução civil de ambos os projetos |

---

## 3. IDs CRÍTICOS DO DRIVE

| Local | ID |
|---|---|
| **Vault raiz** (`ILSON_ENG`) | `1jzX9l751K6oAi3SRYUrFuvcmMHIzPEC3` |
| Emails MD (`07_EMAILS/MD`) | `1uqKwjDAVqB23f-fTnwlC-z-SI9kdhhRj` |
| Índice Mestre | `1S4COoJkthGcC820qLQonauSkB0AnwPWN` |
| MAPA INSTRUÇÕES OPERADOR v4.3 | `199H7kAmtCEKnghjpz4-C_3qJfO5JRcMD` |
| PAINEL OPERACIONAL | `1MKikhr-LNTLKfj5bzFq6PUS4dMyXNvNT` |
| DIÁRIO CONECTOR v10 | `1Q_FjR83uRSiF63PXXx9obVhSyHnQlQlq` |
| CARTA OPERADOR 22/05 | `13Q-zunY87zJeQgbxnsQth13mxi__At42` |
| Mapa Ações 25103 | `1EkKedZmwKEtvpfeTWT_qU0snhD_Tng0U` |
| RSA S20 25103 | `1RLz5n-yPJr25P9hwlSgrkdkNUJqTB2Nn` |
| Histograma BL0 MOD/MOI | `14lKcg6GFUCH-P6wTyvMymv2arz0mSBess` |
| Restrições Consolidadas | `12vDfQoIWsoWMDFzYG6qKdzW720-apBk1` |

### IDs para limpeza (Operador deve deletar)
| Arquivo | ID |
|---|---|
| MAPA v4.2 (antigo) | `1xjHiDRKmmCBhMthDUuxb77np6eKJXHzR` |
| PAINEL temp | `1kc7-I32WiJfTIus89J92K4S0jEy-LlgR` |
| Teste xlsx 22/05 | `11j5T2KvoILEvOB27VDRjHR-EQ0r-X1X8` |
| GESTAO xlsx incompleto 22/05 | `1ftYrNdqAiQWSc2Sz_rLYSy-M03ClbASX` |
| DIALOGO_AGENTES v1 (substituído) | `1oYnZJRM6LhxIIk0gIPDCMZCH9MUfWC35` |
| INBOX_PARA_OPERADOR v1 (substituído) | `16CBqv4j_ZoNuJDzUWm4ULjU6r2fEKt8H` |

---

## 4. ARQUIVOS QUE EU MANTENHO (fonte de verdade)

| Arquivo | Local | Atualizo quando |
|---|---|---|
| `CONTROLE_Restricoes_25103.md` | Drive 02_CAMPO/25103 | A cada sessão com info nova |
| `CONTROLE_Restricoes_25098.md` | Drive 02_CAMPO/25098 | A cada sessão com info nova |
| `GESTAO_RESTRICOES_Cristalia_DDMMYY.xlsx` | Gero localmente → Ilson baixa | Atualização diária |
| `DIARIO_CLAUDE_CONECTOR_v[N].md` | Drive vault raiz + Git | Cada sessão |
| Notas de campo `.md` | Drive 02_CAMPO/[projeto] | Quando Ilson relata evento |
| Registros técnicos `.md` | Drive 02_CAMPO/[projeto] | Quando evento relevante |
| `MAPA_INSTRUCOES_CONECTOR.md` | Drive vault raiz + Git | Este arquivo |

### Arquivos que o OPERADOR mantém (eu não escrevo)
- `PAINEL_OPERACIONAL.md` — inventário do vault
- `MAPA_INSTRUCOES_OPERADOR.md` — manual dele
- RSA semanal
- RDOs (via script)
- Perfis ATOR

---

## 5. REGRAS PERMANENTES

### DEC-17 — SISTEMA DE COMUNICAÇÃO ENTRE AGENTES (criado 24/05/2026)
> **Ler PRIMEIRO em cada sessão — antes de qualquer input do Ilson:**
> 1. `INBOX_PARA_CONECTOR.md` — processar itens pendentes, marcar [LIDO]
> 2. `DIALOGO_AGENTES.md` — responder perguntas do Operador, postar novidades
> 3. `INBOX_PARA_OPERADOR.md` — escrever pedidos/notificações para o Operador
>
> IDs dos 3 arquivos (vault raiz):
> - INBOX_PARA_CONECTOR: `10Je2HqjlSDPqtLb7mHBL1_ByngmNu8ml`
> - INBOX_PARA_OPERADOR: `1T9jnGJk4rOeRJPa2n83H4mio-vm4veuV` (v2)
> - DIALOGO_AGENTES: `1nSk71n2lV1F8csCLeRb3VVoGr-PlCacF` (v2)

### DEC-16 — OBRIGATÓRIO
> **Ao início e ao fim de cada sessão:** lembrar Ilson de TODAS as ações manuais pendentes. Nunca remover da lista sem confirmação explícita dele.

### Nomenclatura de arquivos de campo
`YYYYMMDD_DISC_STATUS_Descricao-Curta.md`
Exemplos:
- `20260522_CIVIL_ALERTA_Krrom-Efetivo-Reduzido.md`
- `20260522_CIVIL_REGISTRO_Krrom-Mobilizacao-Analise-Completa.md`

### Wikilinks obrigatórios em todo `.md` do vault
`[[25098]]`, `[[25103]]`, `[[CIVIL]]`, `[[ABELV]]`, `[[KRROM]]`, `[[NomePessoa]]`

### YAML obrigatório em notas de campo
```yaml
---
projeto: "[[25103]]"
disciplina: "[[CIVIL]]"
empresa: "[[KRROM]]"
status: ALERTA
data: YYYY-MM-DD
semana: S[N]
autor: "[[Ilson]]"
---
```

### Fluxo CONTROLE → GESTÃO (nunca inverter)
```
Campo / Ilson / Emails / ATAs
        ↓
Eu → escrevo CONTROLE.md (fonte de verdade)
        ↓
Eu → gero GESTAO.xlsx via Python
        ↓
Ilson baixa → usa na reunião
        ↓
Operador → pode ler para dashboards complementares
```

---

## 6. COMO GERO CADA ARQUIVO

### `.md` — Drive MCP
```
mcp create_file → parentId: [pasta destino] → textContent: [conteúdo]
```

### `.xlsx` — Python + download
```python
import openpyxl, base64
# gerar workbook
wb.save('/tmp/arquivo.xlsx')
# entregar via SendUserFile
```
> ⚠️ Upload direto de xlsx via MCP ainda não é confiável para arquivos grandes. Usar download local.

### Git — sempre ao final da sessão
```bash
git add .
git commit -m "Descrição clara do que foi feito"
git push -u origin claude/onedrive-access-permissions-WeExM
```

---

## 7. ATORES CONHECIDOS

| Nome | Empresa | Papel |
|---|---|---|
| Ilson | ABELV | Gestor de obra — meu usuário |
| Leobino | ABELV | Engenheiro Civil |
| Tiago | ABELV | Gestor de Projetos |
| Yohanna | ABELV | Engenheira Mecânica |
| Uehara | ABELV | Engenheiro Mecânico HVAC |
| Ana Assis | ABELV | Gerente de Suprimentos |
| Erik Massola | ABELV | Comprador |
| Edimar Cunha | ABELV | (confirmar papel) |
| Diego | KRROM | Gerente de Projetos |
| Rodrigo | KRROM | Técnico de Planejamento |
| Edson | Cristália | (confirmar papel) |
| Celso | ABELV | Gestor de Projetos |
| Rodrigo (KRROM) | KRROM | Téc. Planejamento |

> Perfis completos: solicitar ao Operador criar `.md` para cada ator

---

## 8. SITUAÇÃO ATUAL (atualizar a cada sessão)

**Data:** 22/05/2026 | **Semana:** S21

### 25103 Farmoquímica
- Projeto: 0,21% REAL vs 0,17% PREV → +0,04pp à frente
- Civil KRROM: **3 MOD** — sinal financeiro NÃO emitido
- Gate crítico: **06/08/2026** — Liberação para Escavações
- Marco 1.5.1 INÍCIO ATIV. CIVIL: 0% (não reconhecido)
- Remoção interferências: 15,71% REAL vs 10,39% PREV → adiantado

### 25098 Citostático
- Projeto: 1,20% REAL vs 1,20% PREV → em dia
- Civil Pav. Térreo: 10,97% vs 11,55% PREV → -0,58pp
- Hidrossanitária: 37,15% vs 41,86% PREV → -4,71pp ⚠️
- Civil Radier: 4,35% vs 2,61% PREV → adiantado

### GESTÃO DE RESTRIÇÕES
- **38 restrições** (28 CISTO + 10 FARMO)
- 17 ATRASADO | 5 ALERTA | 8 CONCLUÍDO | 6 NO PRAZO
- Último arquivo gerado: `GESTAO_RESTRICOES_Cristalia_220526.xlsx`

---

## 9. CHECKLIST DE INÍCIO DE SESSÃO

```
[ ] Ler este arquivo (MAPA_INSTRUCOES_CONECTOR.md)
[ ] Verificar AÇÕES MANUAIS PENDENTES do Ilson (DEC-16)
[ ] Perguntar: "O que mudou desde a última sessão?"
[ ] Identificar se há novos RDOs, emails ou eventos a registrar
[ ] Abrir CONTROLE_Restricoes e verificar o que precisa atualizar
[ ] Ao final: atualizar este arquivo com o que mudou
[ ] Ao final: commit + push no git
[ ] Ao final: lembrar Ilson das AÇÕES MANUAIS PENDENTES (DEC-16)
```

---

## 10. AÇÕES MANUAIS PENDENTES — ILSON (DEC-16)

| # | Ação | Status |
|---|---|---|
| 1 | Upload `Restricoes_Consolidadas_Cristalia_22052026.xlsx` → pasta RESTRICOES_DA_REUNIAO (`1mUSv86gHHWGpR3Mj9Em_7W3EjpRFYoxD`) | ⏳ |
| 2 | Upload `20260522_CIVIL_ALERTA_Krrom-Efetivo-Reduzido.md` → Drive 02_CAMPO/25103 | ⏳ |
| 3 | Upload `20260522_CIVIL_REGISTRO_Krrom-Mobilizacao-Analise-Completa.md` → Drive 02_CAMPO/25103 | ⏳ |
| 4 | Baixar `GESTAO_RESTRICOES_Cristalia_220526.xlsx` (entregue nesta sessão) e salvar/compartilhar | ⏳ |
| 5 | Operador: deletar IDs de limpeza (ver seção 3) | ⏳ |
| 6 | Operador: criar perfis ATOR para Ana Assis, Erik Massola, Edimar Cunha, Rodrigo | ⏳ |

---

## 11. ERROS CONHECIDOS E SOLUÇÕES

| Erro | Causa | Solução |
|---|---|---|
| Upload xlsx via MCP corrompido | Arquivo grande + base64 incompleto no tool call | Gerar local → SendUserFile → Ilson baixa |
| Sessão do agente encerra cedo | Limite de tokens do agente background | Ler arquivos manualmente, não via agente |
| Search result overflow do Drive | `search_files` retorna > 100k chars | Salvar em /tmp → processar com Python |

---

*Versão 1.0 — criado em 22/05/2026 — Claude Conector*
*Próxima atualização: início da sessão seguinte*
