# Aula 7 — Grafos II: buscas e caminho mínimo

Estruturas de Dados — UniLasalle EAD

Como **percorrer** um grafo: a **busca em largura (BFS)**, que anda em ondas
com uma fila e encontra o menor número de saltos, e a **busca em
profundidade (DFS)**, que mergulha e volta com uma pilha (ou recursão).
Com elas, contamos **componentes conexas**. Por fim, o **algoritmo de
Dijkstra** para caminho mínimo com pesos. Tudo na mesma **rede da filial**
da Aula 6, agora com a lista de adjacências na ordem do livro de Ascencio &
Araújo (p. 391) e com as latências do exemplo da p. 409.

## Estrutura desta pasta

```
python/                     # demos da aula (só biblioteca padrão)
├── p1_bfs.py               # P1 — slides 05 a 09 e 31
├── p2_dfs.py               # P2 — slides 13 a 15 e 32
├── p3_componentes.py       # P3 — slides 16 e 33
└── p4_dijkstra.py          # P4 — slides 21 a 25 e 34
c/                          # as mesmas demos em ANSI C (arquivo único cada)
├── p1_bfs.c  p2_dfs.c  p3_componentes.c  p4_dijkstra.c
└── Makefile
exercicios/
└── exercicios-aula07.md    # 10 exercícios guiados, em ordem de dificuldade
solucoes/                   # gabarito — ver solucoes/README.md
```

## O que cada demo mostra

| Arquivo | Prática | O que observar na saída |
|---|---|---|
| `p1_bfs.py` | P1 | a fila a cada passo; ordem 1 6 2 5 3 4; `dist` e `pai`; caminho com menos saltos até cada roteador |
| `p2_dfs.py` | P2 | a recursão com recuo (visita/volta); a versão com pilha explícita, na mesma ordem 1 6 5 4 3 2 |
| `p3_componentes.py` | P3 | a rede depois da tempestade: 4 ilhas; quem alcança quem; cabos mínimos para reconectar |
| `p4_dijkstra.py` | P4 | a tabela de rodadas do Dijkstra; rota mais rápida até cada roteador; BFS (2 saltos, 10 ms) × Dijkstra (3 saltos, 9 ms) |

Cada arquivo traz as **versões "limpas"** das funções, idênticas às dos
slides, e versões que mostram cada passo. No topo de cada um há uma
constante (`ORIGEM` ou a lista de arestas) para você trocar e rodar de novo.

## Como executar

Cada arquivo é autocontido e usa só a biblioteca padrão: dá para colar
direto no [OnlineIDE Pro — playground Python](https://www.onlineide.pro/playground/python)
ou no [playground C](https://www.onlineide.pro/playground/c). No GitHub,
use o botão **Copy raw file** para copiar o arquivo inteiro.

### Python

```bash
cd python
python3 p1_bfs.py
python3 p2_dfs.py
python3 p3_componentes.py
python3 p4_dijkstra.py
```

No Windows, use `py` ou `python` no lugar de `python3`. A fila da BFS usa
`collections.deque`, que tira do início em O(1), como a fila encadeada da Aula 2.

### C

```bash
cd c
make
./p1_bfs
./p2_dfs
./p3_componentes
./p4_dijkstra
```

Os programas compilam sem avisos com `-std=c11 -Wall -Wextra -pedantic` e a
saída é **idêntica** à da versão em Python. Em C, a lista de adjacências é
**contígua** (um vetor de vizinhos por vértice) e a fila e a pilha são
vetores com índices de início e fim: como cada vértice entra na fila no
máximo uma vez, um vetor de N posições basta.

O Dijkstra está na versão simples, O(V²), que procura o menor `dist`
varrendo o vetor. O livro usa uma lista de prioridades (heap), que leva a
O((V + E) log V).

## Exercícios

A lista [`exercicios/exercicios-aula07.md`](exercicios/exercicios-aula07.md)
tem 10 exercícios: 5 no papel (rastreios de BFS, DFS e Dijkstra, e quando
usar cada algoritmo) e 5 de programação, em Python e em C, terminando com o
desafio do labirinto. O gabarito está em [`solucoes/`](solucoes/): tente
antes de olhar.

## Referências

- ASCENCIO, A. F. G.; ARAÚJO, G. S. *Estruturas de dados: algoritmos, análise da
  complexidade e implementações em JAVA e C/C++*. São Paulo: Pearson Prentice
  Hall, 2010. Cap. 8, p. 378–425.
- CORMEN, T. H. et al. *Introduction to Algorithms*. 3. ed. MIT Press, 2009.
  Seções 22.2, 22.3 e 24.3 (para ir além: caps. 22 a 25).

---

Prof. Filipo Novo Mór — 2026 — [filipomor.com](https://filipomor.com)
