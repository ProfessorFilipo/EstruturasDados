# Exercício 5 — Merge Sort no papel

Vetor: `[9, 4, 7, 1, 8, 2]` (a metade esquerda fica com `n // 2` elementos).

```
dividir:                 [9, 4, 7, 1, 8, 2]
                    [9, 4, 7]          [1, 8, 2]
                  [9]   [4, 7]       [1]   [8, 2]
                       [4]  [7]           [8]  [2]

intercalar:
                       [4, 7]              [2, 8]          1 + 1 comparação
                  [4, 7, 9]           [1, 2, 8]            2 + 1 comparações
                         [1, 2, 4, 7, 8, 9]                5 comparações
```

| intercalação | comparações |
|---|---|
| [4] + [7] → [4, 7] | 1 |
| [9] + [4, 7] → [4, 7, 9] | 2 (9×4, 9×7; o 9 sobra) |
| [8] + [2] → [2, 8] | 1 |
| [1] + [2, 8] → [1, 2, 8] | 1 (1×2; o resto sobra) |
| [4, 7, 9] + [1, 2, 8] → [1, 2, 4, 7, 8, 9] | 5 |

**Total: 10 comparações.** Para comparar: n log2 n = 6 × 2,58 ≈ 15,5, e o
limite inferior é ⌈log2 6!⌉ = ⌈log2 720⌉ = 10.
