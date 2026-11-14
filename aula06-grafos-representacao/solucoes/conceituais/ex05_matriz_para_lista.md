# Exercício 5 — Da matriz para o desenho e para a lista

**(a) Dirigido.** A matriz **não é simétrica**: por exemplo, `M[1][2] = 1`
mas `M[2][1] = 0`. Num grafo não dirigido toda aresta aparece nas duas
posições.

**(b)** As setas são as posições com 1, lidas como "linha → coluna":
`1→2, 1→3, 2→4, 3→2, 3→4, 4→5`.

```
  1 ──→ 2 ──→ 4 ──→ 5
  │     ↑     ↑
  └──→  3 ────┘
```
(3 aponta para 2 e para 4.)

**(c)** Lista de adjacências:

```
1: 2 -> 3
2: 4
3: 2 -> 4
4: 5
5: (vazia)
```

**(d)** Saída = soma da **linha**; entrada = soma da **coluna**.

| Vértice | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| Saída | 2 | 1 | 2 | 1 | 0 |
| Entrada | 0 | 2 | 1 | 2 | 1 |

Soma das saídas = soma das entradas = 6 = número de setas.
**Fonte** (entrada 0): vértice **1**. **Sumidouro** (saída 0): vértice **5**.
