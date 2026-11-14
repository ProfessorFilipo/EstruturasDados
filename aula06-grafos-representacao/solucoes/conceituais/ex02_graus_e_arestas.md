# Exercício 2 — Graus e arestas

`E = {AB, AC, BC, BD, CE, DE, DF, EF}`: 8 arestas.

**(a)** Um desenho possível:

```
    A
   / \
  B---C
  |   |
  D---E
   \ /
    F
```

**(b)** Graus (conte as pontas de aresta em cada vértice):

| Vértice | A | B | C | D | E | F |
|---|---|---|---|---|---|---|
| Grau | 2 | 3 | 3 | 3 | 3 | 2 |

**(c)** Soma dos graus = 2 + 3 + 3 + 3 + 3 + 2 = **16** = 2 × 8. Confere.

**(d)** Quatro vértices têm grau ímpar (B, C, D e E). Esse número é sempre
**par**: a soma de todos os graus é `2 × |E|`, um número par. Os vértices de
grau par contribuem com uma parcela par; para o total continuar par, a
soma dos graus ímpares também precisa ser par, e uma soma de números
ímpares só é par quando há uma quantidade par deles.
