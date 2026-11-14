/*
 * p4_comparando_representacoes.c
 *
 * Estruturas de Dados — Aula 6 — Prática P4 (Matriz x Lista)
 * Slides 23 (teoria) e 31 (prática) · versão em C de python/p4_comparando_representacoes.py
 *
 * Três perguntas para decidir entre matriz e lista de adjacências:
 *   1. "u e v são vizinhos?"   matriz: O(1)       lista: O(grau(u))
 *   2. "quem são os vizinhos?" matriz: O(V)       lista: O(grau(u))
 *   3. "quanta memória?"       matriz: V x V      lista: V + 2 x E
 *
 * Para manter o código curto, aqui a lista de adjacências é CONTÍGUA (um
 * vetor de vizinhos por vértice, como a lista contígua da Aula 1); a versão
 * encadeada está em p3_lista_adjacencias.c.
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

/* Lista de adjacências contígua: viz[u][0..grau[u]-1] */
typedef struct {
    int viz[N + 1][N];
    int grau[N + 1];
} ListaAdj;

void criar_matriz(int m[N + 1][N + 1]) {
    int i, j;
    for (i = 0; i <= N; i++)
        for (j = 0; j <= N; j++) m[i][j] = 0;
    for (i = 0; i < NARESTAS; i++) {
        int u = ARESTAS[i][0], v = ARESTAS[i][1];
        m[u][v] = m[v][u] = 1;
    }
}

void criar_lista(ListaAdj *g) {
    int i;
    for (i = 0; i <= N; i++) g->grau[i] = 0;
    for (i = 0; i < NARESTAS; i++) {
        int u = ARESTAS[i][0], v = ARESTAS[i][1];
        g->viz[u][g->grau[u]++] = v;
        g->viz[v][g->grau[v]++] = u;
    }
}

/* ------------------------------------------------------------------ */
/* Versões "limpas", idênticas às do slide.                            */
/* ------------------------------------------------------------------ */
int vizinhos_matriz(int m[N + 1][N + 1], int u, int v) {
    return m[u][v] == 1;                /* um acesso direto: O(1) */
}

int vizinhos_lista(const ListaAdj *g, int u, int v) {
    int k;
    for (k = 0; k < g->grau[u]; k++)    /* percorre a lista de u: O(grau(u)) */
        if (g->viz[u][k] == v) return 1;
    return 0;
}

void matriz_para_lista(int m[N + 1][N + 1], ListaAdj *g) {
    int u, v;
    for (u = 0; u <= N; u++) g->grau[u] = 0;
    for (u = 1; u <= N; u++)
        for (v = 1; v <= N; v++)        /* varre a linha inteira: O(V) por vértice */
            if (m[u][v] == 1) g->viz[u][g->grau[u]++] = v;
}

void lista_para_matriz(const ListaAdj *g, int m[N + 1][N + 1]) {
    int u, k, j;
    for (u = 0; u <= N; u++)
        for (j = 0; j <= N; j++) m[u][j] = 0;
    for (u = 1; u <= N; u++)
        for (k = 0; k < g->grau[u]; k++) m[u][g->viz[u][k]] = 1;
}

/* Versão da busca na lista que conta os passos (para a demonstração). */
int vizinhos_lista_contando(const ListaAdj *g, int u, int v, int *passos) {
    int k;
    *passos = 0;
    for (k = 0; k < g->grau[u]; k++) {
        (*passos)++;
        if (g->viz[u][k] == v) return 1;
    }
    return 0;
}

int matrizes_iguais(int a[N + 1][N + 1], int b[N + 1][N + 1]) {
    int i, j;
    for (i = 0; i <= N; i++)
        for (j = 0; j <= N; j++)
            if (a[i][j] != b[i][j]) return 0;
    return 1;
}

/* imprime um inteiro grande no padrão brasileiro (1.234.567), alinhado à direita */
void imprimir_fmt(long long x, int largura) {
    char buf[32], saida[40];
    int len, i, j = 0, k;
    len = sprintf(buf, "%lld", x);
    for (i = 0; i < len; i++) {
        if (i > 0 && (len - i) % 3 == 0) saida[j++] = '.';
        saida[j++] = buf[i];
    }
    saida[j] = '\0';
    for (k = j; k < largura; k++) printf(" ");
    printf("%s", saida);
}

int main(void) {
    int m[N + 1][N + 1], m2[N + 1][N + 1], m3[N + 1][N + 1];
    ListaAdj adj, adj2;
    int consultas[3][2] = {{2, 6}, {1, 4}, {4, 5}};
    int k, v, i;
    const char *nomes[3] = {"rede da filial", "campus (1 cabo por PC)", "rede social (50 amigos)"};
    long long vs[3] = {6, 1000, 1000000};
    long long es[3] = {10, 1500, 25000000};

    criar_matriz(m);
    criar_lista(&adj);

    printf("1) 'u e v sao vizinhos?' nas duas representacoes\n");
    for (k = 0; k < 3; k++) {
        int u = consultas[k][0], w = consultas[k][1], passos;
        int r_m = vizinhos_matriz(m, u, w);
        int r_l = vizinhos_lista_contando(&adj, u, w, &passos);
        if (r_m != r_l || r_l != vizinhos_lista(&adj, u, w)) return 1;
        printf("   (%d,%d): %s   matriz: 1 acesso   lista: %d passo(s)\n",
               u, w, r_m ? "sim" : "nao", passos);
    }

    printf("\n2) Convertendo uma na outra\n");
    matriz_para_lista(m, &adj2);
    for (v = 1; v <= N; v++) {
        printf("   %d: [", v);
        for (k = 0; k < adj2.grau[v]; k++) printf("%s%d", k > 0 ? ", " : "", adj2.viz[v][k]);
        printf("]\n");
    }
    lista_para_matriz(&adj2, m3);
    printf("   matriz -> lista -> matriz volta igual? %s\n", matrizes_iguais(m3, m) ? "sim" : "nao");
    lista_para_matriz(&adj, m2);
    printf("   lista -> matriz confere com a original? %s\n", matrizes_iguais(m2, m) ? "sim" : "nao");

    printf("\n3) Memoria (celulas) em tres cenarios\n");
    printf("   %-26s%20s%16s\n", "cenario", "matriz V x V", "lista V + 2E");
    for (i = 0; i < 3; i++) {
        printf("   %-26s", nomes[i]);
        imprimir_fmt(vs[i] * vs[i], 20);
        imprimir_fmt(vs[i] + 2 * es[i], 16);
        printf("\n");
    }
    printf("   -> grafo ESPARSO (poucas arestas): lista. Grafo DENSO: matriz.\n");
    return 0;
}
