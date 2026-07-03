# Ciclo de Atualização Push List — OTZ Engenharia / GPLAN
## Projeto ASU Jundiaí (26001) | OTZ × Messer Gases for Life

---

## Padrão vigente

O modelo oficial (visual e estrutura) é o definido na **REV3**, gerado pelo script:

```
gerar_push_list_rev3.py
```

Saídas geradas:
- `DAENG_PUSH_LIST_ASU_JUNDIAI.html` — dashboard interativo (tema dark navy)
- `DAENG_PUSH_LIST_ASU_JUNDIAI.xlsx` — planilha de controle (tema claro, texto escuro)

Não alterar o padrão visual sem aprovação do Supervisor de Planejamento
(Ilson do Santos Azevedo).

---

## Fluxo de atualização (como acionar o Claude)

### O que Ilson envia
Um Excel atualizado — pode ser:
- O arquivo que Lucas (DAENG) devolveu com as datas preenchidas
- Qualquer versão revisada do `DAENG_PUSH_LIST_ASU_JUNDIAI_REV0_CORRE__O.xlsx`

Com mudanças em uma ou mais colunas:
| Coluna | O que muda |
|--------|-----------|
| **Status** | Pendente → Concluído / Em andamento |
| **Previsão** | Datas de entrega prevista (dd/mm/aaaa) |
| **Conclusão** | Data efetiva de conclusão (dd/mm/aaaa) |
| **Peso** | Prioridade 1–5 (quando Caio definir) |

### O que o Claude faz automaticamente
1. Lê o novo Excel (substitui o `EXCEL_IN` no script)
2. Atualiza `LEVAN_DATE` se o levantamento for novo (ou mantém se for só revisão de datas)
3. Recalcula os avanços por card (% = concluídas/total, ponderado por peso)
4. Recalcula todos os KPIs: Avanço Físico, Concluídas, Pendentes, Ações Atrasadas
5. Regenera o HTML e o Excel de saída
6. Commita e faz push para o branch `claude/onedrive-access-permissions-WeExM`
7. Entrega os dois arquivos para download

### O que o Claude NÃO muda automaticamente
- Layout dos cards (fotos, GPS, endereço, horário)
- Nomes dos locais (exceto correções da lista `NOME_FIX`)
- Padrão visual (cores, fontes, gauge, filtros)
- Fotos de levantamento já embarcadas

---

## Informações fixas do projeto

| Campo | Valor |
|-------|-------|
| Projeto | ASU Jundiaí — 26001 |
| Ref. contrato | CLM-216 |
| Contratada | Andrade e Rocha (DAENG) |
| Gerenciadora | OTZ Engenharia — GPLAN |
| Supervisor | Ilson do Santos Azevedo |
| Data de levantamento | 02/07/2026 |
| Branch Git | `claude/onedrive-access-permissions-WeExM` |

---

## Quando adicionar foto de PÓS / REALIZADO

Quando Ilson enviar a foto de conclusão de um local:
- Informar o **Local Nº** (ex: "Local 05") e o arquivo da foto
- O Claude adiciona ao `AREA_META` e embarca na zona "PÓS / REALIZADO" do card
- A zona "ANTES / LEVANTAMENTO" permanece inalterada

---

## Quando ativar a Curva-S

Assim que Lucas preencher as datas de Previsão e Conclusão:
- O Claude gera o gráfico Curva-S (Previsto × Realizado) no lugar do placeholder
- Substituição automática na seção de KPIs do dashboard
