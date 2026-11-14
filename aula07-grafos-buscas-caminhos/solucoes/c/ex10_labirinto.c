/*
 * ex10_labirinto.c — Solução do Exercício 10 (Aula 7)
 *
 * O labirinto é um grafo IMPLÍCITO: cada casa livre é um vértice e há
 * aresta entre casas vizinhas (cima, baixo, esquerda, direita). A BFS a
 * partir de E dá o menor número de passos até S; pai[] desenha o caminho.
 * Cada casa (linha, coluna) vira o número linha * COLUNAS + coluna.
 *
 * Saída idêntica à da versão em Python. Só <stdio.h>.
 */
#include <stdio.h>

#define LINHAS 10
#define COLUNAS 10
#define CASAS (LINHAS * COLUNAS)

static char lab[LINHAS][COLUNAS + 1] = {
    "##########",
    "#E.....#.#",
    "#.##.###.#",
    "#.#..#...#",
    "#.#.####.#",
    "#...#..#.#",
    "###.#.##.#",
    "#.....#..#",
    "#.###...S#",
    "##########"
};
static const int MOV[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};  /* cima, baixo, esq, dir */

int acha(char letra) {
    int i, j;
    for (i = 0; i < LINHAS; i++)
        for (j = 0; j < COLUNAS; j++)
            if (lab[i][j] == letra) return i * COLUNAS + j;
    return -1;
}

void bfs_labirinto(int inicio, int dist[], int pai[]) {
    int fila[CASAS], ini = 0, fim = 0, c, k;
    for (c = 0; c < CASAS; c++) { dist[c] = -1; pai[c] = -1; }
    dist[inicio] = 0;
    fila[fim++] = inicio;
    while (ini < fim) {
        int u = fila[ini++];
        int i = u / COLUNAS, j = u % COLUNAS;
        for (k = 0; k < 4; k++) {       /* os vizinhos são calculados na hora */
            int ni = i + MOV[k][0], nj = j + MOV[k][1];
            int v = ni * COLUNAS + nj;
            if (lab[ni][nj] != '#' && dist[v] == -1) {
                dist[v] = dist[u] + 1;
                pai[v] = u;
                fila[fim++] = v;
            }
        }
    }
}

int main(void) {
    int dist[CASAS], pai[CASAS], e = acha('E'), s = acha('S'), c, u, alcancaveis = 0, i;

    bfs_labirinto(e, dist, pai);
    if (dist[s] == -1) {
        printf("Nao ha caminho da entrada ate a saida.\n");
        return 0;
    }
    for (c = 0; c < CASAS; c++) if (dist[c] != -1) alcancaveis++;
    printf("Menor caminho de E ate S: %d passos\n", dist[s]);
    printf("Casas alcancaveis a partir de E: %d\n\n", alcancaveis);

    for (u = pai[s]; u != e; u = pai[u])   /* marca o caminho, de trás para frente */
        lab[u / COLUNAS][u % COLUNAS] = '*';
    for (i = 0; i < LINHAS; i++) printf("   %s\n", lab[i]);
    return 0;
}
