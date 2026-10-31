# Exercício 8 — Quicksort com mediana de três (resultados e pergunta)

O código está em `../python/ex08_quick_mediana_tres.py` e
`../c/ex08_quick_mediana_tres.c`. Resultados do Python (n = 500, semente 2026):

| cenário | pivô = último | mediana de três |
|---|---|---|
| aleatório | 4.558 | 3.990 |
| já ordenado | **124.750** | 3.498 |
| ordem inversa | **124.750** | 6.018 |

(Na versão em C, a linha "aleatório" muda um pouco, porque os números
sorteados vêm de outro gerador.)

**Por que funciona?** Com o vetor já ordenado ou invertido, o último
elemento é sempre o maior ou o menor de todos — o pior pivô possível, que
tira só um elemento do problema a cada partição (n níveis, n(n − 1)/2
comparações). A mediana de três olha também o elemento do **meio**, que
nesses dois cenários é exatamente a mediana: a partição divide o vetor ao
meio, e o custo volta para a casa de n log n.

No cenário "inverso" o número é um pouco maior que no "ordenado" porque as
trocas da partição bagunçam a parte da direita, e as medianas escolhidas
nas chamadas seguintes já não são perfeitas — mas o resultado continua
muito longe do pior caso.
