# Gabarito comentado — Atividade prática: Campo Minado

Estruturas de Dados — UniLasalle EAD — Grau 1 — Aula 4

A atividade **não tem entrega**: ela serve para você praticar e consolidar
as quatro aulas do Grau 1. Use este gabarito para **conferir** as suas
respostas — mas tente resolver cada parte antes de olhar aqui.

As Partes B e C (os TODOs do código) são conferidas automaticamente pelo
`testes.py`, e a implementação completa está nos arquivos desta pasta.
Este documento traz as respostas das partes **sem código**: a modelagem no
papel (Parte A) e a análise de complexidade (Parte D). As regras do jogo
e as técnicas de implementação estão explicadas em detalhe no capítulo
"Campo Minado" da apostila da Aula 4.

---

## Parte A — Modelagem no papel

Tabuleiro 5 × 5, com minas nas posições (linha, coluna), contando a
partir de 1: **(1, 4)**, **(2, 2)** e **(4, 5)**. Ao examinar as vizinhas,
use a ordem: ↖ noroeste, ↑ norte, ↗ nordeste, ← oeste, → leste,
↙ sudoeste, ↓ sul, ↘ sudeste.

### A1. Números de cada célula

Cada número é a quantidade de minas entre as (até) 8 vizinhas. `*` é mina.

|       | 1 | 2 | 3 | 4 | 5 |
|:-----:|:-:|:-:|:-:|:-:|:-:|
| **1** | 1 | 1 | 2 | * | 1 |
| **2** | 1 | * | 2 | 1 | 1 |
| **3** | 1 | 1 | 1 | 1 | 1 |
| **4** | 0 | 0 | 0 | 1 | * |
| **5** | 0 | 0 | 0 | 1 | 1 |

Exemplo: a célula (2, 3) vale 2 porque, das suas 8 vizinhas, duas são
minas: (1, 4) e (2, 2). A célula (1, 1) é um canto: tem só 3 vizinhas —
(1, 2), (2, 1) e (2, 2) —, e uma delas é mina, então vale 1.

### A2. Conversão entre (linha, coluna) e índice

Com linhas e colunas contadas **a partir de 1** e 5 colunas:

> índice = (linha − 1) × 5 + (coluna − 1)
> linha = índice ÷ 5 (divisão inteira) + 1  coluna = resto de índice ÷ 5 + 1

| Célula | Conta | Índice |
|:------:|:-----:|:------:|
| (1, 4) | 0 × 5 + 3 | 3 |
| (2, 2) | 1 × 5 + 1 | 6 |
| (4, 5) | 3 × 5 + 4 | **19** |

Índice **12** → 12 ÷ 5 = 2, resto 2 → linha 3, coluna 3 → **(3, 3)**.

No código, linhas e colunas começam em 0, então a conta fica mais simples:
`indice = linha * colunas + coluna`. Essa é a ideia da **lista contígua**
da Aula 1: a matriz 5 × 5 vira uma lista de 25 posições, e qualquer
célula é acessada em O(1).

### A3. Abertura em cascata com Fila — clique em (5, 1)

A célula é marcada como aberta **no momento em que entra** na fila.
A fila é mostrada do início (à esquerda, próxima a sair) para o fim.

| Passo | Sai da fila | Número | Entram na fila | Fila depois do passo |
|:-:|:-:|:-:|:-:|:-|
| 0 | — | — | (5,1) | (5,1) |
| 1 | (5,1) | 0 | (4,1) (4,2) (5,2) | (4,1) (4,2) (5,2) |
| 2 | (4,1) | 0 | (3,1) (3,2) | (4,2) (5,2) (3,1) (3,2) |
| 3 | (4,2) | 0 | (3,3) (4,3) (5,3) | (5,2) (3,1) (3,2) (3,3) (4,3) (5,3) |
| 4 | (5,2) | 0 | — | (3,1) (3,2) (3,3) (4,3) (5,3) |
| 5 | (3,1) | 1 | — | (3,2) (3,3) (4,3) (5,3) |
| 6 | (3,2) | 1 | — | (3,3) (4,3) (5,3) |
| 7 | (3,3) | 1 | — | (4,3) (5,3) |
| 8 | (4,3) | 0 | (3,4) (4,4) (5,4) | (5,3) (3,4) (4,4) (5,4) |
| 9 | (5,3) | 0 | — | (3,4) (4,4) (5,4) |
| 10 | (3,4) | 1 | — | (4,4) (5,4) |
| 11 | (4,4) | 1 | — | (5,4) |
| 12 | (5,4) | 1 | — | (vazia) |

Pontos de atenção:

- Só as células com **0** espalham a abertura. Uma célula numerada é
  aberta, mas não coloca ninguém na fila (passos 5, 6, 7, 10, 11 e 12).
- No passo 4, a célula (5, 2) é um 0, mas todas as suas vizinhas já
  estavam abertas: ninguém entra. É por isso que marcamos ao **colocar**:
  sem essa marcação, (4, 2), (4, 3) e (5, 3) entrariam de novo.
- Ordem de saída: (5,1) (4,1) (4,2) (5,2) (3,1) (3,2) (3,3) (4,3) (5,3)
  (3,4) (4,4) (5,4). A área cresce "em ondas", a partir do clique.

### A4. A mesma abertura com Pilha

A pilha é mostrada da base (à esquerda) para o **topo** (à direita, o
próximo a sair).

| Passo | Sai da pilha | Número | Entram na pilha | Pilha depois do passo |
|:-:|:-:|:-:|:-:|:-|
| 0 | — | — | (5,1) | (5,1) |
| 1 | (5,1) | 0 | (4,1) (4,2) (5,2) | (4,1) (4,2) (5,2) |
| 2 | (5,2) | 0 | (4,3) (5,3) | (4,1) (4,2) (4,3) (5,3) |
| 3 | (5,3) | 0 | (4,4) (5,4) | (4,1) (4,2) (4,3) (4,4) (5,4) |
| 4 | (5,4) | 1 | — | (4,1) (4,2) (4,3) (4,4) |
| 5 | (4,4) | 1 | — | (4,1) (4,2) (4,3) |
| 6 | (4,3) | 0 | (3,2) (3,3) (3,4) | (4,1) (4,2) (3,2) (3,3) (3,4) |
| 7 | (3,4) | 1 | — | (4,1) (4,2) (3,2) (3,3) |
| 8 | (3,3) | 1 | — | (4,1) (4,2) (3,2) |
| 9 | (3,2) | 1 | — | (4,1) (4,2) |
| 10 | (4,2) | 0 | (3,1) | (4,1) (3,1) |
| 11 | (3,1) | 1 | — | (4,1) |
| 12 | (4,1) | 0 | — | (vazia) |

Ordem de saída: (5,1) (5,2) (5,3) (5,4) (4,4) (4,3) (3,4) (3,3) (3,2)
(4,2) (3,1) (4,1). A Pilha segue um caminho "em profundidade" — vai até
o fim da linha 5 antes de voltar.

**As mesmas 12 células** são abertas nos dois casos. Só a **ordem** muda.

### A5. Estado depois do clique

- Células abertas: **12** (6 com 0 e 6 numeradas).
- Células seguras no tabuleiro: 25 − 3 = 22.
- Células seguras que ainda faltam abrir: 22 − 12 = **10**.

---

## Parte D — Análise de complexidade

Notação: L = linhas, C = colunas, k = número de minas, f = número de
bandeiras. Os números medidos abaixo são a saída de
`analise_complexidade.py` (semente fixa 2026).

### D1. `indice()` e `coordenadas()`

**Θ(1).** São só contas (multiplicação, soma, divisão inteira e resto),
sem nenhum laço. É a vantagem da lista contígua da Aula 1: o endereço de
qualquer célula é calculado diretamente.

### D2. `vizinhos()`

**Θ(1).** O laço percorre as 8 direções, sempre 8 — não importa o
tamanho do tabuleiro. Uma quantidade fixa de passos é custo constante.

### D3. Cálculo dos números: percorrer as minas × perguntar a cada célula

| Nível | L × C | k | Percorrendo as minas | Perguntando a cada célula |
|:-:|:-:|:-:|:-:|:-:|
| Fácil | 9 × 9 | 10 | 65 | 5.110 |
| Médio | 16 × 16 | 40 | 294 | 68.664 |
| Difícil | 16 × 30 | 99 | 735 | 317.004 |

- **Percorrendo as minas:** cada mina soma 1 em até 8 vizinhas → no máximo
  8k passos → **O(k)**.
- **Perguntando a cada célula:** para cada uma das L·C células, até 8
  consultas `pertence()` ao Conjunto de minas, e cada consulta custa O(k)
  (o Conjunto é uma lista percorrida elemento a elemento) → **O(L·C·k)**.

No nível Difícil, a versão ingênua faz cerca de **431 vezes** mais
trabalho para chegar ao **mesmo resultado**. A escolha do algoritmo
importou muito mais do que qualquer detalhe da máquina.

### D4. Sorteio das minas com o Conjunto

| Nível | k | Sorteios | Comparações no Conjunto | k²/2 |
|:-:|:-:|:-:|:-:|:-:|
| Fácil | 10 | 11 | 172 | 50 |
| Médio | 40 | 44 | 1.254 | 800 |
| Difícil | 99 | 122 | 6.515 | 4.900 |

- Cada inserção no Conjunto chama `pertence()`, que percorre as minas já
  sorteadas: 0 + 1 + 2 + … + (k − 1) = k(k − 1)/2 comparações (a soma de
  Gauss!) → **O(k²)**.
- Também há comparações com as células protegidas do primeiro clique
  (até 9 por sorteio). Para k pequeno, elas pesam mais que o termo k²/2;
  para k grande, o termo quadrático domina.
- **Alternativa:** embaralhar a lista com os L·C índices (Fisher–Yates,
  o mesmo embaralhamento usado em `insertion_sort.c`) e pegar os k
  primeiros que não forem protegidos → **Θ(L·C)**, sem repetições.
  Vale mais a pena quando k é grande em relação ao tabuleiro: com o
  sorteio simples, quase todo candidato já seria mina e as repetições
  explodiriam.

### D5. Por que marcar a célula ao COLOCAR na fila (e não ao retirar)?

| N | Células (N²) | Marcando ao colocar | Marcando ao retirar |
|:-:|:-:|:-:|:-:|
| 10 | 100 | 100 | 343 |
| 20 | 400 | 400 | 1.483 |
| 40 | 1.600 | 1.600 | 6.163 |

Marcando ao colocar, **cada célula entra no máximo uma vez** na estrutura
→ a abertura é **O(L·C)**. Marcando só ao retirar, uma célula ainda
fechada pode ser vista por várias vizinhas antes de sair, e entra na fila
uma vez para cada uma — cerca de 3,4 a 3,9 vezes mais entradas nesses
testes, todas trabalho jogado fora.

### D6. Fila × Pilha na abertura em cascata

| N | Células | Maior tamanho da Fila | Maior tamanho da Pilha |
|:-:|:-:|:-:|:-:|
| 10 | 100 | 19 | 44 |
| 20 | 400 | 39 | 142 |
| 40 | 1.600 | 79 | 487 |
| 80 | 6.400 | 159 | 1.777 |

- **Mesmas células, ordem diferente.** Com Fila, a área cresce em ondas
  (busca em largura); com Pilha, avança em profundidade.
- **Mesmo tempo:** as duas fazem N² entradas e as mesmas verificações de
  vizinhas → **Θ(L·C)** nos dois casos.
- **Memória diferente:** a Fila guarda só a "frente da onda" — cerca de
  2N − 1 células num tabuleiro vazio aberto pelo canto. A Pilha acumula
  muito mais. Como a nossa Pilha é **contígua, com capacidade fixa**
  (Aula 2), ela é criada com capacidade L·C: no pior caso, quase todas as
  células podem estar empilhadas ao mesmo tempo.

### D7. Verificar a vitória: contador × varrer o tabuleiro

Varrendo a lista `reveladas` a cada jogada: **O(L·C) por jogada** (81,
256 ou 480 células por nível). Com o contador `celulas_seguras_restantes`,
atualizado a cada célula aberta: **O(1) por jogada**. Numa partida com
J jogadas, O(J·L·C) contra O(J).

### D8. Bandeiras em um Conjunto

`pertence()` custa **O(f)**. A abertura em cascata consulta as bandeiras
para cada vizinha examinada, então, no pior caso, custa **O(L·C·f)**. Na
prática, f é pequeno (no máximo algumas dezenas).

Para deixar a consulta O(1): usar uma lista de booleanos com uma posição
por célula, como já fazemos com `reveladas`. É uma troca de **memória
por tempo** — ocupa L·C posições sempre, mesmo sem nenhuma bandeira.

### D9. Ranking

- `inserir_ordenado()` é um passo do Insertion Sort: **Θ(n)** no pior
  caso (o novo recorde é o melhor de todos e todos se deslocam) e
  **Θ(1)** no melhor caso (é o pior tempo e fica no fim).
- `ordenar_por_insercao()` ao carregar o arquivo: como o próprio programa
  salva o arquivo **já ordenado**, o Insertion Sort cai no **melhor caso,
  Θ(n)** — exatamente o cenário do slide "melhor caso: vetor já
  ordenado". Se alguém embaralhar o arquivo à mão, vira Θ(n²); com
  n ≤ 10, isso não faz diferença na prática.

### D10. Custo de uma partida inteira

- **Primeiro clique:** sorteio O(k²) + números O(k) + abertura
  O(L·C·f) — com f = 0 no começo, O(L·C).
- **Cada clique seguinte:** testar se é mina O(k) + abertura
  O(L·C·f) no pior caso (normalmente, bem menos).
- **Cada bandeira ou desfazer:** O(f).
- **Desenhar o tabuleiro** (`mapa_visivel`): O(L·C + k + f).

---

## Questões de reflexão

**1. Por que o tabuleiro é uma lista linear, e não uma lista de listas?**
As duas funcionam. A lista linear deixa explícita a conta de endereço da
Aula 1 (`linha * colunas + coluna`), guarda tudo num único bloco contíguo
e facilita usar um único número (o índice) para identificar a célula nos
Conjuntos e nas estruturas da abertura.

**2. Por que as regras ficam em `tabuleiro.py`, separadas das interfaces?**
Porque a mesma lógica serve à interface de texto e à gráfica, e pode ser
testada automaticamente sem abrir nenhuma janela (`testes.py`). Trocar a
interface não exige mexer nas regras, e vice-versa.

**3. O que mudaria se a Fila não tivesse a referência para o fim?**
Enfileirar passaria a percorrer a fila inteira para achar o último nó:
O(n) em vez de O(1). A abertura em cascata, que enfileira até L·C
células, passaria de O(L·C) para O((L·C)²) — a mesma pergunta de
reflexão da Aula 2, agora com um exemplo real.

---

Prof. Filipo Novo Mór — 2026 — [filipomor.com](https://filipomor.com)
