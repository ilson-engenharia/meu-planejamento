---
tipo: carta-operacional
de: Claude Conector — Ministro das Pontes Digitais
para: Claude Code — Operador de Cofre
data: 2026-05-22
assunto: Atualização completa da sessão 22/05/2026 — MAPA v4.3 + DEC-16 + Insights de Campo
prioridade: ALTA
---

# CARTA AO CLAUDE OPERADOR DE COFRE
## De: [[Claude Conector]] | Para: [[Claude Operador]] | 22/05/2026

---

> **LEIA ANTES DE QUALQUER COISA:**
> Esta carta substitui todas as cartas anteriores. Ela reflete o estado
> real do vault em 22/05/2026 após uma sessão de atualização completa.
> Leia do início ao fim antes de executar qualquer ação.

---

## 1. O QUE FOI FEITO NESTA SESSÃO (22/05/2026)

Esta sessão foi a mais densa desde a incorporação do Conector. Foram
11 ações executadas, com destaque para a **amarração total entre o
MAPA de Instruções e o BRIEFING Conector** — algo que estava pendente
desde o início.

### Resumo das ações:

| # | O que foi feito | ID no Drive |
|---|---|---|
| 1 | Restrições 22/05 — CONTROLE md depositado no vault | `16CgZBMgU8qad2JjAOT4qW-9teqgTa93z` |
| 2 | BRIEFING v8 seções 5–9 expandidas (LOOP-03 + Obsidian) | `1d2zIdsjC4ztAi1PkN-w2wNpSQ01XxksU` |
| 3 | **MAPA_DE_INSTRUÇÕES v4.3 criado e deployado ao vault** | `199H7kAmtCEKnghjpz4-C_3qJfO5JRcMD` |
| 4 | PAINEL_OPERACIONAL atualizado (v4.3 + DEC-16) | `1MKikhr-LNTLKfj5bzFq6PUS4dMyXNvNT` |
| 5 | DIÁRIO Conector v10 — sessão 22/05 completa | `1Q_FjR83uRSiF63PXXx9obVhSyHnQlQlq` |
| 6 | Git: 4 commits pushados — branch claude/onedrive-access-permissions-WeExM | commit `789475e` |

---

## 2. AÇÕES URGENTES — VOCÊ, OPERADOR, PRECISA FAZER

### 2.1 🔴 DELETAR MAPA v4.2 DO VAULT ROOT

**O MAPA v4.2 antigo ainda está no vault root e precisa ser deletado.**
O v4.3 já está no lugar correto (ID acima), mas o v4.2 continuará
confundindo qualquer agente que ler o vault enquanto não for removido.

```
DELETAR do vault root:
ID: 1xjHiDRKmmCBhMthDUuxb77np6eKJXHzR
Título: MAPA_DE_INSTRUÇÕES_CLAUDE_CODE_OPERADOR_COFRE.md (v4.2)
```

> ⚠️ **SE VOCÊ NÃO CONSEGUIR DELETAR VIA MCP:**
> Ilson, você precisa fazer isso manualmente no Drive Web.
> Entre na pasta ILSON_ENG → localize o arquivo pelo ID acima
> (ou procure o arquivo com data de modificação anterior a 22/05/2026)
> → botão direito → Mover para lixeira.

---

### 2.2 🔴 LIMPEZA GERAL DO MY DRIVE ROOT — 30+ ARQUIVOS TEMPORÁRIOS

Cada sessão do Conector usa a manobra `create (root) → copy_file (vault)`,
o que deixa arquivos temporários acumulados no My Drive root.
A lista abaixo está atualizada até 22/05/2026.

**Delete todos estes IDs do My Drive root:**

| ID | O que é | Sessão |
|---|---|---|
| `1QN5XAxgZwQFvCF0nw2CWWIvkeppxuD0J` | PAINEL temp (MAPA v4.3) | 22/05 |
| `15RP0EqP9HnIAgVIIeCp6XKPelRcYzxrL` | DIÁRIO v10 temp | 22/05 |
| `1-QchXBljOphB_1UcVoSHNEy9Df6qc-2z` | MAPA v4.3 temp | 22/05 |
| `1cEFhDaOnK73-o8__nYYQOXb6QmFTiu7t` | BRIEFING v8 temp (DEC-16) | 22/05 |
| `178e6aHn6UMN46oFgnseqmJjUgD_U9d7I` | DIÁRIO v10 temp (DEC-16) | 22/05 |
| `1H9QpSV5IdarsY-VOXHLZ1oT4JkUZVrFy` | BRIEFING v8 pré-DEC-16 | 22/05 |
| `1cVTvH67dZPBDuijKOVKA0UPo7r2NG3vw` | DIÁRIO v10 pré-DEC-16 | 22/05 |
| `1kc7-I32WiJfTIus89J92K4S0jEy-LlgR` | PAINEL DEC-16 (substituído) | 22/05 |
| `1-AmK6qFanQzXde2lGUdTN-1nfpaE9pzG` | PAINEL pré-DEC-16 | 22/05 |
| `1rdlV4ZjRS7RI5epOg-K2Ir34kt16jbYx` | CONTROLE xlsx temp | 21/05 |
| `18bv-jS4pSObLdyU8uED-Y2IEjSXj6X_A` | CONECTOR xlsx temp | 21/05 |
| `13fVIQfCFEKO5u89jUBZr_vMaE2oczA1k` | CONTROLE md temp | 21/05 |
| `1-dLVpTEsVBHJH0MZI5xG59QG4LGZyhKJ` | CONECTOR md temp | 21/05 |
| `1nctr4OCuLD4jimCbVjv5lgadTvYctAgi` | PAINEL 21/05 (substituído) | 21/05 |
| `1bO2oODrUKzZ76FbulbOIfA5DbweoFp6U` | PAINEL 19/05 | 19/05 |
| `1Rgo604Lv50H-gCnwv-NqMIUscXwkliDV` | DIÁRIO v8 | 19/05 |
| `18njNdLH940Og8J0wZGR8hVmGJxpzFWUm` | BRIEFING v6 | 19/05 |
| `13MFrdzICLc9qbV_dT_QaaE3SE4hGqv8I` | DIÁRIO v6 | 19/05 |
| `1ERQky2zLM7j_isIAlUrdvhyFdClGHX9S` | DIÁRIO v7 | 19/05 |
| `1SR83SjlA-0UN2LYFkHwIw6iZdMxEuzPm` | BRIEFING v4 | 08/05 |
| `1dvjkzxnwipgQ-ucynS1zAuEJH36y4KZU` | PAINEL antigo 07/05 | 07/05 |
| `1pgtMg0gKTg-CH2mdIBGVS1aUIRRwWFyq` | xlsx corrompido | 19/05 |
| `17vtkoMMedqD1ZH1L_gvSRAae-WHY00ML` | RESTRICOES 07/05 v1 | 08/05 |
| `1wgIpBXfqiRYVabRiimBKRY2XfCYhVfzG` | RESTRICOES 08/05 v1 | 08/05 |
| `1PgLDHcMfuj0-yxs1ACtvV5AFhZNLvDq8` | RESTRICOES 12/05 v1 | 19/05 |
| `10BcCgUExulaJHu_qSg9mR1Xzp3nBbhRI` | RESTRICOES 14/05 v1 | 19/05 |
| `1oA_KERcP493JdcIIMiVt8Svmk2TLvtjR` | RESTRICOES 15/05 v1 | 19/05 |
| `1JjiLeCtAnbN21Qof0T7S8S98Z74XYoQ4` | RESTRICOES 19/05 v1 | 19/05 |
| `1c8QxhcLlZl3_JsiOaSklyEUj5rINMUR_` | RESTRICOES duplicata | 19/05 |
| `1IISrEbSHuO74RGbVk-1vrzx_I-txXkrW` | BRIEFING v5 temp | 19/05 |
| `1FmUVH84A19It7YCzN-d6fdVmJL2v7HZ2` | DIÁRIO v7 temp | 19/05 |
| `1foIf2qUdOhEoz-JT3I493UdNOS4zQayw` | PAINEL temp | 19/05 |
| Prefixos `1yL0CkP*`, `1EA6NKf*`, `1ti-n7K*`, `13cq8lO*`, `1MQhDQb*`, `1OQuGH6*` | Temps sessões <19/05 | <19/05 |
| Prefixos `16e9QMz*`, `14q66QU*`, `1D-7ydE*`, `1Kj17uU*` | Temps sessão 07/05 | 07/05 |

> ⚠️ **SE VOCÊ NÃO CONSEGUIR DELETAR VIA MCP:**
> Ilson, abra o Drive Web → no campo de busca pesquise o ID de cada
> arquivo → selecione → Mover para lixeira. Ou vá ao "My Drive" e
> ordene por "Última modificação" — todos os arquivos com nome
> `DIARIO_CLAUDE_CONECTOR_v10.md`, `BRIEFING_CLAUDE_CONECTOR_2026-05-22_v8.md`,
> `PAINEL_OPERACIONAL.md`, `MAPA_DE_INSTRUÇÕES_CLAUDE_CODE_OPERADOR_COFRE.md`
> que estiverem na raiz do My Drive (não dentro de ILSON_ENG) são temporários
> e devem ser deletados.

---

### 2.3 🟡 CRIAR PERFIS DE 4 NOVOS ATORES NO VAULT

Estes atores foram identificados na sessão de 19/05/2026 e ainda não
têm perfil `.md` no vault. Eles aparecem nos registros de restrições
e precisam de wikilink funcional.

Criar em `0.0_ATORES/` de cada projeto relevante:

| Ator | Cargo | Empresa | Projeto | Arquivo sugerido |
|---|---|---|---|---|
| **Ana Assis** | Gerente de Suprimentos | ABELV | 25098 (Cito) | `AnaAssis.md` |
| **Erik Massola** | Comprador | ABELV | 25098 (Cito) | `ErikMassola.md` |
| **Edimar Cunha** | Supervisor de Suprimentos | ABELV | 25098 (Cito) | `EdimarCunha.md` |
| **Rodrigo** | Técnico de Planejamento | Krrom | 25103 (Farmo) | `Rodrigo.md` |

> ⚠️ **ATENÇÃO:** Edimar Cunha (Suprimentos ABELV) é diferente do
> Edimar Mestre de Obras (Krrom). O perfil precisa deixar isso claro
> para não confundir.

---

## 3. DEC-16 — REGRA PERMANENTE (VOCÊ TAMBÉM PRECISA SEGUIR)

> **Esta regra vale para todos os agentes da família, incluindo você.**

A partir de 22/05/2026, toda sessão deve começar e terminar com a
exibição das **AÇÕES MANUAIS PENDENTES** acumuladas para o Ilson.
Nunca remova um item da lista sem confirmação explícita do Ilson.
Acumule os itens — nunca sobrescreva.

**Lista atual de ações pendentes do Ilson:**

| # | Arquivo | Destino no Drive | Sessão | Status |
|---|---|---|---|---|
| 1 | `Restricoes_Consolidadas_Cristalia_22052026.xlsx` | Pasta RESTRICOES_DA_REUNIAO — ID: `1mUSv86gHHWGpR3Mj9Em_7W3EjpRFYoxD` | 22/05 | ⏳ Aguardando Ilson |

> **Ilson:** O arquivo xlsx das restrições de 22/05 está disponível no
> chat com o Conector e no repositório Git (branch
> `claude/onedrive-access-permissions-WeExM`, arquivo
> `Restricoes_Consolidadas_Cristalia_22052026.xlsx`). Você precisa
> fazer o upload manual via Drive Web para a pasta RESTRICOES_DA_REUNIAO.
> O MCP continua rejeitando arquivos .xlsx por bug server-side (base64).

---

## 4. O QUE MUDOU NO MAPA v4.3 — LEIA PARA ENTENDER SUA NOVA VERSÃO

O MAPA v4.3 (seu documento de instruções) foi atualizado para ficar
em sincronismo total com o BRIEFING Conector. As mudanças principais:

1. **Nova seção 2.10** — DECISÕES DO CLAUDE CONECTOR (DEC-12 a DEC-16)
   com referência ao BRIEFING Conector v8 (ID: `1d2zIdsjC4ztAi1PkN-w2wNpSQ01XxksU`)

2. **LOOP-03 expandido** — seção completa com protocolo de 7 passos
   para registro de campo e insights. Aponta para BRIEFING v8 seções 7/8/9.

3. **Seção 8 atualizada** — tabela completa com os 11 códigos de
   disciplina sincronizados com o BRIEFING:
   CIVIL, MECTUB, ELET, HVAC, ESTMET, SMS, SUP, DOC, AUTO, QUAL, PLA

4. **Teia de Aço atualizada** — 10 novos atores adicionados:
   Uehara, Alexandre, Elson, Keite, Ana Assis ⚠️, Erik Massola ⚠️,
   Edimar Cunha ⚠️, Rodrigo ⚠️, Lucas, Edson
   (⚠️ = perfil ainda não criado no vault — item 2.3 acima)

5. **Vault tree atualizado** — inclui BRIEFING Conector v8, DIÁRIO
   Conector v10, pasta RESTRICOES_DA_REUNIAO e marcadores ⚠️ CRIAR
   para os 4 novos atores

6. **Seção 2.1 SAFETY LOOP** — novo item 6: se a sessão envolver
   campo ou restrições, leia o BRIEFING Conector antes de agir

---

## 5. SINTAXE OBSIDIAN — REGRA ATIVA PARA TODOS OS .md DO VAULT

O BRIEFING v8 (seções 8 e 9) define a sintaxe obrigatória para
qualquer arquivo `.md` criado no vault. Como Operador, você precisa
seguir estas regras em qualquer arquivo que criar ou editar:

### YAML frontmatter obrigatório:
```yaml
---
tipo: [tipo do arquivo]
projeto: "[[25098]]"  # ou [[25103]]
disciplina: "[[CIVIL]]"  # código de 2-7 letras
responsavel: "[[NomePessoa]]"
data: YYYY-MM-DD
status: "NO PRAZO | ALERTA | ATRASADO | CONCLUÍDO"
---
```

### Wikilinks obrigatórios no corpo:
- Pessoas → `[[NomePessoa]]` (ex: `[[Leobino]]`, `[[Diego]]`)
- Projetos → `[[Cristália]]`, `[[25098]]`, `[[25103]]`
- Documentos → `[[RE-137]]`, `[[PTS-001]]`

### Footer padrão em todo arquivo:
```
*[[BRIEFING_L99]] | [[INDEX_L99]] | [[Cristália]] | [[CRI_202]] | [[RE-137]] [[RE-138]] [[RE-139]] | [[PTS-001]] [[PTS-002]]*
```

### Nomenclatura de arquivos de campo:
```
YYYYMMDD_DISC_STATUS_DESCRICAO.md
```

---

## 6. ESTADO ATUAL DO VAULT — IDs VÁLIDOS (22/05/2026)

Use esta tabela como referência. Qualquer ID não listado aqui
para estes arquivos é temporário e deve ser deletado.

| Arquivo | ID válido no vault |
|---|---|
| MAPA_DE_INSTRUÇÕES v4.3 | `199H7kAmtCEKnghjpz4-C_3qJfO5JRcMD` |
| BRIEFING Conector v8 | `1d2zIdsjC4ztAi1PkN-w2wNpSQ01XxksU` |
| DIÁRIO Conector v10 | `1Q_FjR83uRSiF63PXXx9obVhSyHnQlQlq` |
| PAINEL_OPERACIONAL | `1MKikhr-LNTLKfj5bzFq6PUS4dMyXNvNT` |
| Restrições 22/05 — CONTROLE md | `16CgZBMgU8qad2JjAOT4qW-9teqgTa93z` |
| Restrições 21/05 — CONTROLE md | `1r02Xg78t7O9j8yhs9YqNt2qn4fIowaPs` |
| Restrições 21/05 — CONTROLE xlsx | `1x8F4ALIi_nwwBgKdpA56xicnsL3o4ZF_` |
| Restrições 21/05 — CONECTOR md | `1MUkdZZX9TrDtxYQAJ00g2zvAmt9C6k6L` |
| Restrições 21/05 — CONECTOR xlsx | `17DzxYpzzL_Ci4m3GFmVrleMahkj01boj` |
| Restrições 19/05 | `1jrDZsTC4ZScknVRsvUQrUaZ0UiIw2heC` |
| Planilha Consolidada 19/05 xlsx | `1TNaw2xDkIy1UNQ1uPVOCXX7iTIJc0VUP` |
| Planilha Consolidada 21/05 xlsx | `15kDiZvYBkdeIz4XkPbpkNfqh5jKuHEIc` |
| Git branch ativo | `claude/onedrive-access-permissions-WeExM` |

---

## 7. LOCAIS DO 02_CAMPO — PARA NOVOS REGISTROS

O Conector deposita insights e observações de campo aqui:

| Projeto | Pasta | ID |
|---|---|---|
| Citostático (25098) | `2.1.1.1.1_CRISTALIA_25098_CITOSTATICO/02_CAMPO/` | `1hGH243jDC7qLWyILNjCFHPIs0ydge4lw` |
| Farmoquímico (25103) | `2.1.1.1.2_CRISTALIA_25103_FARMOQUIMICO/02_CAMPO/` | `14EHc-WjUDx_n5yBjIUPJLSxRuyerw4a9` |

---

## 8. CHECKLIST — O QUE FAZER NESTA SESSÃO (OPERADOR)

Use este checklist ao abrir sua próxima sessão:

- [ ] **Ler** esta carta do início ao fim
- [ ] **Ler** MAPA v4.3 (`199H7kAmtCEKnghjpz4-C_3qJfO5JRcMD`) — sua versão atual
- [ ] **Deletar** MAPA v4.2 do vault root (ID: `1xjHiDRKmmCBhMthDUuxb77np6eKJXHzR`)
- [ ] **Deletar** 30+ arquivos temporários do My Drive root (lista na seção 2.2)
- [ ] **Criar** perfis de 4 novos atores (seção 2.3)
- [ ] **Lembrar o Ilson** das ações manuais pendentes (seção 3 — DEC-16)
- [ ] **Confirmar** com Ilson se o xlsx 22/05 foi feito upload pelo Ilson

---

## 9. LEMBRETE FINAL — DEC-16 (PARA O OPERADOR)

> **Ilson deve ser lembrado no INÍCIO e no FIM de toda sessão sobre
> as ações manuais pendentes. Esta é uma regra permanente da família
> de agentes. Você, Operador, também deve seguir esta regra.**
>
> A lista de pendências está na seção 3 desta carta e no
> PAINEL_OPERACIONAL (`1MKikhr-LNTLKfj5bzFq6PUS4dMyXNvNT`),
> seção "AÇÕES MANUAIS PENDENTES — ILSON FAZ ISSO".
>
> Nunca remova um item sem confirmação explícita do Ilson.

---

*[[MAPA_DE_INSTRUÇÕES_CLAUDE_CODE_OPERADOR_COFRE]] | [[PAINEL_OPERACIONAL]] | [[DIARIO_CLAUDE_CONECTOR]] | [[Cristália]] | [[25098]] | [[25103]]*
*Claude Conector — Ministro das Pontes Digitais → Claude Operador de Cofre | 22/05/2026*
