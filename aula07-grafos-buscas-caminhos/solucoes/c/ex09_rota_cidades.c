/*
 * ex09_rota_cidades.c — Solução do Exercício 9 (Aula 7)
 *
 * Dijkstra O(V^2) com nomes: a rota mais rápida de Porto Alegre até cada
 * cidade da Região Metropolitana. Tempos (minutos) ILUSTRATIVOS.
 *
 * Saída idêntica à da versão em Python. Só <stdio.h>.
 */
#include <stdio.h>

#define N 8
#define NESTRADAS 10
#define INF 1000000000

static const char *CIDADES[N + 1] = {"", "Porto Alegre", "Canoas", "Esteio",
    "Sapucaia do Sul", "Sao Leopoldo", "Novo Hamburgo", "Cachoeirinha", "Gravatai"};
static const int ESTRADAS[NESTRADAS][3] = {
    {1, 2, 20}, {1, 7, 25}, {2, 3, 12}, {2, 7, 15}, {3, 4, 8},
    {4, 5, 10}, {5, 6, 15}, {7, 8, 12}, {8, 6, 50}, {3, 5, 22}
};

int viz[N + 1][N], peso[N + 1][N], grau[N + 1];

void criar_lista(void) {
    int i;
    for (i = 0; i < NESTRADAS; i++) {
        int u = ESTRADAS[i][0], v = ESTRADAS[i][1], w = ESTRADAS[i][2];
        viz[u][grau[u]] = v; peso[u][grau[u]++] = w;
        viz[v][grau[v]] = u; peso[v][grau[v]++] = w;
    }
}

void dijkstra(int s, int dist[], int pai[]) {
    int fechado[N + 1] = {0}, r, v, k;
    for (v = 0; v <= N; v++) { dist[v] = INF; pai[v] = 0; }
    dist[s] = 0;
    for (r = 0; r < N; r++) {
        int u = -1;
        for (v = 1; v <= N; v++)
            if (!fechado[v] && (u == -1 || dist[v] < dist[u])) u = v;
        if (dist[u] == INF) break;
        fechado[u] = 1;
        for (k = 0; k < grau[u]; k++) {
            int w = viz[u][k];
            if (!fechado[w] && dist[u] + peso[u][k] < dist[w]) {
                dist[w] = dist[u] + peso[u][k];
                pai[w] = u;
            }
        }
    }
}

void imprimir_rota(const int pai[], int destino) {
    if (pai[destino] != 0) {
        imprimir_rota(pai, pai[destino]);
        printf(" -> ");
    }
    printf("%s", CIDADES[destino]);
}

int main(void) {
    int dist[N + 1], pai[N + 1], ordem[N], i, j, origem = 1;

    criar_lista();
    dijkstra(origem, dist, pai);
    printf("Rotas mais rapidas a partir de %s (tempos ilustrativos)\n\n", CIDADES[origem]);

    for (i = 0; i < N; i++) ordem[i] = i + 1;
    for (i = 1; i < N; i++) {           /* insertion sort por dist (estável) */
        int x = ordem[i];
        for (j = i - 1; j >= 0 && dist[ordem[j]] > dist[x]; j--) ordem[j + 1] = ordem[j];
        ordem[j + 1] = x;
    }
    for (i = 0; i < N; i++) {
        int v = ordem[i];
        if (v == origem) continue;
        printf("%-16s%4d min   ", CIDADES[v], dist[v]);
        imprimir_rota(pai, v);
        printf("\n");
    }
    return 0;
}
