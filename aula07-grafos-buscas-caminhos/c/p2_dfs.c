/*
 * p2_dfs.c
 *
 * Estruturas de Dados — Aula 7 — Prática P2 (Busca em profundidade — DFS)
 * Slides 13 a 15 (teoria) e 32 (prática) · versão em C de python/p2_dfs.py
 *
 * A DFS vai sempre em frente pelo primeiro caminho ainda não visitado e,
 * quando trava, VOLTA (backtracking). Quem guarda "para onde voltar" é uma
 * PILHA (Aula 2) — na versão recursiva, a própria pilha de chamadas.
 *
 * Mesmo grafo e mesma ordem de vizinhos do livro de Ascencio & Araújo.
 * Custo: O(V + E). A saída é idêntica à da versão em Python.
 * Arquivo único, só <stdio.h> — cole direto no onlineide.pro/playground/c
 */
#include <stdio.h>

#define N 6
#define ORIGEM 1

static const int GRAU[N + 1]   = {0, 2, 4, 4, 2, 4, 4};
static const int ADJ[N + 1][4] = {
    {0}, {6, 2}, {5, 3, 1, 6}, {6, 5, 4, 2}, {5, 3}, {6, 4, 3, 2}, {5, 3, 2, 1}
};

/* ------------------------------------------------------------------ */
/* Versão "limpa", idêntica à do slide (recursiva).                    */
/* ------------------------------------------------------------------ */
void dfs(int u, int marcado[], int ordem[], int *n) {
    int k;
    marcado[u] = 1;
    ordem[(*n)++] = u;                  /* visita u */
    for (k = 0; k < GRAU[u]; k++) {
        int v = ADJ[u][k];
        if (!marcado[v])
            dfs(v, marcado, ordem, n);  /* mergulha em v; ao voltar, segue o laço */
    }
}

/* A mesma DFS, com recuo mostrando a profundidade da recursão. */
void dfs_passo_a_passo(int u, int marcado[], int ordem[], int *n, int nivel) {
    int k, i;
    marcado[u] = 1;
    ordem[(*n)++] = u;
    printf("   ");
    for (i = 0; i < nivel; i++) printf("  ");
    printf("visita %d\n", u);
    for (k = 0; k < GRAU[u]; k++) {
        int v = ADJ[u][k];
        if (!marcado[v]) dfs_passo_a_passo(v, marcado, ordem, n, nivel + 1);
    }
    printf("   ");
    for (i = 0; i < nivel; i++) printf("  ");
    printf("volta de %d\n", u);
}

/* Versão com PILHA explícita, sem recursão. Devolve quantos foram visitados. */
int dfs_pilha(int s, int ordem[]) {
    int marcado[N + 1] = {0};
    int pilha[64], topo = 0, n = 0, k;  /* cabe 1 + 2E empilhamentos */
    pilha[topo++] = s;
    while (topo > 0) {
        int u = pilha[--topo];          /* tira do TOPO */
        if (marcado[u]) continue;       /* já visitado por outro caminho */
        marcado[u] = 1;
        ordem[n++] = u;
        for (k = GRAU[u] - 1; k >= 0; k--) {    /* invertido: o 1o vizinho fica no topo */
            int v = ADJ[u][k];
            if (!marcado[v]) pilha[topo++] = v;
        }
    }
    return n;
}

int main(void) {
    int marcado[N + 1] = {0}, marcado2[N + 1] = {0};
    int ordem[N], ordem2[N], ordem3[N];
    int n = 0, n2 = 0, n3, i, iguais = 1;

    printf("1) DFS recursiva a partir de %d (o recuo mostra a profundidade)\n", ORIGEM);
    dfs_passo_a_passo(ORIGEM, marcado, ordem, &n, 0);
    printf("   ordem de visita:");
    for (i = 0; i < n; i++) printf(" %d", ordem[i]);
    printf("\n");

    dfs(ORIGEM, marcado2, ordem2, &n2);             /* confere com a versão limpa */
    for (i = 0; i < n; i++) if (ordem2[i] != ordem[i]) return 1;

    printf("\n2) DFS com pilha explicita (sem recursao)\n");
    n3 = dfs_pilha(ORIGEM, ordem3);
    printf("   ordem de visita:");
    for (i = 0; i < n3; i++) printf(" %d", ordem3[i]);
    printf("\n");
    for (i = 0; i < n; i++) if (ordem3[i] != ordem[i]) iguais = 0;
    printf("   mesma ordem da recursiva? %s\n", (iguais && n3 == n) ? "sim" : "nao");

    printf("\n3) Comparando com a BFS (P1) a partir do mesmo vertice\n");
    printf("   BFS (fila):  1 6 2 5 3 4   -> anda em ondas, por distancia\n");
    printf("   DFS (pilha):");
    for (i = 0; i < n; i++) printf(" %d", ordem[i]);
    printf("   -> vai fundo primeiro, depois volta\n");
    return 0;
}
