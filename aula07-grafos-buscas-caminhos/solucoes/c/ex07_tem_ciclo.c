/*
 * ex07_tem_ciclo.c — Solução do Exercício 7 (Aula 7)
 *
 * Grafo NÃO dirigido tem ciclo se a DFS encontra um vizinho JÁ MARCADO
 * que não é o pai do vértice atual. Essa aresta "fecha" o ciclo.
 *
 * Saída idêntica à da versão em Python. Só <stdio.h>.
 */
#include <stdio.h>

#define MAX 8

typedef struct {
    int n;
    int viz[MAX][MAX];
    int grau[MAX];
} Grafo;

void criar_lista(Grafo *g, int n, const int arestas[][2], int na) {
    int i;
    g->n = n;
    for (i = 0; i <= n; i++) g->grau[i] = 0;
    for (i = 0; i < na; i++) {
        int u = arestas[i][0], v = arestas[i][1];
        g->viz[u][g->grau[u]++] = v;
        g->viz[v][g->grau[v]++] = u;
    }
}

/* devolve 1 se achou ciclo; a aresta que fecha vai para *a e *b */
int dfs_ciclo(const Grafo *g, int u, int pai, int marcado[], int *a, int *b) {
    int k;
    marcado[u] = 1;
    for (k = 0; k < g->grau[u]; k++) {
        int v = g->viz[u][k];
        if (!marcado[v]) {
            if (dfs_ciclo(g, v, u, marcado, a, b)) return 1;
        } else if (v != pai) {
            *a = u; *b = v;             /* v já visitado e não é o pai: ciclo! */
            return 1;
        }
    }
    return 0;
}

int tem_ciclo(const Grafo *g, int *a, int *b) {
    int marcado[MAX] = {0}, v;
    for (v = 1; v <= g->n; v++)         /* testa todas as componentes */
        if (!marcado[v] && dfs_ciclo(g, v, 0, marcado, a, b)) return 1;
    return 0;
}

void testar(const char *nome, int n, const int arestas[][2], int na) {
    Grafo g;
    int a, b;
    criar_lista(&g, n, arestas, na);
    if (tem_ciclo(&g, &a, &b))
        printf("%-28s tem ciclo: sim (fechado pela aresta %d-%d)\n", nome, a, b);
    else
        printf("%-28s tem ciclo: nao\n", nome);
}

int main(void) {
    static const int filial[10][2] = {
        {1, 2}, {1, 6}, {2, 3}, {2, 5}, {2, 6}, {3, 4}, {3, 5}, {3, 6}, {4, 5}, {5, 6}
    };
    static const int arvore_mais[6][2] = {          /* árvore + a aresta 4-6 no fim */
        {1, 2}, {1, 3}, {2, 4}, {2, 5}, {3, 6}, {4, 6}
    };
    static const int floresta[5][2] = {{1, 2}, {2, 3}, {4, 5}, {5, 6}, {5, 7}};

    testar("1) rede da filial", 6, filial, 10);
    testar("2) arvore com 6 vertices", 6, arvore_mais, 5);
    testar("3) floresta (duas arvores)", 7, floresta, 5);
    testar("4) arvore + aresta 4-6", 6, arvore_mais, 6);
    return 0;
}
