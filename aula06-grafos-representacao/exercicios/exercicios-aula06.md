# Exercícios Guiados — Aula 6: Grafos I (conceitos e representação)

Estruturas de Dados — UniLasalle EAD

Lista adicional com 10 exercícios sobre o conteúdo da Aula 6: o que é um
grafo, tipos de grafo, grau, caminhos, conexidade, matriz e lista de
adjacências. Estão em ordem crescente de dificuldade. Nenhum repete os
exercícios resolvidos nos slides; aqui o objetivo é praticar sozinho.

## Como usar este guia

- **Siga a ordem.** A Parte 1 se faz com papel e lápis; a Parte 2 pede código.
- **Desenhe os grafos.** Antes de responder qualquer item, faça o desenho:
  bolinhas (vértices) e linhas ou setas (arestas).
- **Tente antes de olhar o gabarito.** As soluções estão em
  [`../solucoes/`](../solucoes/). Use-as **depois**, para comparar.
- **Teste seu código.** Use o [OnlineIDE Pro](https://www.onlineide.pro/)
  ([playground Python](https://www.onlineide.pro/playground/python) /
  [playground C](https://www.onlineide.pro/playground/c)). Os arquivos da
  pasta [`../python/`](../python/) (ou [`../c/`](../c/)) servem de ponto de partida.
- **Marque seu progresso** trocando `[ ]` por `[x]` em cada item concluído.

**Legenda de dificuldade:** 🟢 fácil · 🟡 médio · 🔴 difícil · ✍️ papel (sem código) · 💻 programação (Python e C)

---

## Parte 1 — Conceitos

### Exercício 1 — Que tipo de grafo? 🟢 ✍️

- [ ] Concluído

**Objetivo:** escolher o modelo certo antes de programar.

Para cada situação, diga: (i) se o grafo é **dirigido** ou **não dirigido**;
(ii) se é **ponderado** (e o que o peso representaria); (iii) se ele **pode
ter ciclos** ou se, pela natureza do problema, não deveria ter.

- (a) As ruas de um bairro, algumas de mão única, com o tempo médio para
  percorrer cada quarteirão.
- (b) Uma árvore genealógica, com uma ligação de cada pai ou mãe para cada filho.
- (c) Os pré-requisitos das disciplinas do seu curso.
- (d) Os fios de uma instalação elétrica residencial, ligando o quadro de
  distribuição às tomadas.

---

### Exercício 2 — Graus e arestas 🟢 ✍️

- [ ] Concluído

**Objetivo:** praticar grau e o lema do aperto de mãos.

Considere o grafo não dirigido com `V = {A, B, C, D, E, F}` e
`E = {AB, AC, BC, BD, CE, DE, DF, EF}`.

- (a) Desenhe o grafo.
- (b) Calcule o grau de cada vértice.
- (c) Confira o lema: a soma dos graus é `2 × |E|`?
- (d) Quantos vértices têm grau **ímpar**? Por que esse número nunca pode ser
  ímpar, em nenhum grafo?

---

### Exercício 3 — Grafos regulares 🟡 ✍️

- [ ] Concluído

**Objetivo:** usar o lema do aperto de mãos para provar que algo é impossível.

Um grafo é **r-regular** quando todos os vértices têm grau `r`.

- (a) Existe um grafo 3-regular com 7 vértices? Justifique sem tentar desenhar.
- (b) Desenhe um grafo 3-regular com 6 vértices.
- (c) Quantas arestas tem um grafo r-regular com n vértices?
- (d) O grafo completo `Kₙ` é regular? De que grau?

---

### Exercício 4 — Ciclos e árvores 🟡 ✍️

- [ ] Concluído

**Objetivo:** relacionar número de arestas, ciclos e árvores.

Uma rede **conexa** tem 7 computadores e 9 cabos.

- (a) Essa rede pode ser uma árvore? Por quê?
- (b) Quantos cabos, no mínimo, precisam ser retirados para que ela vire uma
  árvore (uma *árvore geradora*), sem deixar ninguém desconectado?
- (c) Se retirarmos 4 cabos, a rede ainda pode continuar conexa? E se
  retirarmos 3?

---

### Exercício 5 — Da matriz para o desenho e para a lista 🟢 ✍️

- [ ] Concluído

**Objetivo:** ler uma matriz de adjacências.

```
     1  2  3  4  5
 1   0  1  1  0  0
 2   0  0  0  1  0
 3   0  1  0  1  0
 4   0  0  0  0  1
 5   0  0  0  0  0
```

- (a) O grafo é dirigido ou não dirigido? Como você sabe só olhando a matriz?
- (b) Desenhe o grafo.
- (c) Escreva a lista de adjacências.
- (d) Calcule o grau de entrada e o grau de saída de cada vértice. Quem é
  **fonte**? Quem é **sumidouro**?

---

## Parte 2 — Programação (Python e C)

### Exercício 6 — Contando arestas e laços 🟢 💻

- [ ] Concluído

**Objetivo:** extrair informação da matriz de adjacências.

Escreva as funções:

- `contar_arestas(m, n, dirigido)`: devolve `|E|` a partir da matriz.
  Cuidado: num grafo não dirigido cada aresta aparece **duas** vezes na
  matriz, **exceto o laço**, que só aparece na diagonal `M[v][v]`.
- `tem_laco(m, n)`: devolve verdadeiro se existe algum laço.

Teste com a rede da filial (10 arestas), com a mesma rede vista como dígrafo,
com a rede mais um laço em 4 (11 arestas) e com o dígrafo `1→2, 2→1, 2→3`
(3 arestas: ida e volta contam como duas setas).

---

### Exercício 7 — Completo e regular 🟡 💻

- [ ] Concluído

**Objetivo:** percorrer a matriz com propósito (este é o "para casa" da aula).

Escreva as funções:

- `eh_completo(m, n)`: verdadeiro se existe aresta entre **todo** par de
  vértices distintos.
- `eh_regular(m, n)`: devolve o grau comum a todos os vértices, ou `-1` se o
  grafo não for regular.

Teste com a rede da filial, com `K4`, com o ciclo `C5` (1-2-3-4-5-1) e com
`K4` sem a aresta 1-2. Algum desses grafos é regular sem ser completo?

---

### Exercício 8 — Invertendo as setas 🟡 💻

- [ ] Concluído

**Objetivo:** construir o **grafo transposto** com lista de adjacências.

Numa rede social, "u segue v" é a seta `u → v`. Os 5 perfis são ligados
pelas setas `1→2, 1→3, 2→3, 3→1, 4→3, 5→4`.

- (a) Monte a lista de adjacências ("quem cada perfil segue").
- (b) Escreva `transposto(adj, n)`, que inverte todas as setas
  ("quem segue cada perfil").
- (c) Use o transposto para descobrir o perfil mais seguido e os perfis sem
  nenhum seguidor.
- (d) Confira que transpor duas vezes devolve o grafo original.

---

### Exercício 9 — Caçando o erro na lista 🟡 💻

- [ ] Concluído

**Objetivo:** validar uma lista de adjacências de grafo **não dirigido**.

Se `v` está na lista de `u`, então `u` **tem** de estar na lista de `v`.
Escreva `validar(adj, n)`, que mostra todos os pares que quebram essa regra.
Teste com a rede da filial (correta) e com a lista abaixo, que tem um erro:

```
1: 2 -> 4
2: 1 -> 3
3: 2
4: 1 -> 3
```

Pense: que linha do `criar_lista` da aula, se esquecida, produziria esse
tipo de erro?

---

### Exercício 10 — Amigos em comum 🔴 💻

- [ ] Concluído

**Objetivo:** combinar matriz e lista, cada uma no que faz melhor.

Rede de amizades com 8 pessoas: 1 Ana, 2 Bruno, 3 Carla, 4 Davi, 5 Elisa,
6 Fabio, 7 Gabi, 8 Hugo. Amizades:

```
Ana-Bruno  Ana-Carla  Ana-Davi  Bruno-Carla  Bruno-Elisa  Carla-Elisa
Carla-Fabio  Davi-Elisa  Davi-Fabio  Elisa-Gabi  Fabio-Gabi  Gabi-Hugo
```

- (a) `amigos_em_comum(u, v)`: percorra a **lista** de `u` e teste na
  **matriz** se cada amigo também é amigo de `v`.
- (b) `sugerir_amizade(u)`: entre quem **não** é amigo de `u`, sugira quem tem
  mais amigos em comum com `u` (empate: o de menor número).
- (c) Qual é a complexidade de `amigos_em_comum`? E se usássemos só a lista?

---

Prof. Filipo Novo Mór — 2026 — [filipomor.com](https://filipomor.com)
