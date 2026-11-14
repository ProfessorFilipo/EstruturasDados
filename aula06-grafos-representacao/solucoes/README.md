# Soluções — Exercícios Guiados da Aula 6

Gabarito de referência para [`exercicios/exercicios-aula06.md`](../exercicios/exercicios-aula06.md).

## Organização

```
solucoes/
├── conceituais/   # exercícios 1 a 5 (papel)
├── python/        # exercícios 6 a 10
└── c/             # exercícios 6 a 10 (com Makefile)
```

Os nomes dos arquivos seguem `exNN_descricao.{md,py,c}`, correspondendo ao
número do exercício no guia.

| Exercício | Arquivo | Assunto |
|---|---|---|
| 1 | `conceituais/ex01_tipo_de_grafo.md` | dirigido, ponderado, com ou sem ciclos |
| 2 | `conceituais/ex02_graus_e_arestas.md` | graus e lema do aperto de mãos |
| 3 | `conceituais/ex03_grafos_regulares.md` | grafos r-regulares |
| 4 | `conceituais/ex04_ciclos_e_arvores.md` | árvores com n − 1 arestas |
| 5 | `conceituais/ex05_matriz_para_lista.md` | ler uma matriz de dígrafo |
| 6 | `ex06_contar_arestas.{py,c}` | contar arestas e laços pela matriz |
| 7 | `ex07_completo_regular.{py,c}` | grafo completo e grafo regular |
| 8 | `ex08_grafo_transposto.{py,c}` | inverter as setas (seguidores) |
| 9 | `ex09_validar_lista.{py,c}` | achar o erro numa lista de adjacências |
| 10 | `ex10_amigos_em_comum.{py,c}` | amigos em comum e sugestão de amizade |

## Uma nota sobre o repositório público

Os gabaritos ficam visíveis junto com os enunciados. O valor está em tentar
**antes** de abrir a solução e comparar depois.

## Como executar

### Python

```bash
cd python
python3 ex06_contar_arestas.py
python3 ex07_completo_regular.py
python3 ex08_grafo_transposto.py
python3 ex09_validar_lista.py
python3 ex10_amigos_em_comum.py
```

No Windows, use `py` ou `python` no lugar de `python3`. Todos os arquivos
também rodam colados no [playground Python](https://www.onlineide.pro/playground/python).

### C

```bash
cd c
make            # compila as cinco soluções
./ex06
./ex07
./ex08
./ex09
./ex10
```

Os programas compilam sem avisos com `-std=c11 -Wall -Wextra -pedantic`, a
saída é idêntica à da versão em Python, e eles também podem ser colados no
[playground C](https://www.onlineide.pro/playground/c).

---

Prof. Filipo Novo Mór — 2026 — [filipomor.com](https://filipomor.com)
