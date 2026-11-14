# Exercício 4 — Dijkstra no papel

Pesos: `S-A 7, S-B 2, A-B 3, A-C 4, B-D 8, C-D 2, C-T 5, D-T 3`.
A cada rodada fecha-se o vértice **aberto** com a menor `dist`; depois,
relaxam-se os vizinhos ainda abertos.

| Rodada | Fecha | S | A | B | C | D | T | O que aconteceu |
|---|---|---|---|---|---|---|---|---|
| início | — | 0 | ∞ | ∞ | ∞ | ∞ | ∞ | |
| 1 | S (0) | 0 | 7 | 2 | ∞ | ∞ | ∞ | A = 0+7, B = 0+2 |
| 2 | B (2) | 0 | **5** | 2 | ∞ | 10 | ∞ | A melhorou: 2+3 = 5 < 7; D = 2+8 |
| 3 | A (5) | 0 | 5 | 2 | 9 | 10 | ∞ | C = 5+4 |
| 4 | C (9) | 0 | 5 | 2 | 9 | 10 | 14 | D: 9+2 = 11, não melhora 10; T = 9+5 |
| 5 | D (10) | 0 | 5 | 2 | 9 | 10 | **13** | T melhorou: 10+3 = 13 < 14 |
| 6 | T (13) | 0 | 5 | 2 | 9 | 10 | 13 | fim |

`pai`: A ← B, B ← S, C ← A, D ← B, T ← D.

Caminho mais rápido até T: **S → B → D → T**, custo **13** (2 + 8 + 3).
Repare que o caminho "óbvio" S → A, que começa pela aresta direta, só vale
a pena chegando em A **por B** (5 em vez de 7).
