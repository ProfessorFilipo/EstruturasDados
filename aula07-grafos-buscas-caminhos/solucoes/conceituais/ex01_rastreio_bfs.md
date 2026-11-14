# Exercício 1 — Rastreando a BFS

Listas de adjacências (ordem alfabética):

```
A: B D        E: B D F G
B: A C E      F: C E H
C: B F        G: E H
D: A E        H: F G
```

| Passo | Sai da fila | Entram (com dist) | Fila depois |
|---|---|---|---|
| início | — | A (0) | [A] |
| 1 | A | B (1), D (1) | [B, D] |
| 2 | B | C (2), E (2) | [D, C, E] |
| 3 | D | — (A e E já marcados) | [C, E] |
| 4 | C | F (3) | [E, F] |
| 5 | E | G (3) | [F, G] |
| 6 | F | H (4) | [G, H] |
| 7 | G | — | [H] |
| 8 | H | — | [] |

**(a)** Ordem de visita: **A B D C E F G H**

**(b)**

| | A | B | C | D | E | F | G | H |
|---|---|---|---|---|---|---|---|---|
| dist | 0 | 1 | 2 | 1 | 2 | 3 | 3 | 4 |
| pai | — | A | B | A | B | C | E | F |

**(c)** Seguindo `pai` de trás para frente a partir de H: H ← F ← C ← B ← A.
Caminho: **A → B → C → F → H**, com 4 corredores.
