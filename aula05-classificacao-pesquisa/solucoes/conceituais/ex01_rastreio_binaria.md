# Exercício 1 — Rastreando a busca binária

IDs: `101 104 105 109 112 113 118 121 125 126 130 134 137 141 142 150` (posições 0 a 15).

## (a) Buscando 126

| passo | inicio | meio | fim | v[meio] | decisão |
|---|---|---|---|---|---|
| 1 | 0 | 7 | 15 | 121 | 121 < 126 → `inicio = 8` |
| 2 | 8 | 11 | 15 | 134 | 134 > 126 → `fim = 10` |
| 3 | 8 | 9 | 10 | 126 | achou! |

**Resposta:** posição **9**, com **3 comparações**.

## (b) Buscando 100 (não existe)

| passo | inicio | meio | fim | v[meio] | decisão |
|---|---|---|---|---|---|
| 1 | 0 | 7 | 15 | 121 | 121 > 100 → `fim = 6` |
| 2 | 0 | 3 | 6 | 109 | 109 > 100 → `fim = 2` |
| 3 | 0 | 1 | 2 | 104 | 104 > 100 → `fim = 0` |
| 4 | 0 | 0 | 0 | 101 | 101 > 100 → `fim = -1` |

Agora `inicio` (0) é maior que `fim` (-1): o intervalo ficou vazio e a
função devolve **-1**, depois de **4 comparações**. Repare que o alvo é
menor que todos, então a busca sempre descarta a metade da direita.
