# Exercícios Guiados — Aula 7: Grafos II (buscas e caminho mínimo)

Estruturas de Dados — UniLasalle EAD

Lista adicional com 10 exercícios sobre o conteúdo da Aula 7: busca em
largura (BFS), busca em profundidade (DFS), componentes conexas e o
algoritmo de Dijkstra. Estão em ordem crescente de dificuldade. Nenhum
repete os exercícios resolvidos nos slides.

## Como usar este guia

- **Siga a ordem.** A Parte 1 é rastreio no papel; a Parte 2 pede código.
- **Rastreie com uma tabela.** Para BFS, anote a **fila** a cada passo; para
  DFS, a **pilha** (ou a recursão); para Dijkstra, o vetor **dist** a cada
  rodada. Depois confira rodando os arquivos de [`../python/`](../python/)
  com o seu grafo.
- **Tente antes de olhar o gabarito.** As soluções estão em
  [`../solucoes/`](../solucoes/).
- **Teste seu código** no [OnlineIDE Pro](https://www.onlineide.pro/)
  ([playground Python](https://www.onlineide.pro/playground/python) /
  [playground C](https://www.onlineide.pro/playground/c)).
- **Marque seu progresso** trocando `[ ]` por `[x]` em cada item concluído.

**Legenda de dificuldade:** 🟢 fácil · 🟡 médio · 🔴 difícil · ✍️ papel (sem código) · 💻 programação (Python e C)

O **mapa do campus** usado nos exercícios 1 a 3 (grafo não dirigido; cada
vértice é um prédio, cada aresta um corredor):

```
A ── B ── C
|    |    |
D ── E ── F
     |    |
     G ── H
```

Arestas: `A-B, A-D, B-C, B-E, C-F, D-E, E-F, E-G, F-H, G-H`.
Salvo quando o exercício disser o contrário, os vizinhos de cada vértice são
visitados em **ordem alfabética**.

---

## Parte 1 — Rastreios no papel

### Exercício 1 — Rastreando a BFS 🟢 ✍️

- [ ] Concluído

**Objetivo:** praticar a fila da BFS.

Rode a BFS no mapa do campus a partir de **A**. A cada vértice retirado da
fila, anote: quem saiu, quem entrou e como ficou a fila. Ao final, dê:

- (a) a ordem de visita;
- (b) os vetores `dist` e `pai`;
- (c) o caminho com menos corredores de A até H.

---

### Exercício 2 — Rastreando a DFS 🟢 ✍️

- [ ] Concluído

**Objetivo:** praticar a recursão (ou a pilha) da DFS.

Rode a DFS recursiva no mesmo mapa, a partir de **A**.

- (a) Qual é a ordem de visita?
- (b) Desenhe a **árvore DFS** (só as arestas usadas para descobrir vértices novos).
- (c) Qual vértice ficou mais "fundo" na recursão? Em que nível?

---

### Exercício 3 — A ordem dos vizinhos importa? 🟡 ✍️

- [ ] Concluído

**Objetivo:** separar o que é propriedade do grafo do que é detalhe da implementação.

Repita a BFS do Exercício 1, mas agora visitando os vizinhos em ordem
alfabética **inversa** (por exemplo, os vizinhos de E na ordem G, F, D, B).

- (a) A ordem de visita mudou?
- (b) O vetor `dist` mudou?
- (c) O caminho encontrado de A até H mudou? Ele continua sendo mínimo?
- (d) Conclua: o que a BFS **garante** e o que **depende** da ordem das listas?

---

### Exercício 4 — Dijkstra no papel 🟡 ✍️

- [ ] Concluído

**Objetivo:** montar a tabela do Dijkstra rodada a rodada.

Grafo não dirigido com pesos (tempo, em minutos):

```
S-A 7   S-B 2   A-B 3   A-C 4   B-D 8   C-D 2   C-T 5   D-T 3
```

Rode o Dijkstra a partir de **S**. Monte uma tabela com uma linha por
rodada: qual vértice foi **fechado** e como ficou `dist` para S, A, B, C, D e T.
Depois, dê o caminho mais rápido de S até T e o seu custo.

---

### Exercício 5 — Qual algoritmo usar? 🟡 ✍️

- [ ] Concluído

**Objetivo:** entender os limites de cada algoritmo.

- (a) Se todos os pesos de um grafo forem iguais a 1, o Dijkstra e a BFS
  dão as mesmas distâncias? Qual dos dois você usaria, e por quê?
- (b) Monte um grafo com 3 vértices em que o caminho com **menos arestas**
  não é o de **menor custo**.
- (c) Um colega propõe: "se há pesos negativos, basta somar uma constante a
  todos os pesos para eles ficarem positivos e então rodar o Dijkstra".
  Mostre com um exemplo pequeno que essa ideia **não funciona**.
- (d) Para cada situação, escolha BFS, DFS ou Dijkstra: (i) GPS que busca o
  menor tempo; (ii) menor número de conexões entre duas pessoas numa rede
  profissional; (iii) verificar se todos os computadores de uma rede se
  alcançam; (iv) menor número de movimentos de um cavalo para ir de uma casa
  a outra do tabuleiro de xadrez.

---

## Parte 2 — Programação (Python e C)

### Exercício 6 — Graus de separação 🟢 💻

- [ ] Concluído

**Objetivo:** usar a BFS num problema de rede social (este é o "para casa" da aula).

Use a rede de amizades do Exercício 10 da Aula 6 (Ana, Bruno, Carla, Davi,
Elisa, Fabio, Gabi e Hugo). A partir de **Ana**:

- (a) mostre o grau de separação de cada pessoa;
- (b) liste os "amigos de amigos" de Ana (grau exatamente 2);
- (c) encontre a pessoa mais distante e a cadeia de apresentações até ela.

---

### Exercício 7 — Existe ciclo? 🟡 💻

- [ ] Concluído

**Objetivo:** adaptar a DFS para responder outra pergunta.

Escreva `tem_ciclo(adj, n)` para grafos **não dirigidos**, usando DFS. Dica:
durante a DFS, encontrar um vizinho **já marcado** que **não é o pai** do
vértice atual significa que existe um ciclo. Por que o pai não conta?

Teste com: a rede da filial; a árvore `1-2, 1-3, 2-4, 2-5, 3-6`; a floresta
`1-2, 2-3, 4-5, 5-6, 5-7`; e a mesma árvore com a aresta extra `4-6`.

---

### Exercício 8 — Dois times sem rivais 🟡 💻

- [ ] Concluído

**Objetivo:** usar a BFS para "pintar" um grafo (teste de grafo bipartido).

Numa turma de 6 alunos, as rivalidades são `1-2, 1-4, 2-3, 3-6, 4-5, 5-6`.
O professor quer dividir a turma em dois times sem nenhum par de rivais no
mesmo time.

- (a) Escreva `dividir(adj, n)`: BFS em que cada vértice recebe o time
  oposto ao de quem o descobriu. Se dois vizinhos caírem no mesmo time, a
  divisão é impossível.
- (b) Teste com a turma acima, com a turma mais a rivalidade `1-3` e com 7
  alunos (o 7 sem rivais).
- (c) Por que um "triângulo de rivais" sempre torna a divisão impossível?

---

### Exercício 9 — Rota entre cidades 🟡 💻

- [ ] Concluído

**Objetivo:** usar o Dijkstra com nomes e reconstruir a rota.

Estradas da Região Metropolitana de Porto Alegre, com tempos **ilustrativos**
(minutos):

```
Porto Alegre-Canoas 20      Porto Alegre-Cachoeirinha 25   Canoas-Esteio 12
Canoas-Cachoeirinha 15      Esteio-Sapucaia do Sul 8       Sapucaia do Sul-Sao Leopoldo 10
Sao Leopoldo-Novo Hamburgo 15   Cachoeirinha-Gravatai 12   Gravatai-Novo Hamburgo 50
Esteio-Sao Leopoldo 22
```

Mostre, para cada cidade, o menor tempo a partir de Porto Alegre e a rota
completa, em ordem crescente de tempo.

---

### Exercício 10 — Saindo do labirinto 🔴 💻

- [ ] Concluído

**Objetivo:** perceber que um grafo pode estar "escondido" num problema.

```
##########
#E.....#.#
#.##.###.#
#.#..#...#
#.#.####.#
#...#..#.#
###.#.##.#
#.....#..#
#.###...S#
##########
```

Cada casa livre (`.`, `E` ou `S`) é um vértice, e casas vizinhas na
horizontal ou na vertical estão ligadas. Sem montar lista nem matriz de
adjacências (os vizinhos são calculados na hora), use a BFS para:

- (a) achar o menor número de passos de `E` até `S`;
- (b) desenhar o caminho com `*`;
- (c) contar quantas casas são alcançáveis a partir de `E`.

---

Prof. Filipo Novo Mór — 2026 — [filipomor.com](https://filipomor.com)
