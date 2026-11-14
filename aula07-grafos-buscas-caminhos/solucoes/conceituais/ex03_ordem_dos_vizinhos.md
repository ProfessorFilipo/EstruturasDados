# Exercício 3 — A ordem dos vizinhos importa?

Listas em ordem alfabética **inversa**:

```
A: D B        E: G F D B
B: E C A      F: H E C
C: F B        G: H E
D: E A        H: G F
```

| Sai | Entram (dist, pai) | Fila depois |
|---|---|---|
| A | D (1, A), B (1, A) | [D, B] |
| D | E (2, D) | [B, E] |
| B | C (2, B) | [E, C] |
| E | G (3, E), F (3, E) | [C, G, F] |
| C | — | [G, F] |
| G | H (4, G) | [F, H] |
| F | — | [H] |
| H | — | [] |

**(a) Mudou:** agora é **A D B E C G F H** (antes: A B D C E F G H).

**(b) Não mudou:** `dist` continua A 0, B 1, C 2, D 1, E 2, F 3, G 3, H 4.

**(c) Mudou**, mas continua mínimo: agora é **A → D → E → G → H**, também
com 4 corredores. O grafo tem mais de um caminho mínimo; a BFS devolve um
deles.

**(d)** A BFS **garante** a menor distância (em número de arestas) da
origem até cada vértice, porque isso é uma propriedade do **grafo**. A
**ordem** de visita e **qual** dos caminhos mínimos aparece em `pai`
dependem da ordem em que os vizinhos estão guardados nas listas.
