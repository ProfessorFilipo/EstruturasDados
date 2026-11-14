/*
 * ex06_contar_arestas.c — Solução do Exercício 6 (Aula 6)
 *
 * Contar as arestas a partir da matriz de adjacências e detectar laços.
 *   - dígrafo:      cada 1 da matriz é uma seta -> |E| = total de 1s
 *   - não dirigido: cada aresta aparece duas vezes, EXCETO o laço (só na
 *                   diagonal). Contamos o triângulo de cima, com a diagonal.
 *
 * Saída idêntica à da versão em Python. Só <stdio.h>.
 */
#include <stdio.h>

#define MAX 7                           /* até 6 vértices (índices 1..6) */

void criar_matriz(int m[MAX][MAX], int n, const int arestas[][2], int na, int dirigido) {
    int i, j;
    for (i = 0; i <= n; i++)
        for (j = 0; j <= n; j++) m[i][j] = 0;
    for (i = 0; i < na; i++) {
        int u = arestas[i][0], v = arestas[i][1];
        m[u][v] = 1;
        if (!dirigido) m[v][u] = 1;
    }
}

int contar_arestas(int m[MAX][MAX], int n, int dirigido) {
    int i, j, total = 0;
    for (i = 1; i <= n; i++)
        for (j = dirigido ? 1 : i; j <= n; j++)   /* não dirigido: só j >= i */
            total += m[i][j];
    return total;
}

int tem_laco(int m[MAX][MAX], int n) {
    int v;
    for (v = 1; v <= n; v++)
        if (m[v][v] == 1) return 1;
    return 0;
}

void relatorio(const char *nome, int m[MAX][MAX], int n, int dirigido) {
    printf("%s: %d aresta(s), laco? %s\n", nome, contar_arestas(m, n, dirigido),
           tem_laco(m, n) ? "sim" : "nao");
}

int main(void) {
    static const int filial[11][2] = {
        {1, 2}, {1, 6}, {2, 3}, {2, 5}, {2, 6},
        {3, 4}, {3, 5}, {3, 6}, {4, 5}, {5, 6},
        {4, 4}                          /* o laço só entra no teste 3 */
    };
    static const int ida_e_volta[3][2] = {{1, 2}, {2, 1}, {2, 3}};
    int m[MAX][MAX];

    criar_matriz(m, 6, filial, 10, 0);
    relatorio("1) rede da filial (nao dirigido)", m, 6, 0);
    criar_matriz(m, 6, filial, 10, 1);
    relatorio("2) mesmas arestas como digrafo  ", m, 6, 1);
    criar_matriz(m, 6, filial, 11, 0);  /* o roteador 4 ganhou um cabo de loopback */
    relatorio("3) filial + laco em 4           ", m, 6, 0);
    criar_matriz(m, 3, ida_e_volta, 3, 1);
    relatorio("4) digrafo 1->2, 2->1, 2->3     ", m, 3, 1);
    return 0;
}
