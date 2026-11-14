# Exercício 1 — Que tipo de grafo?

| Situação | Dirigido? | Ponderado? | Ciclos? |
|---|---|---|---|
| (a) Ruas do bairro | **Sim**: rua de mão única é uma seta; rua de mão dupla vira duas setas (ida e volta). | **Sim**: o peso é o tempo de cada quarteirão. | **Podem existir**: dar a volta no quarteirão é um ciclo. |
| (b) Árvore genealógica | **Sim**: a seta vai do pai ou da mãe para o filho. | Não (nada a medir em cada ligação). | **Não deveria ter**: ninguém é ancestral de si mesmo. É um grafo dirigido acíclico (DAG). |
| (c) Pré-requisitos | **Sim**: a seta vai da disciplina pré-requisito para a disciplina que depende dela. | Não, normalmente. Se quiser, o peso pode ser a carga horária. | **Não pode ter**: um ciclo de pré-requisitos impediria qualquer aluno de se formar. |
| (d) Instalação elétrica | **Não**: o fio liga dois pontos, sem sentido de percurso. | Opcional: o peso pode ser o comprimento do fio (custo do material). | Numa instalação residencial típica, os circuitos saem do quadro e se ramificam **sem ciclos**: é uma árvore com raiz no quadro. |

**Lição:** antes de escolher matriz ou lista, decida o **modelo**. Ser
dirigido e ponderado muda o código; ter ou não ciclos muda quais algoritmos
fazem sentido.
