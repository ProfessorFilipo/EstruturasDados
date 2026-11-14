/*
 * p2_graus.c
 *
 * Estruturas de Dados — Aula 6 — Prática P2 (Grau dos vértices)
 * Slides 13 e 14 (teoria) e 29 (prática) · versão em C de python/p2_graus.py
 *
 * Na matriz de adjacências:
 *   - grafo NÃO dirigido: grau(v) = soma da linha v
 *   - dígrafo: grau de SAÍDA(v)   = soma da linha v   (setas que saem de v)
 *              grau de ENTRADA(v) = soma da coluna v  (setas que chegam em v)
 *
 * Lema do aperto de mãos: num grafo não dirigido, a soma dos graus é
 * 2 x |E|, porque cada aresta tem duas pontas.
 *
 * A saída é idêntica à da versão em Python.
 * Arquivo único, só <stdio.h> — cole direto no onlineide.pro/playground/c
 */
#include <stdio.h>

#define N 6
#define NARESTAS 10

static const int ARESTAS[NARESTAS][2] = {
    {1, 2}, {1, 6}, {2, 3}, {2, 5}, {2, 6},
    {3, 4}, {3, 5}, {3, 6}, {4, 5}, {5, 6}
};

void criar_matriz(int m[N + 1][N + 1], int dirigido) {
    int i, j;
    for (i = 0; i <= N; i++)
        for (j = 0; j <= N; j++)
            m[i][j] = 0;
    for (i = 0; i < NARESTAS; i++) {
        int u = ARESTAS[i][0], v = ARESTAS[i][1];
        m[u][v] = 1;
        if (!dirigido) m[v][u] = 1;
    }
}

/* ------------------------------------------------------------------ */
/* Versões "limpas", idênticas às do slide.                            */
/* ------------------------------------------------------------------ */
int grau(int m[N + 1][N + 1], int v) {          /* soma da linha v */
    int j, g = 0;
    for (j = 1; j <= N; j++) g += m[v][j];
    return g;
}

int grau_saida(int m[N + 1][N + 1], int v) {    /* soma da linha v */
    int j, g = 0;
    for (j = 1; j <= N; j++) g += m[v][j];
    return g;
}

int grau_entrada(int m[N + 1][N + 1], int v) {  /* soma da coluna v */
    int i, g = 0;
    for (i = 1; i <= N; i++) g += m[i][v];
    return g;
}

/* imprime um vetor no formato de lista do Python: [1, 2, 3] */
void imprimir_vetor(const int v[], int n) {
    int i;
    printf("[");
    for (i = 0; i < n; i++) printf("%s%d", i > 0 ? ", " : "", v[i]);
    printf("]");
}

int main(void) {
    int m[N + 1][N + 1], d[N + 1][N + 1];
    int v, k, soma = 0, maior = 0;
    int lista[N], qtd = 0;
    int fontes[N], nf = 0, sumidouros[N], ns = 0;
    int soma_saida = 0, soma_entrada = 0;

    /* ---------------- Parte 1: grafo não dirigido ---------------- */
    criar_matriz(m, 0);
    printf("1) Rede da filial (NAO DIRIGIDO): grau de cada roteador\n");
    for (v = 1; v <= N; v++) {
        int g = grau(m, v);
        soma += g;
        if (g > maior) maior = g;
        printf("   grau(%d) = %d  ", v, g);
        for (k = 0; k < g; k++) printf("#");
        printf("\n");
    }
    printf("   soma dos graus = %d   2 x |E| = 2 x %d = %d\n", soma, NARESTAS, 2 * NARESTAS);
    printf("   aperto de maos confere? %s\n", soma == 2 * NARESTAS ? "sim" : "NAO");
    for (v = 1; v <= N; v++)
        if (grau(m, v) == maior) lista[qtd++] = v;
    printf("   roteadores mais conectados (grau %d): ", maior);
    imprimir_vetor(lista, qtd);
    printf("\n");

    /* ---------------- Parte 2: o mesmo desenho como dígrafo ---------------- */
    criar_matriz(d, 1);
    printf("\n2) Mesmas arestas como DIGRAFO (cada par (u, v) vira u -> v)\n");
    printf("   vertice  saida  entrada\n");
    for (v = 1; v <= N; v++) {
        int gs = grau_saida(d, v), ge = grau_entrada(d, v);
        soma_saida += gs;
        soma_entrada += ge;
        if (ge == 0) fontes[nf++] = v;          /* ninguém aponta para v */
        if (gs == 0) sumidouros[ns++] = v;      /* v não aponta para ninguém */
        printf("   %7d  %5d  %7d\n", v, gs, ge);
    }
    printf("   soma das saidas = %d, soma das entradas = %d, |E| = %d\n",
           soma_saida, soma_entrada, NARESTAS);
    printf("   fontes (entrada 0): ");
    imprimir_vetor(fontes, nf);
    printf("    sumidouros (saida 0): ");
    imprimir_vetor(sumidouros, ns);
    printf("\n");
    return 0;
}
