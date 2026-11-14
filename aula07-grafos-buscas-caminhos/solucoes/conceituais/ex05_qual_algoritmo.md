# Exercício 5 — Qual algoritmo usar?

**(a)** Sim: com todos os pesos iguais a 1, o custo de um caminho é o
número de arestas, que é justamente o que a BFS mede. Use a **BFS**: ela
custa O(V + E) e não precisa procurar o menor `dist` a cada rodada (o
Dijkstra simples custa O(V²); com heap, O((V + E) log V)).

**(b)** Exemplo: `S-A` com peso 10, `S-B` com peso 1 e `B-A` com peso 1.
A BFS chega em A por `S → A` (1 aresta, custo 10). O caminho mais barato é
`S → B → A` (2 arestas, custo 2).

**(c)** Somar uma constante **penaliza caminhos com mais arestas**, porque
cada aresta recebe o acréscimo. Exemplo (dígrafo):

| Seta | Peso original | Peso + 3 |
|---|---|---|
| S → T | 1 | 4 |
| S → A | 2 | 5 |
| A → T | −2 | 1 |

- Original: `S → A → T` custa 2 + (−2) = **0**, melhor que `S → T` (1).
- Com +3: `S → A → T` passa a custar 5 + 1 = 6, e `S → T` custa **4**.

O Dijkstra no grafo modificado responderia `S → T`, que **não** é o
caminho mínimo do grafo original. Para pesos negativos use o
**Bellman-Ford** (Cormen et al., seção 24.1), que não faz parte desta aula.

**(d)**
- (i) GPS, menor tempo: **Dijkstra** (pesos = tempos, não negativos).
- (ii) Menor número de conexões entre duas pessoas: **BFS**.
- (iii) Todos os computadores se alcançam? **BFS ou DFS** a partir de
  qualquer um: a rede é conexa se todos forem marcados.
- (iv) Menor número de movimentos do cavalo: **BFS** num grafo implícito
  (cada casa do tabuleiro é um vértice; os movimentos em "L" são as arestas),
  como no labirinto do Exercício 10.
