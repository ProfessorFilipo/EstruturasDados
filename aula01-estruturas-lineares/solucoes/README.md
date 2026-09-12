# Soluções — Exercícios Guiados da Aula 1

Gabarito de referência para [`exercicios/exercicios-aula01.md`](../exercicios/exercicios-aula01.md).

## Organização

```
solucoes/
├── c/             # exercícios 1, 5, 6, 8, 9, 11, 12, 13, 14
├── python/        # exercícios 2, 5, 7, 8, 10, 11, 12, 13, 14
└── conceituais/   # exercícios 3, 4 e 15 (sem código)
```

Os nomes dos arquivos seguem `exNN_descricao.{c,py}`, correspondendo ao
número do exercício no guia.

## Uma nota sobre uso em sala/no repositório público

Este repositório é público, então os gabaritos ficam visíveis junto com
os enunciados. Isso é intencional — mas vale considerar:

- Para os exercícios 6, 7, 9 e 10 (implementar "do zero"), o valor
  pedagógico está em tentar **antes** de olhar aqui. Isso já está
  avisado no guia de exercícios, mas repetir na aula não faz mal.
- Se preferir controlar quando os gabaritos ficam visíveis (por
  exemplo, só depois do prazo de entrega), duas opções sem sair do
  GitHub: mover esta pasta para uma **branch separada** (`solucoes`,
  não mergeada na `main` até a data certa), ou torná-la **privada**
  temporariamente em um repositório separado. Nenhuma das duas eu fiz
  aqui — os arquivos estão prontos, a decisão de quando/como publicar
  é sua.

## Como executar

### C

```bash
cd c
make            # compila todas as soluções
./ex01          # roda uma específica
```

Alguns exercícios (12 e 14) evitam incluir `lista_contigua.h` e
`lista_encadeada.h` no mesmo arquivo — os dois reutilizam os mesmos
nomes de função para tipos diferentes, o que causa erro de compilação
(e também de linkagem, já que as implementações têm símbolos globais
com os mesmos nomes) se usados juntos no mesmo executável. Esses dois
exercícios usam uma implementação local mínima para o lado que não é
incluído via header — o comentário no topo de cada arquivo explica.

### Python

```bash
cd python
python3 ex02_referencias_compartilhadas.py
```

Os exercícios que reaproveitam `ListaContigua`/`ListaEncadeada` do
repositório (5, 8, 11, 12, 13, 14) importam automaticamente de
`../../python/` — não precisa configurar nada, só rodar o arquivo.

---

Prof. Filipo Novo Mór — 2026 — [filipomor.com](https://filipomor.com)
