# Exercício 4 — Busca binária numa lista encadeada?

**(a)** Para chegar ao primeiro meio (posição 499 ou 500), `obter(pos)`
precisa caminhar nó a nó desde o início: cerca de **500 nós** (n/2).

**(b)** Somando todos os passos: n/2 + n/4 + n/8 + ... ≈ **n** nós, ou seja,
cerca de **1.000 nós** percorridos — **O(n)**, a mesma ordem de grandeza da
pesquisa sequencial. As comparações caem para log2 n ≈ 10, mas o custo de
**chegar** aos elementos continua linear, e é ele que manda no tempo total.

**(c)** Além de dados ordenados, é preciso **acesso por índice em O(1)** —
ou seja, um vetor (lista contígua, Aula 1), em que o endereço de `v[meio]`
é calculado diretamente. Pesquisa binária é coisa de vetor.
