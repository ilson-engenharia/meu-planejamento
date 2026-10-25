# /lumina-erp — Skill do Sistema Lumina ERP (Global Service)

> Skill criada a partir do Manual Oficial "Capacitação do sistema Lumina ERP"
> Fonte: e-mail de treinamento de Samuel Toniello (samuel@globalsrv.com.br) — 22/09/2026
> Vídeo de referência: https://www.youtube.com/watch?v=AggPRPuzKNY
> Projeto: EPR Litoral Pioneiro / Global Service Engenharia

---

## O QUE É O LUMINA ERP

O **Lumina ERP** (LuminaIT) é o sistema de gestão de requisições e pedidos da Global Service Engenharia. Ele controla todo o ciclo de compras e contratações, desde a solicitação na obra até o pagamento ao fornecedor.

**Responsável pelo treinamento na obra:** Samuel Toniello (samuel@globalsrv.com.br)  
**Responsável pelo processo na obra:** Giovana Sousa (giovana.sousa@globalsrv.com.br)

---

## FLUXO COMPLETO: REQUISIÇÃO AO PEDIDO

```
REQUISITANTE (obra/escritório)
    ↓
[1] MONTAR/REVISAR REQUISIÇÃO
    ↓
[2] APROVAÇÃO DA REQUISIÇÃO
    ↓ (se aprovado)
[3] SUPRIMENTOS: MONTAR/REVISAR MAPA DE COTAÇÃO
    ↓
[4] APROVAÇÃO DO MAPA DE COTAÇÃO (Gerente Suprimentos)
    ↓
[5] CRIAR/REVISAR PEDIDO PARA APROVAÇÃO
    ↓
[6] APROVAÇÃO DO PEDIDO (Gerente Obra)
    ↓
[7] APROVAÇÃO DO PEDIDO (Gerente Custos)
    ↓
[8] APROVAÇÃO DO PEDIDO (Diretor de Operações)
    ↓ (se aprovado)
[9] ENVIAR PEDIDO PARA O FORNECEDOR
```

---

## 3 ETAPAS PARA CRIAR UMA REQUISIÇÃO

### ETAPA 01 — Projeto Executivo

**O que é:** Ponto de partida da requisição. Baseado no orçamento (Projeto Meta), permite acrescentar/remover insumos conforme a dinâmica da obra.

**Passo a passo:**
1. Verifique se está acessando com o **coletor de custo correto**
2. Acesse o **Projeto Executivo** (via Menu ou Atalho)
3. Na parte superior da tela: selecione a **tarefa/atividade** referente à composição
4. Na parte inferior: selecione a linha da composição
5. Informe **quantidade** e **valor**
6. Repita para múltiplas composições sem sair da tela
7. Ao finalizar, feche o Projeto Executivo — as informações são **salvas automaticamente**

---

### ETAPA 02 — Montar Requisição

**O que é:** Agrupamento lógico das composições. Define como serão separadas para cada requisição (e consequentemente nos pedidos).

> **Atenção:** No caso de requisições de cotação, se o agrupamento não estiver correto, o comprador poderá reagrupar.

**Passo a passo:**
1. Acesse a tela "Montar Requisição" (via Menu ou Atalho)
2. Agrupe as composições conforme necessário
3. Confirme — o sistema cria a requisição e define seu **número único**
4. A confirmação é exibida na tela com o número gerado

---

### ETAPA 03 — Transmitir Requisição

**O que é:** Define o **tipo** da requisição e envia para o fluxo de aprovação.

**Campos obrigatórios em todas as transmissões:**
- Tipo da requisição (ver abaixo)
- Empresa para faturamento (responsável pelo pagamento)
- Campo de observações (use para detalhar a requisição)
- Arquivos anexos (aceita todos os tipos e tamanhos)

**Passo a passo:**
1. Acesse "Transmitir Requisição" (via Menu ou Atalho)
2. Selecione a requisição na parte inferior da tela
3. Selecione o **tipo** da requisição
4. Preencha os campos específicos do tipo (ver abaixo)
5. Insira observações e arquivos anexos se necessário
6. Clique em **Transmitir** — a requisição entra no fluxo de aprovação

---

## 6 TIPOS DE REQUISIÇÃO

### 1. COTAÇÃO
**Quando usar:** Compra de material ou contratação de serviço que precisa passar pelo processo de suprimentos (pesquisa de preços junto a fornecedores).

**Campos:**
- Empresa para faturamento
- Observações e anexos

**Fluxo:** Requisição → Aprovação → Mapa de Cotação → Aprovação → Pedido → Envio ao Fornecedor

---

### 2. REGULARIZAÇÃO
**Quando usar:** A compra já foi feita e o material/serviço já foi consumido — falta apenas o pagamento da NF.

**Campos obrigatórios:**
- Empresa para faturamento
- Condição de pagamento
- Fornecedor (deve estar cadastrado previamente)
- Conta de crédito do fornecedor (DOC/TED) — opcional, pode ser informado depois

---

### 3. PEDIDO DIRETO
**Quando usar:** Contratação ou compra feita diretamente por uma área (EC ou obra), sem passar pelo processo de suprimentos. Também usado para pagamento de contas de consumo.

**Campos obrigatórios:**
- Empresa para faturamento
- Condição de pagamento
- Fornecedor (deve estar cadastrado previamente)
- Conta de crédito do fornecedor — opcional

---

### 4. REEMBOLSO
**Quando usar:** Ressarcimento de funcionário por despesas vinculadas às atividades da empresa.

**Campos obrigatórios:**
- Empresa para faturamento
- Condição de pagamento
- Fornecedor = **o próprio funcionário** (deve estar cadastrado)
- Itens de reembolso: lançar cada recibo/nota com valor

**Como lançar itens de reembolso:**
1. Clicar em "Itens de reembolso"
2. Lançar cada nota/recibo individualmente
3. Fechar a tela após lançar todos os itens

**Resultado:** O sistema gera automaticamente um relatório "Solicitação de reembolso"

---

### 5. CAIXINHA
**Quando usar:** Prestação de contas de despesas pagas com dinheiro de caixinha (área ou obra). Pode ser usada também para repor o saldo do caixinha.

**Campos obrigatórios:**
- Empresa para faturamento
- Condição de pagamento
- Fornecedor
- Recibos/notas das despesas (igual ao reembolso)

---

### 6. FATURA DIRETA
**Quando usar:** Pagamentos que não precisam passar pela liberação fiscal. Após aprovação do pedido, vai direto para o financeiro (pula a análise fiscal).

**Exemplos:** Pagamentos a órgãos públicos, contas específicas.

**Campos obrigatórios:**
- Empresa para faturamento
- Fornecedor (empresa ou órgão público)
- Dados da nota fiscal (lançados automaticamente ao transmitir)

**Atenção:** Ao transmitir, o sistema abre automaticamente a tela de lançamento da nota. Clique em "OK" para enviar ao financeiro após aprovação.

---

## COMO ACOMPANHAR UMA REQUISIÇÃO

Após transmitir, o sistema envia **e-mails automáticos** a cada aprovação, atualizando o status.

**Pesquisa de Requisição — opções:**
1. Pesquisa própria: todas as requisições do seu coletor de custo
2. Pesquisa geral: todas as requisições dos coletores que você tem acesso

**Como acessar:**
- Menu → Pesquisa de Requisições
- Atalho na tela principal

**O que você vê:**
- Número da requisição
- Status atual (em aprovação, aprovado, aguardando suprimentos, etc.)
- Botão "Detalhes" para ver todo o histórico

---

## CONTA DE CRÉDITO DO FORNECEDOR

Para pagamentos via DOC ou TED (módulo de Pagamento Eletrônico), é necessário cadastrar a conta bancária do fornecedor na tela de transmissão.

**Quando informar:** Na transmissão de Pedido Direto, Regularização, Reembolso ou Caixinha.

**Quando não informar:** Pode ser informado posteriormente na consulta de pedidos.

---

## DICAS IMPORTANTES

- **Coletor de custo correto:** Sempre verifique antes de iniciar qualquer requisição
- **Fornecedor não cadastrado:** Antes de fazer requisição de Regularização, Pedido ou Reembolso, o fornecedor DEVE estar no sistema
- **Composições:** Podem ser adicionadas ao Projeto Executivo mesmo que não estejam no orçamento original
- **Agrupamento:** Pense bem no agrupamento na Etapa 02 — facilita o trabalho do comprador
- **Observações:** Sempre preencha o campo de observações com o máximo de detalhes possível

---

## PARA USAR ESTA SKILL

Quando o usuário precisar de ajuda com o Lumina:
- `/lumina-erp criar requisição` → guia passo a passo da Etapa 01 ao 03
- `/lumina-erp cotação` → fluxo específico de cotação
- `/lumina-erp reembolso` → passo a passo de reembolso
- `/lumina-erp acompanhar` → como pesquisar status de uma requisição
- `/lumina-erp` (genérico) → pergunta o que o usuário precisa fazer

---

## REFERÊNCIAS

| Fonte | Conteúdo |
|-------|---------|
| Manual treinamento- Requisição.pptx | 26 slides — processo completo |
| Processo (Suprimentos) - Requisição ao Pedido - R00.pdf | Fluxograma oficial de aprovação |
| Vídeo YouTube | https://www.youtube.com/watch?v=AggPRPuzKNY |
| E-mail origem | Samuel Toniello, 22/09/2026 |
