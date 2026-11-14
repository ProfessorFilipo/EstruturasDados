# Exercício 3 — Grafos regulares

**(a) Não existe.** Num grafo 3-regular com 7 vértices, a soma dos graus
seria 7 × 3 = 21, um número ímpar. Pelo lema do aperto de mãos, essa soma é
sempre `2 × |E|`, um número par. Contradição: tal grafo não existe.

**(b)** Duas respostas possíveis (há outras):

- o **prisma triangular**: dois triângulos (1-2-3 e 4-5-6) mais as
  arestas 1-4, 2-5 e 3-6;
- o **bipartido completo K₃,₃**: {1, 2, 3} ligados a todos de {4, 5, 6}.

Em ambos, cada vértice tem grau 3, e há 9 arestas (6 × 3 / 2).

**(c)** Soma dos graus = `n × r` = `2 × |E|`, logo **|E| = n·r / 2**.
Consequência: se `n` e `r` forem ambos ímpares, o grafo não existe.

**(d)** Sim. Em `Kₙ` cada vértice está ligado a todos os outros `n − 1`:
é **(n−1)-regular**. Pela fórmula do item (c), tem `n(n−1)/2` arestas.
