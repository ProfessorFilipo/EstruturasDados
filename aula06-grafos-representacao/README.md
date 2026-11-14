# Aula 6 — Grafos I: conceitos e representação

Estruturas de Dados — UniLasalle EAD

O que é um grafo, tipos de grafo (dirigido, ponderado, simples, completo),
**grau** e o lema do aperto de mãos, **caminhos**, **ciclos**, **componentes
conexas** e **árvores**; e as duas formas clássicas de guardar um grafo na
memória: **matriz de adjacências** e **lista de adjacências**. Tudo no
cenário da **rede da filial**: 6 roteadores ligados por 10 cabos, o mesmo
grafo do livro de Ascencio & Araújo (cap. 8, p. 391), que volta na Aula 7.

## Estrutura desta pasta

```
python/                           # demos da aula (só biblioteca padrão)
├── p1_matriz_adjacencias.py      # P1 — slides 21 e 28
├── p2_graus.py                   # P2 — slides 13, 14 e 29
├── p3_lista_adjacencias.py       # P3 — slides 22 e 30
└── p4_comparando_representacoes.py  # P4 — slides 23 e 31
c/                                # as mesmas demos em ANSI C (arquivo único cada)
├── p1_matriz_adjacencias.c  p2_graus.c  p3_lista_adjacencias.c
├── p4_comparando_representacoes.c
└── Makefile
exercicios/
└── exercicios-aula06.md          # 10 exercícios guiados, em ordem de dificuldade
solucoes/                         # gabarito — ver solucoes/README.md
```

## O que cada demo mostra

| Arquivo | Prática | O que observar na saída |
|---|---|---|
| `p1_matriz_adjacencias.py` | P1 | a matriz 6 × 6, simétrica, com 20 uns (2 × \|E\|); troque `DIRIGIDO = True` e ela perde a simetria |
| `p2_graus.py` | P2 | grau = soma da linha; soma dos graus = 20 = 2 × 10; no dígrafo, fonte (1) e sumidouro (6) |
| `p3_lista_adjacencias.py` | P3 | a lista de cada roteador; grau = tamanho da lista; 26 células contra 36 da matriz |
| `p4_comparando_representacoes.py` | P4 | "u e v são vizinhos?" em 1 acesso (matriz) ou em grau(u) passos (lista); memória em três cenários |

Cada arquivo traz as **versões "limpas"** das funções, idênticas às dos
slides, e partes extras que mostram cada passo.

## Como executar

Cada arquivo é autocontido e usa só a biblioteca padrão: dá para colar
direto no [OnlineIDE Pro — playground Python](https://www.onlineide.pro/playground/python)
ou no [playground C](https://www.onlineide.pro/playground/c). No GitHub,
use o botão **Copy raw file** (ícone de dois quadradinhos, acima do código)
para copiar o arquivo inteiro.

### Python

```bash
cd python
python3 p1_matriz_adjacencias.py
python3 p2_graus.py
python3 p3_lista_adjacencias.py
python3 p4_comparando_representacoes.py
```

No Windows, use `py` ou `python` no lugar de `python3`.

Os programas usam dados fixos, sem leitura do teclado: a saída é sempre a
mesma, em qualquer computador. É assim que todos conferem os resultados no
chat durante a aula.

### C

```bash
cd c
make
./p1_matriz_adjacencias
./p2_graus
./p3_lista_adjacencias
./p4_comparando_representacoes
```

Os programas compilam sem avisos com `-std=c11 -Wall -Wextra -pedantic` e a
saída é **idêntica** à da versão em Python.

Os vértices são numerados de 1 a n, como no livro: a posição 0 dos vetores e
da matriz existe na memória, mas fica sem uso. Em
`p3_lista_adjacencias.c`, cada lista de vizinhos é uma **lista encadeada**
(a mesma da Aula 1), criada com `malloc` e liberada com `free`; em
`p4_comparando_representacoes.c`, a lista é **contígua** (um vetor de vizinhos
por vértice), para o código ficar mais curto.

## Exercícios

A lista [`exercicios/exercicios-aula06.md`](exercicios/exercicios-aula06.md)
tem 10 exercícios: 5 no papel (tipos de grafo, graus, grafos regulares,
árvores, leitura de matriz) e 5 de programação, em Python e em C. O gabarito
está em [`solucoes/`](solucoes/): tente antes de olhar.

## Referências

- ASCENCIO, A. F. G.; ARAÚJO, G. S. *Estruturas de dados: algoritmos, análise da
  complexidade e implementações em JAVA e C/C++*. São Paulo: Pearson Prentice
  Hall, 2010. Cap. 8, p. 368–378.
- CORMEN, T. H. et al. *Introduction to Algorithms*. 3. ed. MIT Press, 2009.
  Apêndice B.4–B.5 e seção 22.1.

---

Prof. Filipo Novo Mór — 2026 — [filipomor.com](https://filipomor.com)
