# Aula 5 — Classificação e Pesquisa

Estruturas de Dados — UniLasalle EAD

Pesquisa sequencial e binária; ordenação com **Insertion Sort**, **Merge
Sort** e **Quicksort**; o **limite inferior Ω(n log n)** das ordenações por
comparação; e a ordenação **sem comparação** com **Counting Sort** e
**Radix Sort**. Tudo no cenário da **Central de Impressão** (Aula 2), que
agora guarda um histórico com milhares de trabalhos `(id, paginas)`.

## Estrutura desta pasta

```
python/                     # demos da aula (só biblioteca padrão)
├── busca_sequencial.py     # Bloco 1 — slides 05 e 06
├── busca_binaria.py        # Bloco 2 — slides 07 a 13
├── insertion_estavel.py    # Bloco 3 — slides 14 e 15
├── merge_sort.py           # Bloco 4 — slides 16 a 20 (inclui recursão)
├── quick_sort.py           # Bloco 5 — slides 21 a 26
├── limite_inferior.py      # Bloco 6 — slides 27 e 28
├── counting_radix.py       # Bloco 7 — slides 29 a 31
└── corrida_ordenacao.py    # PARA CASA: todos os algoritmos competindo
c/                          # as mesmas demos em C (arquivo único cada)
├── busca_sequencial.c  busca_binaria.c  insertion_estavel.c  merge_sort.c
├── quick_sort.c  limite_inferior.c  counting_radix.c
└── Makefile
exercicios/
└── exercicios-aula05.md    # 13 exercícios guiados, em ordem de dificuldade
solucoes/                   # gabarito — ver solucoes/README.md
```

## O que cada demo mostra

| Arquivo | Bloco | O que observar na saída |
|---|---|---|
| `busca_sequencial.py` | 1 | melhor caso (achou cedo) × pior caso (10.000 comparações) |
| `busca_binaria.py` | 2 | rastreio de `inicio`/`meio`/`fim`; 1 bilhão de IDs em 30 comparações |
| `insertion_estavel.py` | 3 | empates mantêm a ordem de chegada; dobrar n → ×4 comparações |
| `merge_sort.py` | 4 | pilha de chamadas; intercalação de filas; dobrar n → ×2,2 |
| `quick_sort.py` | 5 | partição passo a passo; vetor ordenado = pior caso (124.750) |
| `limite_inferior.py` | 6 | força bruta em todas as ordens; Merge Sort colado em log2(n!) |
| `counting_radix.py` | 7 | contar, acumular, posicionar; corrida com 100.000 trabalhos; Radix |
| `corrida_ordenacao.py` | casa | comparações e tempo de 5 algoritmos em 3 cenários |

Cada arquivo traz, além das versões que contam comparações e mostram cada
passo, as **versões "limpas"** das funções, idênticas às dos slides.

## Como executar

Cada arquivo é autocontido e usa só a biblioteca padrão: dá para colar
direto no [OnlineIDE Pro — playground Python](https://www.onlineide.pro/playground/python)
ou no [playground C](https://www.onlineide.pro/playground/c). No GitHub,
use o botão **Copy raw file** (ícone de dois quadradinhos, acima do código)
para copiar o arquivo inteiro.

### Python

```bash
cd python
python3 busca_sequencial.py
python3 busca_binaria.py
python3 insertion_estavel.py
python3 merge_sort.py
python3 quick_sort.py
python3 limite_inferior.py
python3 counting_radix.py
python3 corrida_ordenacao.py
```

No Windows, use `py` ou `python` no lugar de `python3`.

Os programas usam uma **semente aleatória fixa** (2026): a saída é sempre a
mesma, em qualquer computador — é assim que todos conferem os números no
chat durante a aula.

### C

```bash
cd c
make
./busca_sequencial
./busca_binaria
./insertion_estavel
./merge_sort
./quick_sort
./limite_inferior
./counting_radix
```

Os programas compilam sem avisos com `-std=c11 -Wall -Wextra -pedantic` e
não precisam de `<math.h>` (nem de `-lm`). As partes com dados fixos têm
saída **idêntica** à da versão em Python; nas partes com dados sorteados, o
C usa um gerador próprio (congruencial linear), então os números diferem um
pouco — as conclusões, não.

No Merge Sort em C, o vetor auxiliar é criado com `malloc` e liberado com
`free`: é ali que a memória extra O(n) fica visível.

## Exercícios

A lista [`exercicios/exercicios-aula05.md`](exercicios/exercicios-aula05.md)
tem 13 exercícios — rastreios no papel, perguntas de reflexão e quatro
exercícios de programação (em Python e em C). O gabarito está em
[`solucoes/`](solucoes/): tente antes de olhar.

---

Prof. Filipo Novo Mór — 2026 — [filipomor.com](https://filipomor.com)
