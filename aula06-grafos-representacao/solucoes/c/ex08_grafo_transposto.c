/*
 * ex08_grafo_transposto.c — Solução do Exercício 8 (Aula 6)
 *
 * "u segue v" é a seta u -> v. Para saber "quem ME segue", invertemos
 * todas as setas: é o grafo TRANSPOSTO. Na lista de adjacências, cada
 * seta u -> v vira v -> u. O grau de SAÍDA no transposto é o grau de
 * ENTRADA no original.
 *
 * Lista de adjacências contígua (um vetor de vizinhos por vértice).
 * Saída idêntica à da versão em Python. Só <stdio.h>.
 */
#include <stdio.h>

#define N 5
#define NSETAS 6

static const int SEGUE[NSETAS][2] = {{1, 2}, {1, 3}, {2, 3}, {3, 1}, {4, 3}, {5, 4}};

typedef struct {
    int viz[N + 1][N];
    int grau[N + 1];
} Grafo;

void criar_lista(Grafo *g) {
    int i;
    for (i = 0; i <= N; i++) g->grau[i] = 0;
    for (i = 0; i < NSETAS; i++) {
        int u = SEGUE[i][0], v = SEGUE[i][1];
        g->viz[u][g->grau[u]++] = v;
    }
}

void transposto(const Grafo *g, Grafo *t) {
    int u, k;
    for (u = 0; u <= N; u++) t->grau[u] = 0;
    for (u = 1; u <= N; u++)
        for (k = 0; k < g->grau[u]; k++) {
            int v = g->viz[u][k];
            t->viz[v][t->grau[v]++] = u;    /* u -> v vira v -> u */
        }
}

void imprimir_vetor(const int v[], int n) {
    int i;
    printf("[");
    for (i = 0; i < n; i++) printf("%s%d", i > 0 ? ", " : "", v[i]);
    printf("]");
}

void imprimir(const Grafo *g, const char *rotulo) {
    int v;
    for (v = 1; v <= N; v++) {
        printf("   perfil %d %s: ", v, rotulo);
        if (g->grau[v] == 0) printf("(ninguem)");
        else imprimir_vetor(g->viz[v], g->grau[v]);
        printf("\n");
    }
}

int iguais(const Grafo *a, const Grafo *b) {
    int v, k;
    for (v = 1; v <= N; v++) {
        if (a->grau[v] != b->grau[v]) return 0;
        for (k = 0; k < a->grau[v]; k++)
            if (a->viz[v][k] != b->viz[v][k]) return 0;
    }
    return 1;
}

int main(void) {
    Grafo g, t, tt;
    int v, mais = 1, ninguem[N], nn = 0;

    criar_lista(&g);
    printf("1) Quem cada perfil SEGUE (grafo original)\n");
    imprimir(&g, "segue");

    transposto(&g, &t);
    printf("\n2) Quem SEGUE cada perfil (grafo transposto)\n");
    imprimir(&t, "e seguido por");

    for (v = 2; v <= N; v++)
        if (t.grau[v] > t.grau[mais]) mais = v;
    printf("\n3) Perfil mais seguido: %d (%d seguidores)\n", mais, t.grau[mais]);
    for (v = 1; v <= N; v++)
        if (t.grau[v] == 0) ninguem[nn++] = v;
    printf("   Perfis sem nenhum seguidor: ");
    imprimir_vetor(ninguem, nn);
    printf("\n");
    transposto(&t, &tt);
    printf("   Transpor duas vezes volta ao original? %s\n", iguais(&tt, &g) ? "sim" : "nao");
    return 0;
}
