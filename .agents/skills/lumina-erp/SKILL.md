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

---

## WORKFLOW DE APROVAÇÃO — DETALHES

O Lumina possui um **workflow configurável** com múltiplos níveis. Cada nível pode ter:
- Alçadas por valor (ex.: pedidos até R$ 5.000 aprovados pelo Gerente de Obra; acima disso vai ao Diretor)
- Aprovação via **APP mobile** (não precisa estar no computador)
- **Questionamentos eletrônicos**: qualquer aprovador pode registrar perguntas/comentários no histórico do documento

**Aprovações no fluxo padrão de cotação:**

| Etapa | Quem aprova | O que aprova |
|-------|-------------|--------------|
| 1 | Gerente de Obra | Requisição |
| 2 | Gerente de Suprimentos | Mapa de cotação |
| 3 | Gerente de Obra | Pedido |
| 4 | Gerente de Custos | Pedido |
| 5 | Diretor de Operações | Pedido |

> Atenção: o workflow é configurado por empresa/obra. As alçadas e os aprovadores acima podem variar. Consulte o responsável pela configuração do sistema (Samuel Toniello ou Giovana Sousa) para saber o workflow exato da sua obra.

**Como saber em qual etapa está sua requisição:**
1. Acesse "Pesquisa de Requisições"
2. O campo "Status" mostra a etapa atual
3. Botão "Detalhes" → histórico completo com quem aprovou, quando e observações

---

## RASTREAMENTO DE CUSTOS

O Lumina alimenta automaticamente o controle de custos da obra. Entender esse fluxo evita confusão ao ver os valores no relatório:

```
REQUISIÇÃO TRANSMITIDA
    → valor entra em: "Total de Requisição" (apenas comprometimento de intenção)
    ↓
PEDIDO APROVADO
    → valor migra para: "Total de Pedido" (comprometido — já foi autorizado)
    ↓
NOTA FISCAL LANÇADA
    → valor entra em: "Incorrido" (já foi recebido ou executado)
```

**Tipos de custo no relatório:**
- **Comprometido** = pedidos aprovados (Total de Pedido)
- **Incorrido** = notas fiscais lançadas
- **Requisição em andamento** = requisições transmitidas ainda em aprovação

> Regra prática: enquanto a requisição não virar pedido aprovado, o valor fica apenas como "requisição em andamento" — não afeta o comprometido.

---

## FUNCIONALIDADE: REQUISIÇÃO NA NUVEM

Versão simplificada para criação de requisições no campo (celular, tablet):

**Fluxo simplificado:**
1. Requisitante (obra) abre a tabela de serviços e insumos
2. Seleciona os itens e informa as quantidades
3. Requisição criada — aguarda complementação
4. Outra pessoa (back office ou suprimentos) completa a alocação no projeto, detalhes e metas

**Quando usar esta modalidade:**
- Requisições feitas diretamente no campo por responsáveis da obra
- Quando o requisitante não tem acesso ao Projeto Executivo completo
- Urgências onde a alocação pode ser feita depois

---

## SITUAÇÕES ESPECIAIS E ERROS COMUNS

### Nota Fiscal com data anterior ao pedido
O sistema detecta automaticamente quando a NF tem data de emissão anterior à data de aprovação do pedido.

**O que acontece:**
- O sistema exibe um alerta e solicita justificativa
- Opções de justificativa incluem: "Compra direta pela obra", "Regularização de compra anterior"

**Como resolver:**
1. Selecione a justificativa adequada
2. Confirme o lançamento
3. O sistema registra a exceção no histórico

---

### Fornecedor não cadastrado
**Sintoma:** Campo de fornecedor não encontra o CNPJ/nome ao pesquisar.

**Solução:**
- Solicitar cadastro ao setor de Suprimentos antes de criar a requisição
- Informar: razão social, CNPJ, dados bancários (para DOC/TED)
- Não é possível transmitir Regularização, Pedido Direto ou Reembolso sem fornecedor cadastrado

---

### Requisição reprovada — como corrigir e retransmitir
**O que acontece quando reprova:**
- O sistema envia e-mail automático informando a reprovação e o motivo
- A requisição retorna ao status "Pendente de correção"

**Como corrigir:**
1. Acesse "Pesquisa de Requisições"
2. Localize a requisição reprovada
3. Clique em "Detalhes" → leia o motivo da reprovação no histórico
4. Faça as correções necessárias (valores, quantidades, tipo, observações)
5. Retransmita a requisição — ela reinicia o fluxo de aprovação

---

### Coletor de custo errado
**Sintoma:** Requisição lançada no coletor errado — valores aparecem no custo da atividade errada.

**Atenção:** Verificar o coletor de custo é o **primeiro passo** antes de qualquer requisição. Uma vez aprovado e virado pedido, é difícil (ou impossível) corrigir o coletor sem cancelar o pedido.

**Como verificar:** Na tela inicial do Projeto Executivo, o coletor ativo aparece no topo da tela.

---

### Agrupamento incorreto na Etapa 02
**Sintoma:** Requisição chegou ao suprimentos agrupando itens que deveriam estar separados (ex.: materiais de fornecedores diferentes no mesmo grupo).

**Quem pode reagrupar:** O comprador de suprimentos pode reagrupar ao montar o Mapa de Cotação.

**Boa prática:** Ao montar a requisição, agrupar por:
- Tipo de fornecedor (material vs. serviço)
- Disciplina (elétrica, mecânica, civil)
- Urgência (itens críticos em grupos separados)

---

## DICAS PRÁTICAS DO DIA A DIA

### Aprovação pelo celular
- Baixe o **APP Lumina** no smartphone
- Aprovadores recebem notificação push quando há itens para aprovar
- No app: toque no documento → revise → Aprovar ou Reprovar (com comentário)
- Não precisa abrir o sistema no computador para aprovações rotineiras

### Como pesquisar uma requisição antiga
1. Menu → Pesquisa de Requisições → "Pesquisa Geral"
2. Filtros disponíveis: número, data, status, coletor de custo, tipo
3. Para ver TODAS as requisições da obra: use "Pesquisa Geral" em vez de "Pesquisa Própria"
4. Botão "Detalhes": mostra todo o histórico de aprovações, datas e comentários

### Campos de observação — como usar bem
- **Seja específico:** informe o motivo exato da compra, não apenas "material para obra"
- **Boas práticas:** "Compra de X para atividade Y, prevista no cronograma de Z"
- **Para regularizações:** informe a data da compra real e o motivo da regularização
- **Para reembolsos:** informe o nome do funcionário e o evento que gerou a despesa

### Uso de anexos
- Aceita todos os tipos de arquivo (PDF, Excel, foto, etc.)
- **Sempre anexar** NF ou orçamento nas regularizações e pedidos diretos
- Para reembolsos: anexar todos os recibos/notas digitalizadas
- Limite de tamanho: sem restrição declarada, mas prefira PDF comprimido

### Conta de crédito (DOC/TED)
- Pode ser informada na transmissão **ou** depois na consulta de pedidos
- Se não tiver em mãos no momento: transmita sem e informe depois
- Necessária para pagamentos eletrônicos ao fornecedor

---

## VÍDEOS DE TREINAMENTO DISPONÍVEIS

| Vídeo | Link | Conteúdo |
|-------|------|---------|
| Treinamento Parte 01 (oficial Global Service) | https://www.youtube.com/watch?v=AggPRPuzKNY | Fluxo completo de requisição ao pedido |
| Treinamento Parte 03 | https://www.youtube.com/watch?v=WKoy844iKg0 | Parte 3 do treinamento oficial |
| Como criar pedido de faturamento | https://www.youtube.com/watch?v=zd65mK5S7_E | Pedido de faturamento (Lumina Construtoras) |
| Lumina ERP para Construtoras | https://www.youtube.com/watch?v=38WRM682MqI | Visão geral do sistema |
| Controle de parceiros com limite de faturamento | https://www.youtube.com/watch?v=gTr3_Sad-8w | Controle de parceiros por valor |

> Nota: estes vídeos não foram assistidos diretamente (YouTube bloqueado no ambiente de nuvem). Conteúdo desta skill é baseado no manual oficial (26 slides) + PDF de processo + informações do site luminaerp.com.

---

## REFERÊNCIAS

| Fonte | Conteúdo |
|-------|---------|
| Manual treinamento- Requisição.pptx | 26 slides — processo completo |
| Processo (Suprimentos) - Requisição ao Pedido - R00.pdf | Fluxograma oficial de aprovação |
| Vídeo YouTube (Parte 01) | https://www.youtube.com/watch?v=AggPRPuzKNY |
| Vídeo YouTube (Parte 03) | https://www.youtube.com/watch?v=WKoy844iKg0 |
| Site Lumina ERP | https://www.luminaerp.com |
| E-mail origem | Samuel Toniello, 22/09/2026 |
