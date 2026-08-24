# /atualizar-ld — Ciclo de Atualização do Dashboard LD

## Projeto
**ASU Jundiaí (E-179) | OTZ Engenharia × Messer Gases for Life**

---

## O que Ilson envia

Um arquivo Excel atualizado da Lista de Documentos:
- Nome original: `PLDE179PLA340000001_AAAA.MM.DD_*.xlsx` (ou variação)
- Aba: **`LD`** — cabeçalho na linha 8, dados a partir da linha 9

---

## O que o Claude faz automaticamente

1. Atualiza `EXCEL_IN` e `LD_DATA` no script com o novo arquivo e data
2. Roda `gerar_ld_dashboard.py`
3. Valida os KPIs no terminal (Total, Ativos, Excluídos, Finalizados, Avanço)
4. Commita + push para `claude/onedrive-access-permissions-WeExM`
5. Entrega `OTZ_E179_LISTA_DOCUMENTOS.html` para download

---

## Arquivos do projeto LD

| Arquivo | Função |
|---------|--------|
| `projetos/OTZ_ASU_JUNDIAI/lista_documentos/gerar_ld_dashboard.py` | Script gerador — **padrão vigente** |
| `projetos/OTZ_ASU_JUNDIAI/lista_documentos/OTZ_E179_LISTA_DOCUMENTOS.html` | Dashboard HTML gerado |
| `projetos/OTZ_ASU_JUNDIAI/lista_documentos/ld_finalizados.json` | Histórico de finalizados fixos |

---

## Mapeamento de colunas Excel (0-indexado, linha 9+)

| Índice | Campo | Descrição |
|--------|-------|-----------|
| 0 | disc | Disciplina |
| 3 | num_doc | Número do documento |
| 4 | titulo | Título |
| 5 | rev | Revisão (número inteiro) |
| 11 | base_ult | Baseline — última emissão (data) |
| 19 | peso | Peso ponderado |
| 20 | avanco | Avanço % (0–100) |
| 21 | status_doc | Status do documento no escopo: `ATIVO` ou `EXCLUÍDO` |
| 23 | status | Status de fluxo: ver tabela abaixo |

---

## Regras de negócio permanentes

### 1. Excluídos — regra NÃO NECESSÁRIO

> **`NÃO NECESSÁRIO` é sempre excluído do escopo ativo, independente de `status_doc`.**

Alguns documentos podem ter `status_doc=ATIVO` mas `status=NÃO NECESSÁRIO` por ajuste manual na planilha. O script os trata como excluídos.

```python
ativos = [
    d for d in docs
    if str(d.get("status_doc", "")).strip().upper() == "ATIVO"
    and str(d.get("status", "")).strip().upper() != "NÃO NECESSÁRIO"
]
excl_cnt = total_all - len(ativos)
```

### 2. Finalizados fixos

> **Documento que já foi `DOC. FINALIZADO` não pode sair do dashboard em versões futuras.**

O histórico é persistido em `ld_finalizados.json`:
```json
{ "numeros": ["doc-001", "doc-002", ...], "atualizado": "DD/MM/YYYY" }
```
A cada geração, `save_finalizados()` atualiza o arquivo com todos os finalizados do Excel atual.

### 3. Classificação de status

| `status` | Categoria |
|----------|-----------|
| `DOC. FINALIZADO` | Finalizado |
| `AGUARDANDO MARKUP` | EM FLUXO → Em Processo |
| `ATENDER MARKUP` | EM FLUXO → Em Processo |
| `PATEC EMITIDO` | EM FLUXO → Em Processo |
| `EMITIR EMISSÃO INICIAL` | EM FLUXO → Não Iniciados |
| `NÃO NECESSÁRIO` | **Excluído** (mesmo que status_doc=ATIVO) |

### 4. Aderência ao Baseline

Calculada apenas sobre os documentos **EM FLUXO** (não finalizados, não NÃO NECESSÁRIO):

- **ATRASADO**: `base_ult` (col 11) é data < hoje
- **SEM BASELINE**: `base_ult` vazio ou nulo
- **NO PRAZO**: `base_ult` >= hoje

### 5. Retrabalho — Nível de Revisão

Baseado no campo `rev` (col 5, inteiro):

| Valor de `rev` | Categoria |
|----------------|-----------|
| vazio / nulo | Sem Emissão |
| 0 | Sem Revisão (Rev 0) |
| 1 | Sem Retrabalho (Rev 1) |
| ≥ 2 | Com Retrabalho |

Calculado separadamente para **Finalizados** e **EM FLUXO**.

### 6. Avanço Físico Ponderado

Calculado apenas sobre documentos ATIVO (excluindo NÃO NECESSÁRIO) **com peso > 0**:

```
Avanço = Σ(peso × avanco) / Σ(peso) × 100
```
Documentos sem peso são excluídos do cálculo e contados em "sem peso".

---

## Estilo visual — padrão cliente (imutável)

> **Não alterar o estilo sem aprovação do Supervisor de Planejamento (Ilson do Santos Azevedo).**

| Elemento | Valor |
|----------|-------|
| Fundo da página | `#EAECEF` |
| Header | `#C0392B` (vermelho) |
| Subheader | `#004562` (azul escuro) |
| Cards | `white`, borda topo colorida |
| Avanço Físico | `linear-gradient(#004562, #0057A8)`, 72px |
| Tabelas `<th>` | `#004562` |
| Barra progresso verde | `≥ 95%` → `#1E8449` |
| Barra progresso laranja | `85–94%` → `#CA6F1E` |
| Barra progresso vermelho | `< 85%` → `#C0392B` |
| Gráficos | Chart.js 4.4.1 via `cdnjs.cloudflare.com` |
| Logo Messer | base64 JPEG em `/tmp/messer_logo_b64.txt` |

### Seções do dashboard (ordem fixa)

1. **VISÃO GERAL** — Total, Ativos, Excluídos
2. **STATUS DOS DOCUMENTOS ATIVOS** — Finalizados + EM FLUXO (Em Processo / Não Iniciados)
3. **AVANÇO FÍSICO PONDERADO** — painel gradiente azul, % em 72px
4. **ADERÊNCIA AO BASELINE** — Atrasados, Sem Baseline, No Prazo
5. **4 Donuts Chart.js** — G1 Ativos/Excluídos · G2 Status Ativos · G3 EM FLUXO detalhe · G4 Baseline
6. **RETRABALHO** — tabelas Finalizados vs EM FLUXO
7. **Avanço por Disciplina** — barra horizontal Chart.js (canvas c7)
8. **INDICADORES POR DISCIPLINA** — tabela com barras de progresso inline
9. **Footer** — `#1C2833`

---

## Informações fixas do projeto

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

## O que o Claude NÃO muda

- Estilo visual (cores, fontes, layout das seções)
- Nomes de disciplinas
- Regras de negócio acima (só mudam com instrução explícita de Ilson)
- Logo Messer (base64 fixo em `/tmp/messer_logo_b64.txt`)
- Informações fixas do projeto (PM, PL, LD ref.)

---

## Quando Ilson enviar uma nova foto de conclusão

Informar: **Disciplina** e **arquivo da foto**.
O Claude embarca na zona correspondente no script (funcionalidade futura — placeholder ativo).

---

## Referências de consistência

Comparar sempre com o último dashboard gerado:
- `30/06/2026`: Total=524, Ativos=419, Excluídos=105, Finalizados=353, Avanço=94.22%
- `07/07/2026`: Total=524, Ativos=419, Excluídos=105, Finalizados=358, Avanço=94.46%

Se Excluídos ≠ 105 ou Total ≠ 524, verificar a regra NÃO NECESSÁRIO antes de publicar.
