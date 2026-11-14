/*
 * ex07_completo_regular.c — Solução do Exercício 7 (Aula 6)
 *
 *   - completo: existe aresta entre TODO par de vértices distintos
 *   - regular:  todos os vértices têm o MESMO grau (devolve o grau, ou -1)
 *
 * Saída idêntica à da versão em Python. Só <stdio.h>.
 */
#include <stdio.h>

#define MAX 7

void criar_matriz(int m[MAX][MAX], int n, const int arestas[][2], int na) {
    int i, j;
    for (i = 0; i <= n; i++)
        for (j = 0; j <= n; j++) m[i][j] = 0;
    for (i = 0; i < na; i++) {
        int u = arestas[i][0], v = arestas[i][1];
        m[u][v] = m[v][u] = 1;
    }
}

int eh_completo(int m[MAX][MAX], int n) {
    int i, j;
    for (i = 1; i <= n; i++)
        for (j = 1; j <= n; j++)
            if (i != j && m[i][j] == 0) return 0;   /* achou um par sem aresta */
    return 1;
}

int grau(int m[MAX][MAX], int n, int v) {
    int j, g = 0;
    for (j = 1; j <= n; j++) g += m[v][j];
    return g;
}

int eh_regular(int m[MAX][MAX], int n) {
    int v, g = grau(m, n, 1);
    for (v = 2; v <= n; v++)
        if (grau(m, n, v) != g) return -1;
    return g;
}

void testar(const char *nome, int n, const int arestas[][2], int na) {
    int m[MAX][MAX], r;
    char reg[32];
    criar_matriz(m, n, arestas, na);
    r = eh_regular(m, n);
    if (r >= 0) sprintf(reg, "sim, grau %d", r);
    else sprintf(reg, "nao");
    printf("%-22s completo? %-4s regular? %s\n", nome, eh_completo(m, n) ? "sim" : "nao", reg);
}

int main(void) {
    static const int filial[10][2] = {
        {1, 2}, {1, 6}, {2, 3}, {2, 5}, {2, 6}, {3, 4}, {3, 5}, {3, 6}, {4, 5}, {5, 6}
    };
    static const int k4[6][2] = {{1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {3, 4}};
    static const int c5[5][2] = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 1}};

    testar("rede da filial (6)", 6, filial, 10);
    testar("K4 (completo, 4)", 4, k4, 6);
    testar("ciclo C5 (5)", 5, c5, 5);
    testar("K4 sem a aresta 1-2", 4, k4 + 1, 5);   /* pula o primeiro par (1,2) */
    return 0;
}
