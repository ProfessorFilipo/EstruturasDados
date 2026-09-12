# Aula 2 — Pilhas e Filas

Estruturas de Dados — UniLasalle EAD — Grau 1

Códigos de apoio da Aula 2: os TADs Pilha e Fila, e um exemplo combinando
os dois (central de impressão) — em **C** e em **Python**.

## Estrutura desta pasta

```
c/
├── pilha.h / pilha.c              # TAD Pilha
├── fila.h / fila.c                # TAD Fila
├── demo_pilha.c                   # programa de demonstração — Pilha
├── demo_fila.c                    # programa de demonstração — Fila
├── central_impressao.c            # exemplo combinando Pilha + Fila
├── testes.c                       # suíte de testes (assert) de pilha.c e fila.c
└── Makefile
python/
├── pilha.py
├── fila.py
├── demo_pilha.py
├── demo_fila.py
├── central_impressao.py
└── testes.py
exercicios/
├── c/atividade_central_impressao.c
└── python/atividade_central_impressao.py
solucoes/
├── c/atividade_central_impressao.c
└── python/atividade_central_impressao.py
```

## Como executar

### C

```bash
cd c
make            # compila demo_pilha, demo_fila, central_impressao e testes
make test       # roda a suíte de testes (assert)
./demo_pilha
./demo_fila
./central_impressao
```

### Python

```bash
cd python
python3 demo_pilha.py
python3 demo_fila.py
python3 central_impressao.py
python3 testes.py
```

---

Prof. Filipo Novo Mór — 2026 — [filipomor.com](https://filipomor.com)
