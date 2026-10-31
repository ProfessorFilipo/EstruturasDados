# Exercício 10 — O limite para 5 trabalhos

**(a)** 5! = 5 × 4 × 3 × 2 × 1 = **120** ordens possíveis.

**(b)** Com k comparações (perguntas de sim/não), separamos no máximo 2^k
ordens. Precisamos de 2^k ≥ 120: como 2^6 = 64 < 120 ≤ 128 = 2^7, são
necessárias pelo menos **7 comparações** no pior caso (⌈log2 120⌉ = 7).

**(c)** Rodando `limite_inferior.py` com `(3, 4, 5)`:

```
   n=5: 120 ordens | limite = 7 | insertion = 10 | merge = 8
```

O Merge Sort precisa de **8** comparações no pior caso. Isso **não**
contradiz o limite: o limite é um **piso** — nenhum algoritmo de comparação
consegue menos de 7 —, mas ele não garante que um algoritmo específico
chegue exatamente a 7. (Existe um algoritmo que ordena 5 elementos com
exatamente 7 comparações, o "merge insertion" de Ford e Johnson.) O que o
limite garante é a ordem de grandeza: Ω(n log n), e o Merge Sort fica
colado nela para n grande.
