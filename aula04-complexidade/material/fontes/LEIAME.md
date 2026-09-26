# Fontes dos materiais da Aula 4

Arquivos LaTeX da **apostila** e do **enunciado da atividade Campo Minado**.

| Arquivo ou pasta | Conteúdo |
|---|---|
| `Apostila_Aula04_Complexidade.tex` | arquivo principal da apostila (capa, sumário, "Como usar") |
| `capitulos/` | um arquivo por capítulo (`cap01.tex` a `cap16.tex`) e o apêndice |
| `Atividade_Pratica_Aula04_Campo_Minado.tex` | enunciado da atividade prática |
| `estilo-ed.sty` | modelo visual comum (cores, fontes, caixas, código, tabelas) |
| `figuras/` | gráficos, títulos pixelados e ilustrações |
| `tabelas/` | tabelas e saídas geradas pelos programas da pasta `python/` |

## Como compilar

- **Overleaf:** envie esta pasta inteira (ou o ZIP), abra o arquivo `.tex` desejado e
  mude o compilador para **XeLaTeX** (Menu > Compiler > XeLaTeX). Compile duas vezes
  para acertar o sumário, as referências e o "Página N de M".
- **No computador (TeX Live ou MiKTeX):**

```bash
xelatex Apostila_Aula04_Complexidade.tex
xelatex Apostila_Aula04_Complexidade.tex

xelatex Atividade_Pratica_Aula04_Campo_Minado.tex
xelatex Atividade_Pratica_Aula04_Campo_Minado.tex
```

Fontes usadas: Carlito (mesmas métricas da Calibri dos slides), DejaVu Sans Mono
(código), DejaVu Sans (símbolo ★) e Latin Modern Math (fórmulas) — todas incluídas
no TeX Live.
