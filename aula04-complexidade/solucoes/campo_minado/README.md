# Campo Minado — solução de exemplo

Estruturas de Dados — UniLasalle EAD — Grau 1 — Aula 4

Implementação completa e comentada da atividade prática da Aula 4. A
atividade **não tem entrega**: esta solução está aqui para você estudar,
comparar com a sua e tirar dúvidas.

> **Sugestão:** tente primeiro o esqueleto, em
> [`../../exercicios/campo_minado/`](../../exercicios/campo_minado/), e só
> depois abra estes arquivos. Nesta pasta, cada trecho que era um TODO no
> esqueleto está marcado com o comentário `# TODO n (resolvido)` — use
> esses marcadores para comparar as duas versões.

As regras do jogo e a explicação de cada técnica usada aqui estão no
capítulo **"Campo Minado: regras do jogo e técnicas de implementação"**
da apostila da Aula 4.

## Como rodar

Requer Python 3.10 ou mais novo. Usa só a biblioteca padrão — nada para
instalar com `pip`.

```bash
python jogo_gui.py                    # interface gráfica (tkinter)
python jogo_terminal.py               # interface de texto
python testes.py                      # testes automáticos (29 testes)
python analise_complexidade.py        # medições da Parte D
```

No Windows, use `python` ou `py`; no macOS e no Linux, `python3`. No
PyCharm, basta abrir a pasta, clicar com o botão direito no arquivo e
escolher **Run**.

- **Linux:** se aparecer `No module named 'tkinter'`, instale o pacote
  do sistema (`sudo apt install python3-tk` no Ubuntu/Debian).
- **Só IDE online?** Use `campo_minado_arquivo_unico.py`: é a versão de
  texto com todo o código num único arquivo, para colar no
  [OnlineIDE Pro — playground Python](https://www.onlineide.pro/playground/python).
  A interface gráfica não funciona em IDEs online.

## Ordem de leitura sugerida

| # | Arquivo | O que observar |
|:-:|---|---|
| 1 | `estruturas.py` | Pilha, Fila e Conjunto das Aulas 2 e 3, com a mesma interface. Repare no `pertence()` do Conjunto: um laço explícito, que conta cada comparação. |
| 2 | `tabuleiro.py` | O coração do jogo. Leia na ordem: endereçamento (TODOs 1–3), sorteio e números (4–5), abertura em cascata (6), jogadas (7–10). Cada método informa o seu custo. |
| 3 | `ranking.py` | Inserção ordenada (um passo do Insertion Sort) e o Insertion Sort completo ao carregar o arquivo — que cai no melhor caso. |
| 4 | `jogo_terminal.py` | Uma interface que só lê comandos, chama o `Tabuleiro` e desenha o resultado. Nenhuma regra do jogo aqui. |
| 5 | `jogo_gui.py` | A mesma ideia com tkinter: funções chamadas quando há um clique (eventos), `after()` para o relógio e a animação. |
| 6 | `testes.py` | Como verificar automaticamente cada regra, inclusive o tabuleiro da Parte A. |
| 7 | `analise_complexidade.py` | Cada técnica medida contra uma alternativa ingênua. |
| 8 | `GABARITO.md` | Respostas comentadas das Partes A e D. |

## Onde cada aula aparece

| Aula | Conceito | Onde |
|:-:|---|---|
| 1 | Lista contígua, acesso por índice O(1) | `numeros` e `reveladas` em `tabuleiro.py`; `indice()` e `coordenadas()` |
| 2 | Fila encadeada (FIFO) | abertura em cascata "em ondas" — `_abrir_a_partir_de()` |
| 2 | Pilha contígua (LIFO) | abertura "em profundidade" e histórico de jogadas — `_desfazer()` |
| 3 | Conjunto sem duplicatas | sorteio das minas e bandeiras — `_posicionar_minas()` |
| 4 | Contagem de operações, O/Ω/Θ, melhor e pior caso | `ContadorOperacoes`, custos nas docstrings, `ranking.py`, `analise_complexidade.py` |

## No jogo, experimente

- **Menu Análise → Abrir com Pilha** e **Numerar a ordem de abertura**:
  clique numa área vazia e compare com a Fila. As células são as mesmas;
  a ordem, não.
- Observe o **painel de análise** a cada jogada: o primeiro clique custa
  bem mais que os outros (sorteio das minas + cálculo dos números +
  abertura).
- Marque uma bandeira e tecle **Ctrl+Z**. Depois revele uma célula e
  tente Ctrl+Z de novo: o topo da Pilha agora é um "revelar", que não
  tem volta.

## Ideias para ir além (opcional)

- **Abertura por acorde:** clicar num número já aberto abre as vizinhas,
  se a quantidade de bandeiras em volta for igual ao número.
- **Bandeiras em O(1):** trocar o Conjunto de bandeiras por uma lista de
  booleanos e medir a diferença com o `analise_complexidade.py`.
- **Sorteio por embaralhamento (Fisher–Yates):** implementar e comparar
  as comparações com o sorteio atual, principalmente com muitas minas.
- **Nível personalizado** na interface gráfica.

---

Prof. Filipo Novo Mór — 2026 — [filipomor.com](https://filipomor.com)
