# Soluções — Exercícios Guiados da Aula 7

Gabarito de referência para [`exercicios/exercicios-aula07.md`](../exercicios/exercicios-aula07.md).

## Organização

```
solucoes/
├── conceituais/   # exercícios 1 a 5 (rastreios no papel)
├── python/        # exercícios 6 a 10
└── c/             # exercícios 6 a 10 (com Makefile)
```

Os nomes dos arquivos seguem `exNN_descricao.{md,py,c}`, correspondendo ao
número do exercício no guia.

| Exercício | Arquivo | Assunto |
|---|---|---|
| 1 | `conceituais/ex01_rastreio_bfs.md` | fila da BFS passo a passo |
| 2 | `conceituais/ex02_rastreio_dfs.md` | recursão da DFS e árvore DFS |
| 3 | `conceituais/ex03_ordem_dos_vizinhos.md` | o que muda com a ordem das listas |
| 4 | `conceituais/ex04_dijkstra_no_papel.md` | tabela de rodadas do Dijkstra |
| 5 | `conceituais/ex05_qual_algoritmo.md` | limites da BFS e do Dijkstra |
| 6 | `ex06_graus_separacao.{py,c}` | graus de separação (BFS) |
| 7 | `ex07_tem_ciclo.{py,c}` | detectar ciclo (DFS) |
| 8 | `ex08_dois_times.{py,c}` | grafo bipartido (BFS pintando) |
| 9 | `ex09_rota_cidades.{py,c}` | Dijkstra com nomes e rota |
| 10 | `ex10_labirinto.{py,c}` | BFS num grafo implícito (grade) |

## Uma nota sobre o repositório público

Os gabaritos ficam visíveis junto com os enunciados. Nos rastreios, o valor
está em montar a tabela **antes** de abrir a solução e conferir depois,
rodando os programas da pasta [`../python/`](../python/) com o seu grafo.

## Como executar

### Python

```bash
cd python
python3 ex06_graus_separacao.py
python3 ex07_tem_ciclo.py
python3 ex08_dois_times.py
python3 ex09_rota_cidades.py
python3 ex10_labirinto.py
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

Os tempos entre cidades do Exercício 9 são **ilustrativos**: servem para o
exercício, não para planejar viagem.

---

Prof. Filipo Novo Mór — 2026 — [filipomor.com](https://filipomor.com)
