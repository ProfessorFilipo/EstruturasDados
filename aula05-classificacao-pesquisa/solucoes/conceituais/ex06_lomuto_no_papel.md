# Exercício 6 — Partição de Lomuto no papel

Vetor: `[7, 2, 9, 4, 1, 8, 5]`, pivô = **5** (o último). `i` começa em 0.

| j | v[j] | decisão | vetor depois | i |
|---|---|---|---|---|
| 0 | 7 | 7 ≥ 5: fica | [7, 2, 9, 4, 1, 8, 5] | 0 |
| 1 | 2 | 2 < 5: troca com a posição 0 | [2, 7, 9, 4, 1, 8, 5] | 1 |
| 2 | 9 | 9 ≥ 5: fica | [2, 7, 9, 4, 1, 8, 5] | 1 |
| 3 | 4 | 4 < 5: troca com a posição 1 | [2, 4, 9, 7, 1, 8, 5] | 2 |
| 4 | 1 | 1 < 5: troca com a posição 2 | [2, 4, 1, 7, 9, 8, 5] | 3 |
| 5 | 8 | 8 ≥ 5: fica | [2, 4, 1, 7, 9, 8, 5] | 3 |

No fim, o pivô troca com a posição `i = 3`:

```
[2, 4, 1, 5, 9, 8, 7]
          ^ pivô na posição final 3
```

**6 comparações** (n − 1). À esquerda ficaram os menores que 5
(`[2, 4, 1]`); à direita, os maiores (`[9, 8, 7]`).
