# Aula 1 — Estruturas Lineares (Parte 1)

Estruturas de Dados — UniLasalle EAD — Grau 1

Códigos de apoio da Aula 1: estruturas contíguas x encadeadas, e o TAD
Lista implementado das duas formas — em **C** e em **Python**.

## Estrutura desta pasta

```
c/
├── memoria_ponteiros.c     # Bloco 2: ponteiros em C
├── lista_contigua.h        # TAD Lista sobre array
├── lista_contigua.c
├── main_contigua.c         # programa de demonstração
├── lista_encadeada.h       # TAD Lista com nós ligados por ponteiros
├── lista_encadeada.c
├── main_encadeada.c        # programa de demonstração
└── Makefile
python/
├── memoria_referencias.py  # Bloco 2: referências em Python
├── lista_contigua.py       # TAD Lista sobre list()
└── lista_encadeada.py      # TAD Lista com nós ligados por referências
exercicios/
└── exercicios-aula01.md
solucoes/                   # gabarito dos exercícios — ver solucoes/README.md
```

Cada TAD implementa a mesma interface, discutida em aula:

| Operação | Descrição | Custo — Contígua | Custo — Encadeada |
|---|---|---|---|
| `inserir(pos, valor)` | insere na posição | O(n) | O(n) |
| `inserir_inicio(valor)` | atalho para `inserir(0, ...)` | O(n) | O(1) |
| `inserir_fim(valor)` | atalho para `inserir(tamanho, ...)` | O(1)* | O(1) |
| `remover(pos)` | remove da posição | O(n) | O(n) |
| `buscar(valor)` | retorna a posição do valor (ou -1) | O(n) | O(n) |
| `obter(pos)` | lê o valor de uma posição | O(1) | O(n) |
| `tamanho()` | quantidade de elementos | O(1) | O(1) |
| `percorrer()` | imprime todos os elementos | O(n) | O(n) |

\* amortizado, considerando o custo ocasional de realocação.

## Como executar

### C

Requer um compilador C (gcc/clang). Com o `make`:

```bash
cd c
make            # compila os três programas
./memoria       # demo de ponteiros
./contigua      # demo da lista contígua
./encadeada     # demo da lista encadeada
```

Sem `make`, compilando manualmente:

```bash
gcc -std=c11 -o contigua main_contigua.c lista_contigua.c
```

Sem instalar nada localmente, dá pra usar o [OnlineIDE Pro — playground C](https://www.onlineide.pro/playground/c).

### Python

Requer Python 3.10+ (usa apenas a biblioteca padrão, sem dependências).

```bash
cd python
python3 memoria_referencias.py
python3 lista_contigua.py
python3 lista_encadeada.py
```

Sem instalar nada localmente, dá pra usar o [OnlineIDE Pro — playground Python](https://www.onlineide.pro/playground/python).

## Testes

As duas implementações em Python foram validadas com um teste de
equivalência aleatório (200 rodadas de 60 operações cada) contra a
`list` nativa do Python, e a versão em C da lista encadeada foi
verificada quanto a vazamento de memória (todo `malloc` tem um `free`
correspondente). Nenhum framework de testes foi incluído no repositório
— o objetivo aqui é material didático, não uma biblioteca de produção.

---

Prof. Filipo Novo Mór — 2026 — [filipomor.com](https://filipomor.com)
