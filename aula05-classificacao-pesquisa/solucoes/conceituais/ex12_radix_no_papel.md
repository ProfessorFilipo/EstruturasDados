# Exercício 12 — Radix Sort no papel

IDs: `[618, 204, 531, 125, 902, 340]`. Cada passada é um Counting Sort
**estável** pelo dígito indicado (em destaque entre colchetes).

```
entrada:       618  204  531  125  902  340
por unidade:   34[0] 53[1] 90[2] 20[4] 12[5] 61[8]
               -> [340, 531, 902, 204, 125, 618]
por dezena:    9[0]2 2[0]4 6[1]8 1[2]5 5[3]1 3[4]0
               -> [902, 204, 618, 125, 531, 340]
por centena:   [1]25 [2]04 [3]40 [5]31 [6]18 [9]02
               -> [125, 204, 340, 531, 618, 902]
```

Na passada da dezena, 902 e 204 empatam (dezena 0). Como o counting sort é
estável, 902 continua antes de 204 — a ordem que a passada da unidade
construiu.

**E se a passada fosse instável?** Os empates poderiam sair em qualquer
ordem, e o trabalho das passadas anteriores seria perdido. Neste exemplo
as centenas são todas diferentes, então o resultado final daria certo por
sorte; mas com IDs como 512 e 518 (mesma centena e mesma dezena), uma
última passada instável poderia devolver 518 antes de 512.
