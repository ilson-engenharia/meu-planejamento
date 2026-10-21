# CARTA DE PASSAGEM — CLAUDE OPERADOR
## Projeto ASU Jundiaí (E-179) | OTZ Engenharia × Messer Gases for Life
### Data: 07/07/2026 | Elaborado por: Ilson do Santos Azevedo

---

## O QUE FOI FEITO NESTA SESSÃO

Olá Claude Operador. Esta carta registra tudo o que foi executado nesta sessão para que você possa continuar o trabalho sem perder nenhum contexto.

### 1. Dashboard LD atualizado — status 07/07/2026

Recebi de Ilson o arquivo `PLDE179PLA340000010_2026.07.07_REPLAN.xlsx` com a LD atualizada.
Rodei o script `gerar_ld_dashboard.py` e gerei o dashboard `OTZ_E179_LISTA_DOCUMENTOS.html`.

**KPIs validados e confirmados:**

| Indicador | Valor |
|-----------|-------|
| Total de Documentos | 524 |
| Documentos Ativos | 419 (80,0%) |
| Documentos Excluídos | 105 (20,0%) |
| DOC. FINALIZADO | 358 (85,4% dos ativos) |
| EM FLUXO | 61 (14,6%) |
| — Em Processo | 40 |
| — Não Iniciados | 21 |
| ATRASADOS (EM FLUXO) | 47 (77,0%) |
| SEM BASELINE | 14 (23,0%) |
| NO PRAZO | 0 |
| **Avanço Físico Ponderado** | **94,46%** |

### 2. Regra permanente estabelecida — NÃO NECESSÁRIO

Descobrimos que 14 documentos têm `status_doc=ATIVO` mas `status=NÃO NECESSÁRIO`.
A regra permanente é: **NÃO NECESSÁRIO é sempre excluído do escopo ativo, independente do campo status_doc.**
Esta regra está implementada no script e documentada na skill `/atualizar-ld`.

### 3. Skill `/atualizar-ld` criada

Arquivo: `.claude/commands/atualizar-ld.md`
Contém todas as regras de negócio permanentes do dashboard LD.

### 4. Arquivos enviados ao cofre (Google Drive)

Pasta do cofre: `ASU_JUNDIAI > 01_PLANEJAMENTO > LD`

| Arquivo | ID no Drive | Status |
|---------|-------------|--------|
| `Dashboard_LD_ASU_Messer_07072026.html` | `1P1jdlz3DsAEzQKGJlvW4b-hZHgdTKtFT` | Enviado |
| `Dashboard_LD_ASU_Messer_07072026.md` | `1jxQvtGcK9_iD7THcfIiJbQbGmMp0QsMl` | Enviado |
| `REGISTRO_DASHBOARD_LD.md` (novo) | `17glaDV8oZt71mBGaA_42paLc71cG8A-A` | Enviado — versão atualizada |

**Ação pendente no Drive:** Ilson precisa deletar o `REGISTRO_DASHBOARD_LD.md` antigo
(ID: `1WxoxyboTJ_V7xab40By3y09iitkrKOp0`) — o novo já está correto.

---

## ONDE COLOCAR OS ARQUIVOS BAIXADOS

Ilson baixou 3 arquivos desta conversa. Veja onde cada um deve ser copiado:

### Arquivo 1: `Dashboard_LD_ASU_Messer_07072026.html`
Copiar para:
```
C:\Users\ilson\OneDrive\Documentos\OTZ\QUALIDADE\DOCUMENTAÇÃO\
```
Também renomear uma cópia como:
```
Dashboard_LD_ASU_Messer_LATEST.html
```
(substituir o arquivo LATEST antigo na mesma pasta)

### Arquivo 2: `Dashboard_LD_ASU_Messer_07072026.md`
Copiar para:
```
C:\Users\ilson\OneDrive\Documentos\OTZ\QUALIDADE\DOCUMENTAÇÃO\
```

### Arquivo 3: `CARTA_PARA_CLAUDE_OPERADOR_07072026.md`
Este arquivo (a carta que você está lendo agora).
Guardar em:
```
C:\Users\ilson\OneDrive\Documentos\OTZ\QUALIDADE\DOCUMENTAÇÃO\
```

---

## ESTADO DO REPOSITÓRIO GIT

- Branch: `claude/onedrive-access-permissions-WeExM`
- Repositório: `ilson-engenharia/meu-planejamento`
- Status: **limpo — tudo commitado e sincronizado**

**Arquivos principais do projeto LD no repositório:**

| Caminho | Função |
|---------|--------|
| `projetos/OTZ_ASU_JUNDIAI/lista_documentos/gerar_ld_dashboard.py` | Script gerador — padrão vigente |
| `projetos/OTZ_ASU_JUNDIAI/lista_documentos/OTZ_E179_LISTA_DOCUMENTOS.html` | Dashboard HTML gerado (última versão) |
| `projetos/OTZ_ASU_JUNDIAI/lista_documentos/ld_finalizados.json` | Histórico de 358 finalizados fixos |
| `.claude/commands/atualizar-ld.md` | Skill com todas as regras permanentes |

---

## REFERÊNCIAS DE CONSISTÊNCIA (para validação futura)

Use estes valores para verificar se a próxima geração está correta:

| Data | Total | Ativos | Excluídos | Finalizados | Avanço |
|------|-------|--------|-----------|-------------|--------|
| 22/06/2026 | 524 | 419 | 105 | 347 | 94,20% |
| 30/06/2026 | 524 | 419 | 105 | 353 | 94,22% |
| **07/07/2026** | **524** | **419** | **105** | **358** | **94,46%** |

**Se Excluídos ≠ 105 ou Total ≠ 524 em qualquer geração futura — verificar a regra NÃO NECESSÁRIO antes de publicar.**

---

## INFORMAÇÕES FIXAS DO PROJETO

| Campo | Valor |
|-------|-------|
| Projeto | ASU Jundiaí — E-179 |
| LD ref. | P-LD-E-179-PLA34-000-001 |
| Cliente | Messer Gases Ltda |
| Project Manager | Eduardo Vessoni |
| Project Leader | Antonio Julião |
| Supervisor GPLAN | Ilson do Santos Azevedo |
| Branch Git | `claude/onedrive-access-permissions-WeExM` |

---

## COMO INICIAR A PRÓXIMA SESSÃO

Quando Ilson enviar uma nova LD atualizada, basta dizer:

> *"Claude, tenho uma nova LD. Use /atualizar-ld"*

O Claude Operador vai:
1. Ler a skill `/atualizar-ld` com todas as regras
2. Atualizar o script com o novo arquivo Excel e data
3. Rodar o script e validar os KPIs
4. Commitar e fazer push para a branch
5. Entregar o HTML para download e subir ao cofre

---

*Carta elaborada em 07/07/2026 por Claude Code — Painel de Controle GPLAN / OTZ Engenharia*
