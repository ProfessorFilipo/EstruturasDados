# Exercício 2 — Rastreando a DFS

Recursão (o recuo é a profundidade):

```
visita A
  visita B            (1o vizinho de A)
    visita C          (A já marcado; C é o próximo vizinho de B)
      visita F        (B marcado; F)
        visita E      (C marcado; E)
          visita D    (B marcado; D)
          volta de D  (A e E já marcados)
          visita G    (F marcado; G)
            visita H  (E marcado; H)
            volta de H
          volta de G
        volta de E
      volta de F
    volta de C
  volta de B          (E já foi visitado por outro caminho)
volta de A            (D já foi visitado)
```

**(a)** Ordem de visita: **A B C F E D G H**

**(b)** Árvore DFS (arestas que descobriram vértices novos):
`A-B, B-C, C-F, F-E, E-D, E-G, G-H`. São 7 arestas para 8 vértices: é uma
**árvore geradora**. As arestas que sobraram (`A-D`, `B-E`, `F-H`) não
aparecem nela.

```
A
└─ B
   └─ C
      └─ F
         └─ E
            ├─ D
            └─ G
               └─ H
```

**(c)** **H**, no nível 6 (A está no nível 0). Compare com a BFS, onde H
estava a distância 4: a DFS **não** encontra caminhos mínimos, ela "mergulha".
