# Aula 4 — Complexidade de Algoritmos

Estruturas de Dados — UniLasalle EAD — Grau 1

Última aula do Grau 1. Contagem de operações, as notações **O**, **Ω** e
**Θ**, melhor, pior e caso médio (com o Insertion Sort como estudo de caso),
famílias de funções e um toque de Cálculo — tudo ligado às estruturas das
Aulas 1 a 3. Inclui a atividade prática **Campo Minado** (sem entrega).

## Estrutura desta pasta

```
c/                          # demos em C (arquivo único, cabem no OnlineIDE)
├── contagem_operacoes.c    # Bloco 2: conta os passos e compara com 3n + 4
├── insertion_sort.c        # Bloco 5: passo a passo e os 3 cenários
├── busca_saltos.c          # Bloco 6: confirma que o melhor salto é √n
└── Makefile
python/                     # as mesmas demos em Python
├── contagem_operacoes.py
├── insertion_sort.py       # demo ao vivo da aula (slide 33)
├── crescimento_funcoes.py  # tabelas das famílias de funções (slides 37 e 38)
└── busca_saltos.py
exercicios/
└── campo_minado/           # atividade prática: esqueleto com 12 TODOs
solucoes/
└── campo_minado/           # solução de exemplo comentada + GABARITO.md
material/
├── Apostila_Aula04_Complexidade.pdf            # apostila (80 páginas)
├── Atividade_Pratica_Aula04_Campo_Minado.pdf   # enunciado da atividade
└── fontes/                 # fontes LaTeX da apostila e do enunciado
```

## Como executar as demos

Cada arquivo é autocontido e usa só a biblioteca padrão: dá para colar
direto no [OnlineIDE Pro — playground Python](https://www.onlineide.pro/playground/python)
ou no [playground C](https://www.onlineide.pro/playground/c).

### C

```bash
cd c
make
./contagem_operacoes
./insertion_sort
./busca_saltos
```

Os programas compilam sem avisos com `-std=c11 -Wall -Wextra -pedantic`.

### Python

```bash
cd python
python3 contagem_operacoes.py
python3 insertion_sort.py
python3 crescimento_funcoes.py
python3 busca_saltos.py
```

No Windows, use `py` ou `python` no lugar de `python3`.

## Atividade prática: Campo Minado

Prática de autoestudo, **sem entrega**. Comece pelo esqueleto em
[`exercicios/campo_minado/`](exercicios/campo_minado/): a interface gráfica
já vem pronta, e os testes automáticos (`python testes.py`) conferem cada
TODO. A solução de exemplo e o gabarito das partes sem código estão em
[`solucoes/campo_minado/`](solucoes/campo_minado/) — tente antes de olhar.

O enunciado completo, com o passo a passo de instalação do Python e do
PyCharm (ou do Thonny), está em
[`material/Atividade_Pratica_Aula04_Campo_Minado.pdf`](material/Atividade_Pratica_Aula04_Campo_Minado.pdf).

## Material de estudo

A [apostila](material/Apostila_Aula04_Complexidade.pdf) acompanha a aula
capítulo a capítulo: cada slide indica a página que aprofunda o assunto. O
capítulo 14 explica as regras e as técnicas do Campo Minado; o capítulo 15
traz 28 exercícios resolvidos, incluindo questões objetivas no estilo da
prova do Grau 1; o capítulo 16 é um resumo para a prova.

As fontes em LaTeX estão em `material/fontes/` (compile com XeLaTeX —
veja o `LEIAME.md` da pasta).

---

Prof. Filipo Novo Mór — 2026 — [filipomor.com](https://filipomor.com)
