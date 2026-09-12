# Aula 3 — Estruturas Lineares (Consolidação) + Conjuntos

Estruturas de Dados — UniLasalle EAD — Grau 1

Última aula do bloco de Estruturas Lineares antes da prova do G1.
Consolida Lista, Pilha e Fila (já vistas nas Aulas 1 e 2) e traz o
conteúdo novo: o TAD Conjunto — em **C** e em **Python**.

## Estrutura desta pasta

```
revisao/
└── c/                      # Bloco 2: cópia dos demos de Lista/Pilha/Fila
    ├── contigua, encadeada (Aula 1)
    ├── demo_pilha, demo_fila (Aula 2)
    └── Makefile
c/
├── demo_conjunto.c         # Bloco 4: demo ao vivo — Conjunto sobre array
└── Makefile
python/
└── demo_conjunto.py        # Bloco 4: demo ao vivo — set() nativo
exercicios/
└── atividade_conjunto.py   # Bloco 5: atividade prática (com TODOs)
solucoes/
└── atividade_conjunto.py   # gabarito da atividade
```

## Sobre o Bloco 2 (consolidação de Lista, Pilha e Fila)

Esse bloco não traz código novo — é reexecução dos demos das Aulas 1 e
2, copiados para `revisao/c/` só por conveniência (evita abrir a pasta
de outra aula durante a apresentação). O código-fonte de referência
continua sendo `aula01-estruturas-lineares/` e `aula02-pilhas-filas/`.

```bash
cd revisao/c
make
./contigua
./encadeada
./demo_pilha
./demo_fila
```

## Como executar os demos desta aula

### C

Todo o conteúdo de cada arquivo cabe em uma única tela — pensado para
colar direto no [OnlineIDE Pro — playground C](https://www.onlineide.pro/playground/c),
sem precisar de múltiplos arquivos.

Localmente, com `make`:

```bash
cd c
make
./demo_conjunto
```

### Python

Sem nenhum `import` de terceiros — cole direto no
[OnlineIDE Pro — playground Python](https://www.onlineide.pro/playground/python).

```bash
cd python
python3 demo_conjunto.py
```

## Atividade prática

`exercicios/atividade_conjunto.py` implementa um Conjunto do zero (sem
usar o `set()` nativo), replicando em Python a lógica vista em C —
mesmo formato das atividades anteriores: complete os trechos marcados
com `# TODO`, o `main()` já mostra o resultado esperado. Gabarito em
`solucoes/atividade_conjunto.py`.

---

Prof. Filipo Novo Mór — 2026 — [filipomor.com](https://filipomor.com)
