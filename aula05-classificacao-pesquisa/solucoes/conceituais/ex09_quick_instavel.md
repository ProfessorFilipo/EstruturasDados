# Exercício 9 — O Quicksort não é estável

Um exemplo com 3 trabalhos `(id, paginas)`:

```
antes:  [(101, 5), (102, 5), (103, 3)]      101 chegou antes de 102
```

Pivô = último = `(103, 3)`. Nenhum dos dois primeiros tem menos de 3
páginas, então `i` fica em 0 e o pivô troca com a posição 0:

```
depois: [(103, 3), (102, 5), (101, 5)]      102 passou na frente de 101!
```

Os dois trabalhos de 5 páginas trocaram de ordem: a troca "de longe" do
pivô embaralhou o empate. Por isso o Quicksort **não é estável** — diferente
do Insertion Sort e do Merge Sort, que só movem elementos vizinhos ou
intercalam tirando primeiro da esquerda.
