# Campo Minado — esqueleto da atividade prática

Estruturas de Dados — UniLasalle EAD — Grau 1 — Aula 4

Atividade de **prática, sem entrega**: você vai completar a lógica de um
Campo Minado usando as estruturas das Aulas 1 a 3 e analisar o custo de
cada parte com o que vimos na Aula 4. O enunciado completo está no PDF
da atividade, e as regras do jogo e as técnicas estão explicadas no
capítulo "Campo Minado" da apostila da Aula 4.

## Como começar

1. Abra esta pasta no PyCharm (ou no Thonny) — veja o passo a passo no
   enunciado.
2. Rode `python jogo_gui.py`. A janela já abre, mas ao clicar aparece
   "Falta implementar: TODO 1": é por aí que você começa.
3. Complete os TODOs **em ordem**, em `tabuleiro.py` e `ranking.py`.
4. Depois de cada TODO, rode os testes para conferir:

```bash
python testes.py
```

No começo, quase todos os testes falham com `NotImplementedError`.
Conforme você avança, eles passam a mostrar `ok`.

**Só IDE online?** Use `campo_minado_arquivo_unico.py` (versão de texto,
num único arquivo): cole no
[OnlineIDE Pro — playground Python](https://www.onlineide.pro/playground/python)
e procure por `TODO`.

## Os TODOs

| TODO | Arquivo | O que fazer | Aula |
|:-:|---|---|:-:|
| 1 | `tabuleiro.py` | `indice()`: (linha, coluna) → posição na lista | 1 |
| 2 | `tabuleiro.py` | `coordenadas()`: posição na lista → (linha, coluna) | 1 |
| 3 | `tabuleiro.py` | `vizinhos()`: as até 8 vizinhas, respeitando as bordas | 1 |
| 4 | `tabuleiro.py` | `_posicionar_minas()`: sorteio sem repetição com o Conjunto | 3 |
| 5 | `tabuleiro.py` | `_calcular_numeros()`: percorrer as minas, somando nas vizinhas | 4 |
| 6 | `tabuleiro.py` | `_abrir_a_partir_de()`: abertura em cascata com Fila ou Pilha | 2 |
| 7 | `tabuleiro.py` | `_revelar()`: regras da jogada (derrota, abertura, vitória) | — |
| 8 | `tabuleiro.py` | `_alternar_bandeira()`: marcar/desmarcar e registrar no histórico | 2, 3 |
| 9 | `tabuleiro.py` | `_desfazer()`: desfazer a bandeira do topo da Pilha | 2 |
| 10 | `tabuleiro.py` | `ultimas_jogadas()`: consultar a Pilha sem remover | 2 |
| 11 | `ranking.py` | `inserir_ordenado()`: um passo do Insertion Sort | 4 |
| 12 | `ranking.py` | `ordenar_por_insercao()`: o Insertion Sort completo | 4 |

Os TODOs 4 e 5 são testados juntos (o sorteio termina chamando o cálculo
dos números), e o mesmo vale para o 6 e o 7 (a abertura é usada pela
jogada "revelar").

Os arquivos `estruturas.py`, `jogo_terminal.py`, `jogo_gui.py`,
`testes.py` e `analise_complexidade.py` já vêm prontos: você não precisa
alterá-los. Quando todos os testes passarem, rode
`python analise_complexidade.py` para responder à Parte D.

## Regras desta atividade

- No `tabuleiro.py`, não use `set()`, `collections.deque` nem
  `queue.Queue`: use a `Pilha`, a `Fila` e o `Conjunto` de `estruturas.py`.
- Não mude os nomes nem os parâmetros dos métodos: as interfaces e os
  testes dependem deles.

## Travou?

A solução de exemplo, completa e comentada, está em
[`../../solucoes/campo_minado/`](../../solucoes/campo_minado/), junto com
o gabarito das Partes A e D (`GABARITO.md`). Como não há entrega, ela é
de livre consulta — mas você aprende muito mais se tentar primeiro.

---

Prof. Filipo Novo Mór — 2026 — [filipomor.com](https://filipomor.com)
