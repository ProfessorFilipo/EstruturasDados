# Exercício 2 — Quantas comparações?

| n | sequencial (pior caso) | binária: ⌊log2 n⌋ + 1 |
|---|---|---|
| 500 | 500 | ⌊8,97⌋ + 1 = **9** |
| 1.000.000.000 | 1.000.000.000 | ⌊29,90⌋ + 1 = **30** |
| 4.000.000.000 | 4.000.000.000 | ⌊31,90⌋ + 1 = **32** |

Ao passar de 1 bilhão para 4 bilhões (n multiplicado por 4):

- a **sequencial** fica **4 vezes** maior (é linear: O(n));
- a **binária** ganha só **2 comparações**, porque multiplicar por 4 é
  dobrar duas vezes, e cada dobra custa +1 comparação (é O(log n)).
