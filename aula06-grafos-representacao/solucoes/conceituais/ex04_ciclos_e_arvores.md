# Exercício 4 — Ciclos e árvores

Fato usado: **uma árvore com n vértices tem exatamente n − 1 arestas.**
Com menos que isso o grafo é desconexo; com mais, tem ciclo.

**(a) Não pode ser árvore.** Com 7 computadores, uma árvore teria 6 cabos.
A rede tem 9: sobram 3, e cada cabo a mais fecha um ciclo.

**(b) 3 cabos** (9 − 6). Mas não podem ser 3 quaisquer: cada cabo retirado
precisa ser de um ciclo (nunca um cabo cuja retirada separaria a rede). O
que sobra é uma **árvore geradora**: todos os 7 continuam conectados, com o
mínimo de cabos.

**(c)**
- Retirando **4**: sobram 5 cabos para 7 computadores, menos que os 6 de
  uma árvore. A rede fica **necessariamente desconexa**.
- Retirando **3**: **pode** continuar conexa, desde que sejam os 3 cabos
  "sobrando" do item (b). Se tirar um cabo errado, ela se separa.

Esses fatos voltam na Aula 7: a **árvore BFS** e a **árvore DFS** são
árvores geradoras que as buscas constroem "de brinde".
