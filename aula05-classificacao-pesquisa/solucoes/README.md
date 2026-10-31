# Soluções — Exercícios Guiados da Aula 5

Gabarito de referência para [`exercicios/exercicios-aula05.md`](../exercicios/exercicios-aula05.md).

## Organização

```
solucoes/
├── conceituais/   # exercícios 1, 2, 4, 5, 6, 8 (resultados), 9, 10, 11 e 12
├── python/        # exercícios 3, 7, 8 e 13
└── c/             # exercícios 3, 7, 8 e 13 (com Makefile)
```

Os nomes dos arquivos seguem `exNN_descricao.{md,py,c}`, correspondendo ao
número do exercício no guia.

## Uma nota sobre o repositório público

Os gabaritos ficam visíveis junto com os enunciados. Para os exercícios de
rastreio (feitos no papel), o valor está em tentar **antes** de abrir a
solução — confira depois, rodando os arquivos da aula.

## Como executar

### Python

```bash
cd python
python3 ex03_buscar_primeira.py
python3 ex07_merge_sort_estavel.py
python3 ex08_quick_mediana_tres.py
python3 ex13_ordenar_automatico.py
```

No Windows, use `py` ou `python` no lugar de `python3`. Todos os arquivos
também rodam colados no [playground Python](https://www.onlineide.pro/playground/python).

### C

```bash
cd c
make            # compila as quatro soluções
./ex03
./ex07
./ex08
./ex13
```

Os programas compilam sem avisos com `-std=c11 -Wall -Wextra -pedantic` e
também podem ser colados no [playground C](https://www.onlineide.pro/playground/c).
Onde há dados sorteados, a versão em C usa um gerador próprio: os números
diferem um pouco dos da versão em Python, mas as conclusões são as mesmas.

---

Prof. Filipo Novo Mór — 2026 — [filipomor.com](https://filipomor.com)
