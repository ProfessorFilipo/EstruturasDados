/*
 * ex09_validar_lista.c — Solução do Exercício 9 (Aula 6)
 *
 * Num grafo NÃO dirigido, se v está na lista de u, então u TEM de estar
 * na lista de v. A função imprime todos os pares quebrados.
 *
 * Lista de adjacências contígua: viz[u][0..grau[u]-1].
 * Saída idêntica à da versão em Python. Só <stdio.h>.
 */
#include <stdio.h>

#define MAX 7

typedef struct {
    int n;
    int viz[MAX][MAX];
    int grau[MAX];
} Grafo;

int esta_na_lista(const Grafo *g, int u, int x) {
    int k;
    for (k = 0; k < g->grau[u]; k++)
        if (g->viz[u][k] == x) return 1;
    return 0;
}

/* devolve quantos pares quebrados existem (e imprime cada um) */
int validar(const Grafo *g, const char *nome) {
    int u, k, quebrados = 0;
    for (u = 1; u <= g->n; u++)
        for (k = 0; k < g->grau[u]; k++) {
            int v = g->viz[u][k];
            if (!esta_na_lista(g, v, u)) {   /* u vê v, mas v não vê u */
                printf("%s: %d esta na lista de %d, mas %d NAO esta na lista de %d\n",
                       nome, v, u, u, v);
                quebrados++;
            }
        }
    if (quebrados == 0) printf("%s: lista consistente\n", nome);
    return quebrados;
}

int main(void) {
    Grafo filial = {6,
        {{0}, {2, 6}, {1, 3, 5, 6}, {2, 4, 5, 6}, {3, 5}, {2, 3, 4, 6}, {1, 2, 3, 5}},
        {0, 2, 4, 4, 2, 4, 4}};
    Grafo torta = {4,
        {{0}, {2, 4}, {1, 3}, {2}, {1, 3}},
        {0, 2, 2, 1, 2}};
    Grafo esqueceu = {3,                /* o código esqueceu a 2a inserção em 1-2 */
        {{0}, {2, 3}, {0}, {1}},
        {0, 2, 0, 1}};

    validar(&filial, "1) rede da filial");
    validar(&torta, "2) lista do enunciado");
    validar(&esqueceu, "3) segunda insercao esquecida");
    return 0;
}
