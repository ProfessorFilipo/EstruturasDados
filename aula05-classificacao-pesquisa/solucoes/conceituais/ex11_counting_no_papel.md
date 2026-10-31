# Exercício 11 — Counting Sort no papel

Páginas: `[2, 4, 1, 4, 3, 1, 2, 4]`, k = 4.

**a) Contar** (quantos trabalhos com 1, 2, 3 e 4 páginas):

```
páginas:   1  2  3  4
contagem: [2, 2, 1, 3]
```

**b) Acumular** (onde começa o bloco de cada valor):

```
páginas:          1  2  3  4
bloco começa em: [0, 2, 4, 5]
```

**c) Posicionar** (percorrendo a entrada na ordem de chegada):

```
saída: [1, 1, 2, 2, 3, 4, 4, 4]
        0  1  2  3  4  5  6  7
```

Foram 8 + 4 + 8 = 20 operações simples (2n + k) e **nenhuma** comparação
entre elementos.
