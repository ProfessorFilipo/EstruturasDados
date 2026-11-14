/*
 * p1_matriz_adjacencias.c
 *
 * Estruturas de Dados — Aula 6 — Prática P1 (Matriz de adjacências)
 * Slides 21 (teoria) e 28 (prática) · versão em C de python/p1_matriz_adjacencias.py
 *
 * A "rede da filial": 6 roteadores ligados por 10 cabos — o mesmo grafo do
 * livro de Ascencio & Araújo (cap. 8, p. 391).
 *
 * Matriz de adjacências M (n x n):
 *     M[u][v] = 1  se existe a aresta (u, v)
 *     M[u][v] = 0  caso contrário
 * Os vértices vão de 1 a n, como no livro: a linha 0 e a coluna 0 ficam
 * sem uso (por isso a matriz é declarada com N + 1).
 *
 * Experimente: troque DIRIGIDO 0 por 1 e rode de novo.
 * A saída é idêntica à da versão em Python.
 *
 * Arquivo único, só <stdio.h> — cole direto no onlineide.pro/playground/c
 */
#include <stdio.h>

#define N 6                     /* número de vértices (roteadores) */
#define NARESTAS 10
#define DIRIGIDO 0              /* 1: cada par (u, v) vira a seta u -> v */

static const int ARESTAS[NARESTAS][2] = {
    {1, 2}, {1, 6}, {2, 3}, {2, 5}, {2, 6},
    {3, 4}, {3, 5}, {3, 6}, {4, 5}, {5, 6}
};

/* ------------------------------------------------------------------ */
/* Versão "limpa", idêntica à do slide.                                */
/* ------------------------------------------------------------------ */
void criar_matriz(int m[N + 1][N + 1], int dirigido) {
    int i, j;
    for (i = 0; i <= N; i++)            /* começa tudo com 0 */
        for (j = 0; j <= N; j++)
            m[i][j] = 0;
    for (i = 0; i < NARESTAS; i++) {
        int u = ARESTAS[i][0], v = ARESTAS[i][1];
        m[u][v] = 1;
        if (!dirigido)
            m[v][u] = 1;                /* não dirigido: vale nos dois sentidos */
    }
}

void imprimir_matriz(int m[N + 1][N + 1]) {
    int i, j;
    printf("      ");
    for (j = 1; j <= N; j++) printf("%s%2d", j > 1 ? " " : "", j);
    printf("\n");
    for (i = 1; i <= N; i++) {
        printf("   %2d", i);
        for (j = 1; j <= N; j++) printf(" %2d", m[i][j]);
        printf("\n");
    }
}

int eh_simetrica(int m[N + 1][N + 1]) {
    int i, j;
    for (i = 1; i <= N; i++)
        for (j = i + 1; j <= N; j++)
            if (m[i][j] != m[j][i]) return 0;
    return 1;
}

int contar_uns(int m[N + 1][N + 1]) {
    int i, j, total = 0;
    for (i = 1; i <= N; i++)
        for (j = 1; j <= N; j++)
            total += m[i][j];
    return total;
}

int main(void) {
    int m[N + 1][N + 1];
    int consultas[3][2] = {{2, 5}, {1, 4}, {5, 2}};
    int k, uns;

    printf("1) Grafo %s: %d vertices e %d arestas\n",
           DIRIGIDO ? "DIRIGIDO" : "NAO DIRIGIDO", N, NARESTAS);
    criar_matriz(m, DIRIGIDO);
    imprimir_matriz(m);

    printf("\n2) A matriz e simetrica (M[i][j] == M[j][i])? %s\n",
           eh_simetrica(m) ? "sim" : "nao");

    uns = contar_uns(m);
    if (DIRIGIDO)
        printf("3) Quantidade de 1s: %d = |E| (cada seta marca 1 posicao)\n", uns);
    else
        printf("3) Quantidade de 1s: %d = 2 x |E| (cada aresta marca 2 posicoes)\n", uns);

    printf("\n4) Consultas diretas, custo O(1):\n");
    for (k = 0; k < 3; k++) {
        int u = consultas[k][0], v = consultas[k][1];
        printf("   existe aresta %d -> %d?  M[%d][%d] = %d  (%s)\n",
               u, v, u, v, m[u][v], m[u][v] == 1 ? "sim" : "nao");
    }

    printf("\n5) Memoria: a matriz tem %d x %d = %d celulas uteis, mas so %d guardam 1.\n",
           N, N, N * N, uns);
    return 0;
}
