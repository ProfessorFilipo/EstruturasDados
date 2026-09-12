# Exercícios Guiados — Aula 1: Estruturas Lineares

Estruturas de Dados — UniLasalle EAD — Grau 1

Sequência de 15 exercícios cobrindo todo o conteúdo da Aula 1 — memória e
referências, estruturas contíguas x encadeadas, e o TAD Lista nas duas
implementações — em ordem crescente de dificuldade.

## Como usar este guia

- **Siga a ordem.** Cada bloco depende do raciocínio construído no anterior.
- **Tente antes de olhar a solução de referência.** Os exercícios 6, 7, 9 e
  10 pedem para implementar operações que **já existem prontas** em
  `c/lista_contigua.c`, `python/lista_contigua.py`,
  `c/lista_encadeada.c` e `python/lista_encadeada.py` neste repositório.
  Não abra esses arquivos antes de tentar — use-os só **depois**, para
  comparar sua solução com a referência.
- **Teste seu código.** Use o [OnlineIDE Pro](https://www.onlineide.pro/)
  ([playground C](https://www.onlineide.pro/playground/c) /
  [playground Python](https://www.onlineide.pro/playground/python)) ou o
  ambiente local que você já configurou.
- **Marque seu progresso** trocando `[ ]` por `[x]` em cada item conforme
  for concluindo.

**Legenda de dificuldade:** 🟢 fácil · 🟡 médio · 🔴 difícil · ✍️ reflexão (sem código)

---

## Parte 1 — Memória e Referências (Aquecimento)

### Exercício 1 — Troca de valores com ponteiros 🟢 `C`

- [ ] Concluído

**Objetivo:** fixar o conceito de ponteiro como "endereço de outra variável".

Escreva um programa em C que declare duas variáveis inteiras `a` e `b`
com valores diferentes, e troque os valores delas usando **apenas
ponteiros** — ou seja, escreva uma função `trocar(int *p1, int *p2)` que
recebe os endereços de `a` e `b` e troca os valores apontados por eles.

**Como testar:** imprima `a` e `b` antes e depois de chamar `trocar()`.
Os valores devem estar invertidos depois da chamada.

---

### Exercício 2 — Referências compartilhadas 🟢 `Python`

- [ ] Concluído

**Objetivo:** fixar que, em Python, atribuição não copia — cria uma nova
referência ao mesmo objeto.

Crie uma lista `original = [1, 2, 3]`. Em seguida:

1. Crie `mesma_lista = original` e mostre, com `is`, que ambas apontam
   para o mesmo objeto.
2. Crie `copia = original.copy()` (ou `original[:]`) e mostre que
   **não** é o mesmo objeto.
3. Modifique `mesma_lista` (ex.: `.append(4)`) e imprima `original` —
   explique em um comentário por que ela também mudou.
4. Modifique `copia` e mostre que `original` **não** muda dessa vez.

---

## Parte 2 — Contíguas x Encadeadas (Conceitual)

### Exercício 3 — Contando deslocamentos 🟢 `papel e caneta`

- [ ] Concluído

**Objetivo:** internalizar o custo de inserção em cada estrutura.

Considere uma lista com 6 elementos: `[10, 20, 30, 40, 50, 60]`.

Para cada operação abaixo, calcule **manualmente** quantos elementos
precisariam ser deslocados na versão **contígua** (array), e compare com
o custo na versão **encadeada** (assumindo que você já tem um ponteiro
para o nó anterior à posição, quando aplicável):

1. Inserir `99` na posição 0.
2. Inserir `99` na posição 3.
3. Inserir `99` na posição 6 (no fim).
4. Remover o elemento da posição 0.

---

### Exercício 4 — Complete a tabela de complexidade 🟡 `papel e caneta`

- [ ] Concluído

**Objetivo:** consolidar a comparação de custos vista no slide 7 da aula,
mas justificando cada resposta com suas próprias palavras (não vale só
copiar a tabela do slide).

Para cada operação, escreva O(1) ou O(n) para cada estrutura **e uma
frase explicando por quê**:

| Operação | Contígua | Por quê? | Encadeada | Por quê? |
|---|---|---|---|---|
| Acesso por índice | | | | |
| Inserir no início | | | | |
| Inserir no fim | | | | |
| Buscar por valor | | | | |

---

## Parte 3 — TAD Lista e Lista Contígua

### Exercício 5 — `esta_vazia()` 🟡 `C` e `Python`

- [ ] Concluído (C)
- [ ] Concluído (Python)

**Objetivo:** estender o TAD Lista com uma operação que ainda não existe
no repositório.

Implemente uma função `esta_vazia(lista)` que retorna verdadeiro se a
lista não tem elementos. Implemente **para as quatro combinações**:
Lista Contígua em C, Lista Contígua em Python, Lista Encadeada em C,
Lista Encadeada em Python.

**Como testar:** deve retornar `1`/`True` para uma lista recém-criada, e
`0`/`False` depois de qualquer inserção.

---

### Exercício 6 — `inserir_fim` e `buscar`, do zero 🟡 `C`

- [ ] Concluído

**Objetivo:** implementar, sem consultar a referência, as operações
básicas da Lista Contígua.

Em um arquivo novo (não abra `lista_contigua.c`), defina sua própria
`struct` para uma lista contígua de inteiros e implemente:

- `inserir_fim(lista, valor)`
- `buscar(lista, valor)` → retorna o índice, ou `-1` se não encontrado

**Como testar:** insira `10, 20, 30` e confirme que `buscar(lista, 20)`
retorna `1` e `buscar(lista, 99)` retorna `-1`.

---

### Exercício 7 — `inserir_fim` e `buscar`, do zero 🟡 `Python`

- [ ] Concluído

**Objetivo:** o mesmo do Exercício 6, agora em Python.

Em um arquivo novo (não abra `lista_contigua.py`), crie uma classe
`ListaContigua` com `inserir_fim(valor)` e `buscar(valor)`.

**Como testar:** mesmo caso do Exercício 6.

---

### Exercício 8 — `remover_valor(lista, valor)` 🟡 `C` e `Python`

- [ ] Concluído (C)
- [ ] Concluído (Python)

**Objetivo:** diferenciar remoção **por posição** (já implementada no
repositório) de remoção **por valor**.

Implemente `remover_valor(lista, valor)`, que localiza a primeira
ocorrência do valor e remove essa posição (pode reaproveitar
`buscar()` + `remover()` por posição, se já tiver as duas prontas).
Trate o caso em que o valor não existe na lista.

**Como testar:** em `[10, 20, 30, 20]`, remover o valor `20` deve deixar
`[10, 30, 20]` — só a **primeira** ocorrência sai.

---

## Parte 4 — Lista Encadeada

### Exercício 9 — `inserir_inicio` e `percorrer`, do zero 🟡 `C`

- [ ] Concluído

**Objetivo:** implementar, sem consultar a referência, a estrutura de nós
ligados por ponteiros.

Em um arquivo novo (não abra `lista_encadeada.c`), defina sua própria
`struct No` (valor + ponteiro `proximo`) e implemente
`inserir_inicio(lista, valor)` e `percorrer(lista)`.

**Como testar:** insira `10`, depois `20`, depois `30` no início, nessa
ordem — `percorrer()` deve imprimir `30, 20, 10`.

---

### Exercício 10 — `inserir_inicio` e `percorrer`, do zero 🟡 `Python`

- [ ] Concluído

**Objetivo:** o mesmo do Exercício 9, agora em Python.

Em um arquivo novo (não abra `lista_encadeada.py`), crie as classes `No`
e `ListaEncadeada` com `inserir_inicio(valor)` e `percorrer()`.

**Como testar:** mesmo caso do Exercício 9.

---

### Exercício 11 — `inverter(lista)` 🔴 `C` ou `Python`

- [ ] Concluído

**Objetivo:** manipular ponteiros/referências para reorganizar a lista
**sem criar nós novos** — só religando os já existentes.

Implemente `inverter(lista)`, que inverte a ordem dos elementos da Lista
Encadeada. Pode usar a implementação de referência do repositório como
ponto de partida desta vez (a estrutura em si não é o foco do
exercício — a lógica de inversão é).

**Dica:** você vai precisar de três ponteiros/referências auxiliares
(anterior, atual, próximo) para não perder a referência ao resto da
lista enquanto religa os nós.

**Como testar:** uma lista `[10, 20, 30]` deve virar `[30, 20, 10]`
depois de `inverter()`, sem nenhum valor perdido ou duplicado.

---

### Exercício 12 — `contigua_para_encadeada(lista)` 🔴 `C` ou `Python`

- [ ] Concluído

**Objetivo:** transitar entre as duas representações do mesmo TAD —
reforça que a interface é a mesma, a estrutura de memória é que muda.

Implemente uma função que recebe uma `ListaContigua` já preenchida e
retorna uma nova `ListaEncadeada` com os mesmos elementos, na mesma
ordem.

**Como testar:** partindo de uma `ListaContigua` com `[5, 10, 15]`, o
resultado deve ser uma `ListaEncadeada` cujo `percorrer()` imprime
`5, 10, 15` nessa ordem.

---

### Exercício 13 — `remover_duplicatas(lista)` 🔴 `C` ou `Python`

- [ ] Concluído

**Objetivo:** combinar busca e remoção em uma operação mais elaborada.

Implemente `remover_duplicatas(lista)` para a Lista Encadeada: percorra
a lista e remova qualquer nó cujo valor já tenha aparecido antes,
mantendo apenas a primeira ocorrência de cada valor.

**Como testar:** `[5, 3, 5, 8, 3, 9]` deve virar `[5, 3, 8, 9]`.

**Dica:** para uma versão mais simples (aceitável), pode usar uma
estrutura auxiliar (lista/array/set) para lembrar quais valores já
viu. Para um desafio extra, tente resolver sem estrutura auxiliar
(custo maior, mas sem gastar memória extra).

---

### Exercício 14 — Medindo desempenho na prática 🔴 `C` ou `Python`

- [ ] Concluído

**Objetivo:** confirmar experimentalmente a tabela de complexidade do
Exercício 4 — sair da teoria e ver o custo acontecer de verdade.

Escreva um pequeno programa que:

1. Insira **10.000 elementos no início** de uma Lista Contígua e meça o
   tempo total (em Python, `time.time()` antes/depois; em C,
   `clock()` da `<time.h>`).
2. Repita, agora inserindo **no fim**.
3. Repita os dois casos para a Lista Encadeada.
4. Imprima os quatro tempos e escreva, em um comentário, se o resultado
   bateu com o que a tabela de complexidade previa.

---

## Parte 5 — Encerramento

### Exercício 15 — Reflexão final ✍️ `escrito, sem código`

- [ ] Concluído

**Objetivo:** consolidar o critério de decisão entre as duas estruturas
(objetivo 5 da aula).

Em poucas linhas, responda: **você está projetando um sistema que
processa uma fila de atendimento, onde elementos são constantemente
inseridos no fim e removidos do início, e raramente é preciso acessar
uma posição aleatória. Qual estrutura você escolheria — contígua ou
encadeada — e por quê?** Use os custos discutidos nos Exercícios 3, 4 e
14 para justificar sua resposta.

---

Prof. Filipo Novo Mór — 2026 — [filipomor.com](https://filipomor.com)
