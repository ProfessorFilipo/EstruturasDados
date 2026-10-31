# Exercícios Guiados — Aula 5: Classificação e Pesquisa

Estruturas de Dados — UniLasalle EAD

Sequência de 13 exercícios cobrindo todo o conteúdo da Aula 5 — pesquisa
sequencial e binária, Insertion Sort, Merge Sort, Quicksort, o limite
inferior Ω(n log n) e a ordenação sem comparação (Counting Sort e Radix
Sort) — em ordem crescente de dificuldade. Todos usam o cenário da aula: o
histórico da **Central de Impressão**, com trabalhos `(id, paginas)`.

## Como usar este guia

- **Siga a ordem.** Cada parte depende do raciocínio construído na anterior.
- **Faça os exercícios de rastreio no papel.** Desenhar o vetor a cada passo
  é o melhor jeito de fixar como cada algoritmo funciona. Depois, confira
  rodando os arquivos da pasta `python/` (ou `c/`).
- **Tente antes de olhar o gabarito.** As soluções estão em
  [`../solucoes/`](../solucoes/) — use-as só **depois**, para comparar.
- **Teste seu código.** Use o [OnlineIDE Pro](https://www.onlineide.pro/)
  ([playground Python](https://www.onlineide.pro/playground/python) /
  [playground C](https://www.onlineide.pro/playground/c)) ou o ambiente
  local que você já configurou.
- **Marque seu progresso** trocando `[ ]` por `[x]` em cada item conforme
  for concluindo.

**Legenda de dificuldade:** 🟢 fácil · 🟡 médio · 🔴 difícil · ✍️ reflexão / papel (sem código)

---

## Parte 1 — Pesquisa

### Exercício 1 — Rastreando a busca binária 🟢 ✍️

- [ ] Concluído

**Objetivo:** praticar o movimento de `inicio`, `meio` e `fim`.

Use os 16 IDs da aula (slide 8):

```
posição: 0    1    2    3    4    5    6    7    8    9    10   11   12   13   14   15
ID:      101  104  105  109  112  113  118  121  125  126  130  134  137  141  142  150
```

Para cada busca, monte uma tabela com `inicio`, `meio`, `fim` e `v[meio]`
em cada passo, e diga quantas comparações foram feitas e o que a função
devolve:

- (a) buscar o trabalho **126**;
- (b) buscar o trabalho **100** (ele não existe).

**Como conferir:** em `python/busca_binaria.py`, troque `ALVO = 137` por
126 e por 100.

---

### Exercício 2 — Quantas comparações? 🟢 ✍️

- [ ] Concluído

**Objetivo:** sentir a diferença entre O(n) e O(log n).

Complete a tabela com o número **máximo** de comparações (pior caso) de
cada busca. Para a binária, use ⌊log2 n⌋ + 1.

| n | sequencial | binária |
|---|---|---|
| 500 | | |
| 1.000.000.000 | | |
| 4.000.000.000 | | |

Depois responda: quantas vezes maior ficou o pior caso de cada uma ao
passar de 1 bilhão para 4 bilhões?

---

### Exercício 3 — A primeira ocorrência 🟡 `Python` `C`

- [ ] Concluído

**Objetivo:** adaptar a busca binária a um problema novo.

Num vetor **ordenado por páginas**, há muitos trabalhos com o mesmo
número de páginas. A busca binária da aula devolve **alguma** posição do
valor procurado — não necessariamente a primeira.

Escreva `buscar_primeira(v, alvo)` (em C: `int buscar_primeira(const int v[], int n, int alvo, int *comparacoes)`)
que devolve a posição da **primeira** ocorrência de `alvo` em `v` (ou -1),
continuando **O(log n)**.

> **Dica:** quando achar o alvo, guarde a posição e continue procurando
> **à esquerda** (`fim = meio - 1`).

**Como testar:** com `v = [1, 3, 3, 3, 7, 7, 9, 12, 12, 12, 12, 20]`, a
função deve devolver 7 para o alvo 12, 1 para o alvo 3, 0 para o alvo 1,
11 para o alvo 20 e -1 para o alvo 5 — sempre com, no máximo, 4 comparações.

---

### Exercício 4 — Busca binária numa lista encadeada? 🟡 ✍️

- [ ] Concluído

**Objetivo:** ligar o custo da busca ao custo de acesso da estrutura (Aula 1).

Imagine aplicar a busca binária a uma **lista encadeada** com 1.000 nós,
em que `obter(pos)` precisa caminhar nó a nó desde o início.

- (a) Quantos nós são percorridos só para chegar ao **primeiro** meio?
- (b) Somando todos os passos (n/2 + n/4 + n/8 + ...), qual é a ordem de
  grandeza do total? Compare com a pesquisa sequencial.
- (c) Então, o que é preciso, além de ordem, para a busca binária valer a pena?

---

## Parte 2 — Ordenação por comparação

### Exercício 5 — Merge Sort no papel 🟢 ✍️

- [ ] Concluído

**Objetivo:** visualizar o dividir e intercalar.

Aplique o Merge Sort a `[9, 4, 7, 1, 8, 2]` (no Python da aula, a metade
esquerda fica com `n // 2` elementos). Desenhe a árvore de divisões e
intercalações e conte **quantas comparações** acontecem no total.

**Como conferir:** em `python/merge_sort.py`, troque a lista da parte 2
por `[9, 4, 7, 1, 8, 2]`.

---

### Exercício 6 — Partição de Lomuto no papel 🟢 ✍️

- [ ] Concluído

**Objetivo:** dominar a partição, o coração do Quicksort.

Particione `[7, 2, 9, 4, 1, 8, 5]` com o esquema da aula (pivô = último
elemento, o 5). Mostre o vetor depois de **cada troca**, a posição final
do pivô e o número de comparações.

**Como conferir:** em `python/quick_sort.py`, troque a lista da parte 1.

---

### Exercício 7 — Merge Sort estável para trabalhos 🟡 `Python` `C`

- [ ] Concluído

**Objetivo:** adaptar o Merge Sort a registros e verificar a estabilidade.

Escreva `merge_sort_por_paginas(trabalhos)` que ordena uma lista de
trabalhos `(id, paginas)` **pelas páginas**, mantendo os empates na ordem
de chegada (em C, use um vetor de `struct { int id; int paginas; }`).

**Como testar:**

1. Ordene os 8 trabalhos da Demo 3:
   `[(101, 12), (102, 3), (104, 12), (105, 7), (107, 3), (108, 20), (110, 7), (111, 1)]`.
   O resultado tem de ser idêntico ao do Insertion Sort:
   `[(111, 1), (102, 3), (107, 3), (105, 7), (110, 7), (101, 12), (104, 12), (108, 20)]`.
2. Gere 1.000 trabalhos com páginas aleatórias de 1 a 30 e confira que o
   seu resultado é igual ao do Insertion Sort (ou, em Python, ao de
   `sorted(trabalhos, key=lambda t: t[1])`, que também é estável).

---

### Exercício 8 — Quicksort com mediana de três 🔴 `Python` `C`

- [ ] Concluído

**Objetivo:** corrigir o pior caso do Quicksort sem sortear o pivô.

Na **mediana de três**, o pivô é o valor do meio entre `v[inicio]`,
`v[meio]` e `v[fim]`. Antes de particionar, troque esse elemento com
`v[fim]` e use a partição da aula normalmente.

Meça as comparações com n = 500 nos três cenários abaixo e compare com o
pivô sempre no último elemento:

| cenário | pivô = último | mediana de três |
|---|---|---|
| aleatório | | |
| já ordenado | 124.750 | |
| ordem inversa | | |

**Pergunta:** por que a mediana de três resolve justamente os casos
"ordenado" e "inverso"?

---

### Exercício 9 — O Quicksort não é estável 🟡 ✍️

- [ ] Concluído

**Objetivo:** entender, com um exemplo mínimo, o que é perder a estabilidade.

Encontre uma lista com **apenas 3 trabalhos** `(id, paginas)` em que a
partição da aula (pivô = último, comparando as páginas) troque a ordem de
dois trabalhos com o mesmo número de páginas. Mostre o vetor antes e depois.

---

## Parte 3 — Limite inferior

### Exercício 10 — O limite para 5 trabalhos 🟡 ✍️

- [ ] Concluído

**Objetivo:** aplicar o argumento da árvore de decisão.

- (a) De quantas formas 5 trabalhos podem chegar à fila?
- (b) Qual é o número **mínimo** de comparações que qualquer ordenação por
  comparação precisa fazer, no pior caso, para 5 elementos?
- (c) Rode `python/limite_inferior.py` trocando `(3, 4)` por `(3, 4, 5)`.
  Quantas comparações o Merge Sort precisa no pior caso para n = 5? Isso
  contradiz o limite? Explique.

---

## Parte 4 — Ordenação sem comparação

### Exercício 11 — Counting Sort no papel 🟢 ✍️

- [ ] Concluído

**Objetivo:** praticar os três passos: contar, acumular, posicionar.

Ordene as páginas `[2, 4, 1, 4, 3, 1, 2, 4]` (k = 4). Mostre o vetor de
**contagem**, o vetor com o **início de cada bloco** e a **saída**.

---

### Exercício 12 — Radix Sort no papel 🟡 ✍️

- [ ] Concluído

**Objetivo:** ver a estabilidade trabalhando a cada passada.

Ordene os IDs `[618, 204, 531, 125, 902, 340]` com o Radix Sort (LSD —
Least Significant Digit, começando pela unidade). Mostre a lista depois de
cada passada (unidade, dezena e centena).

**Pergunta:** o que daria errado se a passada usasse um algoritmo
**instável**?

---

### Exercício 13 — Um ordenador que escolhe sozinho 🔴 `Python` `C`

- [ ] Concluído

**Objetivo:** juntar a aula inteira numa decisão automática — a mesma ideia
do Timsort do Python, que escolhe entre Insertion Sort e Merge Sort.

Escreva `ordenar(v)` que devolve a lista ordenada **e o nome do algoritmo
escolhido**, seguindo estas regras:

1. se `len(v) <= 32` → **Insertion Sort** (poucos dados);
2. senão, se a faixa de valores for pequena — `max(v) - min(v) <= 2 * len(v)`
   → **Counting Sort** (desloque os valores por `min(v)` para começar em 0);
3. senão → **Merge Sort**.

**Como testar:**

- `[5, 2, 9, 1]` → Insertion Sort;
- 1.000 páginas aleatórias de 1 a 30 → Counting Sort;
- 1.000 números aleatórios de 1 a 1.000.000 → Merge Sort.

Confira sempre que a saída é igual à do `sorted()` (em C, que está em
ordem crescente).

---

Prof. Filipo Novo Mór — 2026 — [filipomor.com](https://filipomor.com)
