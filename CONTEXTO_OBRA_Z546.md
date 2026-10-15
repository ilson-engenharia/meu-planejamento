---
tipo: base_de_conhecimento_contratual
titulo: Contexto da Obra, Contrato e Cadeia Crítica — RNEST Z-546 / UGH U-36
projeto: RNEST Trem 2 — LOTE D — U-36 (UGH) + SE-3400
contrato_otz: 00025129 (CONSAG × OTZ) · início 05/12/2025
contrato_epc: 5900.0131300.25-2 (PETROBRAS × Consórcio CONSAG UGH)
data_base_dados: 2026-08-17 a 2026-08-19
gerado_em: 2026-08-21
autor: Claude Opus — para Eng. Ilson dos Santos Azevedo, Planejamento OTZ
complementa: TAXONOMIA_COMPLETA_Z546.md · METODOLOGIA_VELOCIDADE_Z546.md · GLOSSARIO_NOMENCLATURA_PW_RNEST.md
cobertura: obra · contrato · escopo · financeiro · marcos · fontes de dados · dependências · cadeia crítica · visão do gestor
---

# Contexto da Obra, do Contrato e da Cadeia Crítica — Z-546

Enquanto o `TAXONOMIA_COMPLETA_Z546.md` é a **planta baixa do dado** e o
`METODOLOGIA_VELOCIDADE_Z546.md` é a **régua de medição do fluxo**, este documento é o
**manual da obra e do contrato**: o que está sendo construído, quem deve o quê a quem, o que
trava o quê, e onde a OTZ está exposta hoje.

Fontes lidas nesta rodada (todas primárias, nenhuma segunda mão):

| # | Documento | O que é |
|---|---|---|
| 1 | `RUGH-PEX-OTZ-EX-U036-PRJ-PT-0002` rev. 0, 26/06/2026, 20 pág. | **Procedimento de Coordenação OTZ × CONSAG** — as regras do jogo |
| 2 | `MD-5290.00-22311-940-PEI-903` rev. 0, 17/07/2023, 14 pág. | **Memorial Descritivo de Projeto da PETROBRAS** — o escopo-mãe e a baseline quantitativa |
| 3 | `RL-5290.00-2000-940-C1U-007` rev. 0, período 21/06→20/07/2026, 21 pág. | **Relatório Mensal de Engenharia** — o retrato gerencial mais recente |
| 4 | `ACF-001_6_250701` rev. R6, 29/06/2026, 3 pág. | **Documentos e Atividades de Planejamento** — a rotina obrigatória do time |
| 5–10 | 6 relatórios brutos (SIGEM ×3, E-CLIC ×3) de 17/08/2026 | Fontes de dados cruas |
| 11 | `LD-5290.00-22311-940-C1U-002` rev. 0_0, 17/08/2026 | **LD de Documentos de Fornecedores** (a "outra LD") |
| — | `LD-5290.00-22311-911-C1U-001` rev. F_0, 19/08/2026 | LD principal — relida aqui só para dependências e cadeia crítica |

> **Convenção:** ✅ verificado contra dado primário · ⚠️ risco/inconsistência · ❓ precisa
> confirmação do Ilson · 🧠 inferência de engenharia (marcada como tal, não é dado).

---

## 1. O que é a obra RNEST Z-546

### 1.1 Em uma frase

A OTZ Engenharia **complementa, corrige e conclui o projeto executivo de uma unidade de
geração de hidrogênio de refinaria que já foi projetada e parcialmente construída**, para que a
CONSAG possa terminar de construí-la e a Petrobras possa partir o Trem 2 da RNEST.

### 1.2 A geografia física

| Camada | Identificação |
|---|---|
| Programa | **RNEST** — Refinaria Abreu e Lima, Ipojuca / PE |
| Gerência Petrobras | **SRGE/SI-IV/RNEST-T2** (Serviços de Implantação — Implantação do Projeto) |
| Fase do empreendimento | **TREM 2** — a segunda linha de refino, retomada após anos parada |
| Lote contratual | **LOTE D** |
| Unidades do Lote D | **U-36 — Unidade de Geração de Hidrogênio (UGH)** + **Subestação SE-3400** |
| Código de área N-1710 | **22311** = U-36 · (`22313` = U-32/UHDT-D, é **outro** lote — ver ⚠️ §6.8) |
| Código do projeto na OTZ | **Z-546** |
| Prefixo CONSAG | **RUGH-** (Refinaria / UGH) |

### 1.3 O que é uma UGH e por que ela importa

Uma Unidade de Geração de Hidrogênio produz H₂ de alta pureza por **reforma a vapor de gás
natural**, seguida de **purificação por PSA** (Pressure Swing Adsorption). O H₂ é o insumo das
unidades de hidrotratamento (HDT/UHDT) — sem UGH, o Trem 2 não hidrotrata, e sem
hidrotratamento não há diesel S-10. **A UGH é uma unidade de utilidade crítica: ela não gera
receita sozinha, mas trava o Trem 2 inteiro se atrasar.** 🧠

Os equipamentos que aparecem nominalmente nos documentos do projeto confirmam essa
arquitetura — ✅ todos extraídos dos títulos reais de RMs, isométricos e desenhos:

| TAG | Equipamento | Papel |
|---|---|---|
| **R-36004** | **Forno reformador** (com queimadores Q-R-36004-025…384 e tubos de catalisador) | Coração da unidade — reforma CH₄ + H₂O → H₂ + CO |
| R-36001 / R-36002 / R-36003 | Reatores (plataformas próprias, estrutura II) | Shift / tratamento |
| V-36001, V-36002, V-36006, V-36007, V-36009, V-36011, V-36012 | Vasos | Separação / acumulação |
| P-36026, P-36027, P-36061, P-36063, P-36064 | Permutadores / resfriadores (casco-tubo, água, start-up) | Recuperação e rejeito de calor |
| B-36002 A/B, B-Z-36004A | Bombas (incl. bomba de solução de fosfato) | Água de caldeira / tratamento |
| TB-C-36001 / TB-C-36002 | Turbo-compressores (com ejetores de descarga e embreagens) | Compressão |
| TQ-Z-36004 | Tanque com agitador | Química |
| Pacote **PSA** | Purificação de H₂ | Produto final |
| **SE-3400** | Subestação | Alimentação elétrica da unidade |

Disciplinas fisicamente presentes: Pipe-rack I e II, cable-rack, plataformas, passarelas,
travessia pipe-rack/pontilhão, fundações, drenagem, pavimentação, SPDA, iluminação,
detecção de gás (CH₄ e H₂), dilúvio e combate a incêndio.

### 1.4 A natureza do serviço — e por que ela define tudo

⚠️ **Este NÃO é um projeto novo.** O MD-903 §6.1 é explícito: o escopo da CONTRATADA é
*"atualizar e complementar o projeto de detalhamento **fornecido pela PETROBRAS**"*.

Consequências práticas que explicam metade dos problemas do projeto:

1. **O Trem 1 é o gabarito.** A U-36 do Trem 2 é gêmea de uma unidade já construída no Trem 1.
   Boa parte do trabalho é **compatibilizar Trem 2 × Trem 1** — 153 linhas da LD trazem
   literalmente esse texto na coluna de restrições ✅ (*"DOCUMENTO EM REVISÃO MAIS AVANÇADA NO
   TREM 1. REQUER VERIFICAÇÃO E ATUALIZAÇÃO NO TREM 2"* × 74; *"Subir a revisão de forma a
   compatibilizá-lo com o documento correlato do Trem 1"* × 43; *"Emitir documento do Trem 2 com
   base no correspondente do Trem 1"* × 36).
2. **O insumo vem de fora e atrasa.** Documento do Trem 1 que não chega vira SDT
   (Solicitação de Documentação Técnica) e para a disciplina. O E-CLIC guarda **17.673
   documentos de referência** recebidos (63% de todo o acervo) ✅, boa parte via GRDs de origem
   `SDT_UGH_RESIDUAL_*`.
3. **A severidade da revisão é contratual, não técnica.** O MD-903 §7.10 classifica cada
   documento a revisar em BAIXO (≤30% de alteração), MÉDIO (30–60%), ALTO (60–100%, aproveita
   só a numeração) e NOVO. 🔴 **A coluna `SEVERIDADE` da LD está 100% vazia** (0 de 2.824
   previstos) — ver §10.3.
4. **As-built é obrigatório até para documento intocado.** MD-903 §18.5: *"Mesmo os documentos
   que não sofreram alteração durante a execução da obra deverão ter suas revisões emitidas
   'conforme construído'"*. Isso é uma segunda onda de emissões, hoje inteiramente à frente.
5. **Bases de dados são entregáveis.** MD-903 §18.7/18.8: COMOS e E3D (AVEVA Everything3D)
   devem ser transferidos consolidados e "passíveis de carga". O modelo 3D não é ferramenta
   interna — **é produto contratual**.

---

## 2. Estrutura contratual completa

### 2.1 A cadeia

```
                    PETROBRAS  (REFINO, GÁS E ENERGIA — SRGE/SI-IV/RNEST-T2)
                        │  Cliente final / dono do ativo / dono do GED SIGEM
                        │  Contrato EPC nº 5900.0131300.25-2
                        ▼
        CONSÓRCIO CONSAG UGH  (também grafado "CONSAG UHDT-D")
        CNPJ 60.490.557/0001-80 — Cabo de Santo Agostinho/PE
                        │  CONTRATANTE da engenharia / dono do GED ProjectWise (PW)
                        │  Responsável Técnico: Gildeon Luiz dos Santos Filho — CREA/RJ 2002103729
                        │  Contrato de prestação de serviços nº 00025129, de 05/12/2025
                        ▼
        OTZ ENGENHARIA LTDA  (CONTRATADA)
        CNPJ 05.016.005/0001-26 — Rua da Quitanda 180, Centro, Rio de Janeiro/RJ
        Local de trabalho: Rua Buenos Aires, 48 — 4º, 5º e 8º andares (RJ)
                        │  Projetista / dono do GED E-CLIC
                        ▼
        FORNECEDORES (ENGEMASA, WEG, ASVOTEC, VIBROPAC, INCASE, VMF, ASHCROFT,
        YOKOGAWA, VALMET, EMERSON, ALUTAL, BAKER HUGHES, IOPE, SPIRAX SARCO, DISMAG, DURCON…)
```

### 2.2 A regra de ouro da comunicação ⚠️

> *"Todas as comunicações, notificações, trocas de informações e/ou solicitações da equipe da
> OTZ destinadas à PETROBRAS devem ser realizadas **exclusivamente por intermédio da CONSAG**.
> A OTZ não deve efetuar contato direto com a PETROBRAS sobre o objeto do contrato, exceto
> quando houver autorização expressa e por escrito da CONSAG. **O descumprimento desta
> orientação poderá implicar na aplicação das penalidades previstas no contrato.**"*
> — Procedimento de Coordenação §7.1

Consequência operacional: a Petrobras é **cliente do dado, não interlocutora**. Toda métrica
de "atraso da Petrobras" que a OTZ produza só tem valor contratual se for endereçada à CONSAG.

Apenas **Comitê Executivo e Diretora de Engenharia** podem assinar correspondência da OTZ
para a CONSAG.

### 2.3 Quem é quem — nomes credenciados ✅

**CONSAG**
| Papel | Nome |
|---|---|
| Gerente de Contrato | Ana Paula Dalariva |
| Gerente de Planejamento da Engenharia e Suprimentos | **Karla de Faria de Carvalho** |
| Coordenador de Projeto | Pedro Ivo Quintana de Oliveira |

**OTZ — organograma do contrato** (Procedimento §5.3.1 + RL mensal)
| Papel | Nome |
|---|---|
| Diretor de Engenharia | Monica Salgado / Gildeon Filho *(as duas versões do organograma divergem — ver ❓ §11)* |
| Gerente de Engenharia | Luiz Nery |
| Coordenador de Engenharia | **Gustavo Lima** |
| **Planejamento de Engenharia** | **Elizabeth Azevedo** ← *a caixa do Ilson* |
| Qualidade e Documentação | Denise Depentor |
| Líder Tubulação | Ricardo Amorim |
| Líder Instrumentação/Automação | Raphael Sant'Ana |
| Líder Elétrica | Davi Gaichi |
| Líder Processo | Enilson Cruz |
| Líder Segurança | Gildeon Filho |
| Líder Mecânica-Fornos | Sylvio Lopes |
| Líder Mecânica Estático | Bruno Lee |
| Líder Mecânica Dinâmico | Edson Amorim |
| Líder Civil | Wellington Santos |
| Líder Arquitetura | Lucilia Divenyi |
| Líder Telecom | Bruno Peixoto |
| Líder ADM 3D (E3D) | Johnes Nunes |
| Líder ADM 2D (CAE) | Rodrigo Aranha |

**Equipe dimensionada: 57 pessoas** ✅ (quadro do RL mensal). Distribuição:
Tubulação 12 · Elétrica 5 · Instr&Aut 5 · COMOS/E3D 5 · **Planejamento 5** · CDA 4 ·
Mecânica 3 · Processo 7 · Gestão Corporativa 3 · Ger./Coord./Adm. 3 · Civil 2 · Segurança 2 ·
Telecom 1 · Coordenação de Projeto 1 · demais.

**Nomes do Planejamento que aparecem no ACF-001** (a rotina real): Bruna, Aline, Léo,
Gilberto, Amanda, Laylla, Pietro, Luiz Sobreira. ❓ Confirmar quem ainda está e quem é o Ilson
no lugar de quem.

### 2.4 Os três GEDs — a espinha dorsal do contrato ✅

| GED | Dono | Papel | Fonte de dado que gera |
|---|---|---|---|
| **E-CLIC** | OTZ | Fluxo interno de elaboração, verificação, aprovação; GRDs | `RELATÓRIO DOCUMENTO`, `RELATÓRIO EMISSÃO`, `RELATÓRIO MARKUP` |
| **PW (ProjectWise)** | CONSAG | Análise e aprovação pela engenharia da CONSAG | `RELATÓRIO PW` (CSV, 70 colunas) |
| **SIGEM** | Petrobras | Emissão oficial, workflow de comentários, **base da medição** | `RELATÓRIO SIGEM`, `SIGEM DOCUMENTOS PREVISTOS`, `SIGEM CONSOLIDAÇÃO` |

> 🔑 **A OTZ é contratualmente responsável por gerir o fluxo nos TRÊS sistemas** (Procedimento
> §9.1 e §9.5), *"incluindo documentos de fornecedores e/ou subcontratados da CONSAG e da
> PETROBRAS que estejam relacionados ao escopo de engenharia da OTZ"*, e pela **tramitação do
> PW da CONSAG para o SIGEM e vice-versa**. Ou seja: quando um documento fica parado entre dois
> sistemas, o ônus operacional é da OTZ mesmo que a culpa não seja.

### 2.5 O fluxo de revisões de documento de projeto ✅

```
Rev. 0_0  →  Emissão Preliminar — PARA COMENTÁRIOS CONSAG          (só no PW)
Rev. 0_1  →  Atendendo Comentários — PARA APROVAÇÃO CONSAG         (só no PW)
Rev. 0    →  EMISSÃO ORIGINAL — "Para Construção" ou "Para Compra" (PW + SIGEM)
              ↓
        PETROBRAS avalia no SIGEM (10 dias úteis)
              ↓ com comentário → nova revisão (A, B, C…) → volta ao ciclo
              ↓ sem comentário → Fluxo Encerrado no SIGEM
        ... ao final da obra → revisão "CONFORME CONSTRUÍDO" (as-built)
```

⚠️ **Regra contratual que muita gente erra:** *"o projeto **não prevê emissão para a Petrobras
com propósito PARA COMENTÁRIOS**, somente PARA CONSTRUÇÃO ou PARA COMPRA"* (Procedimento §9.2).
Todo documento que sobe ao SIGEM já sobe assumindo responsabilidade técnica plena — e o MD-903
§2.2 reforça: *"os comentários realizados pela PETROBRAS não eximem a CONTRATADA da integral
responsabilidade pelo documento"*.

O propósito **"Para Informação" é proibido** para qualquer documento com workflow SIGEM;
só vale para tramitação interna OTZ↔CONSAG.

### 2.6 Prazos contratuais do ciclo documental ✅ (Procedimento §9.2)

| Etapa | Prazo | Responsável |
|---|---|---|
| Comentar ou aprovar documento emitido no SIGEM/PW | **10 dias úteis** | CONSAG e PETROBRAS |
| Analisar comentários e emitir documento revisado | **5 dias úteis** | **OTZ** |

Esse par 10/5 é **a régua contratual** de todo o dashboard de velocidade. Ver
`METODOLOGIA_VELOCIDADE_Z546.md` §8 para as duas leituras possíveis.

### 2.7 O fluxo de documentos de fornecedor — o labirinto das extensões ✅

Regra alinhada em ata de 16/04/2026 (item 25), com base no Anexo VII PB
(`ET-5290.00-22000-91A-1LV-003_Rev.0`):

```
Fornecedor publica no PW
   → CDA OTZ baixa, publica no E-CLIC, inicia fluxo para a disciplina
   → Disciplina OTZ comenta em VERMELHO  →  arquivo  *-OTZ           (sobe ao PW)
   → CONSAG comenta em AZUL sobre o mesmo arquivo → *-OTZ-CONSAG     (volta ao PW)
   → OTZ consolida os dois → *-CI                → arquivo que vai à PETROBRAS
   → PETROBRAS devolve comentários → *-CC
   → OTZ insere comentários PB em VERDE → *-CS   → CDA emite ao FORNECEDOR pelo PW
```

Revisões: `Rev. 0` Emissão original — **Pendente de Certificação** → `Rev. A` Atendendo
comentários — Pendente de Certificação → **Revisão final — Certificado** (carimbo "aceite de
certificado"). Carimbos de voto da OTZ: *sem comentários* / *com comentários* / *recusado*.

⚠️ Nota do próprio procedimento: *"CONSAG não analisará todos os documentos de fornecedores.
Ao receber a LD fará a seleção dos documentos a serem comentados"* — o que significa que a
**LD-940 (LD de fornecedores) é o instrumento que dispara a seleção da CONSAG**.

### 2.8 Numeração — duas identidades obrigatórias para o mesmo papel ✅

| Sistema | Padrão | Exemplo |
|---|---|---|
| **PETROBRAS (N-1710)** | `TT-5290.00-AAAAA-GGG-EEE-NNN` | `IS-5290.00-22311-200-C1U-07309` |
| **CONSAG** | `RUGH-XXX-YYY-EX-U036-DIS-PT-NNNN` | `RUGH-ICF-ENG-EX-U036-TUB-PT-0001` |

Documentação gerencial da OTZ tem numeração própria:
`GRD_OTZ_546_SSSS` · `GRDI_OTZ_Z-546_SSSS` · `AT-Z-546-XXX49-YYYY` (atas) ·
`NR-Z-546-XXX49-YYY` (notas de reunião) · `RDO-Z-546-XXX-AA-DD_MM` ·
`OTZ-Z-546-AAAA-SSS` (cartas). Arquivos: `numeração` + `=` + `revisão`.

**Assunto de e-mail padronizado obrigatório:** `[Z-546 – RNEST - UGH] - [descrição]`.

### 2.9 Trigramas de disciplina oficiais (Procedimento, Tabela 1) ✅

`ARQ` Arquitetura · `CIV` Civil-Concreto · `ELE` Elétrica · `EST` Civil-Est. Metálicas ·
`INF` Civil-Infraestrutura · `INS` Instrumentação & Automação · `INC` Incêndio ·
`GES` Gestão do Projeto · `GER` Geral · `HVA` HVAC · `CLD` Caldeiraria · `FRN` Fornos ·
`DNM` Dinâmicos · `PRO` Processo · `SEG` Segurança · `TEL` Telecomunicações · `TUB` Tubulação ·
`PLA` Planejamento · `QUA` Qualidade · `CDA` CDA

> ✅ Confirma a conclusão do `TAXONOMIA_COMPLETA_Z546.md` §4.2: o **6º campo do CÓDIGO CONSAG é
> a chave canônica de disciplina** — ela é exatamente esta tabela, definida em procedimento
> assinado. Não é convenção interna, é norma do contrato.

### 2.10 Instrumentos formais e o que cada um pode (e não pode) fazer ⚠️

| Sigla | Nome | Emitido por | Pode alterar escopo? |
|---|---|---|---|
| **SIT** | Solicitação de Informação Técnica | OTZ → CONSAG (→ PB) | ❌ **"A SIT NÃO é um instrumento validador para alteração de escopo"** (MD-903 §2.6) |
| **CT** | Consulta Técnica | OTZ | ❌ **"A CT NÃO é instrumento validador para alteração de escopo"** (MD-903 §2.3) |
| **SDT** | Solicitação de Documentação Técnica | OTZ | ❌ — só pede documento existente |
| **NMP** | **Notificação de Mudança de Projeto** | OTZ → Gerente de Contrato CLIENTE | ✅ **Requer aprovação — é o instrumento de mudança** (Anexo I do Procedimento) |
| **Controle de Mudanças de Escopo** | — | Equipe Técnica → Gerente de Contrato OTZ | ✅ instrumento interno de registro |
| **Anexo XV** | Procedimento para Solicitação de Alteração de Escopo Contratual | — | ✅ o rito formal |

🔴 **Esta é a cláusula mais perigosa do contrato para quem trabalha no dia a dia.** A OTZ hoje
tem 55 SITs previstas na LD e o COMOS/E3D incompletos. Toda hora gasta resolvendo lacuna via
SIT **não vira aditivo automaticamente** — precisa migrar para NMP / Anexo XV.

### 2.11 Anexos contratuais Petrobras que regem o trabalho ✅

| Anexo | Assunto | Onde morde o Planejamento |
|---|---|---|
| **VI** | Diretriz de Planejamento e Controle (`ET-5290.00-22000-911-1LV-001`) | Estrutura do cronograma, EAP |
| **VII** | **Diretriz de Engenharia e Documentação Técnica** | Propósitos de emissão, precedência, relatórios BI, controle de markup |
| VIII | Diretriz de Suprimentos | PT / pareceres técnicos |
| X | Diretriz para Gestão da Qualidade | Verificação antes de emitir, NCs, auditorias |
| XIV | Diretriz de Documentação de Engenharia | Tramitação, SIT, entrega final |
| **XV** | **Procedimento para Solicitação de Alteração de Escopo Contratual** | O rito do aditivo |
| XVI | Ferramentas Computacionais e Sistema Integrado de Gestão | COMOS / PDMS-E3D como entregável |
| XVII / XIX | **Relação de Documentos** (`Rev.AD.xlsx`, aba `06 - REFERÊNCIA_PROJETO`) | **A origem da LD** |
| IIA/IIB/IIC/IID | **Planilha de Preços** | **A origem da PPU e da EAP Financeira** |

Normas: **N-381 rev. M** (execução de desenhos) · **N-1710 rev. N** (codificação) ·
**N-2064 rev. D** (emissão e revisão) · N-1913 (RM de equipamento tagueado) · DI-1PBR-00337
(classificação da informação).

---

## 3. Escopo de engenharia — o que a OTZ entrega

### 3.1 As 13 obrigações-mãe (MD-903 §6.1) ✅

1. Projetos de detalhamento
2. Revisão, complementação e eliminação de inconsistências do projeto de detalhamento
3. Análises de risco de processo — **HAZOP, APR e LOPA**
4. Automação de projetos — **CAE 2D**
5. Automação de projetos — **CAE 3D** (AVEVA E3D)
6. Gerenciamento eletrônico de documentos (os três GEDs)
7. Levantamento de quantitativos de projeto (por disciplina, unidade e sistema, **sem folga**)
8. Planejamento e controle
9. Gestão da qualidade de projeto
10. Gerenciamento das interfaces de projeto (**inclui levantamento de campo**)
11. Gerenciamento de mudanças de projeto
12. **Assistência Técnica à fase de Construção e Montagem — com equipe alocada na obra**
13. Emissão do **as-built** ("conforme construído" e "conforme comprado")

Disciplinas nomeadas: Arquitetura, Construção Civil, Elétrica, Instrumentação e Automação,
Telecomunicações, Mecânica, Segurança Industrial, Riscos e Automação de Projetos —
mais Tubulação, Caldeiraria, Fornos, Processo (on-site e off-site), Dinâmicos, HVAC.

### 3.2 A baseline quantitativa contratual 🔑 ✅

MD-903 §7.11 — **este é o número que a Petrobras contratou**, por tipo e severidade:

| Tipo de documento | BAIXO | MÉDIO | ALTO | NOVO | **Total** |
|---|---:|---:|---:|---:|---:|
| **Isométrico (IS)** | **879** | – | – | **46** | **925** |
| Desenho (DE) | 446 | 66 | 29 | 121 | 662 |
| Folha de Dados (FD) | 44 | 59 | 11 | 42 | 156 |
| Especificação Técnica (ET) | 45 | 14 | 3 | 55 | 117 |
| Memória de Cálculo (MC) | 32 | 1 | 10 | 40 | 83 |
| Lista (LI) | 18 | 33 | – | 29 | 80 |
| Relatório (RL) | 2 | 1 | – | 61 | 64 |
| Lista de Documentos (LD) | 19 | 3 | 1 | 20 | 43 |
| Requisição de Materiais (RM) | 32 | – | – | 5 | 37 |
| Parecer Técnico (PT) | 5 | 4 | – | 9 | 18 |
| Memorial Descritivo (MD) | 2 | – | – | 6 | 8 |
| **TOTAL** | **1.524** | **181** | **54** | **434** | **2.193** |

Definições de severidade (MD-903 §7.10):

| Severidade | Critério | Exemplo dado pela Petrobras |
|---|---|---|
| **BAIXO** | até 30% de modificação | Cancelamento, extração do 3D/COMOS, correção de legenda/TAG, refletir última revisão do Trem 1, incorporar marcas de campo |
| **MÉDIO** | 30% a 60% | Refletir última revisão do Trem 1, incorporar marcas de campo |
| **ALTO** | 60% a 100% | Correção total, aproveitando **apenas a numeração N-1710** |
| **NOVO** | documento a elaborar | — |

🔴 **Compare com a realidade:** a LD rev. F_0 prevê **2.824 documentos de projeto + 1.600
IS-955 de construção = 4.424 entregas**, contra **2.193 da baseline contratual**. A diferença é
quase inteiramente isométrico. Ver §4.3 e §10.1.

### 3.3 Os Memoriais Descritivos de escopo por disciplina ✅

Cada disciplina tem seu MD específico — são os documentos que definem "o que exatamente
revisar" e devem estar na mão de cada líder:

| Documento | Disciplina |
|---|---|
| `MD-5290.00-22311-100-PEI-902` | Civil |
| `MD-5290.00-22311-190-PEI-902` | Arquitetura e Urbanização |
| `MD-5290.00-22311-200-PEI-901` | **Tubulações — U-36** |
| `MD-5290.00-22311-300-PEI-902` | Documentação de Equipamentos Dinâmicos |
| `MD-5290.00-22311-422-PEI-901` | **R-36004 (forno reformador)** |
| `MD-5290.00-22311-500-PEI-902` | Caldeiraria |
| `MD-5290.00-22311-700-PEI-901` | Elétrica |
| `MD-5290.00-22311-760-PPT-901` | Telecomunicações |
| `MD-5290.00-22311-800-APJ-901` | Instrumentação |
| `MD-5290.00-22311-940-PEI-901` | Processo **ON**site |
| `MD-5290.00-22311-940-PEI-902` | Processo **OFF**site |
| `MD-5290.00-22311-940-PEI-903` | **Projeto (o guarda-chuva — lido aqui)** |
| `MD-5290.00-22311-940-PEI-904` | **Modelo 3D** |
| `MD-5290.00-22311-940-PEI-905` | Automação de Projetos — CAE 2D |
| `MD-5290.00-22311-947-PEI-901` | Sistemas de Segurança |
| `MD-5290.00-22311-983-PEI-902` | Análises de Risco de Processo |

❓ **Nenhum destes foi lido ainda.** São os documentos que fecham o mapa de dependências
disciplina a disciplina — recomendação forte de leitura na próxima rodada (§11).

### 3.4 Volumes reais por disciplina — LD rev. F_0 (19/08/2026) ✅

Documentos **previstos** (exclui EXCLUÍDO), aba `LD UGH Trem 2`:

| Disciplina OTZ | Previstos | 1ª emissão PW | % | 1ª emissão SIGEM | % | Em atraso (1ª PW) | Finalizados |
|---|---:|---:|---:|---:|---:|---:|---:|
| **Tubulação** | **2.011** | 659 | **33%** | 621 | 31% | 173 | 617 |
| **Instr&Aut** | **228** | 76 | **33%** | 73 | 32% | **53** | 62 |
| Estrutura Metálica | 139 | 139 | **100%** | 139 | 100% | 0 | 139 |
| Elétrica | 134 | 80 | 60% | 76 | 57% | 32 | 73 |
| Processo | 86 | 57 | 66% | 47 | 55% | 28 | 36 |
| Fornos | 47 | 42 | 89% | 14 | 30% | 28 | 12 |
| Engenharia Digital (E3D) | 43 | 19 | 44% | 15 | 35% | 8 | 13 |
| Segurança | 39 | 25 | 64% | 22 | 56% | 4 | 18 |
| Telecom | 29 | 23 | 79% | 24 | 83% | 6 | 17 |
| Caldeiraria | 19 | 10 | 53% | 10 | 53% | 0 | 7 |
| Dinâmicos | 18 | 17 | 94% | 16 | 89% | 1 | 16 |
| Civil | 17 | 11 | 65% | 8 | 47% | 1 | 7 |
| Mecânica / Coordenação / CONSAG / Arquitetura | 14 | 6 | — | 6 | — | 5 | 2 |
| **TOTAL** | **2.824** | **1.164** | **41%** | **1.069** | **38%** | **339** | **1.019** |

Mais a aba `LD Trem 2 -ICs`: **1.600 IS-955 previstos, 241 emitidos no PW (15%)**.

Por tipo de documento (previstos, LD principal): IS 1.778 · DE 503 · RM 153 · PT 92 · MC 83 ·
LI 55 · **SIT 55** · RL 52 · FD 36 · ET 10 · MD 4 · LD 3.

> 🔑 **Tubulação é 71% do projeto em número de documentos.** Somando os IS-955, isométricos
> são **3.378 de 4.424 entregas = 76%**. **Este contrato é, numericamente, um contrato de
> isometria com apêndices.**

---

## 4. Financeiro — PPU, medição e pagamento

### 4.1 A lógica: preço por evento de emissão, não por hora ✅

**PPU = Planilha de Preços Unitários** (Anexos IIA/IIB/IIC/IID do edital). O contrato paga por
**par `TIPO_DOC – ESCOPO`**, a preço unitário fechado:

```
Item da PPU  =  Tipo do Doc  +  " - "  +  ESCOPO(NOVO|REVISÃO)
                  ex.:  "IS - REVISÃO"  ·  "DE - NOVO"  ·  "FD - REVISÃO"
```

Peso/ponderação dos itens: **valor de venda apresentado à CONSAG** (ACF-001) — ou seja, a EAP
Financeira é ponderada por dinheiro, e a EAP Física por objetos (3D/COMOS).

### 4.2 A EAP Financeira — quatro bolsos ✅ (RL mensal, fechamento 20/07/2026)

| Item da EAP | Descrição | Avanço acumulado | Unidade |
|---|---|---:|---|
| **1.** | **SERVIÇOS DE ENGENHARIA** | **31,4%** | — |
| 1.1 | **PARCELAS FIXAS** | 44,4% | VB (verba) |
| 1.2 | **SERVIÇOS DE ENGENHARIA — PROJETO REMANESCENTE** | 26,5% | — |
| 1.3 | **RM / PATEC / ADF** | 30,4% | Global |

**Quadro de valores medidos — julho/2026** ✅

| Item | jul/26 | Acumulado | % Acum. | Valor total implícito 🧠 |
|---|---:|---:|---:|---:|
| Parcela Fixa | R$ 422.791,67 | R$ 3.382.333,33 | 44,44% | ≈ R$ 7,61 M |
| Projeto Remanescente | R$ 1.078.214,91 | R$ 4.393.218,16 | 22,12% | ≈ R$ 19,86 M |
| RM/PATEC/ADF | R$ 31.548,28 | R$ 901.679,92 | 30,37% | ≈ R$ 2,97 M |
| **Total Contrato** | **R$ 1.532.554,86** | **R$ 8.677.231,42** | **28,51%** | **≈ R$ 30,44 M** |
| Infra CONSAG (Adicional) | R$ 28.933,33 | R$ 217.000,00 | 41,67% | ≈ R$ 0,52 M |
| **NMP 3D FORNO/PSA** | R$ 0,00 | R$ 868.935,15 | **100,00%** | R$ 0,87 M (aditivo já 100% medido) |
| **Total (Contrato + Adicionais)** | **R$ 1.561.488,19** | **R$ 9.763.166,56** | **30,29%** | ≈ R$ 32,23 M |

Outros parâmetros contratuais ✅:
- **Adiantamento: 10% do valor do contrato**, com **amortização a partir do BM 09 (agosto/26)**
  — 🔴 **começa AGORA**; o caixa de agosto em diante cai.
- **Retenção CONSAG** aplicada sobre o valor líquido.
- Ciclo: **medição fecha dia 20 → faturamento no mês seguinte → recebimento no mês seguinte ao
  faturamento**. Julho/26 medido → **ago/26 faturado → set/26 recebido** ≈ 60 dias de defasagem.

### 4.3 Consumo da PPU — a exposição contratual 🔴 ✅

Duas fotos, mesma tendência (a segunda é mais recente):

| Item da PPU | Qtde PPU (contrato) | Docs na LD (20/07) | Saldo (20/07) | Docs na LD (19/08) | Saldo (19/08) |
|---|---:|---:|---:|---:|---:|
| **IS - NOVO** | **46** | 534 | **−488** 🔴 | 533 | **−487** 🔴 |
| **IS - REVISÃO** | **879** | 1.245 | **−366** 🔴 | 1.245 | **−366** 🔴 |
| MC - REVISÃO | 44 | 45 | −1 | 46 | −2 |
| RL - NOVO | 61 | 8 | +53 | 17 | (−12 na aba interna ⚠️) |
| DE - NOVO | 121 | 14 | +107 | 20 | +101 |
| DE - REVISÃO | 544 | 492 | +52 | 483 | +61 |
| FD - REVISÃO | 114 | 18 | +96 | 18 | +96 |
| ET - NOVO / REVISÃO | 55 / 62 | 3 / 7 | +52 / +55 | 3 / 7 | +52 / +55 |
| LD, LI, MD, MC-NOVO, FD-NOVO | — | — | positivos | — | positivos |
| **TOTAL** | **2.142** | **2.477** | **−335** | **2.486** | **−446** |

Nota da própria OTZ no RL: *"Esta quantidade de documentos na LD não é final… **Não contempla
RM's, PT's, RL de COMOS e E3D**"* — ou seja, o saldo real é ainda pior do que a tabela mostra.

> 🔴 **Diagnóstico:** o contrato comprou **925 isométricos** (879 revisão + 46 novos). A LD
> prevê **1.778 IS-200 + 1.600 IS-955 = 3.378**. Mesmo contando só os 1.778 da LD principal,
> são **853 isométricos acima do contratado**. É a mesma conta que o MD-903 §7.11 já dizia.
> **O valor total do contrato ainda não foi atingido** (RL) — porque isométrico é o item mais
> barato da PPU (IS-REVISÃO R$ 2.010,59; IS-NOVO R$ 5.744,54, contra DE-NOVO R$ 17.773,67).
> Isso é a armadilha: **a OTZ vai estourar a quantidade sem estourar o valor**, e a CONSAG pode
> argumentar que ainda há saldo financeiro. Ver §10.1.

### 4.4 Gatilhos de medição ✅ (`PADRÃO!AA:AB`, confirmado pela taxonomia)

| Evento | % medido |
|---|---:|
| EMISSÃO LIBERADO — APROVADO PB | **100%** |
| RM EMITIDA NO SIGEM / PT EMITIDO SIGEM / **ADF 1ª EMISSÃO** | **70%** |
| RM APROVADA PB / PT APROVADO PB / **ADF CERTIFICADO** | **30%** |

**Avanço físico do documento**: função escada `0 → 0,5 → 0,7 → 1,0` sobre o `STATUS DO
DOCUMENTO`. As duas réguas são coerentes.

🔑 **A medição depende de emissão no SIGEM, não no PW.** Documento aprovado pela CONSAG mas não
emitido no SIGEM = **0% de receita**. É por isso que os 80 documentos sem pré-carga no SIGEM
(§8.3) são um problema financeiro, não burocrático.

### 4.5 Calendário de medição — a regra dos dois cortes ⚠️

| Regra | Corte | Aplica a |
|---|---|---|
| Período de emissão | dia **20** | agrupamento geral (21 a 20) |
| Medição padrão | dia **6** | todos os tipos **exceto IS** |
| **Medição de isométrico** | dia **19** | **apenas `Tipo do Doc = IS`** |

Errar esse desvio joga ~1.800 isométricos no mês errado de faturamento.

---

## 5. Marcos e prazos — a linha do tempo

### 5.1 Marcos contratuais ✅

| Data | Marco | Fonte |
|---|---|---|
| **05/12/2025** | **Início do contrato 00025129** | RL §1.1 |
| 11/12/2025 | Primeira GRD emitida (`GRDI_OTZ_Z-546_0001` — ata de KOM OTZ×CONSAG) | RL Emissão |
| dez/2025 | **KOM — Kick-off Meeting** | Procedimento §3 |
| 05 e 07/08/2025 | Lista de documentos de projeto executivo rev. "zero" (pré-KOM) | ACF-001 |
| **01/04/2026** | LD_A_0 — **base da curva S atual** (2.852 documentos) | RL §8.2 |
| **05/04/2026** | **Replanejamento entregue** — origem da baseline vigente (BL 1) | RL §8.2 |
| 16/04/2026 | Ata que define o fluxo de documentos de fornecedor (extensões CI/CC/CS) | Procedimento §9.5 |
| jun/2026 | **1ª Auditoria interna — realizada** | RL §10.3 |
| **16/06/2026** | OTZ apresenta reprogramação de Tubulação até fim de ago/2026 | RL §3 |
| **18/06/2026** | CONSAG impõe **metas específicas de Tubulação** até fim de ago/2026 | RL §3 |
| 26/06/2026 | Procedimento de Coordenação rev. 0 emitido (cancela o `PR-…-910-C1U-002`) | Procedimento |
| 29/06/2026 | ACF-001 rev. R6 | ACF |
| **30/06/2026** | **Revisão da LD com programação de Tubulação até abril/2027 — aprovada pela CONSAG** | RL §3 |
| **01/07/2026** | **CONSAG solicita retirada de 98 Folhas de Dados da LD** 🔴 | RL §3 |
| 15/07/2026 | LD-940 (fornecedores) rev. 0 — emissão original para comentários CONSAG | LD-940 CAPA |
| **20/07/2026** | Fechamento do BM de julho — 27,11% real × 28,81% previsto | RL |
| **ago/2026 (BM 09)** | **Início da amortização do adiantamento** | RL §8.3 |
| **21/05/2027** | **Fim da curva de rundown** — último documento previsto (S086) | RL §8.4 |
| **~05/06/2027** | Fim dos 18 meses de engenharia de detalhamento | RL §1.1 |
| dez/2026 e jun/2027 | 2ª e 3ª auditorias internas | RL §10.3 |
| **dez/2027** | Fim da curva S (100%) | RL §8.2 |
| **~05/12/2028** | Fim dos 36 meses de vigência | RL §1.1 |

### 5.2 A curva S contratual (baseline do replanejamento de 05/04/2026) ✅

| Mês | dez-25 | jan-26 | fev-26 | mar-26 | abr-26 | mai-26 | jun-26 | **jul-26** | ago-26 | set-26 | out-26 | nov-26 | dez-26 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **Previsto** | 0,00% | 1,31% | 7,06% | 10,05% | 13,23% | 17,36% | 22,38% | **28,81%** | 37,16% | 45,28% | 53,73% | 63,68% | 71,40% |
| **Realizado** | 0,00% | 1,15% | 5,30% | 8,89% | 13,38% | 17,08% | 22,12% | **27,11%** | — | — | — | — | — |

| Mês | jan-27 | fev-27 | mar-27 | abr-27 | mai-27 | jun-27 | jul-27 | ago-27 | set-27 | out-27 | nov-27 | dez-27 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **Previsto** | 78,55% | 84,02% | 90,22% | 93,14% | 94,48% | 95,76% | 95,76% | 95,76% | 95,76% | 96,36% | 98,94% | 100,00% |

Leitura: **a engenharia acaba em maio/2027 (94,5%); os 5,5% finais são as-built e assistência
técnica arrastados até dez/2027.** O trecho jun-27→set-27 é plano (95,76%) — 🧠 é a janela de
construção/comissionamento em que a OTZ só presta assistência.

⚠️ **O desvio é pequeno em % mas grande em inclinação**: de jul/26 a dez/26 a curva prevista
sobe **42,6 pontos** — mais do que os 28,81 acumulados nos primeiros 8 meses. **O pico do
projeto é agora.**

### 5.3 A curva de rundown de emissões ✅

Escopo de emissões do "Projeto Remanescente — Documentos Conhecidos": **2.740 documentos**,
distribuídos da semana **S019 (dez/25)** até **S086 (21-mai-27)**.

| Semana | Data | Previsto acum. | Real acum. |
|---|---|---:|---:|
| S030 | — | 206 | 206 |
| S040 | — | 575 | ~570 |
| **S043** | **24-jul-26** | **796** | **678** |
| S048 | 28-ago-26 | 1.159 | — |
| S052 | 25-set-26 | 1.422 | — |
| S057 | 30-out-26 | 1.745 | — |
| S061 | 27-nov-26 | 1.953 | — |
| S065 | 25-dez-26 | 2.148 | — |
| S073 | 19-fev-27 | 2.449 | — |
| S086 | 21-mai-27 | **2.740** | — |

Gap na foto de julho: **118 documentos atrás da curva** (678 × 796 = 85,2% de aderência).

---

## 6. Fontes de dados mapeadas

### 6.1 Visão geral — 8 fontes, 3 sistemas

| # | Arquivo | Sistema | Linhas | Colunas | Data-base | Chave |
|---|---|---|---:|---:|---|---|
| 1 | `Z546_RELATÓRIO_DOCUMENTO.xlsx` | E-CLIC | **27.774** | **49** | 17/08/2026 | `Código` |
| 2 | `Z546_RELATÓRIO_EMISSÃO.xlsx` | E-CLIC | 5.877 | 16 | 17/08/2026 | `Número GRD` + `Código` |
| 3 | `Z546_RELATÓRIO_MARKUP.xlsx` | E-CLIC | 3.517 | 14 (header duplo!) | 17/08/2026 | `MK_CodSec` + `DOC_Codigo` |
| 4 | `Z546_RELATÓRIO_PW.csv` | PW | ~18.200 | 70 | — | `N-1710` + `Revisao` |
| 5 | `Z546_RELATÓRIO_SIGEM.xlsx` | SIGEM | **13.461** | 28 | 17/08/2026 | `Documento` + `Revisão` |
| 6 | `Z546_RELATÓRIO_SIGEM_DOCUMENTOS_PREVISTOS.xlsx` | SIGEM | **21.729** | 17 | 17/08/2026 | `DOCUMENTO` + `REVISAO` |
| 7 | `Z546_RELATÓRIO_SIGEM_CONSOLIDAÇÃO_TODAS_AS_REVISÕES.xlsx` | SIGEM | **9.777** | 19 | 17/08/2026 | `Documento` + `Revisão` |
| 8 | `LD-…-940-C1U-002` (LD de Fornecedores) | consolidado | 362 | **75** | 17/08/2026 | `NÚMERO N-1710` |

### 6.2 🔑 Descoberta central: os relatórios avulsos são MUITO maiores que as abas da LD

| Aba dentro da LD-911 | Linhas | Relatório avulso equivalente | Linhas | Fator |
|---|---:|---|---:|---:|
| `RL DOCS` (29 col.) | 4.914 | `RELATÓRIO DOCUMENTO` (**49 col.**) | **27.774** | **5,7×** |
| `RL_EMISSAO` (12 col.) | 5.833 | `RELATÓRIO EMISSÃO` (16 col.) | 5.877 | 1,0× |
| `RL_MARKUP` (12 col.) | 1.769 | `RELATÓRIO MARKUP` (14 col.) | 3.517 | 2,0× |
| `RL_Sigem` (21 col.) | 1.186 | `RELATÓRIO SIGEM` (**28 col.**) | **13.461** | **11,3×** |
| `RL_Previsto_Sigem` (19 col.) | 5.746 | `SIGEM DOCUMENTOS PREVISTOS` | **21.729** | 3,8× |
| — (não existe na LD) | — | **`SIGEM CONSOLIDAÇÃO TODAS AS REVISÕES`** | **9.777** | **∞ — fonte inédita** |

> A LD recebe versões **pré-filtradas** dos relatórios. Isso é bom para a LD (evita ruído) e
> **péssimo para análise**: tudo o que foi filtrado fora — inclusive todo o universo de
> construção e montagem da CONSAG — some do radar. O sistema autônomo deve consumir os
> **relatórios avulsos completos** e aplicar os filtros de forma explícita e auditável.

### 6.3 Ficha de cada fonte

---

#### 📄 `RELATÓRIO DOCUMENTO` — E-CLIC (27.774 × 49) — *o cadastro-mestre da OTZ*

**O que é:** todo objeto que existe dentro do E-CLIC — documento de produto, documento de
referência recebido, markup, GRD, relatório externo.

**Cobertura:** `Data Importação` 09/12/2025 → 17/08/2026 · `Data da Última Emissão`
22/12/2025 → 17/08/2026.

**Composição por diretório de 1º nível** ✅ — *isto explica o tamanho:*

| Diretório | Linhas | O que é |
|---|---:|---|
| `06. DOCUMENTOS DE REFERÊNCIA` | **17.673** | Acervo recebido (Trem 1, cliente, CONSAG) — **63,6%** |
| `04. DOCUMENTO PRODUTO` | **4.699** | **O que a OTZ produz** — 4.694 códigos únicos |
| `10. GRD` | 2.233 | Guias de remessa |
| `07. MARKUP` | 1.788 | Markups recebidos |
| `15. RELATÓRIOS EXTERNOS` | 488 | SIGEM (366) + ProjectWise (122) |
| `05. SUPRIMENTOS` | 452 | PTs, documentos de fornecedor |
| `02. GESTÃO DO PROJETO` | 246 | Atas, correspondência |
| `12. GRD CLIENTE` | 102 | GRDT SIGEM |
| `03. PLANEJAMENTO` / `09. QUALIDADE` / `01. GERAL` | 93 | — |

**Dentro de `04. DOCUMENTO PRODUTO`:** Tubulação domina — isométrico de construção 1.838 ·
revisados-tubulação 1.423 · novos-tubulação 566 = **3.827 de 4.699 (81%)**.

**Colunas exclusivas desta fonte (não existem em lugar nenhum):**
`Folhas` (7.291 preenchidas — **volume real de páginas**, insumo de esforço) ·
`Formato do Documento` (A0/A1/A2/A4) · `Responsável da Atividade` (nominal) ·
`Data Início Fluxo` / `Data Fim Fluxo` / `Data da Última Atividade` (**ciclo interno da OTZ**) ·
`Data Recebimento Markup` + `Tipo Markup` + `Revisão Recebimento Markup` ·
`número rm` + `fornecedor` (vínculo documento↔pacote de compra) ·
`grd origem` (13.237 — rastreia de qual SDT veio cada referência) ·
`PDF atualizado?` e `Conteúdo extraído?` (saúde do repositório).

**Colunas 100% vazias (armadilha):** `Status Emissão`, `Finalidade Próxima Emissão`,
`Data Planejada Último Markup`, `Data Recebimento as Built`, `Data Atendimento as Built`,
`baseline`, `cód atividade`, `hh estimado`, `hold`, `qtd hold`, `área`.
⚠️ **`hold` e `hh estimado` vazios** = o E-CLIC tem os campos, mas ninguém preenche. Oportunidade.

**Quando usar:** esforço por documento (folhas × formato), ciclo interno OTZ, quem está
com o quê, rastreio de referência recebida, vínculo RM↔fornecedor.

---

#### 📄 `RELATÓRIO EMISSÃO` — E-CLIC (5.877 × 16) — *o livro-caixa das GRDs*

**O que é:** uma linha por (GRD × documento). **2.231 GRDs** distintas emitidas entre
11/12/2025 e 17/08/2026. Prefixos: `GRD_` 3.180 (externa) · `GRDI_` 2.697 (interna).

**Emissões por mês** ✅ — a curva de produção real:
dez/25 **15** · jan **284** · fev **283** · mar **573** · abr **656** · mai **902** ·
jun **871** · **jul 1.327** · ago (até 17) **966**.

**Finalidades:** Para Providências 1.897 · Para Construção 1.679 · Para Aprovação 1.024 ·
Para Informação 747 · Para Compra 238 · Para Esclarecimento 123 · Certificado 19 · Recusado 1.

**Disciplinas:** Tubulação 2.216 · Estr. Metálica 666 · Mecânica 643 · Geral 518 ·
Instrumentação 463 · Processo 385 · Elétrica 376 · Segurança 184 · CAE-CAD 126 · Telecom 108 ·
Planejamento 93 · Civil 43.

**Único aqui:** `Destinatários` (136 combinações — quem recebe o quê) e `Observação`
(3.742 preenchidas — texto livre com o histórico das exceções, ex.: *"MARKUP RECEBIDO POR
E-MAIL"*, *"LETs emitidas novamente na revisão 0"*).

**Quando usar:** contar emissões por período (é a fonte mais confiável de "saiu do E-CLIC"),
auditar destinatários, reconstruir histórico de exceções.

---

#### 📄 `RELATÓRIO MARKUP` — E-CLIC (3.517 × 14) — *os comentários recebidos*

⚠️ **Header em DUAS linhas** (grupo `Markup` / grupo `Documento`) — ler com `header=1` e
renomear. 14 colunas reais: 6 do markup + 8 do documento associado.

**1.113 markups distintos** em **1.747 arquivos**, ligados a 1.786 documentos, entre
06/01/2026 e 17/08/2026.

**Classificação** ✅: `07.01. APROVADO` 2.759 · `07.02. APROVADO COM COMENTÁRIOS` 708 ·
`07.03. RECUSADO` 50.

**Por mês:** jan 214 · fev 170 · mar 253 · abr 415 · mai 579 · jun 496 · **jul 772** · ago 618.

⚠️ **1.764 linhas têm `DOC_Disciplina = NÃO SE APLICA`** — são as linhas de GRD, não de
documento. **Devem ser removidas** antes de qualquer estatística (já documentado em
`METODOLOGIA` §2.4). Markups efetivamente ligados a documento de produto: **1.630 linhas,
1.070 documentos distintos**.

**Quando usar:** taxa de retrabalho, IDR (índice de documentos recusados), tempo de
atendimento de markup, disciplinas mais comentadas.

---

#### 📄 `RELATÓRIO SIGEM` (Consulta Geral) — (13.461 × 28) — *o universo Petrobras*

**O que é:** consulta geral do SIGEM sobre a UGH U-36 **inteira** — não só a engenharia.

🔑 **Composição por Nível 2** — a chave para filtrar:

| Nível 2 | Linhas | De quem é |
|---|---:|---|
| **`03.REPARO`** | **10.179** | **CONSAG — inspeção de recebimento de material. NÃO é da OTZ.** |
| `01.IMPLANTAÇÃO` | 1.219 | Mobilização, procedimentos, planos |
| **`04.ENGENHARIA`** | **1.116** | ✅ **É AQUI que mora a OTZ** |
| `15.GESTÃO CONTRATUAL` | 191 | Medição, documentos gerais |
| `12.SMS` | 179 | Segurança/meio ambiente CONSAG |
| `06.MONTAGEM ELETROMECÂNICA` | 177 | Obra |
| `13.PLANEJAMENTO` | 162 | Cronogramas, programações |
| `17.DOCUMENTOS FORNECEDOR` | 102 | DFs |
| demais | 136 | — |

> ⚠️ **Sem o filtro `Nível 2 = '04.ENGENHARIA'`, 92% do que você conta não é seu.** Quem
> reportar "13.461 documentos no SIGEM" está errado por um fator de 12.

**Dentro de `04.ENGENHARIA` — 1.116 linhas / 1.005 documentos únicos** ✅:

| Nível 3 | Linhas | | Tipo | Linhas |
|---|---:|---|---|---:|
| `04.Z.TUBULAÇÃO` | **569** | | Isométrico | **534** |
| `04.J.ESTRUTURA METÁLICA` | 162 | | Desenho | 255 |
| `04.H.ELÉTRICA` | 91 | | Requisição de Material | 186 |
| `04.O.INSTRUMENTAÇÃO` | 85 | | Memória de Cálculo | 34 |
| `04.T.PROCESSO ON SITE` | 48 | | Parecer Técnico | 33 |
| `04.V.SEGURANÇA` | 30 | | Relatório | 23 |
| `04.Q.MÁQUINAS` | 24 | | Lista | 15 |
| `04.X.TELECOM` | 23 | | Esp. Técnica | 9 |
| `04.Y.TRANSFERÊNCIA DE CALOR` | 21 | | Folha de Dados | 7 |
| `04.I.ENGENHARIA DIGITAL` | 18 | | SIT | 7 |
| `04.S.PROCESSO OFF SITE` | 11 | | Lista de Documentos | 6 |
| `04.W.SIT-CT` | 10 | | Memorial Descritivo | 3 |
| `04.D.CIVIL`, `04.L.GERAL`, `04.B.CALDEIRARIA`, `04.A.ARQ`, `04.R.MECÂNICA` | 16 | | Consulta Técnica | 1 |

**Status em 04.ENGENHARIA:** Para Construção 700 · Para Compra 159 · Sem Comentários 140 ·
Com Comentários 70 · Em Análise 22 · Recusado 13 · Cancelado 12.

**Colunas exclusivas:** `Dias úteis em workflow` / `Dias Corridos em workflow`
(média 5,4 DU, mediana 3, **máximo 159**) · `Nome do Workflow` (48 fluxos distintos —
o roteamento real da Petrobras) · `Status Workflow` (TERMINADO 11.390 · SEM INSTÂNCIA 1.648 ·
INICIALIZADO 418 · ABORTADO 4).

⚠️ **6 colunas 100% vazias:** `Finalidade da Revisão`, `Situação do documento`,
`Nome da contratada`, `Situação Petrobras`, `Link`. Não construa nada em cima delas.

**Quando usar:** medição (é a fonte da verdade contratual), SLA da Petrobras,
status oficial do documento, aging em workflow.

---

#### 📄 `SIGEM DOCUMENTOS PREVISTOS` — (21.729 × 17) — *a pré-carga*

**O que é:** o cadastro de documentos **marcados/previstos** no SIGEM, com o flag
`JA_EMITIDO_NO_SIGEM` (S/N). É **a fonte que responde "o documento está pré-cadastrado?"** —
a pergunta que trava a medição.

**Total:** 21.729 linhas · 16.148 documentos únicos · 17.189 pares doc+revisão.
`JA_EMITIDO_NO_SIGEM`: **S = 17.191 · N = 4.537**.

**Filtrado por `CAMINHO` contendo `04.ENGENHARIA`: 5.613 linhas / 3.070 documentos** ✅

| | Total | Já emitido (S) | **Não emitido (N)** |
|---|---:|---:|---:|
| 04.ENGENHARIA | 5.613 | 4.880 | **733** |

**Os 733 não emitidos, por tipo:** IS **481** · PT 64 · DE 55 · SIT 40 · RL 39 · MC 18 ·
I-DE 15 · RM 5 · LI 5 · LD 4 · FD 3 · demais 4.
**Por caminho:** Tubulação **501** · Caldeiraria 51 · Instrumentação 42 · SIT-CT 37 ·
Engenharia Digital 35 · Elétrica 15 · Segurança 11 · Processo 8 · Máquinas 7 · Telecom 6 ·
Transferência de Calor 6 · Civil 4.

⚠️ **`DATA_MARCACAO` tem lixo histórico:** 3.378 registros de **ago/2015** e 1.034 de
**jun/2019** — são pré-cargas herdadas do projeto original do Trem 2, antes da paralisação.
**Filtrar `DATA_MARCACAO >= 2025-10-01`** para ver só o ciclo atual.

**Quando usar:** identificar documento sem pré-carga (bloqueio de medição), medir a fila de
cadastro, auditar o que a Petrobras espera receber.

---

#### 📄 `SIGEM CONSOLIDAÇÃO TODAS AS REVISÕES` — (9.777 × 19) 🆕 *fonte inédita*

**O que é:** **o histórico de consolidação de comentários da Petrobras**, revisão a revisão.
Esta fonte **não existe dentro da LD** — é informação nova.

**Colunas únicas e valiosas:**
- **`Texto de Consolidação`** — 1.822 textos distintos: **o comentário literal da Petrobras**.
  Ex.: *"1 - As atividades de fabricação só podem ser iniciadas após a reunião de PIM, e todos
  os desenhos e procedimentos aprovados"*, *"Este documento não será avaliado pelo SIGEM. Para
  os próximos enviá-lo sem fluxo"*, *"Revisar conforme última revisão enviada por e-mail"*.
- **`Chave do Consolidador`** — 74 chaves de 4 letras = **quem, nominalmente, consolidou na
  Petrobras**. Top: FQG1 (2.953), BTRC (1.452), D1CC (958), UQZ2 (852), SGSM (550).
- `Possui comentário gráfico?` — hoje 100% "NÃO".

**Status:** Sem Comentários 5.278 · **Recusado 2.571** · Com Comentários 1.925 ·
Para Construção 2. Período: 17/10/2025 → 14/08/2026.

**Quando usar:** 🔑 **é a única fonte que permite fazer NLP sobre o motivo da recusa.**
2.571 recusas com texto = a base para classificar automaticamente por que documentos voltam,
e para atribuir gargalo a consolidador específico. **Alto valor para o sistema autônomo.**

---

#### 📄 `LD-5290.00-22311-940-C1U-002` — LD de Fornecedores (362 × 75) 🆕

**O que é:** a **segunda LD** do projeto, irmã da LD-911. Código CONSAG
`RUGH-LDC-OTZ-EX-U036-PLA-PT-0002`. Rev. 0_0 de 15/07/2026 — *"PARA COMENTÁRIOS CONSAG —
EMISSÃO ORIGINAL"*. Controla os **ADF (Análise de Documentos de Fornecedor)**.

**362 documentos de 6 fornecedores, ligados a 13 RMs e 15 LDs de fornecedor:**

| Fornecedor | Docs | Disciplina | Docs | Tipo | Docs |
|---|---:|---|---:|---|---:|
| WEG | 86 | Mecânica | 115 | PR (procedimento) | 150 |
| ASVOTEC | 82 | Elétrica | 86 | DE | 81 |
| VIBROPAC | 73 | Qualidade | 75 | LI | 22 |
| ENGEMASA | 49 | Forno | 49 | MA / FD | 19 / 19 |
| VMF | 40 | Máquinas | 37 | CR / DB | 18 / 18 |
| INCASE | 32 | | | LD / RL / MC / CE / ET | 16/7/6/4/2 |

**Situação em 17/08/2026** ✅:
- **Recebimento do fornecedor:** aguardando 1º envio **268** · recebido **82** ·
  aguardando 1º envio EM ATRASO 10 · aguardando doc revisado EM ATRASO 2.
- **Pré-cadastro no SIGEM:** cadastrado 220 · **não cadastrado 142**.
- **Faixa de atraso:** sem atraso 289 · finalizado 32 · 1 a 3 dias 19 · **>7 dias 16** · excl. 6.
- **Responsabilidade do atraso** (`STATUS PARA ANÁLISE DOS DESVIOS`): fornecedor no prazo 268 ·
  concluído 32 · **CONSAG em atraso 18** · **fornecedor em atraso 12** · CONSAG no prazo 6 ·
  OTZ no prazo 6 · **OTZ em atraso 5** · Petrobras no prazo 1.

> 🔑 **Esta LD tem uma coluna que a LD principal não tem: `STATUS PARA ANÁLISE DOS DESVIOS`,
> que ATRIBUI O ATRASO A UM ATOR NOMINAL** (OTZ / CONSAG / FORNECEDOR / CDA / PETROBRAS), com
> as colunas `DIAS EM ATRASO - OTZ`, `- CONSAG`, `- FORNECEDOR`, `- PETROBRAS`.
> **É o modelo que a LD principal deveria copiar.** Hoje a LD-911 só diz "em atraso", sem dizer
> de quem.

⚠️ **A EAP financeira deste arquivo está zerada** (`% AVANÇO FINANCEIRO` = 0 em todas as 362
linhas; `ITEM DA EAP FINANCEIRA` = `1.3.2.1.5.3` em apenas 86). O ADF vale 70%+30% na régua de
medição (§4.4) — **há receita de ADF não sendo apropriada nesta planilha**. ❓ Confirmar se a
apropriação acontece em outro lugar.

⚠️ **Herança de outro projeto:** as abas `Pré-Alocação` e `CONTROLE` deste arquivo listam
documentos de área **22313 / U-32-UHDT-D**, não 22311/U-36. O arquivo foi clonado do projeto
irmão e **não foi limpo**. Idem o ACF-001, cujo cabeçalho diz *"RNEST — LOTE C"*. ❓ Ver §11.

**Abas do arquivo:** `CAPA` · `Lista Fornecedor` (362×75, a principal) · `TAB_DIN_STATUS`
(pivots de ADF) · `% DE AVANÇO FINANCEIRO` · `Padrões` (calendário, feriados até dez/2027,
de-para de revisão, EAP) · `RL_Documento` (58) · `RL_PW` (18.147×48) · `RL_PW 1ª EMISSÃO` ·
`RL_SIGEM` (1.532×15) · `RL_SIGEM Previsto` (21.649) · `RL_Emissão` (5.670) ·
`Pré-Alocação` (273) · `CONTROLE` (134).

---

### 6.4 Tabela de decisão — qual fonte usar para cada pergunta

| Pergunta | Fonte | Filtro obrigatório |
|---|---|---|
| Quantos documentos eu tenho que entregar? | LD-911 abas `LD UGH Trem 2` + `LD Trem 2 -ICs` | `Previsto / Excluído = PREVISTO` |
| Quantos já emiti para a CONSAG? | LD col. `Data real 1ª Emissão PW` **ou** `RELATÓRIO PW` | `nomeEmpresa ∉ {CONSAG, CONSAG QUALIDADE}` |
| **Quantos já geraram receita?** | **`RELATÓRIO SIGEM`** | **`Nível 2 = 04.ENGENHARIA`** |
| O documento está pré-cadastrado no SIGEM? | `SIGEM DOCUMENTOS PREVISTOS` | `CAMINHO ⊃ 04.ENGENHARIA` e `DATA_MARCACAO ≥ 2025-10` |
| Por que a Petrobras recusou? | **`SIGEM CONSOLIDAÇÃO`** | `Status = Recusado` |
| Quanto esforço tem um documento? | `RELATÓRIO DOCUMENTO` | col. `Folhas` + `Formato` |
| Quem está com o documento agora? | `RELATÓRIO DOCUMENTO` | `Responsável da Atividade` + `Status do Documento` |
| Quantas emissões saíram este mês? | `RELATÓRIO EMISSÃO` | `Data Emissão` |
| Quanto retrabalho estou tendo? | `RELATÓRIO MARKUP` | remover `DOC_Disciplina = NÃO SE APLICA` |
| Documento de fornecedor está atrasado, e de quem é a culpa? | **LD-940 `Lista Fornecedor`** | col. `STATUS PARA ANÁLISE DOS DESVIOS` |
| Qual IS-955 posso emitir hoje? | LD-911 `LD Trem 2 -ICs` col. `Correspondente - IS-200` | cruzar com emissão do IS-200 |

---

## 7. Mapa de dependências de processo

> Esta seção responde **"o que depende de quê"**. Onde há evidência no dado, está marcado ✅;
> onde é engenharia de processo padrão aplicada a este projeto, está marcado 🧠.

### 7.1 A cadeia mestra — visão macro

```
 [A] ACERVO DO TREM 1 + PROJETO BÁSICO DO REVAMP (PETROBRAS)
      ├─ chega via SDT → E-CLIC (17.673 docs de referência) ✅
      ▼
 [B] COMPATIBILIZAÇÃO TREM 2 × TREM 1  ── restrição em 153 linhas da LD ✅
      ▼
 [C] PROCESSO: Fluxogramas de Engenharia (PFD/P&ID) + lista de linhas no COMOS ✅
      │        (17 fluxogramas emitidos p/ comentários + 6 revisados no período)
      ├──────────────┬─────────────────┬──────────────────┐
      ▼              ▼                 ▼                  ▼
 [D] COMOS       [E] SEGURANÇA     [F] INSTRUMENTAÇÃO  [G] MECÂNICA/EQUIP.
   (banco de       HAZOP/APR/LOPA    Lista de           FDs de equipamento
    dados de       → recomendações   Instrumentos       (geradas no COMOS) ✅
    engenharia)    → revisões ✅     ✅
      │                                  │
      │  importação COMOS → E3D ✅       │ Lista de I/O ✅
      ▼                                  ▼
 [H] MODELO 3D — AVEVA E3D  ◄────── [I] ELÉTRICA (motores, cargas, F&A, SPDA)
      │   (arranjo, suportação, clashes, atributos)
      │
      ├──► [J] CIVIL / ESTRUTURA METÁLICA (plataformas, pipe-racks, fundações)
      │        ── suportação depende das cargas de tubulação 🧠
      │
      ├──► [K] TELECOM / BANDEJAS / ELETROCALHAS (encaminhamento) 🧠
      │
      └──► [L] TUBULAÇÃO
             │
             ├─► IS-200  ISOMÉTRICO DE TUBULAÇÃO (detalhamento)  ── 1.778 previstos ✅
             │      │
             │      ├─► MC de Análise de Flexibilidade 🧠
             │      ├─► Suportes especiais de tubulação 🧠
             │      │
             │      └─►► IS-955 ISOMÉTRICO DE CONSTRUÇÃO ── 1.600 previstos ✅
             │              │   (extraído do E3D via CASPOOL / CAJU / CALM)
             │              ├─► SPOOLs (SPL-IS — 689 no E-CLIC) ✅
             │              ├─► planilhas controltub ✅
             │              └─► PESO (kg) ─── régua de avanço da obra ✅
             ▼
 [M] SUPRIMENTOS:  RM → LET → proposta → mapa comparativo → PT/PATEC → pedido
             │
             └─► [N] DOCUMENTOS DE FORNECEDOR (LD-940)
                     └─► retroalimenta FD / DE / E3D / COMOS ("conforme comprado") 🧠
      ▼
 [O] OBRA (CONSAG) → marcas de campo → [P] AS-BUILT (conforme construído)
```

### 7.2 Pré-requisitos técnicos, documento a documento

| Documento a emitir | Precisa ANTES de | Evidência |
|---|---|---|
| **Isométrico IS-200** | Fluxograma de engenharia com a linha; linha carregada no COMOS; modelo E3D da área modelado e com atributos | ✅ LD: *"Reincluir linha. Linha consta no fluxograma. Deve ser mantida"* (9×) e *"Fluxograma ainda não emitido, mas linha consta no fluxograma 'Conforme Construído' do Trem 1"* (6×). A LD tem coluna `FLUXOGRAMA (REF. Isométrico)` — 🔴 **vazia em 100% das linhas** |
| **Isométrico IS-955 (construção)** | **O IS-200 correspondente emitido** | ✅ **dependência 1:1 explícita** — coluna `Correspondente - IS-200`, preenchida em **1.600/1.600 = 100%** |
| **SPOOL / controltub / peso** | IS-955 gerado + ferramentas CASPOOL/CAJU/CALM funcionando | ✅ RL: *"Correção de ferramenta de geração CASPOOL, CAJU e CALM"*; *"Configuração de Spools"* |
| **MC de flexibilidade** | Isométrico + condições de processo (T, P) + suportação | 🧠 + ✅ RL: *"Compatibilização de Memórias de Cálculo de Análise de Flexibilidade"* |
| **Folha de Dados (FD) de equipamento** | Dados de processo no COMOS + geração automática | ✅ RL: *"atualização dos dados de equipamentos e geração das Folhas de Dados de Mecânica no COMOS"* |
| **Lista de Instrumentos** | P&ID compatibilizado | ✅ RL Instrumentação |
| **Lista de I/O para o SDCD** | **Lista de Instrumentos** (INS → ELE/AUT) | ✅ RL Elétrica emitiu a Lista de I/O; a Lista de Instrumentos é da Instrumentação |
| **Plantas de distribuição F&A / SPDA / iluminação** | Lista de Motores e Cargas Elétricas + arranjo 3D | ✅ RL Elétrica |
| **Plantas de locação de instrumentos** | Modelo 3D com instrumentos posicionados | ✅ RL Instrumentação (plantas 2, 3, 4) |
| **Planta de encaminhamento underground (Telecom)** | Arranjo civil/underground + modelo | ✅ RL Telecom |
| **Estruturas / plataformas / pipe-rack** | Layout 3D + cargas das tubulações que suportam | ✅ RL Civil: *"Pipe-rack II — estrutura de suportação dos P-36026/P-36061/P-36064"* |
| **RM (Requisição de Material)** | FD do item + especificação técnica | 🧠 + ✅ LD: *"Solicitado pela PB que a RM fosse emitida após a FD"* |
| **PT / PATEC (Parecer Técnico)** | RM emitida + propostas recebidas + LET respondida | ✅ Quadro de suprimentos do RL |
| **Documento de fornecedor certificado** | PT → pedido → LD do fornecedor → 1ª emissão → análise OTZ → CONSAG → PB | ✅ LD-940 |
| **As-built** | Marcas de campo (obra) + confirmação em campo pela OTZ | ✅ MD-903 §18 |
| **Qualquer emissão no SIGEM** | **Pré-carga/pré-alocação no SIGEM** aprovada pela Petrobras | ✅ 80 docs travados por isso em jul/26 |
| **Qualquer emissão no PW** | **Pré-cadastro no PW** | ✅ coluna `PRÉ CADASTRADO NO PW?` |

### 7.3 Pré-requisitos contratuais — o que "destrava" uma emissão

| Gate | Quem libera | O que trava se faltar |
|---|---|---|
| **Pré-alocação / planilha de carga no PW** | OTZ envia, CONSAG carrega | Não dá para publicar no PW |
| **Pré-carga no SIGEM** | OTZ envia lista → CONSAG → **Petrobras cadastra** | 🔴 **Não dá para emitir → não mede → não fatura** |
| **Aprovação da revisão 0_1 pela CONSAG** | Engenharia CONSAG (10 DU) | Não sobe para o SIGEM como rev. 0 |
| **Numeração CONSAG atribuída** | CONSAG | Documento não entra no PW |
| **LD aprovada pela CONSAG** | CONSAG | Documento não é reconhecido no escopo/medição |
| **Definição de propósito de emissão** | Regra do Anexo VII | Documento sem propósito é rejeitado pelo GED |
| **Meta específica de disciplina** | CONSAG (ex.: Tubulação, 18/06/2026) | Reprioriza tudo |
| **NMP aprovada** | Gerente de Contrato do CLIENTE | Escopo adicional trabalhado sem cobertura |

### 7.4 Dependências de disciplina cruzada

| Consome ↓ / Produz → | Processo | Instr&Aut | Elétrica | Tubulação | Civil/Estrut. | E3D/COMOS | Suprimentos |
|---|---|---|---|---|---|---|---|
| **Processo** | — | P&ID → lista de instrumentos | — | P&ID → linhas | — | carrega COMOS | dados p/ FD |
| **Instr&Aut** | recebe P&ID | — | **lista de I/O → SDCD** | locação em campo | suportes de instrumento | posiciona no 3D | RM de instrumento (47 pacotes!) |
| **Elétrica** | — | recebe lista de I/O | — | encaminhamento | bandejas/eletrocalhas | 3D elétrico | RM de motor/cabo |
| **Tubulação** | **recebe linhas do P&ID** | válvulas de controle | — | — | **envia cargas p/ suportação** | **consome E3D** | RM de válvula/tubo |
| **Civil / Est. Metálica** | — | — | — | **recebe cargas** | — | consome 3D | — |
| **E3D / COMOS** | recebe dados | recebe dados | recebe dados | **entrega isométricos** | entrega arranjo | — | recebe dados de fornecedor |
| **Segurança** | HAZOP sobre P&ID | recomendações → SIF | detecção de gás | dilúvio/incêndio | plantas de rota de fuga | — | RM de sensor/alarme |

🔑 **A leitura de gestão:** Processo e E3D/COMOS são **fornecedores universais**. Tubulação é
**o maior consumidor e o maior produtor**. Elétrica depende de Instrumentação. Civil depende de
Tubulação. **Ninguém depende de Estrutura Metálica — por isso ela conseguiu terminar 100%.** ✅

### 7.5 Dependências externas (fora do controle da OTZ)

| Dependência | Situação hoje | Impacto |
|---|---|---|
| **Documento do Trem 1** | via SDT; há casos aguardando há meses | Trava compatibilização |
| **Pré-carga no SIGEM (Petrobras)** | 80 docs (jul) / 142 na LD-940 | 🔴 Trava medição |
| **Propostas de fornecedor** | **44 pacotes aguardando proposta (CONSAG)** | Trava PT → trava FD → trava projeto |
| **Documentos de fornecedor** | 268 de 362 aguardando 1º envio | Trava "conforme comprado" |
| **Comentários da Petrobras** | SLA 10 DU; máximo observado 159 DU em workflow | Trava revisão seguinte |
| **Definição Petrobras (casos abertos)** | ex.: *"aguardando definição Petrobras, alinhado em reunião do dia 05/02… 19/02"* ✅ | Congela documento |
| **Modelagem do pacote PSA / Fornos no E3D** | 🔴 *"Equipamentos que fazem parte do pacote de PSA, Fornos e áreas adjacentes **não estão modelados no E3D**"* ✅ | Trava isométricos e clashes dessas áreas |
| **Levantamento de campo** | necessário p/ interfaces e as-built | Trava SITs abertas |
| **Licença/normas** | aquisição de normas é da OTZ (MD §17.3) | — |

---

## 8. Cadeia crítica — onde o projeto está travado hoje

### 8.1 🔴 O gargalo nº 1, quantificado: IS-200 → IS-955

Cruzamento feito diretamente na LD rev. F_0 (19/08/2026), coluna `Correspondente - IS-200` ✅:

| Métrica | Valor |
|---|---:|
| IS-200 previstos (LD principal) | **1.778** |
| IS-200 com 1ª emissão no PW | 625 (35%) |
| **IS-200 ainda não emitidos** | **1.153 (65%)** |
| IS-955 previstos (aba ICs) | **1.600** |
| IS-955 já emitidos no PW | 241 (15%) |
| IS-955 com referência IS-200 preenchida | **1.600 (100%)** |
| **IS-955 BLOQUEADOS — o IS-200 pai ainda não saiu** | **1.153 (72%)** 🔴 |
| **IS-955 LIBERADOS e ainda não emitidos (buffer de trabalho)** | **206** |

> 🔑 **Este é o número mais importante deste documento.**
> A frente de isométricos de construção tem **206 documentos de folga**. Se a Tubulação parar
> de produzir IS-200, em poucas semanas os 12 projetistas de Tubulação e a equipe de spool
> ficam **sem trabalho liberado**. **A capacidade de emitir IS-955 é 100% governada pela
> emissão de IS-200 — não adianta cobrar IS-955.**

### 8.2 🔴 O gargalo nº 2: o ritmo necessário × o ritmo real

| | Valor |
|---|---:|
| 1ªs emissões restantes — documentos de projeto | **1.660** |
| 1ªs emissões restantes — IS-955 | **1.359** |
| **TOTAL restante** | **3.019** |
| Semanas até 30/abr/2027 (fim da programação da LD) | **36,3** |
| **Ritmo NECESSÁRIO** | **≈ 83 primeiras emissões / semana** |
| Ritmo realizado mai/jun/jul 2026 | 134 + 207 + 348 = 689 em 13 sem → **≈ 53 / semana** |
| Ritmo realizado ago/2026 (1–19) | 315 em 2,7 sem → **≈ 116 / semana** 🟢 |
| Média dos últimos 4 meses | ≈ **64 / semana** |

**Leitura:** o projeto precisa de **+30% sobre a média histórica**. Agosto mostra que o ritmo
de 116/semana é fisicamente possível — 🧠 provavelmente por causa da meta imposta pela CONSAG
em 18/06. **A questão é se 116/semana é sustentável ou um pico de recuperação de passivo.**
Isso é medível: separar produção corrente de recuperação de passivo (o próprio RL recomenda).

**Programação de 1ªs emissões no PW por mês (BL 1):**
ago/26 **180** · set **179** · **out 256 (pico)** · nov 171 · dez 194 · jan/27 157 ·
fev 177 · mar 120 · abr 89.
**IS-955:** ago/26 **242 (pico)** · set 198 · out 233 · nov 186 · dez 132 · jan/27 139 ·
fev 152 · mar 35.
🔴 **Somando: agosto exige 422 emissões; outubro exige 489.** Isso é ~105–122/semana. **A
programação da LD já está calibrada no ritmo de pico de agosto — não há folga nenhuma.**

### 8.3 🔴 O gargalo nº 3: pré-carga no SIGEM (o freio de receita)

| Fonte | Métrica |
|---|---|
| RL 20/07/2026 | **80 documentos** na LD não cadastrados no SIGEM, **8 já emitidos no PW** |
| LD rev. F_0 (19/08) | `PRÉ CADASTRADO NO SIGEM?` = NÃO **64** + valor `0` **77** = **141** |
| SIGEM Previstos (04.ENGENHARIA) | **733** documentos com `JA_EMITIDO_NO_SIGEM = N` (481 são IS) |
| LD-940 (fornecedores) | **142** de 362 "NÃO CADASTRADO" |

Os 8 documentos nominalmente citados no RL ✅ (é a lista que precisa de cobrança):
`MD-…-100-C1U-101` (Projeto de Fundações/Drenagem/Estruturas/Pavimentação, 1ª emissão PW
16/06) · `MC-…-182-C1U-101` (Sistemas de Drenagem, 25/05) · `PT-…-887-C1U-002` (Bandejas e
Eletrocalhas, 29/05) · `LI-…-700-JEI-002` (Lista de Cabos do Forno, 18/06) ·
`LI-…-781-C1U-001` (Materiais de SPDA, 12/06) · `DE-…-131-CHZ-193` (Travessia Pipe-Rack /
Pontilhão — Formas, 19/06) · `I-DE-…-944-UOP-302` (Instrument Symbols, 17/07) ·
`DE-…-700-CHZ-135` (Distribuição de F&A — Rede Subterrânea, 26/06).

> 🔑 **Documento emitido no PW e não cadastrado no SIGEM = trabalho feito, custo incorrido,
> zero receita.** Alguns desses estão parados desde **maio**. É o item de maior retorno
> imediato por unidade de esforço de gestão.

### 8.4 🔴 O gargalo nº 4: instabilidade das ferramentas de extração do E3D

Registrado no RL como *"principal ponto de atenção"* ✅:
- Instabilidade na extração dos IS-955;
- Ferramentas CASPOOL / CAJU / CALM em correção;
- **28 isométricos emitidos com PESO = ZERO** — precisam de verificação e regularização;
- **122 IS-955 pendentes** em 20/07 (em desenvolvimento e correção);
- **84 documentos em programação para correção**;
- PSA e Fornos **não modelados no E3D**.

Status de peso em 20/07: IS-200 **293 emitidos = 116.068,70 kg** · IS-955 **143 emitidos =
88.353,10 kg**. O peso é a métrica que a obra usa para fabricação — **isométrico com peso zero
não libera fabricação de spool**, mesmo estando emitido. 🧠

### 8.5 O gargalo nº 5: Instrumentação (o segundo maior risco, subestimado)

| Indicador | Instr&Aut |
|---|---|
| Documentos previstos | 228 |
| 1ª emissão PW | 76 (**33%** — mesmo % da Tubulação) |
| **1ªs emissões em atraso** | **53 (23% do total da disciplina)** |
| **Atraso médio dos não emitidos** | **31 dias — o maior do projeto** |
| Pacotes de suprimento | **47 de 95 (49% de todo o suprimento)** |
| Aguardando proposta | 19 |
| Em análise / elaboração de LET | 12 |

🧠 **Por que isso é pior do que parece:** Instrumentação é predecessora de Elétrica (lista de
I/O → SDCD) e de Segurança (SIF, detecção de gás). Metade dos pacotes de compra do projeto é
dela. Se a Tubulação for resolvida e Instrumentação continuar a 31 dias de atraso médio,
**o gargalo simplesmente migra**.

### 8.6 Fila de trabalho — onde estão os 2.824 documentos hoje ✅

| Status do documento | Qtde | Quem tem a bola |
|---|---:|---|
| **EMITIR EMISSÃO INICIAL** | **1.659** | **OTZ** |
| DOC. FINALIZADO | 1.019 | — |
| AGUARDANDO MARKUP CONSAG | 54 | CONSAG |
| EMITIR NO SIGEM | 31 | OTZ / pré-carga |
| ATENDER MARKUP CONSAG | 20 | OTZ |
| AGUARDANDO MARKUP PB | 19 | PETROBRAS |
| ATENDER MARKUP PB | 11 | OTZ |
| DOCUMENTO CANCELADO | 11 | — |

> **59% do escopo ainda não teve sequer a primeira emissão, e a bola está com a OTZ em 1.721
> dos 1.805 documentos em aberto (95%).** O discurso de "a CONSAG/Petrobras está travando"
> **não se sustenta no dado agregado** — embora se sustente pontualmente (pré-carga, propostas).

### 8.7 Distribuição do atraso de 1ª emissão (docs ainda não emitidos, 19/08/2026) ✅

| Faixa | Qtde |
|---|---:|
| Programado para o futuro (no prazo) | 1.470 |
| Atraso 1–15 dias | 54 |
| Atraso 16–30 dias | 56 |
| **Atraso 31–60 dias** | **80** |
| Atraso > 60 dias | 0 |

Atraso médio por disciplina (não emitidos): Tubulação n=96 média 26d (máx 47) ·
**Instr&Aut n=45 média 31d (máx 54)** · Elétrica n=28 média 18d (máx 54) ·
**Fornos n=5 média 54d** · E3D n=3 média 25d · Processo n=6 média 7d.

🟢 **Nota positiva:** ninguém passa de 60 dias. O passivo é recente e recuperável — sinal de
que a reprogramação de 30/06 realmente rebaseou as datas.

---

## 9. VISÃO DO GESTOR SÊNIOR

### 9.1 Diagnóstico da situação atual

**Primeiro: o projeto não está em crise de prazo — está em crise de calibração.** O desvio
físico é de 1,70 pontos (27,11% × 28,81%), dentro da meta de ≤5% do próprio indicador DAF da
OTZ. O desvio financeiro é ainda menor. Ninguém vai ser notificado por causa de 1,7%. Mas os
percentuais foram apurados **sobre revisões diferentes da LD** — previsto sobre a `LD_A_0` de
01/04 (2.852 documentos), realizado sobre a `LD_D_3` de 23/07 (2.404 documentos). Isso está
escrito no próprio relatório mensal da OTZ. **Um indicador calculado sobre denominadores
diferentes não é um indicador; é uma opinião com aparência de número.** Enquanto essa
reconciliação não estiver feita, nenhum número deste projeto — nem os favoráveis à OTZ — tem
força contratual. É a primeira coisa a consertar, e é exatamente o tipo de trabalho que o
Planejamento existe para fazer.

**Segundo: o projeto tem um gargalo único, físico e mensurável, e todo mundo está olhando
para o sintoma errado.** A CONSAG impôs metas de Tubulação e cobra IS-955. Mas 1.153 dos 1.600
IS-955 estão **contratualmente impossibilitados de existir**, porque o IS-200 correspondente
não foi emitido. O estoque de trabalho liberado para a frente de construção é de **206
isométricos**. Cobrar IS-955 é cobrar o efeito. **A única alavanca real é a taxa de emissão de
IS-200, que por sua vez depende do modelo E3D estar completo e das ferramentas de extração
(CASPOOL/CAJU/CALM) estáveis.** E o E3D não está completo: PSA e Fornos não estão modelados,
por registro da própria LD. Ou seja — o gargalo do maior contrato de isometria da OTZ é um
problema de **engenharia digital**, não de produtividade de projetista.

**Terceiro: a exposição financeira é estrutural e está piorando devagar.** O contrato comprou
925 isométricos; a LD prevê 3.378. O saldo de PPU foi de −335 em 20/07 para −446 em 19/08 —
**perdeu 111 documentos de saldo em 30 dias**. A armadilha é sutil: isométrico é o item mais
barato da PPU (R$ 2.010 a revisão), então a OTZ vai **estourar a quantidade sem estourar o
valor do contrato**, e a CONSAG poderá dizer, com razão aritmética, que ainda há saldo
financeiro. O momento de negociar remanejamento entre itens de PPU é **agora**, enquanto ainda
há saldo positivo grande em DE-NOVO (+101), FD-REVISÃO (+96), ET (+107 somados) e LD (+43).
Daqui a seis meses, com 1.500 isométricos a mais entregues, a conversa vira pedido de aditivo —
e aditivo tem rito, prazo e risco de negativa.

**Quarto: há um passivo de gestão contratual mal formalizado que é o maior risco jurídico do
projeto.** Três itens: (a) as **98 Folhas de Dados** que a CONSAG mandou retirar da LD em
01/07 — trabalho já executado, impacto em curva física, financeira, PPU, COMOS e E3D, e a OTZ
até hoje "avaliando"; (b) a coluna **SEVERIDADE da LD está 100% vazia** — a classificação
BAIXO/MÉDIO/ALTO/NOVO é o critério contratual do MD-903 que define o esforço, e sem ela a OTZ
não consegue provar que uma revisão "BAIXO" virou "ALTO"; (c) a **Rede de Precedência também
está 100% vazia**, embora seja exigência do Anexo VII e o ACF-001 a declare "concluída" com
apenas HVAC e Telecom apresentadas. São três buracos de prova. Em pleito contratual, **o que
não está registrado não aconteceu**.

**Quinto: o que está sendo bem gerido merece registro.** A Estrutura Metálica fechou 100% de
1ª emissão e 100% de finalização — é a prova de que o processo funciona quando não há
dependência a montante. O ritmo de agosto (116 primeiras emissões/semana contra 53 na média
mai–jul) mostra que a organização responde a meta clara. Nenhum documento passa de 60 dias de
atraso, o que significa que a reprogramação de 30/06 foi real e não cosmética. A qualidade
está sob controle (IDR 2,1% contra meta ≤3%; 1 recusa em 47 comentados). E a LD de
fornecedores, criada em julho, já traz uma coluna que a LD principal não tem — atribuição
nominal do atraso a OTZ/CONSAG/FORNECEDOR/CDA/PETROBRAS. **Alguém no time está pensando
certo; falta espalhar.**

### 9.2 Mapa de dependências simplificado — o que trava o quê

```
   PSA e FORNOS não modelados no E3D
   Ferramentas CASPOOL/CAJU/CALM instáveis
              │
              ▼
   ┌──────────────────────────────┐
   │   IS-200  (1.778 previstos)  │   ◄── 65% ainda não emitidos
   │   35% emitidos               │
   └──────────────┬───────────────┘
                  │  dependência 1:1, 100% mapeada
                  ▼
   ┌──────────────────────────────┐
   │  IS-955  (1.600 previstos)   │   ◄── 1.153 BLOQUEADOS (72%)
   │  15% emitidos                │       206 liberados = todo o buffer
   └──────────────┬───────────────┘
                  ▼
        SPOOL + peso (kg)  ──► FABRICAÇÃO NA OBRA
                  │
        28 isométricos com PESO ZERO travam fabricação

   ─────────────────────────────────────────────────────

   P&ID / Fluxograma compatibilizado
              ├──► Lista de Instrumentos ──► Lista de I/O ──► SDCD (ELÉTRICA)
              ├──► Linhas no COMOS ────────► IS-200
              └──► HAZOP/APR/LOPA ─────────► recomendações ──► revisões (loop)

   COMOS ──► Folhas de Dados de equipamento ──► RM ──► LET ──► PT
                                                              │
                                        44 pacotes aguardando proposta (CONSAG)
                                                              ▼
                                            Documentos de Fornecedor (LD-940)
                                            268 de 362 aguardando 1º envio
                                                              ▼
                                            "Conforme comprado" ──► FD / DE / 3D

   ─────────────────────────────────────────────────────

   QUALQUER DOCUMENTO
        └─► PRÉ-CARGA NO SIGEM (Petrobras)  ◄── 141 na LD / 733 no relatório
                    └─► EMISSÃO NO SIGEM
                            └─► MEDIÇÃO  ──► FATURAMENTO (M+1) ──► CAIXA (M+2)

   Sem pré-carga = trabalho feito, receita zero.
```

**Resumo em uma linha:** *E3D incompleto → IS-200 lento → IS-955 bloqueado → spool não sai →
obra espera. E, em paralelo, pré-carga ausente → receita retida.*

### 9.3 Top 5 ações prioritárias para os próximos 30 dias

---

**#1 — Zerar a fila de pré-carga no SIGEM. (Retorno financeiro imediato, esforço baixo)**

Há entre 80 e 141 documentos sem pré-carga, 8 deles já emitidos no PW desde maio/junho.
Cada um desses é receita 100% pronta e retida.

*Como fazer:* extrair do `SIGEM DOCUMENTOS PREVISTOS` (filtro `04.ENGENHARIA` +
`JA_EMITIDO_NO_SIGEM = N` + `DATA_MARCACAO ≥ 2025-10`) cruzado com a LD (`PRÉ CADASTRADO NO
SIGEM? ≠ SIM`) e com o PW (já emitido). Emitir **uma carta única à CONSAG** com a lista
nominal, a data de 1ª emissão no PW de cada um e o valor de PPU associado, pedindo prazo de
regularização junto à Petrobras. Colocar como item fixo da reunião semanal com data-alvo.
*Prazo: 5 dias úteis para a lista; 15 para a resposta formal.*

---

**#2 — Publicar o Relatório de Cadeia Crítica de Isométricos, semanal. (Muda a conversa com a CONSAG)**

Hoje a CONSAG cobra IS-955. O relatório deve mostrar, toda sexta:
(a) IS-955 liberados e não emitidos = **capacidade real de produção da semana** (hoje 206);
(b) IS-955 bloqueados por IS-200 pendente (hoje 1.153);
(c) IS-200 emitidos na semana = **a única alavanca**;
(d) isométricos com peso zero (hoje 28);
(e) áreas do E3D não modeladas (PSA, Fornos).

*Por que importa:* transfere a discussão do "vocês estão devagar" para "a fila de entrada está
seca por causa de X". **É a mesma lógica de restrição que o Ilson já usa nos controles de
restrições do Cristália** — só que aqui a evidência é 1:1 e já está na LD.
*Prazo: primeira edição em 7 dias. É um cruzamento de 20 linhas de código.*

---

**#3 — Preencher SEVERIDADE e Rede de Precedência na LD. (Blindagem contratual)**

As duas colunas existem e estão vazias em 2.824 linhas. A severidade é o critério do MD-903
§7.10 e a baseline por severidade já está publicada (§3.2 deste documento: 1.524 BAIXO / 181
MÉDIO / 54 ALTO / 434 NOVO).

*Como fazer:* (a) importar a classificação original do Anexo XIX / MD-903 para a LD;
(b) registrar, documento a documento, quando a severidade real divergir da contratada —
**esse delta É o pleito**; (c) para precedência, começar pelo que já é dado: IS-955→IS-200
(100% pronto), depois P&ID→IS-200, Lista de Instrumentos→Lista de I/O.
*Prazo: 30 dias. É o item de maior valor de longo prazo.*

---

**#4 — Fechar formalmente o caso das 98 Folhas de Dados. (Risco aberto há 50 dias)**

Pedido da CONSAG em 01/07; o RL de 20/07 ainda diz "em avaliação". Cada dia de silêncio
enfraquece a posição.

*Como fazer:* quantificar (a) horas já apropriadas nessas 98 FDs; (b) impacto no avanço físico
e na curva S; (c) impacto no saldo de PPU (FD-REVISÃO tem +96 de saldo — a retirada **piora**
a diluição, não melhora); (d) esforço remanescente de compatibilização de COMOS e E3D que
continua devido mesmo sem a FD. Encaminhar via **NMP**, não via e-mail — SIT e CT não validam
alteração de escopo (§2.10). *Prazo: 15 dias.*

---

**#5 — Reconciliar a base única de indicadores. (Sem isso, nenhum número vale)**

Definir e congelar: qual revisão da LD é o **denominador do previsto**, qual é o do
**realizado**, e publicar a regra. O próprio RL admite que hoje são diferentes.

*Como fazer:* adotar a regra "**previsto = baseline BL1 congelada; realizado = LD corrente;
escopo adicional isolado em linha separada**". Republicar a série histórica jan→ago sobre a
base única. **Anexar a memória de cálculo ao relatório mensal** — isso é o que transforma um
número gerencial em prova documental.
*Prazo: 20 dias, para entrar no fechamento de setembro.*

---

### 9.4 O que o Ilson deveria fazer nos primeiros 60 dias

**Semanas 1–2 — Ouvir e mapear (não mexer em nada).**
Reuniões individuais com: Elizabeth Azevedo (a caixa de Planejamento no organograma),
Gustavo Lima (Coordenador de Engenharia), Ricardo Amorim (Tubulação — 71% do escopo),
Johnes Nunes (ADM 3D — o gargalo raiz), Raphael Sant'Ana (Instr&Aut — o gargalo nº 2),
Denise Depentor (CDA/Qualidade — dona da pré-carga na prática).
Pergunta única para cada um: *"o que você precisa que chegue para você produzir mais?"*
Do lado CONSAG: Karla de Faria de Carvalho (Gerente de Planejamento da Engenharia).

**Semanas 1–4 — Assumir a rotina do ACF-001 sem quebrar nada.** A rotina obrigatória já está
escrita (§9.6). Ela tem entregas com **hora marcada**: programação de 6 semanas às sextas até
12h, justificativas de atraso às terças até 12h, lista de alocados às sextas, previsão de
faturamento quinzenal até o 3º dia útil. **Quem chega novo e perde um desses horários perde
credibilidade antes de ter opinião.** Automatizar exatamente esses, primeiro.

**Semanas 3–6 — Entregar as ações #1 e #2 da lista acima.** São as de maior visibilidade e
menor risco. #1 gera dinheiro; #2 muda a narrativa com a CONSAG. Ambas são cruzamentos de
dados que o Ilson já sabe fazer.

**Semanas 5–8 — Construir a infraestrutura autônoma sobre as fontes certas.** Migrar do
consumo de abas pré-filtradas da LD para os **relatórios avulsos completos** (§6.2), com os
filtros explícitos e versionados. É o pré-requisito técnico para tudo que vem depois.

**Ao longo dos 60 dias — a regra de sobrevivência:** cada número publicado deve vir com
(a) a fonte, (b) o filtro, (c) a data-base. Este projeto já perdeu força de argumento uma vez
por publicar percentuais com denominadores diferentes. **Não repita.**

### 9.5 Reuniões e cobranças mais urgentes

| Prioridade | Fórum | Pauta a levar | Frequência |
|---|---|---|---|
| 🔴 1 | **Reunião semanal OTZ × CONSAG** | Lista nominal de pré-carga pendente + valor de PPU retido | Semanal (obrigação contratual §8.3) |
| 🔴 2 | **Reunião de acompanhamento de metas de Tubulação** | Cadeia crítica IS-200→IS-955; capacidade real = 206 | Semanal |
| 🔴 3 | **Interna: ADM 3D + Tubulação + COMOS** | Modelagem de PSA/Fornos e estabilização CASPOOL/CAJU/CALM — com data | Semanal até resolver |
| 🟠 4 | **Comitê Executivo OTZ × CONSAG** (mensal, Preposto + Diretoria) | 98 FDs; saldo de PPU de isométricos; remanejamento entre itens | Mensal |
| 🟠 5 | **Interna: Instr&Aut** | 53 atrasos, 31 dias médios, 47 pacotes de suprimento | Quinzenal |
| 🟠 6 | **Reunião quinzenal com Petrobras** (via CONSAG) | Pré-carga; consolidadores com fila longa (FQG1: 2.953 consolidações) | Quinzenal |
| 🟡 7 | **RAS (semanal) e RAC (mensal)** | Já existem no ACF-001 — garantir que o número publicado seja o da base única | Conforme ACF |

### 9.6 A rotina obrigatória do Planejamento (ACF-001 rev. R6) ✅

Este é o **contrato de serviço do time do Ilson**. Tudo aqui é obrigação declarada:

| Entrega | Periodicidade | Prazo/hora | Responsável no ACF |
|---|---|---|---|
| **Programação de documentos previstos para 6 SEMANAS (metodologia LPS)** | semanal | **6ª feira até 12h → CONSAG** | Léo / Bruna |
| **Justificativas de atraso da semana anterior** | semanal | **3ª feira até 12h → CONSAG** | Léo / Gilberto / Aline |
| **Lista de alocados ao projeto** (por disciplina/cargo, nominal) | semanal | **6ª feira até 12h → CONSAG** | Léo / Bruna / Aline |
| **LD Projeto CONSAG** (arquivo de trabalho) | diário | envio até 12h | Léo / Bruna |
| **LD Projeto PETROBRAS** (sem informações internas OTZ×CONSAG) | quinzenal | — | Léo / Bruna |
| **Previsão de Faturamento** | quinzenal | **até o 3º dia útil → CONSAG** | Bruna / Aline |
| **Curva de Rundown** (docs previstos p/ emissão por semana) | semanal | — | Aline |
| Curva S | mensal | — | Bruna |
| Cronograma (estrutura da EAP Física, por unidade e disciplina) | semanal | — | Amanda |
| **Histograma do projeto (H·mês)** | mensal | até o 3º dia útil | Léo / Bruna / Aline |
| Planilha de alocação de pessoal (HH / R$) | mensal | após fechamento da medição | Bruna / Aline |
| **RDO — Relatório Diário de Ocorrências** (RDOweb) | diário | **até 11h** (sexta sai na própria sexta) | Léo / Gilberto |
| **Relatório de Controle de Atendimento de Markup** | semanal (emissão mensal à PB) | — | Amanda |
| Relatório Mensal de Projeto | mensal | levantamento semanal | Gilberto / Aline |
| Diligenciamento de propostas de fornecedores e LETs | diário | — | Laylla / Gilberto / Aline |
| Diligenciamento de documentos de fornecedores + **LD DFs** | semanal (acomp. diário) | — | Amanda |
| Lista de pré-carga no PW / no SIGEM | por demanda | — | Léo/Laylla/Amanda · Bruna |
| Apresentação RAS (semanal) / RAC (mensal) / Comitê CSG-OTZ (mensal) | — | — | Aline / Gestão |

**Controles solicitados pela PB/CONSAG via Anexo VII, com status declarado no ACF-001:**

| Controle | Status declarado |
|---|---|
| Diagrama de precedência dos documentos técnicos | "concluído" — mas **só HVAC e Telecom apresentadas** ⚠️ |
| Qtde docs emitidos × pré-alocados no GED | com a emissão da LD e pré-cargas |
| Entrada de docs em workflow | Relatório BI |
| Status de elaboração, inclusive docs em **hold** | Relatório BI |
| Status e propósito de documentos no GED | Relatório BI |
| Cumprimento de prazo de emissão | Relatório BI |
| **Timeline com avanço das atividades** | 🔴 **"não iniciado / não pensado"** |
| Necessidades de correção, controle de comentários e MARKUP | Relatório BI |
| **Atendimento à rede de precedência dos documentos** | 🔴 **"não iniciado / não pensado"** |
| **Controle de atendimento aos comentários da PETROBRAS** | 🔴 **"não iniciado"** |
| **Controle de marcas de campo (emitidas / no GED / pendentes / revisadas)** | 🔴 **"não iniciado"** |

> 🔑 **Quatro controles exigidos por anexo contratual estão declarados como "não iniciado" pela
> própria OTZ, em documento de 29/06/2026.** Isso é uma não conformidade documentada contra si
> mesma. São exatamente os controles que um sistema autônomo entrega quase de graça a partir das
> fontes já mapeadas — **e são a melhor primeira entrega possível do Ilson**, porque fecham uma
> pendência contratual conhecida.

---

## 10. Especialista do contrato — exposição e defesa

### 10.1 🔴 Exposição nº 1 — Quantidade de PPU estourada em isométricos

| | |
|---|---|
| **O fato** | Contrato: 925 IS. LD: 3.378 IS. Saldo de PPU: **−446 documentos** (era −335 em 20/07) |
| **A cláusula** | MD-903 §7.11 fixa os quantitativos por tipo e severidade. A PPU (Anexos IIA–IID) fixa preço unitário e quantidade |
| **O risco** | Produzir ~850 isométricos sem cobertura de preço unitário |
| **A armadilha** | IS é o item mais barato da PPU → **estoura em quantidade sem estourar em valor**; a CONSAG dirá que há saldo financeiro |
| **O que protege a OTZ** | (a) A LD com o excedente **foi aprovada pela CONSAG** em 30/06/2026 ✅ — há concordância documentada com o escopo maior; (b) o saldo positivo em outros itens permite pedir **remanejamento** antes de pedir aditivo; (c) o próprio RL já registra formalmente a divergência e a reconciliação em curso |
| **A ação** | Formalizar por **NMP / Anexo XV** o remanejamento entre itens de PPU **antes** de consumir mais saldo. Registrar a data em que a exposição foi comunicada |

### 10.2 🔴 Exposição nº 2 — As 98 Folhas de Dados

Pedido da CONSAG em 01/07/2026 para retirar 98 FDs da LD. Impactos declarados pela própria
OTZ: escopo, curva física, avanço financeiro, quantitativos de PPU, e **atividades correlatas
de atualização e compatibilização nas bases COMOS e E3D** — que continuam devidas mesmo sem a
FD ser emitida.

**O que protege a OTZ:** MD-903 §12 e §18 mantêm a obrigação de manter COMOS e E3D atualizados
"pari passu" (ACF-001) — logo, retirar a FD **não retira o trabalho**, apenas o entregável
remunerado. Isso é exatamente o argumento de pleito. **O que enfraquece:** 50 dias de
"em avaliação" sem posição formal.

### 10.3 🔴 Exposição nº 3 — Campos contratuais em branco na LD

| Campo | Preenchimento | Por que é contratual |
|---|---|---|
| **`SEVERIDADE`** | **0 / 2.824** | MD-903 §7.10 — é o critério que define esforço de revisão. Sem registro, não há como provar que "BAIXO" virou "ALTO" |
| **`Rede de Precedência`** | **0 / 2.824** | Exigência do Anexo VII; ACF-001 declara "concluído" com 2 disciplinas de 20 |
| **`FLUXOGRAMA (REF. Isométrico)`** | **0 / 2.824** | É a rastreabilidade P&ID→isométrico; sem ela não se prova bloqueio a montante |
| `DOC COM PENDÊNCIA EXTERNA` | 7 / 2.824 | Deveria marcar todo documento travado por terceiro |
| `OBSERVAÇÃO — PENDÊNCIAS E RESTRIÇÕES` | 260 / 2.824 (9%) | É onde vive a prova qualitativa do bloqueio |

> **Princípio contratual:** em pleito, **o ônus da prova é de quem alega**. A OTZ tem os campos
> e não os preenche. Cada dia de não preenchimento é prova perdida de forma irrecuperável —
> ninguém reconstrói em 2027 a severidade real de uma revisão feita em 2026.

### 10.4 🟠 Exposição nº 4 — Prazos do ciclo documental

| Obrigação | Prazo | Quem | Situação |
|---|---|---|---|
| Comentar/aprovar documento emitido | 10 DU | CONSAG e PB | Máximo observado no SIGEM: **159 dias úteis em workflow** ⚠️ |
| **Analisar comentários e emitir revisado** | **5 DU** | **OTZ** | Ver `METODOLOGIA` §5.5 — é a obrigação mais apertada do contrato |
| Entregar documentação técnica ao fim do escopo | — | OTZ | MD-903 §7.9 |
| Corrigir erros imputáveis à OTZ | imediato, **sem ônus**, em qualquer fase | OTZ | MD-903 §6.8 — obrigação perpétua |
| Informar erros/omissões no projeto da PB | obrigatório | OTZ | MD-903 §6.8 — **e essa é a via da SIT** |

🔑 **O prazo de 5 DU da OTZ é mais rígido do que o de 10 DU do cliente, e a OTZ tem muito mais
documentos.** Qualquer medição de SLA que a OTZ publique será usada contra ela também. Publique
os dois lados, sempre, na mesma tabela — assimetria de transparência custa caro em auditoria.

### 10.5 🟠 Exposição nº 5 — Comunicação direta com a Petrobras

Procedimento §7.1: contato direto OTZ→Petrobras **sem autorização escrita da CONSAG** pode
gerar penalidade contratual. Com o Ilson assumindo indicadores e reuniões, é o tipo de erro
fácil de cometer de boa-fé (responder um e-mail em cópia, participar de reunião técnica).
**Regra prática: toda comunicação sai para a CONSAG; a Petrobras entra em cópia só se a CONSAG
tiver colocado.**

### 10.6 ✅ O que protege a OTZ hoje

1. **A LD de 30/06/2026 foi aprovada pela CONSAG** — o escopo maior tem aceite documentado.
2. **O RL mensal registra formalmente todas as divergências** (PPU, denominadores, 98 FDs,
   pré-carga). Relatório emitido e recebido é notificação. **Continue registrando tudo,
   sempre, no relatório mensal** — é o instrumento mais barato de preservação de direito.
3. **A responsabilidade técnica do projeto original é da Petrobras** (MD-903 §6.3). Erro
   herdado não é erro da OTZ, desde que **comunicado por SIT antes da execução** (§6.8, §7.8).
4. **O aditivo NMP 3D FORNO/PSA já foi medido a 100%** (R$ 868.935) — precedente de que
   escopo adicional neste projeto é reconhecido e pago. **Use esse precedente.**
5. **A qualidade está sob controle:** IDR 2,1% (meta ≤3%), DAF 1,70% (meta ≤5%), 1ª auditoria
   interna realizada em jun/26, 12 NCs acumuladas. Sistema de gestão funcionando.
6. **Dependência técnica demonstrável:** a relação IS-955→IS-200 está 100% mapeada no próprio
   arquivo contratual (LD). É prova documental de que a fila de trabalho é governada por
   predecessor, não por produtividade.

### 10.7 Os dados do dashboard que são munição contratual

Em ordem de valor probatório:

| # | Dado | Onde está | Prova o quê |
|---|---|---|---|
| 1 | **Data real 1ª emissão PW × data programada BL0/BL1** | LD | Cumprimento (ou não) do prazo de emissão, por documento |
| 2 | **Dias úteis em workflow no SIGEM** | `RELATÓRIO SIGEM` | Tempo de resposta de CONSAG e Petrobras contra os 10 DU |
| 3 | **Data recebimento markup → data atendimento** | `RELATÓRIO MARKUP` + LD | Cumprimento dos 5 DU da OTZ |
| 4 | **`JA_EMITIDO_NO_SIGEM = N` + já emitido no PW** | `SIGEM PREVISTOS` × PW | Receita retida por ato de terceiro |
| 5 | **`Texto de Consolidação` das recusas** | `SIGEM CONSOLIDAÇÃO` (2.571 recusas) | Natureza do retrabalho: erro da OTZ × mudança de critério do cliente |
| 6 | **`STATUS PARA ANÁLISE DOS DESVIOS`** | LD-940 | **Atribuição nominal do atraso** — o padrão-ouro; replicar na LD-911 |
| 7 | **Saldo de PPU por item, série temporal** | LD `CONSUMO PPU` | Velocidade de consumo da exposição |
| 8 | **`Folhas` e `Formato`** | `RELATÓRIO DOCUMENTO` | Esforço real × severidade contratada |
| 9 | **Cadastro de horas (HH por documento)** | `cadastro_horas` | Custo real da revisão — base de qualquer pleito de esforço |
| 10 | **GRDs com data e destinatário** | `RELATÓRIO EMISSÃO` | Protocolo — a prova de que algo foi entregue e quando |

---

## 11. Lacunas de conhecimento — o que Ilson precisa confirmar

### 11.1 ❓ Documentos que ainda não foram lidos e são necessários

| Prioridade | Documento | Por quê |
|---|---|---|
| 🔴 | **Anexo VII — Diretriz de Engenharia e Documentação Técnica** (`Rev.0`) | Define propósitos, precedência, relatórios BI. É citado em quase toda linha do ACF-001 |
| 🔴 | **Anexos IIA/IIB/IIC/IID — Planilha de Preços** | A PPU completa com valores unitários oficiais e quantidades por item |
| 🔴 | **Anexo VI — Diretriz de Planejamento e Controle** (`ET-5290.00-22000-911-1LV-001`) | Estrutura obrigatória da EAP e do cronograma |
| 🔴 | **Anexo XIX — Relação de Documentos** (`Rev.AD.xlsx`, aba `06 - REFERÊNCIA_PROJETO`) | **É a origem da LD** — e onde deve estar a severidade original |
| 🟠 | **Anexo XV — Alteração de Escopo Contratual** | O rito exato do aditivo |
| 🟠 | `MD-…-200-PEI-901` (Tubulação) e `MD-…-940-PEI-904` (Modelo 3D) | Fecham o gargalo principal |
| 🟠 | `PR-5290.00-22311-910-C1U-001` — Plano da Qualidade | Citado 2× no Procedimento |
| 🟠 | `PR-5290.00-22311-910-C1U-003` — Matriz de Comunicação | Complementa o Anexo I |
| 🟡 | `ET-0000.00-0000-94P-PEI-001` (CAE 2D) e `-002` (CAE 3D) | Critérios de projeto das ferramentas |
| 🟡 | Contrato 00025129 e seus anexos, de 05/12/2025 | O texto contratual em si — penalidades, garantias, rescisão |
| 🟡 | **Mapa de Controle de Pendências** (anexo do RL) e **Mapa de Premissas** | As 20 pendências técnicas nominais |

### 11.2 ❓ Perguntas factuais em aberto

1. **Qual é o valor total do contrato 00025129?** Deduzido em ≈ R$ 30,44 M pelos percentuais
   do RL, mas nunca declarado explicitamente. Confirmar. E o teto de PPU calculado na taxonomia
   é R$ 13,67 M — **os dois números não fecham**; provavelmente PPU cobre só o item 1.2
   (Projeto Remanescente, ≈ R$ 19,86 M). Confirmar a composição.
2. **Quem é o Diretor de Engenharia da OTZ?** O organograma do Procedimento (26/06) diz
   *Monica Salgado*; o do RL mensal (20/07) diz *Gildeon Filho* — que também aparece como Líder
   de Segurança e como Responsável Técnico do consórcio. Provável erro de edição.
3. **`ACF-001` diz "RNEST — LOTE C" no cabeçalho.** O Z-546 é LOTE D. O arquivo é herdado do
   projeto irmão? A rotina descrita vale integralmente para o Z-546?
4. **A LD-940 tem abas com dados da área 22313 / U-32-UHDT-D.** Idem: arquivo clonado. Há um
   projeto irmão na OTZ (UHDT-D / U-32)? Compartilha equipe com o Z-546?
5. **"CONSÓRCIO CONSAG UGH" × "CONSÓRCIO CONSAG UHDT-D"** aparecem no mesmo procedimento
   (§capa e §6.1). São o mesmo CNPJ? Duas denominações do mesmo consórcio?
6. **Contrato Petrobras**: o RL cita `5900.0131300.25-2`; a LD-940 cita `5900.0131300.25.2`
   (ponto × hífen). Qual é o correto para citação formal?
7. **O prazo de engenharia (18 meses → ~jun/2027) × a curva S até dez/2027.** A curva inclui
   assistência técnica e as-built, que estão nos 36 meses de vigência? Formalizado onde?
8. **Existe baseline contratual "BL 0" e "BL 1" na LD.** Qual delas é a baseline oficial
   perante a CONSAG hoje? A reprogramação de 05/04/2026 virou BL1 aprovada ou é referência
   interna?
9. **A EAP financeira da LD-940 está zerada.** O ADF (70%/30%) está sendo medido em outro
   arquivo, ou não está sendo apropriado?
10. **Qual é o preço unitário oficial de cada item da PPU?** Os valores da taxonomia vieram da
    aba `CONSUMO PPU` — confirmar contra o anexo contratual antes de usar em pleito.
11. **Quem, do lado da OTZ, é o dono formal da pré-carga no SIGEM?** O ACF-001 aponta Bruna;
    a LD-940 tem status "AGUARDANDO LD CONSOLIDADA PARA PRÉ CADASTRO NO SIGEM". Precisa de
    dono único e SLA interno.
12. **As 20 pendências técnicas** (Civil 5, Instrumentação 5, Telecom 3, Tubulação 3,
    Elétrica 2, Mecânica 2) — o Mapa de Controle de Pendências não veio anexo. É a lista
    nominal do que trava cada disciplina.
13. **`hold` e `qtd hold` existem no E-CLIC e estão 100% vazios.** O Anexo VII exige controle
    de documentos em hold. Vale ativar o campo?
14. **Os 74 "Chave do Consolidador" da Petrobras** — existe de-para chave→nome? Isso permitiria
    identificar nominalmente onde a fila do cliente engarrafa.

### 11.3 ⚠️ Inconsistências encontradas nesta rodada (para corrigir na fonte)

| # | Inconsistência | Onde |
|---|---|---|
| 1 | Avanço previsto e realizado sobre **revisões diferentes da LD** (2.852 × 2.404) | RL §3, admitido pela própria OTZ |
| 2 | Avanço financeiro citado como **28,51% no quadro e 26,32% no texto** do mesmo relatório | RL §3 × §8.3 |
| 3 | Texto do RL diz *"emitidas até 20-Jun-26"* no quadro que é de **21-Jul-26** | RL §8.2 |
| 4 | Indicador DAF diz *"até 20/06"* usando os números **de 20/07** | RL §10.2 |
| 5 | IDR rotulado *"Junho/26"* em relatório do período 21/06–20/07 | RL §10.2 |
| 6 | Saldo de `RL - NOVO` = **+53** no RL e **−12** na aba `CONSUMO PPU` da LD | RL × LD |
| 7 | Total de docs da LD: **2.740** (quadro de emissão), **2.477** (PPU), **2.824** (previstos LD F_0), **2.404** (LD_D_3), **2.852** (LD_A_0) | cinco números diferentes circulando |
| 8 | `SEVERIDADE`, `Rede de Precedência`, `FLUXOGRAMA` 100% vazios | LD |
| 9 | Cabeçalho "LOTE C" no ACF-001; abas 22313 na LD-940 | arquivos herdados |
| 10 | `DATA_MARCACAO` com registros de 2015 e 2019 no SIGEM Previstos | dado histórico não filtrado |
| 11 | Nome do Diretor de Engenharia divergente entre dois documentos oficiais | Procedimento × RL |
| 12 | `DISCIPLINA OTZ` com caixa inconsistente (`PROCESSO` × `Processo`, 5 pares) | LD — já apontado na taxonomia |

---

## 12. Resumo de uma página — o que decorar

> **A obra.** Complementação do projeto executivo da U-36 (Unidade de Geração de Hidrogênio) +
> SE-3400, Lote D do Trem 2 da RNEST, Ipojuca/PE. Não é projeto novo: é revisão e conclusão de
> um detalhamento existente, espelhado no Trem 1.
>
> **A cadeia.** Petrobras → Consórcio CONSAG UGH (contrato EPC 5900.0131300.25-2) →
> OTZ Engenharia (contrato 00025129, 05/12/2025, 36 meses de vigência / 18 de engenharia).
> A OTZ **nunca** fala direto com a Petrobras.
>
> **Os três GEDs.** E-CLIC (OTZ, interno) → PW (CONSAG, aprovação) → SIGEM (Petrobras,
> **medição**). A OTZ é responsável por gerir o fluxo nos três.
>
> **O dinheiro.** PPU = preço fechado por `TIPO_DOC – NOVO|REVISÃO`. Contrato ≈ R$ 30,4 M.
> Medido até jul/26: R$ 9,76 M (30,29%). **Só emissão no SIGEM gera receita.** Medição fecha
> dia 20 (dia 19 para isométrico), fatura em M+1, recebe em M+2. Amortização do adiantamento
> começou no BM 09 (ago/26).
>
> **O tamanho.** 2.824 documentos de projeto + 1.600 isométricos de construção = **4.424
> entregas**, contra **2.193 na baseline contratual**. Tubulação é **76% de tudo**.
>
> **O gargalo.** **1.153 dos 1.600 IS-955 estão bloqueados** porque o IS-200 correspondente
> ainda não foi emitido. Buffer de trabalho liberado: **206**. A causa-raiz é o E3D incompleto
> (PSA e Fornos não modelados) e as ferramentas de extração instáveis.
>
> **O ritmo.** Faltam **3.019 primeiras emissões** em **36 semanas** → **83/semana**.
> Média mai–jul: 53/sem. Agosto: 116/sem. Precisa sustentar o ritmo de agosto.
>
> **A exposição.** Saldo de PPU **−446 documentos** e piorando ~110/mês, concentrado em
> isométricos. 98 FDs retiradas sem rito. Severidade e precedência sem registro.
>
> **A defesa.** LD aprovada pela CONSAG em 30/06. Relatório mensal registrando tudo.
> Responsabilidade do projeto original é da Petrobras. Precedente de aditivo pago (NMP 3D
> Forno/PSA, R$ 868.935 a 100%). Qualidade dentro das metas.
>
> **A primeira jogada.** Zerar a pré-carga no SIGEM: receita pronta, retida por ato de
> terceiro, com lista nominal de 8 documentos parados desde maio.

---

# 13. PROPOSTA DE DIMENSIONAMENTO DOS KPIs

> Base analisada: `DASH_BOARD_KPI_RNEST_20082026.html` (status 18/08/2026, emissão 20/08/2026),
> a apostila de 38 páginas, a `CARTA_OPUS_DASHBOARD_KPI.md`, o `METODOLOGIA_VELOCIDADE_Z546.md`
> e — o que muda tudo — o **fluxograma do §9.2 do Procedimento de Coordenação**, decodificado
> integralmente nesta rodada (§13.2).
>
> Estado atual: **8 KPIs ativos** (1, 2, 3, 4, 5, 6, 7, 9). O KPI 8 (Curva S) foi removido em
> 20/08/2026 por diretriz.

## 13.0 As cinco regras de assertividade

Antes de qualquer número. Se um KPI viola qualquer uma destas, ele não vai para reunião:

1. **Um número, uma fonte, um filtro, uma data-âncora.** Escrito no rodapé do painel, sempre.
2. **Denominador visível.** Percentual sem `n=` ao lado é opinião.
3. **Régua contratual citada com o artigo.** "SLA de 3 DU" vira "SLA de 3 DU — PROC-COORD
   RUGH-PEX-OTZ-EX-U036-PRJ-PT-0002 rev. 0, §9.2, fluxograma".
4. **Simetria.** Todo KPI que mede o cliente mede também a OTZ, na mesma tabela. Assimetria de
   transparência é o que destrói credibilidade numa auditoria.
5. **O denominador previsto e o realizado vêm da mesma revisão da LD.** É o erro que a própria
   OTZ registrou no RL de julho. Nunca mais.

## 13.1 Diagnóstico estrutural — as três cegueiras do dashboard atual

**Cegueira nº 1 — o dashboard não enxerga o SIGEM.** Os KPIs 3 a 9 vêm inteiramente do
ProjectWise. O PW é o GED da CONSAG. **A medição, o faturamento e o cumprimento contratual
perante a Petrobras acontecem no SIGEM.** Consequência: o dashboard mede *entrega à CONSAG*,
não *entrega ao cliente*. Um documento pode aparecer como "Aceito" no KPI 4 e valer R$ 0. Hoje
há **141 documentos na LD sem pré-carga no SIGEM** e **733 no relatório de previstos da
engenharia** — todos invisíveis no painel. **Esta é a correção mais importante de todas.**

**Cegueira nº 2 — o dashboard não enxerga dependência.** Ele mede quantos documentos saíram,
por quem e em quanto tempo. Não mede **quantos poderiam ter saído**. A frente de isométricos de
construção tem 1.600 documentos previstos e **apenas 206 liberados para produção** — os outros
1.153 estão bloqueados pelo IS-200 correspondente. Nenhum KPI mostra isso. Sem esse número,
toda cobrança de produtividade sobre a Tubulação é injusta e todo compromisso de prazo é chute.

**Cegueira nº 3 — o dashboard não enxerga dinheiro.** Não há PPU, não há saldo contratual, não
há valor retido. O projeto tem **saldo de PPU em −446 documentos**, piorando ~110/mês, e
**R$ 9,76 M medidos de ~R$ 32,2 M**. O painel que a gestão olha não fala a língua em que a
gestão decide.

**O que está sólido e não deve ser mexido:** a arquitetura de filtro compartilhado (KPI 3–9), a
paleta consistente entre KPI 4 / 6 / 7 / 9, a exibição do `n=` sob as barras do KPI 6, a escala
de cor relativa ao SLA no KPI 9, e as seções de ressalvas da apostila. Isso é trabalho de
qualidade profissional. **A proposta abaixo não reconstrói: ela corrige a régua, adiciona a
dimensão que falta e hierarquiza.**

## 13.2 🔑 A régua contratual completa — o fluxograma do §9.2 decodificado

Esta é a descoberta desta rodada e ela **reescreve três KPIs**. O fluxograma do item 9.2 do
Procedimento de Coordenação (folha 11 de 20) não traz apenas os 3 du e 2 du da CONSAG que a
apostila já usa. Ele traz **a escada inteira, incluindo os SLAs da própria OTZ e três cenários
de ciclo fechado com prazo-alvo declarado**:

```
  Rev. 0_0  Emissão Preliminar — Para Comentários CONSAG
      │
      │  ◄── CSG – 3 du
      ▼
  ┌─ Aprovado? ─┐
  │             │
 SIM           NÃO
  │             │  ◄── OTZ – 3 du
  │             ▼
  │   Rev. 0_1(n)  Emissão Preliminar — Para Aprovação CONSAG
  │             │
  │             │  ◄── CSG – 2 du
  │             ▼
  │       ┌─ Aprovado? ─┐
  │      SIM           NÃO ──► OTZ – 3 du ──► volta p/ Rev. 0_1(n)   ⟲
  │       │                                   【CENÁRIO 3 = x du (x dc)】
  │  ◄── OTZ – 2 du
  │       │
  │  ◄── OTZ – 3 du
  ▼       ▼
  Emissão ORIGINAL (R.0)  ──►  PW  ──► ◄◄ OTZ – 0 du ►► ──►  SIGEM
                                            🔴 MESMO DIA

  【CENÁRIO 1 — aprovou de primeira  =  6 du (8 dc)】
  【CENÁRIO 2 — um ciclo de comentário =  10 du (14 dc)】
  【CENÁRIO 3 — dois ou mais ciclos    =  indefinido】

  Depois da Emissão Original no SIGEM e no PW:
     CONSAG e PETROBRAS  →  10 du para comentar ou aprovar   (§9.2, texto)
     OTZ                 →   5 du para analisar e emitir revisado (§9.2, texto)
```

**Quatro consequências imediatas, todas verificáveis no documento assinado:**

| # | Achado | Impacto no dashboard |
|---|---|---|
| 1 | **A OTZ tem SLA interno de 3 du** (emitir a Original após aprovação; e emitir a 0_1 após reprovação) e **2 du** no cenário 2 — **não 5 du** | 🔴 A série laranja do KPI 6 está sendo comparada contra a régua **errada e mais frouxa**. Os 6,2–7,2 du medidos não estouram 5 du por pouco: **estouram 3 du por mais que o dobro** |
| 2 | **`OTZ – 0 du` entre PW e SIGEM** — a Emissão Original deve ir ao SIGEM **no mesmo dia** em que é publicada no PW | 🔴 Obrigação com SLA zero que **ninguém mede**. É exatamente onde vivem os 141 documentos sem pré-carga. **Vira o KPI 10** |
| 3 | **Cenário 1 = 6 du · Cenário 2 = 10 du · Cenário 3 = indefinido** — prazo-alvo de ciclo fechado, declarado | ✅ Permite um KPI de aderência **desenhado pelo próprio procedimento**: o mais defensável que existe neste projeto. **Vira o KPI 11** |
| 4 | Os **10 du de CONSAG e Petrobras** valem **após a emissão no SIGEM *e* no PW** | ⚠️ Se o documento está no PW mas não no SIGEM, **o relógio dos 10 du da Petrobras não começou** — e a culpa do não-início é da cadeia de pré-carga, não da Petrobras |

> 🔑 **O item 4 é a mais elegante peça de defesa do projeto**, e corta nos dois sentidos: protege
> a Petrobras de ser acusada injustamente **e** transforma a pré-carga pendente no gargalo
> nominal e datado que ela realmente é. Usar isso em reunião é jogo de gente grande.

## 13.3 KPI a KPI — diagnóstico e correção

---

### KPI 1 — Horas Utilizadas e Previstas por Disciplina

**Números publicados:** 26.521,4 HH realizado · 42.119,5 HH previsto (teto) · 30.467 HH
previsto (base) · 38,6% avanço em HH · 3.024 docs pendentes · 1.353 docs formalizados ·
9 disciplinas.

**1. Os dados de entrada estão corretos?** ⚠️ **Parcialmente.**
- ✅ Fonte certa: cadastro de horas próprio da OTZ, a única fonte de HH.
- 🔴 **Filtro não declarado no painel:** o realizado de 26.521,4 h exclui PLANEJAMENTO
  (3.970 h) e outros grupos. O total bruto do cadastro é **30.491,4 h**. Quem somar as barras
  não chega ao card. **Declarar a exclusão no rodapé, com o valor bruto ao lado.**
- 🔴 **Horas aprovadas e não aprovadas estão misturadas sem sinalização** (achado da carta:
  1.168 lançamentos sem aprovação; agosto ~45% incompleto). Um número de HH que inclui
  lançamento não aprovado **não sobrevive a uma pergunta da supervisão**.
- ⚠️ Data-âncora: 18/08/2026 — mês de agosto incompleto. A última barra mensal de toda série
  de HH está estruturalmente subdimensionada.

**2. Mede hoje × deveria medir.** Hoje mede *quantas horas foram lançadas*. Deveria medir
*quantas horas foram lançadas, aprovadas e apropriadas ao escopo remunerado*. São coisas
diferentes e a distância entre elas é o risco de estouro de custo.

**3. Como torná-lo 100% assertivo.**
- Separar em **três camadas empilhadas**: `aprovado` · `lançado não aprovado` · `estimado do
  período em aberto`. Uma barra, três tons.
- Excluir o mês corrente do cálculo de tendência e marcá-lo com hachura.
- **Explicitar as duas previsões:** "teto" (42.119,5) e "base" (30.467) precisam de definição
  de uma linha cada — de onde saem, e qual é a usada no % de avanço.
- Publicar `HH por disciplina ÷ documentos formalizados por disciplina` = **HH/doc realizado**,
  ao lado do `Ciclos/doc` que já existe. É a métrica que permite projetar.
- ⚠️ Resolver as 9 disciplinas do cadastro de horas × 15 do PW usando a chave canônica
  (**6º campo do CÓDIGO CONSAG**, §2.9). Não são "cadastros diferentes" — é falta de de-para.

**4. O número defensável em reunião:**
> *"**26.521 HH apropriadas até 18/08/2026**, das quais **X% já aprovadas**; **38,6% do previsto
> base de 30.467 HH**. Fonte: cadastro de horas OTZ, exclui Planejamento (3.970 h). Agosto
> parcial."*
>
> **Não leve** o 42.119,5 sem explicar por que existem dois previstos. Duas previsões sem
> definição é o convite mais rápido para perder o controle de uma reunião.

---

### KPI 2 — O que Consome as Horas (por Atividade)

**Números publicados:** 13 grupos. Topo: `Ident. e Compat. Doc. T1×T2` **4.423 h** ·
`Planejamento de Elaboração` 3.774 h · **`Sem Subitem Registrado` 3.115,5 h** ·
`Supervisão/Coordenação` 3.085 h · `Isométrico — Revisão` 2.925 h.

**1. Dados de entrada.** ✅ Fonte certa, mesma base do KPI 1.
🔴 **`Sem Subitem Registrado` = 3.115,5 h = 10,2% de todas as horas do projeto.** Um em cada
dez reais de mão de obra está sem destino declarado. **Isso não é uma nota de rodapé; é uma
não conformidade de apontamento.**

**2. Mede hoje × deveria medir.** Hoje mede horas por atividade genérica. **Deveria medir horas
por atividade *classificadas em escopo contratado × escopo adicional*.** Este KPI está a um
campo de distância de ser a peça central de qualquer pleito — e não está sendo usado assim.

**3. Como torná-lo 100% assertivo.**
- 🔑 **Adicionar uma dimensão binária: `escopo base` × `escopo potencialmente aditivo`.**
  `Ident. e Compat. Doc. T1×T2` (4.423 h — a maior atividade do projeto) é **exatamente** o
  trabalho que o MD-903 classifica por severidade. Se a severidade real supera a contratada,
  **essas 4.423 h são a base numérica do pleito**. Hoje elas são só uma barra azul-escura.
- Meta declarada para `Sem Subitem`: **< 3%**, com plano e prazo.
- Cruzar `Supervisão/Coordenação` (3.085 h = 10,1%) e `Reunião` (935 h) num indicador de
  **carga indireta** — hoje 13,2%. É a métrica que a diretoria pergunta.

**4. O número defensável:**
> *"**4.423 HH (14,5% do total) foram consumidas em identificação e compatibilização
> Trem 1 × Trem 2** — a maior atividade isolada do projeto, e a que corresponde diretamente à
> classificação de severidade do MD-5290.00-22311-940-PEI-903 §7.10."*
>
> Essa frase, dita numa reunião de comitê, abre a conversa de aditivo sem pedir nada.

---

### KPI 3 — Documentos Elaborados por Disciplina

**Números publicados:** 1.459 documentos, 15 disciplinas. Tubulação 879 (60,2%).

**1. Dados de entrada.** ✅ Fonte PW, filtro `ENG OBRA + OTZ PROJETISTA`, contagem por 1ª
`DataAceiteGRD`. Consistente e reproduzível.
⚠️ **Mas o universo está incompleto.** A LD prevê **4.424 entregas** (2.824 + 1.600 IS-955) e
registra **1.405 com 1ª emissão no PW** (1.164 + 241). O KPI mostra 1.459 — próximo, mas
**sobre outra população**. Os dois números precisam ser reconciliados e a diferença explicada.

**2. Mede hoje × deveria medir.** Hoje: "quantos documentos entraram no PW". Deveria: **"quanto
do escopo contratado foi entregue"** — o que exige um **denominador**. Um KPI de volume sem
denominador não responde à única pergunta que importa: *falta quanto?*

**3. Como torná-lo 100% assertivo.**
- 🔑 **Adicionar o denominador da LD por disciplina.** Vira barra de progresso, não barra de
  contagem: `Tubulação 659/2.011 = 33%`. O dado já existe (§3.4 deste documento).
- Adicionar uma **terceira barra: emitido no SIGEM**. `Elaborado (PW) × Emitido (SIGEM) ×
  Previsto (LD)` — três barras, uma disciplina, história completa.
- Normalizar as 15 disciplinas para os **20 trigramas oficiais** (§2.9). "SAFETY", "PROJETOS",
  "SISTEMA DE MODELO 3D" e "AUTOMAÇÃO" não são disciplinas do contrato.

**4. O número defensável:**
> *"**1.164 dos 2.824 documentos de projeto (41%) e 241 dos 1.600 isométricos de construção
> (15%) tiveram primeira emissão no PW** — LD rev. F_0 de 19/08/2026."*
>
> Fonte única (LD), denominador explícito, revisão citada. **Impossível de contestar.**

---

### KPI 4 — Documentos Revisados × Diretos e Situação do Fluxo

**Números publicados:** velocímetros `Emissão Preliminar 94` · `Atendendo Comentários 20` ·
**`Aguardando Petrobrás 743`** · `Aguardando Definição/Revisão 8` · `Aceito 573`. Total 1.438.

**1. Dados de entrada.** ✅ Classificação por sufixo de revisão (`_0`, `_1+`, sem sufixo) —
elegante, correta e ancorada no §9.2. Melhor ideia do dashboard.
🔴 **Mas o rótulo "Aguardando Petrobrás" está errado em 743 casos** — e é o maior número do
painel. O estado no PW é *Emitido para Cliente / Em Análise Engenharia*. Isso significa
**"saiu do loop interno com a CONSAG"**, não **"está no SIGEM com a Petrobras"**. Como
demonstrado no §13.2 item 4, **o relógio da Petrobras só começa quando o documento está no
SIGEM**. Com 141 documentos sem pré-carga, **parte desses 743 está aguardando a própria
cadeia OTZ→CONSAG→pré-carga, não a Petrobras.**

⚠️ Além disso: 1.438 ≠ 1.459 (KPI 3). 21 documentos não caem em nenhum velocímetro.

**2. Mede hoje × deveria medir.** Hoje mede "onde a revisão atual está no PW". Deveria medir
**"de quem é a bola, agora, com quantos dias de espera"**. Estado sem aging é foto sem relógio.

**3. Como torná-lo 100% assertivo.**
- 🔴 **Renomear `Aguardando Petrobrás` → `Emissão Original — fora do loop CONSAG`** e
  **quebrar em dois**: `no SIGEM (relógio de 10 du correndo)` × `no PW sem emissão SIGEM
  (relógio não iniciado)`. Cruzamento direto com `SIGEM DOCUMENTOS PREVISTOS`.
- **Adicionar aging a cada velocímetro:** mediana e P90 de dias parados. O dado já é calculado
  no KPI 6 — é reuso, não trabalho novo.
- Fechar a diferença de 21 documentos ou criar a categoria `outros estados`.
- 🔑 **Adicionar a coluna de atribuição nominal** — o modelo da LD-940
  (`OTZ / CONSAG / FORNECEDOR / CDA / PETROBRAS`). É o campo que transforma um velocímetro
  numa cobrança.

**4. O número defensável:**
> *"Dos 1.459 documentos no PW, **573 estão em estado terminal aprovado (39%)**. **114 estão no
> loop interno com a CONSAG** (94 em 1ª análise, 20 em reanálise). **743 saíram do loop
> interno** — destes, **N estão emitidos no SIGEM com o prazo de 10 du correndo** e
> **M ainda não foram emitidos no SIGEM**, sendo que **P aguardam pré-carga.**"*
>
> Essa frase, com N, M e P preenchidos, **é a peça mais valiosa que o Ilson pode levar à
> primeira reunião.** Ela demonstra domínio de contrato, de dado e de processo em 30 segundos.

---

### KPI 5 — Documentos Elaborados por Mês

**Números publicados:** série dez/25 → ago/26, soma 1.459.

**1. Dados de entrada.** ✅ Correto e fecha com o KPI 3.
⚠️ **Agosto está incompleto** (dado de 18/08) e é apresentado ao lado de meses cheios. A
tendência lida na última barra é sempre pessimista.

**2. Mede hoje × deveria medir.** Hoje mede ritmo passado. **Deveria medir ritmo passado contra
ritmo necessário.** Um gráfico de produção sem a linha de meta não informa decisão nenhuma.

**3. Como torná-lo 100% assertivo.**
- 🔑 **Adicionar duas linhas horizontais:** `ritmo programado do mês (BL1 da LD)` e
  `ritmo necessário para o marco de abr/2027`. Os dois já estão calculados neste documento
  (§8.2): a programação mensal e os **83 documentos/semana** necessários.
- Hachurar o mês corrente e anotar `(parcial — 18 de 31 dias)`.
- **Separar produção corrente de recuperação de passivo** — recomendação do próprio RL mensal
  da OTZ. Documento cuja data programada já passou é passivo; o resto é corrente. **São duas
  séries, e a gestão precisa das duas.**

**4. O número defensável:**
> *"Ritmo de primeiras emissões: **53/semana** na média de mai–jul; **116/semana** em agosto
> (parcial). Necessário para cumprir a programação da LD até abr/2027: **83/semana**.
> Restam **3.019 primeiras emissões em 36 semanas**."*

---

### KPI 6 — Velocidade de Resposta: OTZ × CONSAG × Petrobrás 🔴 *o que mais precisa de correção*

**Números publicados:** CONSAG 1ª análise 2,86 du (SLA 3, n=1.223) · CONSAG reanálise 2,25 du
(SLA 2, n=263) · **Petrobras 11,22 du (SLA 10, n=250)** · OTZ turnaround **(SLA declarado 5)**.

**1. Dados de entrada.** ⚠️ **Três problemas, um deles grave.**
- 🔴 **O SLA da OTZ está errado.** O fluxograma do §9.2 dá **3 du** para a OTZ (emitir a
  Original após aprovação, e emitir a 0_1 após reprovação) e **2 du** no cenário 2. Os
  **5 du** do texto valem para o **atendimento de comentários pós-emissão original**, que é
  outra fase. **Hoje o dashboard mede a OTZ contra a régua mais frouxa que existe no
  documento.** Em reunião, a CONSAG pode apontar isso — e a OTZ perde o argumento e a
  credibilidade no mesmo minuto. **Corrigir antes de apresentar, por iniciativa própria.**
- 🔴 **Contagem sem feriados.** Os 11,22 du da Petrobras caem para **10,53 du** com feriados
  nacionais. Continua acima do SLA, mas a margem cai de 12% para 5%. **Em contrato brasileiro,
  "dia útil" exclui feriado.** A LD já tem a tabela de feriados até dez/2027 (aba `Padrões`).
  Não há desculpa técnica para não usá-la.
- ⚠️ **A régua da Petrobras deve vir do SIGEM, não do PW.** O `Dias úteis em workflow` do
  relatório SIGEM é o número oficial da própria Petrobras: média **5,4 du**, mediana 3,
  máximo **159**. Julgar a Petrobras com dado da Petrobras é infinitamente mais forte do que
  julgá-la com dado do PW.

**2. Mede hoje × deveria medir.** Hoje mede a média de cada elo. **Deveria medir % de aderência
ao SLA com distribuição** — a média esconde tudo. Média de 5,4 du com máximo de 159 du não é
"dentro do prazo": é uma cauda longa que trava documentos específicos por meses.

**3. Como torná-lo 100% assertivo.**
- Corrigir o SLA da OTZ para **3 du** (e 2 du no cenário 2). Registrar a correção visivelmente.
- Adotar o **calendário de feriados** da aba `Padrões` da LD.
- Trocar a série da Petrobras pela do **SIGEM** (`Dias úteis em workflow`, `Nível 2 =
  04.ENGENHARIA`), mantendo a do PW como série secundária.
- Publicar, para cada elo: **média · mediana · P90 · % dentro do SLA · n**. Cinco números.
- Manter a série da OTZ mesmo sabendo que vai piorar. **É o item 4 das regras de assertividade
  e é o que dá autoridade a todo o resto do painel.**

**4. O número defensável:**
> *"Contra as réguas do PROC-COORD §9.2, com feriados nacionais: **CONSAG 1ª análise 2,86 du
> contra 3 du — dentro** (n=1.223); **CONSAG reanálise 2,25 du contra 2 du — ligeiramente
> acima** (n=263); **OTZ turnaround interno X du contra 3 du** (n=…); **Petrobras 10,53 du
> contra 10 du no PW e 5,4 du de mediana 3 no próprio SIGEM** (n=…). **Todos os elos estão
> próximos do SLA; nenhum é o gargalo do projeto — o gargalo é a fila de entrada, não a
> velocidade de resposta.**"*
>
> 🔑 **Essa última frase é a conclusão mais importante de todo o dashboard**, e ela só aparece
> quando o KPI 6 é lido junto do mapa de dependências. O tempo de resposta dos três atores soma
> ~16 du por ciclo. **O projeto não está travado por lentidão de análise — está travado por
> falta de documento liberado para entrar na fila.**

---

### KPI 7 — Classificação e Quantidade de Documentos Emitidos por Mês

**Números publicados:** 3.046 eventos de emissão, 4 categorias (`0_0` · `A_0/B_0…` · `_1+` ·
sem sufixo).

**1. Dados de entrada.** ✅ Correto e bem construído. A distinção evento × documento está
declarada na apostila (3.046 eventos × 1.459 documentos). É unidade diferente, não divergência.

**2. Mede hoje × deveria medir.** Hoje mede a **mistura de trabalho** do mês — quanto é
produção nova e quanto é retrabalho. É o conceito certo. **Falta o índice que o resume.**

**3. Como torná-lo 100% assertivo.**
- 🔑 **Publicar o índice de retrabalho:** `eventos _1+ ÷ eventos totais do mês`. Uma linha
  sobre as barras. **É a métrica que a Petrobras usa para julgar a qualidade da entrada** e
  hoje ela existe implícita nas barras, sem número.
- Cruzar com o **`Texto de Consolidação` do relatório SIGEM CONSOLIDAÇÃO** (2.571 recusas com
  texto) para classificar o motivo do retrabalho: **erro da OTZ × mudança de critério do
  cliente × dado de entrada ausente**. Essa classificação é a diferença entre "a OTZ erra
  muito" e "a OTZ recebe dado incompleto" — e ela é obtível por NLP simples sobre 1.822 textos
  distintos.
- Adicionar a categoria de **eventos de emissão no SIGEM**, hoje ausente.

**4. O número defensável:**
> *"**Índice de retrabalho interno de X%** no mês (eventos `_1+` sobre o total). O IDR
> contratual — documentos recusados sobre comentados — está em **2,1%, contra meta de ≤3%**
> (RL mensal, jun/26: 1 recusa em 47 comentados)."*
>
> Note que o **IDR já é um indicador contratual do Plano da Qualidade da OTZ e está sendo
> reportado no RL mensal — mas não está no dashboard.** Trazer para cá é ganho puro.

---

### KPI 8 — Curva S de Avanço Físico *(removido em 20/08/2026)* 🔴 *deve voltar, corrigido*

**1. Por que foi removido — e por que a remoção estava certa.** A curva projetava conclusão em
**10/03/2028** com base num tempo-padrão calculado sobre **250 pares de datas** da fase
Petrobras. Uma projeção de 18 meses apoiada em 250 observações, sem intervalo de confiança,
**não sobrevive a uma pergunta técnica.** Remover foi decisão correta.

**2. Por que ela precisa voltar.** 🔴 **A Curva S é obrigação contratual declarada:** consta do
ACF-001 como entrega **mensal** de responsabilidade do Planejamento, e é publicada todo mês no
Relatório Mensal (previsto 28,81% × realizado 27,11% em 20/07). **O dashboard da OTZ não pode
ser o único lugar da empresa onde a Curva S não existe.** Hoje o dashboard e o RL mensal contam
histórias diferentes sobre o mesmo projeto — e é o RL que vai para a CONSAG.

**3. Como fazê-la voltar de forma 100% assertiva.**
- 🔑 **Trocar a base:** a curva não deve ser projetada por tempo-padrão do PW. Deve ser a
  **curva contratual da LD** — previsto pela baseline BL1 congelada, realizado por emissão no
  SIGEM, exatamente como no RL mensal. **A fonte da Curva S é a LD, não o PW.**
- **Congelar o denominador** e publicá-lo: `previsto = 2.852 docs (LD_A_0 de 01/04/2026)`;
  `realizado = base corrente`. Enquanto forem diferentes, **exibir as duas curvas
  sobrepostas**, não uma comparação.
- **Separar a projeção do realizado** em painéis distintos. Projeção sempre com faixa
  (otimista/central/pessimista) e com o `n` que a sustenta.
- Adicionar a **curva de rundown** (2.740 documentos, S019→S086) ao lado — ela é a mesma
  informação em unidade que a obra entende.

**4. O número defensável:**
> *"**Avanço físico 27,11% realizado × 28,81% previsto — desvio de 1,70 ponto**, dentro da meta
> DAF de ≤5%. Base: emissões no SIGEM, curva do replanejamento de 05/04/2026.
> **Ressalva declarada: previsto e realizado ainda são apurados sobre revisões distintas da LD
> (2.852 × 2.404); reconciliação em curso, conclusão prevista para o fechamento de setembro.**"*
>
> 🔑 **Declarar a ressalva você mesmo é o que impede que ela seja usada contra você.** Esta é a
> diferença entre um analista e um gestor.

---

### KPI 9 — Duração Média por Fase, Tipo de Documento e Fornecedor

**Números publicados:** médias globais **2,863 · 2,251 · 11,216 du**. `ISOMÉTRICO` n=1.794,
peso 0,913 · `ISOMÉTRICO DE CONSTRUÇÃO/FABRICAÇÃO` n=1.759, peso 0,853,
**fases 1 e 2 hachuradas (sem dado)** · `REQUISIÇÃO DE MATERIAL` 32,2 du, peso 2,448×.

**1. Dados de entrada.** ✅ Construção rigorosa: limiar `N<5` cai para a média global,
hachura para célula sem dado, quebra por código emissor (C1U/CHZ/JEI/UOP/EVY). É o KPI
tecnicamente mais bem-feito do painel.
⚠️ Mas ele **herda os dois defeitos do KPI 6**: SLA da OTZ errado e contagem sem feriados.
⚠️ `ISOMÉTRICO DE CONSTRUÇÃO` tem **1.759 documentos e fases 1 e 2 sem nenhum dado** — usa a
média global. Ou seja: **o tipo mais numeroso do projeto tem tempo-padrão emprestado.**

**2. Mede hoje × deveria medir.** Hoje mede duração por fase e tipo — e serve de prova de que o
peso do KPI 8 não é arbitrário. **Deveria também ser a base do dimensionamento de capacidade:**
duração × volume restante = HH necessário por disciplina. Está a uma multiplicação de virar
planejamento de recurso.

**3. Como torná-lo 100% assertivo.**
- Aplicar as mesmas correções do KPI 6 (SLA 3 du para a OTZ, feriados).
- **Explicitar a cobertura de cada célula:** ao lado de cada tipo, `n real / n total`. Onde a
  cobertura for < 30%, marcar o tempo-padrão como *estimado*.
- 🔑 **Adicionar a projeção de capacidade:** `duração média × documentos restantes ÷ capacidade
  atual = semanas necessárias`, por disciplina. **É o número que responde "dá tempo?"** — a
  única pergunta que a diretoria realmente faz.
- Usar o código emissor (C1U / CHZ / JEI / UOP) também para **aderência de prazo**, não só para
  duração — a carta já identificou dispersão relevante (C1U +68,4 · CHZ −11,8 · JEI −40,0).

**4. O número defensável:**
> *"Ciclo médio completo de um documento: **16,3 du** (2,86 + 2,25 + 11,22). Requisição de
> Material é o tipo mais lento: **32,2 du, sendo 26,95 du só na fase Petrobras**. Isométrico de
> construção — 1.759 documentos, o tipo mais numeroso — **ainda não tem tempo-padrão próprio;
> usa a média global**, e isso está sinalizado."*

---

## 13.4 KPIs que faltam

Ordenados por **valor contratual ÷ esforço**. Os quatro primeiros são construíveis com dados já
mapeados e não exigem nenhuma fonte nova.

---

### ⭐ KPI 10 — Aderência ao `OTZ – 0 du` (PW → SIGEM) e fila de pré-carga
**Esforço: baixo · Valor: máximo · Prioridade: 1**

**O que mede:** o intervalo entre a Emissão Original no PW e a emissão no SIGEM, contra o
**SLA de 0 dias úteis** do fluxograma §9.2 — e, para os que não conseguiram, **por quê**.

**Fonte:** `LD` (`Data real 1ª Emissão PW` × `DATA REAL - PRIMEIRA EMISSÃO SIGEM`) +
`SIGEM DOCUMENTOS PREVISTOS` (`JA_EMITIDO_NO_SIGEM`) + `LD` (`PRÉ CADASTRADO NO SIGEM?`).

**Visual:** três blocos — `emitido no mesmo dia` · `emitido com atraso de N dias` ·
**`não emitido — bloqueado por pré-carga`**, com lista nominal e valor de PPU associado.

**Por que é o nº 1:** transforma um problema burocrático invisível em **receita retida, com
nome, data e valor**. Hoje há 8 documentos nominalmente identificados parados desde maio/junho,
141 na LD e 733 no relatório de previstos. É o KPI que **paga o próprio dashboard**.

---

### ⭐ KPI 11 — Aderência aos Cenários 1 / 2 / 3 do §9.2
**Esforço: médio · Valor: máximo · Prioridade: 2**

**O que mede:** cada documento é classificado no cenário em que caiu, e o ciclo total
`0_0 → Emissão Original` é medido contra o prazo declarado:

| Cenário | Descrição | Prazo-alvo | O que revela |
|---|---|---|---|
| **1** | Aprovou de primeira | **6 du (8 dc)** | Qualidade de entrada boa |
| **2** | Um ciclo de comentário | **10 du (14 dc)** | Retrabalho controlado |
| **3** | Dois ou mais ciclos | **indefinido** | 🔴 Onde o tempo se perde |

**Fonte:** PW — sequência de sufixos de revisão por documento.

**Por que importa:** **é o único KPI do projeto cujo prazo-alvo foi desenhado pelas duas partes
e assinado.** Não há como a CONSAG contestar a régua — ela a redigiu. E o Cenário 3, que hoje
ninguém conta, é onde mora o custo invisível do retrabalho.

---

### ⭐ KPI 12 — Cadeia crítica: documentos liberados × bloqueados
**Esforço: baixo · Valor: máximo · Prioridade: 3**

**O que mede:** de tudo que falta emitir, **quanto está tecnicamente liberado para produção**.

**Fonte:** `LD Trem 2 -ICs`, coluna `Correspondente - IS-200` (100% preenchida) cruzada com a
emissão do IS-200 na LD principal. Extensível a P&ID→IS-200 e Lista de Instrumentos→Lista de
I/O quando a `Rede de Precedência` for preenchida.

**Número de hoje:** **206 liberados · 1.153 bloqueados · 241 já emitidos** (de 1.600 IS-955).

**Por que importa:** é o KPI que **muda a conversa com a CONSAG** de "vocês estão devagar" para
"a fila de entrada tem 206 itens". É também o que protege a equipe de Tubulação de uma cobrança
que ela não tem como atender.

---

### ⭐ KPI 13 — Consumo e saldo de PPU
**Esforço: baixo · Valor: alto (política) · Prioridade: 4**

**O que mede:** por item de PPU, `qtde contratada × prevista na LD × já emitida × saldo`, com
**série temporal do saldo**.

**Fonte:** aba `CONSUMO PPU` da LD + coluna `CONSUMO PPU` (`BT`) + emissão SIGEM.

**Número de hoje:** **saldo total −446 documentos**, sendo **IS-NOVO −487 e IS-REVISÃO −366**;
saldo positivo em DE-NOVO +101, FD-REVISÃO +96, ET +107.
**Velocidade de deterioração: ~110 documentos/mês** (−335 em 20/07 → −446 em 19/08).

**Por que importa:** é o único KPI que fala a língua do Comitê Executivo. E a **velocidade de
deterioração** é o número que justifica agir agora e não em dezembro.

---

### KPI 14 — Horas não aprovadas e exposição de apontamento
**Esforço: mínimo · Valor: governança · Prioridade: 5**

`HH lançadas × HH aprovadas × HH em aberto`, por disciplina e por mês. Hoje há **1.168
lançamentos sem aprovação** e agosto ~45% incompleto. **Publique antes que perguntem.**

---

### KPI 15 — Diligenciamento de fornecedores (ADF)
**Esforço: baixo · Valor: alto · Prioridade: 6**

**Fonte:** LD-940, coluna `STATUS PARA ANÁLISE DOS DESVIOS` — que já atribui o atraso
nominalmente. **Números prontos:** 268 aguardando 1º envio · 82 recebidos · **18 CONSAG em
atraso · 12 fornecedor em atraso · 5 OTZ em atraso** · 142 sem pré-cadastro no SIGEM ·
**44 pacotes aguardando proposta** (de 95 pacotes totais).

**Por que importa:** metade do suprimento é de Instrumentação (47 de 95 pacotes) e o
diligenciamento é obrigação diária declarada no ACF-001. Hoje **não existe no dashboard**.

---

### KPI 16 — Severidade contratada × severidade real
**Esforço: alto (exige preencher a LD) · Valor: máximo em pleito · Prioridade: 7**

`Documentos por severidade contratada (MD-903 §7.11) × severidade real observada`, com o delta
convertido em HH e em R$. **É a peça que sustenta qualquer pedido de aditivo.** Depende de
preencher a coluna `SEVERIDADE` (ação #3 do §9.3). **Comece a coletar hoje mesmo, ainda que o
KPI só nasça em 60 dias** — severidade não se reconstrói depois.

---

### KPI 17 — Aderência por acervo emissor (C1U × CHZ × JEI × UOP)
**Esforço: baixo · Valor: alto e político · Prioridade: 8**

O código emissor do 5º campo do N-1710 identifica **de quem é o projeto original**. Aplicar
aderência de prazo por acervo separa *"a OTZ atrasou"* de *"o acervo herdado X é
sistematicamente pior"*. A carta já identificou dispersão relevante: **C1U +68,4 · CHZ −11,8 ·
JEI −40,0**. O dado já está no KPI 9, usado apenas para duração.

---

## 13.5 KPIs que devem ser fundidos

| Fundir | Em | Por quê |
|---|---|---|
| **KPI 3 + KPI 5** | **"Entrega por disciplina e no tempo"** — barras de progresso com denominador da LD + série mensal com linha de meta | São a mesma população (1.459), o mesmo conceito, em dois cortes. Separados, nenhum dos dois mostra "falta quanto". Juntos e com denominador, viram **o** painel de escopo |
| **KPI 6 + KPI 9** | **"Régua de tempo do contrato"** — durações por fase, por tipo, contra os SLAs do §9.2 | Já compartilham SLA, convenção de dias úteis e base. A apostila declara que os SLAs são idênticos. Manter separados duplica manutenção e multiplica o risco de divergência |
| **KPI 4 + KPI 10 (novo)** | **"Onde está a bola, há quantos dias, e com quem"** | O KPI 4 dá o estado; o KPI 10 dá o elo PW→SIGEM que hoje o KPI 4 confunde com "Petrobras". Juntos resolvem o erro de rótulo dos 743 |
| **KPI 1 + KPI 2** | *manter separados* ✅ | Recurso por quem × recurso por quê são perguntas de gestão distintas. A separação está certa |

**Resultado:** de 8 painéis fragmentados para **6 painéis densos** — mais 4 novos de alta
prioridade = **10 painéis**, cobrindo escopo, tempo, recurso, dependência, dinheiro e
fornecedor.

## 13.6 Hierarquia de importância — a arquitetura em três camadas

```
┌─ CAMADA 1 — DEFESA CONTRATUAL  (o que a OTZ leva para a CONSAG e a Petrobras)
│
│  1º  KPI 10 — Aderência PW→SIGEM e fila de pré-carga        🔴 receita retida
│  2º  KPI 6+9 — Régua de tempo do §9.2 (todos os elos)       🔴 prova de cumprimento
│  3º  KPI 11 — Aderência aos Cenários 1/2/3                  🔴 régua assinada pelas partes
│  4º  KPI 13 — Consumo e saldo de PPU                        🔴 exposição financeira
│  5º  KPI 8  — Curva S sobre base única (restaurado)         🔴 obrigação mensal
│
├─ CAMADA 2 — DIREÇÃO DE PROJETO  (o que decide a semana)
│
│  6º  KPI 12 — Cadeia crítica: liberado × bloqueado
│  7º  KPI 3+5 — Entrega por disciplina e no tempo, com meta
│  8º  KPI 4+10 — Onde está a bola, há quantos dias, com quem
│  9º  KPI 15 — Diligenciamento de fornecedores
│
└─ CAMADA 3 — GESTÃO DE RECURSO  (o que sustenta o resto)
│
│ 10º  KPI 1 — Horas por disciplina (3 camadas de aprovação)
│ 11º  KPI 2 — Horas por atividade, com marcação escopo base × aditivo
│ 12º  KPI 7 — Mistura de trabalho e índice de retrabalho
│ 13º  KPI 14 — Horas não aprovadas
│ 14º  KPI 16/17 — Severidade e acervo emissor  (maturidade)
```

### 🥇 O KPI mais crítico para defender a OTZ contratualmente

**KPI 6+9 — a régua de tempo do §9.2, com todos os elos medidos contra os SLAs corretos e com
feriados.**

A razão é jurídica, não estatística. **A única obrigação da OTZ com prazo numérico expresso no
procedimento assinado é o tempo de resposta.** Volume não tem prazo por documento; qualidade é
medida por IDR; escopo é discutido por NMP. **Mas o tempo de cada elo tem número, tem artigo e
tem fluxograma.** É o terreno em que uma disputa contratual efetivamente se decide.

E hoje esse KPI está **medindo a OTZ contra uma régua mais frouxa do que a assinada (5 du em vez
de 3 du) e sem feriados**. Ou seja: o principal instrumento de defesa da OTZ tem, embutido, o
argumento que a derruba. **Corrigir isso — por iniciativa própria, com a correção declarada no
painel — é a ação de maior retorno de todo este documento.**

O segundo mais crítico é o **KPI 10**, porque ele é o único que demonstra, com data e nome, que
**parte do atraso atribuído à OTZ é atraso de terceiro na cadeia de pré-carga** — e porque o
próprio fluxograma §9.2 estabelece que o relógio de 10 du da Petrobras **só começa após a
emissão no SIGEM**.

## 13.7 O painel de uma página para a primeira reunião

Se o Ilson tiver 10 minutos e um slide, é este:

| Bloco | Número | Fonte |
|---|---|---|
| **Escopo** | 1.164/2.824 docs de projeto (41%) · 241/1.600 IS-955 (15%) | LD rev. F_0, 19/08/2026 |
| **Ritmo** | 53/sem (mai–jul) · 116/sem (ago parcial) · **83/sem necessário** | LD, primeiras emissões |
| **Cadeia crítica** | **206 IS-955 liberados · 1.153 bloqueados por IS-200** | LD, col. `Correspondente - IS-200` |
| **Tempo** | CONSAG 2,86/3 du · 2,25/2 du · **PB 10,53/10 du** · OTZ X/3 du | PW + SIGEM, §9.2 com feriados |
| **Receita retida** | **N docs emitidos no PW sem emissão no SIGEM**, o mais antigo de maio | LD × SIGEM Previstos |
| **Exposição** | Saldo PPU **−446 docs**, deteriorando **110/mês** | Aba `CONSUMO PPU` |
| **Avanço** | 27,11% real × 28,81% previsto — desvio 1,70 p.p. (meta ≤5%) | RL mensal, curva de 05/04/2026 |
| **Qualidade** | IDR **2,1%** (meta ≤3%) · 12 NCs acumuladas · 1ª auditoria realizada | RL mensal |
| **Ressalva declarada** | Previsto e realizado ainda sobre revisões distintas da LD — reconciliação conclui em setembro | RL mensal |

**Uma frase de abertura:** *"O projeto está 1,7 ponto atrás da curva, com todos os elos de
resposta próximos do SLA. O gargalo não é velocidade: é fila de entrada. 1.153 dos 1.600
isométricos de construção estão tecnicamente bloqueados pelo isométrico de detalhamento
correspondente, e há documentos emitidos no PW desde maio que ainda não foram para o SIGEM por
falta de pré-carga."*

**Uma frase de fechamento:** *"Trago também três ressalvas do nosso próprio dado, antes que
alguém as encontre."*

## 13.8 Checklist de blindagem — antes de qualquer apresentação

- [ ] Todo painel tem rodapé com **fonte · filtro · data-âncora**
- [ ] Todo percentual tem `n=` visível
- [ ] Todo SLA cita **documento, revisão e item** (`PROC-COORD rev. 0, §9.2, fluxograma`)
- [ ] **Dias úteis excluem feriados nacionais** (tabela da aba `Padrões` da LD, até dez/2027)
- [ ] **SLA da OTZ corrigido para 3 du** no loop interno — com a correção anunciada
- [ ] Todo KPI que julga terceiro **julga a OTZ na mesma tabela**
- [ ] Mês corrente hachurado e rotulado `(parcial — N de M dias)`
- [ ] Previsto e realizado da Curva S com **a revisão da LD declarada em cada um**
- [ ] Ressalvas conhecidas ditas **pelo apresentador**, nunca descobertas pela plateia
- [ ] Nenhum número do dashboard **contradiz** o Relatório Mensal enviado à CONSAG — e, se
      contradisser, a diferença está explicada num slide de apoio

---

> **Nota final ao Ilson.** O dashboard que você construiu já é melhor do que a média do mercado:
> filtro compartilhado, paleta coerente, `n=` sob as barras, ressalvas documentadas em 38
> páginas. O que falta não é técnica — é **régua contratual correta, a dimensão SIGEM e a
> dimensão dependência**. As três correções cabem em uma semana de trabalho e transformam um
> painel bonito em **um instrumento de defesa contratual**. E a diferença entre as duas coisas é
> exatamente a diferença entre um bom analista e o engenheiro de planejamento em quem a diretoria
> confia.
