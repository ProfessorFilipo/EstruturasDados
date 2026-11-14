/*
 * ex06_graus_separacao.c — Solução do Exercício 6 (Aula 7)
 *
 * BFS a partir de uma pessoa: dist[v] = graus de separação até v;
 * dist == 2 são os amigos de amigos; pai[] dá a cadeia de apresentações.
 * Mesma rede do Exercício 10 da Aula 6.
 *
 * Saída idêntica à da versão em Python. Só <stdio.h>.
 */
#include <stdio.h>

#define N 8
#define NAMIZADES 12

static const char *NOMES[N + 1] = {"", "Ana", "Bruno", "Carla", "Davi",
                                   "Elisa", "Fabio", "Gabi", "Hugo"};
static const int AMIZADES[NAMIZADES][2] = {
    {1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 5}, {3, 5}, {3, 6},
    {4, 5}, {4, 6}, {5, 7}, {6, 7}, {7, 8}
};

int viz[N + 1][N], grau[N + 1];

void criar_lista(void) {
    int i;
    for (i = 0; i < NAMIZADES; i++) {
        int u = AMIZADES[i][0], v = AMIZADES[i][1];
        viz[u][grau[u]++] = v;
        viz[v][grau[v]++] = u;
    }
}

void bfs(int s, int dist[], int pai[]) {
    int fila[N], ini = 0, fim = 0, v, k;
    for (v = 0; v <= N; v++) { dist[v] = -1; pai[v] = 0; }   /* -1 = não marcado */
    dist[s] = 0;
    fila[fim++] = s;
    while (ini < fim) {
        int u = fila[ini++];
        for (k = 0; k < grau[u]; k++) {
            int w = viz[u][k];
            if (dist[w] == -1) {
                dist[w] = dist[u] + 1;
                pai[w] = u;
                fila[fim++] = w;
            }
        }
    }
}

void imprimir_cadeia(const int pai[], int destino) {
    if (pai[destino] != 0) {            /* recursão: imprime primeiro o começo */
        imprimir_cadeia(pai, pai[destino]);
        printf(" -> ");
    }
    printf("%s", NOMES[destino]);
}

int main(void) {
    int dist[N + 1], pai[N + 1], v, origem = 1, longe = 1, primeiro = 1;

    criar_lista();
    bfs(origem, dist, pai);

    printf("1) Graus de separacao a partir de %s\n", NOMES[origem]);
    for (v = 1; v <= N; v++) printf("   %-6s %d\n", NOMES[v], dist[v]);

    printf("\n2) Amigos de amigos de %s (sugestoes): ", NOMES[origem]);
    for (v = 1; v <= N; v++)
        if (dist[v] == 2) { printf("%s%s", primeiro ? "" : ", ", NOMES[v]); primeiro = 0; }
    printf("\n");

    for (v = 2; v <= N; v++) if (dist[v] > dist[longe]) longe = v;
    printf("\n3) Pessoa mais distante: %s (%d graus)\n", NOMES[longe], dist[longe]);
    printf("   cadeia de apresentacoes: ");
    imprimir_cadeia(pai, longe);
    printf("\n");
    return 0;
}
