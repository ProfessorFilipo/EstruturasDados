/*
 * p3_componentes.c
 *
 * Estruturas de Dados — Aula 7 — Prática P3 (Componentes conexas)
 * Slide 16 (teoria) e 33 (prática) · versão em C de python/p3_componentes.py
 *
 * Dia de tempestade na filial: os cabos 3-4 e 4-5 romperam e chegaram três
 * roteadores novos (7, 8 e 9) — só o 7 e o 8 já foram ligados entre si.
 * Quantas "ilhas" (componentes conexas) a rede tem agora?
 *
 * Ideia: percorra os vértices; cada vez que encontrar um NÃO marcado, ele
 * começa uma ilha nova — uma DFS a partir dele marca a ilha inteira.
 *
 * Custo: O(V + E). A saída é idêntica à da versão em Python.
 * Arquivo único, só <stdio.h> — cole direto no onlineide.pro/playground/c
 */
#include <stdio.h>

#define N 9
#define NARESTAS 9

static const int ARESTAS[NARESTAS][2] = {
    {1, 2}, {1, 6}, {2, 3}, {2, 5}, {2, 6},
    {3, 5}, {3, 6}, {5, 6},             /* 3-4 e 4-5 romperam */
    {7, 8}                              /* roteadores novos */
};

int viz[N + 1][N];                      /* lista de adjacências contígua */
int grau[N + 1];

void criar_lista(void) {
    int i;
    for (i = 0; i <= N; i++) grau[i] = 0;
    for (i = 0; i < NARESTAS; i++) {
        int u = ARESTAS[i][0], v = ARESTAS[i][1];
        viz[u][grau[u]++] = v;
        viz[v][grau[v]++] = u;
    }
}

void dfs(int u, int marcado[], int ilha[], int *tam) {
    int k;
    marcado[u] = 1;
    ilha[(*tam)++] = u;
    for (k = 0; k < grau[u]; k++)
        if (!marcado[viz[u][k]]) dfs(viz[u][k], marcado, ilha, tam);
}

void ordenar(int v[], int n) {          /* insertion sort (Aula 4) */
    int i, j, x;
    for (i = 1; i < n; i++) {
        x = v[i];
        for (j = i - 1; j >= 0 && v[j] > x; j--) v[j + 1] = v[j];
        v[j + 1] = x;
    }
}

/* ------------------------------------------------------------------ */
/* Versão "limpa", idêntica à do slide.                                */
/* Grava cada ilha em ilhas[i][...] e devolve quantas são.             */
/* ------------------------------------------------------------------ */
int componentes(int ilhas[][N], int tam[]) {
    int marcado[N + 1] = {0};
    int v, qtd = 0;
    for (v = 1; v <= N; v++) {
        if (!marcado[v]) {              /* v começa uma ilha nova */
            tam[qtd] = 0;
            dfs(v, marcado, ilhas[qtd], &tam[qtd]);  /* marca a ilha inteira */
            ordenar(ilhas[qtd], tam[qtd]);
            qtd++;
        }
    }
    return qtd;
}

void imprimir_vetor(const int v[], int n) {
    int i;
    printf("[");
    for (i = 0; i < n; i++) printf("%s%d", i > 0 ? ", " : "", v[i]);
    printf("]");
}

int main(void) {
    int ilhas[N][N], tam[N], ilha_de[N + 1];
    int v, i, k, qtd;
    int perguntas[4][2] = {{1, 5}, {1, 4}, {7, 8}, {8, 9}};

    criar_lista();
    printf("1) Rede depois da tempestade: %d roteadores, %d cabos\n", N, NARESTAS);
    for (v = 1; v <= N; v++) {
        printf("   %d: ", v);
        if (grau[v] == 0) printf("(isolado)");
        else imprimir_vetor(viz[v], grau[v]);
        printf("\n");
    }

    qtd = componentes(ilhas, tam);
    printf("\n2) Componentes conexas encontradas: %d\n", qtd);
    for (i = 0; i < qtd; i++) {
        printf("   ilha %d: ", i + 1);
        imprimir_vetor(ilhas[i], tam[i]);
        printf("\n");
    }

    printf("\n3) Perguntas rapidas\n");
    for (i = 0; i < qtd; i++)
        for (k = 0; k < tam[i]; k++) ilha_de[ilhas[i][k]] = i + 1;
    for (i = 0; i < 4; i++) {
        int a = perguntas[i][0], b = perguntas[i][1];
        printf("   %d alcanca %d? %s\n", a, b, ilha_de[a] == ilha_de[b] ? "sim" : "nao");
    }
    printf("   cabos minimos para reconectar tudo: %d (um cabo liga duas ilhas)\n", qtd - 1);
    return 0;
}
