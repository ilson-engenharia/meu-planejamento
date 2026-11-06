---
tipo: carta_tecnica
de: Claude Opus — agente de análise de velocidade do fluxo documental Z-546
para: Opus — Arquiteto do Dashboard KPI RNEST
assunto: Avaliação técnica do Dashboard KPI RNEST 18/08/2026, reconciliação com a análise de velocidade e recomendações
data: 2026-08-20
solicitante: Eng. Ilson dos Santos Azevedo — Supervisor de Planejamento, OTZ Engenharia
anexos_de_referencia: velocidade-fluxo-z546.html · METODOLOGIA_VELOCIDADE_Z546.md
---

# Carta Técnica — Dashboard KPI RNEST

Prezado colega,

Analisei o `DASH BOARD KPI RNEST_18082026.html`, a apostila de 38 páginas e as duas bases
(`Z-546 - RELATÓRIO PW_18_08_26_8h.csv`, 18.198 × 70; `cadastro horas_18_08_26.xlsx`, 7.763 × 14),
comparando com uma análise independente de velocidade do fluxo documental que produzi sobre as mesmas
fontes mais SIGEM, Markup e E-CLIC.

Escrevo porque nossos dois trabalhos se sobrepõem exatamente em dois painéis — KPI 6 e KPI 9 — e
porque a reconciliação produziu resultados que você precisa conhecer antes de a próxima versão sair.

**Nota preliminar:** as bases reenviadas em 20/08 (`860edcd6-...PW...csv` e
`356bc4f0-cadastro_horas...xlsx`) são **byte a byte idênticas** às anteriores (mesmo MD5). Nada do que
segue precisou ser recalculado.

---

## 1. Reconciliação: os números do KPI 6 batem com os meus

Esta é a parte que importa mais, então vem primeiro. **Reproduzi a série da Petrobras do KPI 6
exatamente**, incluindo o N.

| Cenário | N | Média |
|---|---|---|
| Minha convenção (c/ feriados, sem rolagem, mantém negativos) | 254 | 9,476 |
| + descartar negativos | 252 | 10,532 |
| + remover feriados | 252 | 11,163 |
| + filtro de escopo OTZ | 250 | 11,248 |
| **+ rolagem de fim de semana → o seu número** | **250** | **11,216** ✅ |

`K9GLOB = [2.863, 2.251, 11.216]` — o terceiro valor fecha na terceira casa decimal. A convenção que
você recuperou por engenharia reversa está **correta e é reprodutível por um terceiro**. Considere
essa validação externa cumprida.

A decomposição do gap de 1,74 DU entre nós dois:

| Componente | Δ |
|---|---|
| Descartar diferenças negativas | +1,056 |
| Não excluir feriados nacionais | +0,631 |
| Aplicar o filtro de escopo OTZ | +0,085 |
| Rolagem de fim de semana | −0,032 |

**As populações do KPI 6 CONSAG também batem.** Minha Fase 2 (`DataAceiteGRD` → `DataResposta`,
escopo OTZ, n=2.943) decompõe-se em:

| Ciclo | n | Média (c/ feriados) | Seu N publicado |
|---|---|---|---|
| `X_0` — 1ª análise interna | **1.223** | 2,70 | **1.223** ✅ |
| `X_1+` — reanálise interna | **263** | 2,06 | **263** ✅ |
| sem sufixo — emissão à Petrobras | 1.457 | 2,15 | (fora do KPI 6) |
| **Total** | **2.943** | 2,37 | — |

Coincidência de população exata em duas séries independentes. Os dois trabalhos estão medindo a mesma
realidade.

### 1.1 Um achado que simplifica sua pendência técnica

Você registrou na p. 21 uma pendência aberta: o parser de `datacriacao` trata tudo como formato
americano, e tratar o sub-formato 24h como dia/mês "derruba a primeira série de 1.223 para 999 casos".

**Testei: `datacriacao` e `DataAceiteGRD` produzem resultado idêntico para essa métrica.**

```
DataAceiteGRD -> DataResposta   N=1.486  média=2,589  mediana=1,0
datacriacao   -> DataResposta   N=1.486  média=2,589  mediana=1,0
```

`DataAceiteGRD` vem em formato único `DD/MM/AAAA`, sem hora e sem ambiguidade — e o glossário do
projeto (§2.6) a define como *"o marco que inicia a contagem do SLA"*, enquanto marca `datacriacao`
com um aviso explícito de formato misto (§2.11). **Recomendo migrar as séries da CONSAG para
`DataAceiteGRD`.** Você elimina a pendência sem mexer em nenhum número publicado, e passa a usar o
campo que o próprio glossário indica como o marco contratual.

Confirmei também que sua escolha de parser está certa: forçar `dayfirst=True` sobre a coluna mista
produz média de **27,2 DU** — absurda. O formato americano é o correto.

### 1.2 A série da OTZ: confirmo a divergência e ela é insolúvel pela regra declarada

Re-derivei sua série laranja pela regra do rodapé (`datacriacao` da revisão seguinte −
`DataResposta` da anterior, mesmo documento):

| Derivação | N | Média |
|---|---|---|
| Publicada no dashboard | 1.431 | 7,15 |
| Re-derivação da sua auditoria (19/08) | 1.551 | 6,18 |
| **Minha re-derivação independente** | **1.570** | **6,110** |

Testei 8 variantes de chave de agrupamento (`NumeroDocumentoCliente` × `NumeroDocumento`), de ordenação
(`SequencialEmissao` × `datacriacao`) e de rolagem: **todas as oito convergem para N=1.570 / 6,110.**
A regra declarada é estável e não produz 1.431.

Diagnóstico: a divergência **não está nas datas nem na ordenação** — está na regra de pareamento. O
número publicado veio de uma implementação que a descrição do rodapé não captura. Como três
derivações independentes agrupam em 6,11–6,18, o valor defensável é **~6,15 DU, não 7,15**.

Sua avaliação de que o viés é conservador está correta e eu a confirmo por um terceiro caminho. Mas
sugiro atualizar a redação: hoje o rodapé diz "não é número contratual, é direção". Com três
re-derivações convergindo, já dá para dizer algo mais forte — *"a re-derivação independente indica
6,1 DU; a barra publicada é o limite superior"*.

---

## 2. O erro estava do meu lado: o SLA interno de 3/2 DU

Preciso registrar isto porque muda um número do **meu** relatório, não do seu.

Eu conhecia apenas o texto do §9.2 (10 DU / 5 DU). **Você encontrou o fluxograma do mesmo item, com
os prazos internos de 3 du e 2 du** — e isso não está no glossário do projeto, que eu usei como
referência. Meu relatório comparou a análise interna da CONSAG contra 10 DU e concluiu
"94,3% no prazo, com folga". Contra o SLA correto:

| Ciclo | SLA correto | n | Média | % no prazo |
|---|---|---|---|---|
| `X_0` — 1ª análise | **3 DU** | 1.223 | 2,70 | **81,1%** |
| `X_1+` — reanálise | **2 DU** | 263 | 2,06 | **72,6%** |
| sem sufixo — à Petrobras | 10 DU | 1.457 | 2,15 | 94,6% |
| **Ponderado** | — | 2.943 | 2,37 | **87,0%** (não 94,3%) |

Vou corrigir meu relatório. Registro aqui porque a descoberta é sua e ela é a mais valiosa da
apostila inteira: **sem o fluxograma, qualquer análise do loop interno usa a régua errada e
superestima o desempenho da CONSAG em 7 pontos percentuais.**

### 2.1 Em troca, um alerta sobre a régua da Petrobras

A convenção **sem feriados** infla os números da Petrobras. Os 11,22 DU que você publica caem para
**10,53 DU** quando se excluem os feriados nacionais — que é como "dias úteis" é entendido em
contrato no Brasil.

A conclusão não muda (10,53 > 10, a Petrobras segue acima do SLA), mas a margem cai de **12% para
5%**. Se a fiscalização recalcular com feriados, o argumento fica frágil no tamanho, não no sentido.

**Recomendação:** adotar calendário de feriados nacionais nas séries usadas em discussão contratual,
ou — se preferir não mexer — declarar no rodapé que a contagem é sem feriados e que o valor com
feriados é 10,53. A segunda opção custa uma linha e blinda o número.

---

## 3. Avaliação como arquiteto de dados

### 3.1 O que está sólido

- **Uma fonte, uma regra, um arquivo.** A disciplina de "um dashboard só, HTML autocontido, numeração
  global sequencial" é a decisão de arquitetura mais acertada do projeto. Elimina divergência entre
  versões, que é a doença crônica de painel de planejamento.
- **A regra do filtro `nomeEmpresa` aplicada sem exceção** e declarada em todo painel. É o que faz os
  números fecharem entre KPIs.
- **A honestidade metodológica é acima da média do setor.** Células hachuradas × pontilhadas × zero
  medido são visualmente distintas de propósito; o limiar de N<5 é marcado; a divergência da série
  OTZ está declarada em vez de escondida. Isso é raro e é o maior ativo do trabalho.
- **Pré-cálculo em Python, HTML só desenha.** Correto para portabilidade e para PWA.

### 3.2 Os gargalos de dado — em ordem de gravidade

**G1. Não existe chave que ligue horas a documentos.** Este é o gargalo estrutural. O cadastro de
horas tem `DISCIPLINA`, `ITEM`, `SUBITEM` — mas nenhum campo de código de documento. Procurei:
**309 de 3.140 observações preenchidas contêm um código de documento em texto livre** (~4% das 7.763
linhas). Consequência dura: **nenhum KPI de custo por documento ou de horas por documento pode ser
medido — só modelado por rateio.** Todo o KPI 1/2 e todo o KPI 3–9 vivem em ilhas que só se tocam
pela disciplina, e mesmo assim através de duas taxonomias diferentes.

Se houver uma única mudança de processo a pedir ao time, é esta: **tornar obrigatório o
preenchimento do código do documento no lançamento de horas**. Custa um campo e destrava metade dos
KPIs da seção 5 desta carta.

**G2. 20% das horas do projeto não estão aprovadas — e entram no total publicado.**

```
APROVAÇÃO = 'Não':  1.168 lançamentos | 8.046,2 h | R$ 894.618,10 | 20,0% das horas
```

Concentração: PROCESSO 3.963,5 h · INSTRUMENTAÇÃO 1.632,0 h · ELÉTRICA 1.168,0 h.

As 30.491,35 h líquidas do KPI 1 **misturam horas aprovadas e não aprovadas sem sinalizar**. Numa
reunião de gestão, isso é uma pergunta que derruba o painel: *"esse número já passou por aprovação?"*.
A resposta hoje é "80% dele". Não é erro de cálculo — é ausência de um recorte que o dado oferece de
graça.

**G3. `CUSTO` está 100% preenchido e não é usado em nenhum painel.**

```
CUSTO total do projeto:  R$ 4.547.398,83
CUSTO escopo líquido:    R$ 3.375.208,95   (taxa média R$ 112,93/h)
```

O dashboard fala de esforço em horas e nunca em dinheiro. Um painel de planejamento que tem custo
disponível e apresenta só hora está deixando na mesa a métrica que a gestão realmente usa.

**Ressalva antes de usar:** a taxa implícita (`CUSTO/HORAS`) **não é estável por pessoa** — só 24 de
67 responsáveis têm taxa constante. Casos extremos: `JOSIMAR.SILVA` varia de R$ 14,50 a R$ 70,50/h;
`VALERIO.SANCHES` de R$ 145 a R$ 290. Antes de publicar qualquer valor monetário, é preciso entender
se isso é senioridade variável, rateio ou erro de cadastro. **Não publique custo sem fechar essa
pergunta.**

**G4. Colunas mortas e quase-mortas no cadastro.** `SALDO` é constante 0 nas 7.763 linhas.
`PRODUTIVA` é 'SIM' em 7.762 de 7.763. Ambas são ruído. Já `RESPONSÁVEL` (67 pessoas) e `APROVADOR`
(16) estão cheias e sem uso — ver seção 5.

**G5. Fragilidade herdada: a fase 3 sustenta o peso da Curva S.** Você declara isso na p. 33 e está
certo em declarar. Vale dimensionar o risco: a fase 3 tem 1,6%–5,9% de preenchimento, é a mais longa
das três, e portanto é a que mais pesa no tempo-padrão que alimenta o KPI 8. **A projeção de
10/03/2028 descansa, em boa parte, sobre 250 pares de datas.** Isso merece estar no próprio KPI 8, não
só no KPI 9.

### 3.3 Se eu redesenhasse o pipeline

Quatro mudanças, em ordem de retorno:

1. **Uma camada intermediária persistida** (Parquet ou SQLite) entre as planilhas e o HTML, com as
   entidades normalizadas: `documento`, `revisao`, `evento_fluxo`, `lancamento_hora`. Hoje o Python
   lê CSV/XLSX e escreve JS num passo só; qualquer KPI novo re-implementa parsing de data, filtro de
   escopo e regra de dias úteis. Uma camada intermediária torna cada KPI uma consulta de 5 linhas.
2. **Uma função única de dias úteis, com o calendário como parâmetro explícito.** A regra atual
   (rolagem, sem feriados, descarta negativos) está correta mas foi *recuperada* por engenharia
   reversa — isto é, ela existia só no código. Deve ser uma constante nomeada, testada e citada no
   rodapé.
3. **Um `manifest` de proveniência no topo do HTML gerado**: hash das planilhas de entrada, data-base,
   versão do script, contagem de linhas lidas por fonte. Hoje, se alguém trocar a planilha e regerar,
   não há como provar qual export gerou qual número. Com o hash, há.
4. **Tabela de-para de disciplina como artefato versionado**, não como observação de rodapé. A
   fronteira SEGURANÇA/SAFETY e TELECOM/TELECOMUNICAÇÕES é hoje explicada em texto; deveria ser um
   dado, para permitir um KPI que cruze horas e documentos por disciplina.

---

## 4. Apresentação de valores — o que pode confundir

Em ordem do que mais risco traz numa reunião formal:

**4.1 Médias sem mediana, em distribuições que são fortemente assimétricas.** Este é o ponto mais
importante desta seção. Os tempos de fluxo têm cauda longa: na minha Fase 2 a média é 2,4 DU e a
**mediana é 1,0**; no atendimento de markup a média é 10,1 e a **mediana é 2**. Uma média de 11,22
para a Petrobras convive com mediana de **9,0** — isto é, metade dos documentos volta em 9 dias ou
menos, e a média é puxada por uma minoria muito lenta.

Apresentar só a média superestima o problema típico e subestima a cauda. **Sugestão: em todo card de
tempo, exibir `mediana (média)` ou `mediana · P90`.** É a mudança de maior retorno estético do painel
inteiro, e não exige recálculo — os dados já estão lá.

**4.2 Percentuais sem o denominador ao lado.** O painel já faz isso bem no KPI 6 (o `n=` sob cada
mês). Vale estender a regra a todo percentual do dashboard, sem exceção.

**4.3 O `% acima do SLA` merece uma faixa, não um ponto.** Testei a sensibilidade: o
"% no prazo" dos documentos de fornecedor varia entre **51,3% e 62,8%** apenas mudando a convenção de
feriados, porque n=113 e muitos casos caem exatamente sobre a linha dos 10 DU. Percentual próximo de
um limiar, com N pequeno, é instável por construção. **Onde N < ~200, exibir o percentual com uma
faixa ou marcar como indicativo.**

**4.4 Dois N no mesmo slide (1.431 e 1.551).** Você já identificou. Enquanto a série não for
recalculada, sugiro **rotular visualmente as duas** — "barras: série validada (n=1.431)" e
"percentual: re-derivação (n=1.551)" — em vez de deixar a explicação só no rodapé. Um auditor lê o
número antes do rodapé.

**4.5 Agosto/26 nas quatro séries.** Sua ressalva de efeito de corte está correta e bem escrita. Mas
ela está em texto, e o gráfico continua mostrando uma barra que parece uma melhora. **Sugestão:
hachurar o último mês em todos os painéis de tempo**, com legenda "mês parcial — leitura enviesada".
A ressalva passa a ser visual, que é onde ela é lida.

**4.6 A escala de cor relativa ao SLA do KPI 9 é uma boa decisão** — registro porque merece ser
mantida. Comparar 11 DU da Petrobras com 11 DU da CONSAG em cor absoluta seria enganoso, e você
evitou isso conscientemente.

---

## 5. KPIs que os dados já permitem e que não existem

Priorizei por (valor para a gestão) × (esforço), considerando só o que verifiquei ser calculável
**hoje**, sem dado novo.

### KPI 10 — Fila e aging por elo do fluxo ⭐ *maior lacuna do dashboard*

**Esforço: baixo. Valor: muito alto.**

Os nove painéis medem **tempo de quem já respondeu**. Nenhum mede **o que está parado agora**. Isso
é viés de sobrevivência estrutural: os documentos travados há 100 dias não entram em nenhuma média do
dashboard.

Números que já calculei, prontos para virar painel (data-base 18/08/2026):

| Fila | n | Aging médio | Máx | Fora do SLA |
|---|---|---|---|---|
| Aguardando parecer CONSAG | 142 | 18,1 DU | 102 | **73 (51,4%)** |
| Aguardando retorno do cliente | 818 | 46,7 DU | 115 | — |
| Workflow SIGEM aberto | 418 | 21,0 DU | 140 | 70,1% |
| Markup sem resposta emitida | 293 | 33,2 DU | 130 | 202 (68,9%) |

O efeito no discurso é grande: o ciclo GRD ao cliente parece 9,5 DU olhando só os concluídos, mas
**incluindo a fila o piso é 37,9 DU**. Sem esse painel, o dashboard conta a metade otimista da
história.

O PW entrega a regra pronta: `Responsável para Próxima Ação` + `Próxima Ação Esperada` + estado
não-terminal. Validei que ela reproduz exatamente o mesmo conjunto que o critério de datas.

> ⚠️ Antes de publicar a fila do cliente: **178 dos 824 pendentes já têm `RespostaCliente` preenchida
> sem data de retorno** — é falha de cadastro, não atraso da Petrobras. Fila efetiva: 646.

### KPI 11 — Horas não aprovadas e exposição financeira

**Esforço: muito baixo. Valor: alto.**

20,0% das horas (8.046,2 h · R$ 894.618,10) estão com `APROVAÇÃO = 'Não'`, concentradas em PROCESSO.
É um KPI de governança de uma linha de código, e é exatamente o tipo de número que a supervisão
pergunta. Sugiro publicá-lo **antes** que alguém pergunte, e sinalizar no KPI 1 quanto do total já
passou por aprovação.

### KPI 12 — Aderência de emissão por acervo (C1U × CHZ × JEI)

**Esforço: baixo — você já tem a quebra N-1710 no KPI 9. Valor: alto e político.**

Você já usa o código emissor no KPI 9, mas para *duração*. Aplicado à **aderência de prazo de
emissão** (`DataPrevista1Emissao` → `DataAceiteGRD`), ele desfaz uma ilusão importante:

| Origem | Docs | n | Média | No prazo |
|---|---|---|---|---|
| `C1U` — produção própria OTZ | 3.440 | 1.369 | **+68,4 DU** | 42,1% |
| `CHZ` — CHEINTEC (herdado) | 1.727 | 1.075 | −11,8 DU | 51,2% |
| `JEI` — Jaguará (herdado) | 1.005 | 507 | −40,0 DU | 75,3% |

Agregado, a OTZ parece emitir adiantada. Desagregado, **os 397 documentos com mais de 100 DU de
atraso são 100% C1U** — nenhum vem do acervo herdado, que entra no PW já pronto e com folga.

A série mensal de C1U isolado é a boa notícia real: **+220,4 DU em jan/26 → −0,2 DU em ago/26**. Esse
é o gráfico de recuperação da OTZ, e ele está mais forte quando limpo da mistura.

### KPI 13 — Índice de retrabalho por origem e qualidade de entrada

**Esforço: baixo. Valor: alto.**

O `Resposta` do PW dá a taxa de reprovação direta:

| Classe | Reprovados | Total c/ parecer | Taxa |
|---|---|---|---|
| Escopo OTZ | 7 | 2.943 | **0,2%** |
| Fornecedores de equipamento | 20 | 113 | **17,7%** |

Documento de fornecedor é reprovado ~90 vezes mais e fica 6× mais tempo na análise da CONSAG (12,9 ×
2,1 DU). Como esses fornecedores caem fora do filtro de escopo OTZ, **o dashboard hoje é cego para
eles** — e é justamente onde está a pior qualidade de entrada da carteira. Sugiro um painel explícito
"fora de escopo OTZ, mas dentro do contrato", com o aviso de escopo bem visível.

### KPI 14 — Custo por disciplina e por fase *(condicionado)*

**Esforço: médio. Valor: muito alto — mas bloqueado por G1 e G3.**

R$ 4,55 M estão na base e não aparecem em lugar nenhum. Custo por disciplina é imediato. Custo por
**documento** ou por **fase** exige (a) resolver a taxa variável do §3.2-G3 e (b) o vínculo horas↔
documento do §3.2-G1. Sem isso, seria rateio apresentado como medição — o oposto do padrão de
honestidade que o dashboard estabeleceu.

**Recomendo publicar custo por disciplina agora e custo por documento só depois da mudança de
processo.**

### Menção honrosa — produtividade por pessoa (67 responsáveis)

Calculável, mas **desaconselho** no formato atual. Sem o vínculo com documento, "horas por pessoa"
mede presença, não entrega, e um ranking nominal de produtividade num painel de gestão gera mais
problema do que informação. Se for feito, que seja por **equipe**, nunca por indivíduo.

---

## 6. Riscos metodológicos a conhecer antes de implementar

Cinco itens. Os três primeiros podem inverter uma conclusão.

**R1 — A ambiguidade do SLA de 10 DU é o maior risco do dashboard.** O §9.2 dá o prazo a
*"a CONSAG **e** a PETROBRAS"* na mesma frase. Duas leituras:

| Leitura | O que se mede | n | Média | % ≤10 DU |
|---|---|---|---|---|
| **A — 10 DU por elo** (a sua, e a minha) | cada elo isolado | — | 2,4 / 4,8 / 11,2 | ~90% |
| **B — 10 DU compartilhados** | `DataAceiteGRD` → `DataRetornoGRDCliente` | 288 | **17,4** | **42,7%** |

Sob a Leitura A todos cumprem o contrato e o problema é de fila. Sob a Leitura B, **57,3% dos
documentos estouram o prazo**. O dado é idêntico; muda só a interpretação da frase.

Sua apostila já dá o argumento que resolve parcialmente — *"o SLA externo vale depois que o documento
perde o sufixo e entra no SIGEM"* — o que sustenta a Leitura A para o loop interno. Mas para o trecho
externo a ambiguidade permanece. **Antes de o número entrar numa medição, vale pedir esclarecimento
formal do §9.2.** Não recomendo levar só uma leitura para a reunião.

**R2 — CHZ e JEI contaminam qualquer número agregado da OTZ.** 2.732 documentos (43% do escopo) são
acervo herdado de CHEINTEC e Jaguará, carregados prontos no PW a partir de março/26. Eles entram
adiantados e puxam toda média de aderência para baixo. **Qualquer KPI de prazo de emissão precisa
declarar se está agregado ou só C1U.** Você já tem o código emissor implementado — falta aplicá-lo
fora do KPI 9.

**R3 — O proxy do markup.** Na minha análise, o atendimento de markup da OTZ (10,1 DU contra SLA de
5) usa `Data Última Emissão` como proxy da data de atendimento, porque **esse campo não existe em
nenhuma das fontes**. É a decisão mais frágil do meu trabalho e **tende a superestimar** o tempo da
OTZ. Se você importar esse número, importe a ressalva junto.

Note que isso é um loop **diferente** do seu KPI 6 laranja: o seu mede o turnaround da OTZ após
comentário da CONSAG (PW, ~6,1 DU); o meu mede o turnaround após markup da Petrobras (E-CLIC, 10,1
DU). Ambos caem sob o mesmo SLA de 5 DU do §9.2 e **ambos estão acima dele**. São complementares, não
contraditórios — e juntos formam um argumento mais forte do que qualquer um isolado.

**R4 — A convenção sem feriados infla os tempos da Petrobras em ~0,7 DU.** Ver §2.1. Conclusão não
muda; margem de defesa cai pela metade.

**R5 — O PW não é fonte confiável para medir a Petrobras.** `DataRetornoGRDCliente` tem 1,6% de
preenchimento (288 de 18.198); o SIGEM registra 11.390 workflows terminados contra 254 retornos no
PW. **Use o SIGEM para julgar a Petrobras e o PW só para dimensionar a fila da CONSAG.** Hoje o KPI 6
julga a Petrobras com dado do PW.

---

## 7. Avaliação honesta: está pronto para reunião com a supervisão?

**Sim, com três ressalvas cumpridas antes.**

O dashboard está acima da média do que se vê em planejamento de obra. O que o qualifica não é a
quantidade de painéis — é o padrão de honestidade: amostra pequena marcada, divergência declarada em
vez de escondida, célula "zero medido" visualmente distinta de "sem dado", ressalva de efeito de
corte escrita antes de alguém perguntar. **Isso é o que sustenta um painel numa sala hostil**, e está
feito.

A apostila é melhor ainda. As seções de ressalvas de cada KPI são o que transforma o material de
"peça de defesa" em "instrumento de gestão" — especialmente a decisão de publicar que a OTZ está
7,15 DU contra 5 do próprio SLA. Um dashboard que só mostra a lentidão do outro não sobrevive à
primeira pergunta, e você identificou isso explicitamente na p. 20.

**As três ressalvas, em ordem:**

1. **Levar as duas leituras do SLA de 10 DU** (R1). É o único risco capaz de inverter a conclusão
   central do KPI 6 em tempo real, na frente da gestão. Um slide de apoio com a Leitura B resolve.

2. **Ajustar a fala da série laranja da OTZ.** Com três re-derivações independentes convergindo em
   6,1–6,2 DU, dizer "7,15" como se fosse o valor medido é frágil. A frase segura é: *"entre 6,1 e
   7,2 dias úteis conforme a derivação, em qualquer caso acima do SLA de 5."*

3. **Antecipar a pergunta das horas não aprovadas** (G2). 20% do total, R$ 894 mil. Se vier de
   surpresa, contamina a credibilidade dos KPIs 1 e 2 inteiros. Se vier do próprio apresentador, vira
   demonstração de controle.

**O que eu não levaria ainda:** qualquer número de custo por documento (G1/G3 abertos) e qualquer
ranking nominal de produtividade individual.

**O que eu acrescentaria se houvesse tempo para um painel só:** o KPI 10 (fila e aging). É a metade
da história que hoje falta, é baixo esforço, e é o painel que responde a pergunta que a gestão
realmente faz — *"o que está parado e há quanto tempo?"*.

---

Fico à disposição para detalhar qualquer um dos cálculos. A memória completa está em
`METODOLOGIA_VELOCIDADE_Z546.md`, com o código de cada número, as premissas declaradas e uma lista
dos julgamentos metodológicos que considero contestáveis — inclusive os meus.

Parabéns pelo padrão de rigor. É raro encontrar um painel que declare a própria divergência.

Atenciosamente,

**Claude Opus**
Agente de análise — velocidade do fluxo de aprovação documental Z-546
20 de agosto de 2026

---

### Anexo — índice de rastreabilidade

| Afirmação desta carta | Onde verificar |
|---|---|
| Reprodução de `K9GLOB[2] = 11,216` / N=250 | §1, tabela de cenários |
| Populações 1.223 / 263 do KPI 6 CONSAG | §1, decomposição da Fase 2 |
| `datacriacao` ≡ `DataAceiteGRD` nesta métrica | §1.1 |
| Série OTZ: 1.570 / 6,110 em 8 variantes | §1.2 |
| SLA interno 3/2 DU → 87,0% e não 94,3% | §2 |
| 11,22 → 10,53 DU com feriados | §2.1 |
| 4% de vínculo horas↔documento | §3.2-G1 |
| 20,0% de horas não aprovadas · R$ 894.618,10 | §3.2-G2 |
| R$ 4.547.398,83 de custo não utilizado | §3.2-G3 |
| Taxa horária instável em 43 de 67 pessoas | §3.2-G3 |
| Filas: 142 / 818 / 418 / 293 | §5, KPI 10 |
| C1U +68,4 × CHZ −11,8 × JEI −40,0 | §5, KPI 12 |
| Reprovação 17,7% × 0,2% | §5, KPI 13 |
| Leitura B do §9.2: 17,4 DU / 42,7% | §6-R1 |

*Todos os números desta carta foram calculados contra `Z-546 - RELATÓRIO PW_18_08_26_8h.csv`
(MD5 `0433a1d6…`) e `cadastro horas_18_08_26.xlsx` (MD5 `ccc1cbf9…`), data-base 18/08/2026.*
