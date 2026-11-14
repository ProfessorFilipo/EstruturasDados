/*
 * p3_lista_adjacencias.c
 *
 * Estruturas de Dados — Aula 6 — Prática P3 (Lista de adjacências)
 * Slides 22 (teoria) e 30 (prática) · versão em C de python/p3_lista_adjacencias.py
 *
 * Lista de adjacências: um vetor adj[] com uma posição por vértice; cada
 * posição aponta para uma LISTA ENCADEADA com os vizinhos daquele vértice
 * (a mesma lista encadeada da Aula 1, e a mesma ideia do livro de
 * Ascencio & Araújo, p. 377).
 *
 *     adj[1] -> [2] -> [6] -> NULL
 *     adj[2] -> [1] -> [3] -> [5] -> [6] -> NULL
 *
 * Inserimos cada vizinho no FIM da lista para manter a ordem das arestas
 * (e a saída idêntica à da versão em Python). O livro insere no INÍCIO,
 * que é O(1) — por isso, lá, os vizinhos aparecem em ordem invertida.
 *
 * Espaço: n posições no vetor + 2 x |E| nós -> O(V + E).
 *
 * Arquivo único, <stdio.h> e <stdlib.h> — cole no onlineide.pro/playground/c
 */
#include <stdio.h>
#include <stdlib.h>

#define N 6
#define NARESTAS 10
#define DIRIGIDO 0

static const int ARESTAS[NARESTAS][2] = {
    {1, 2}, {1, 6}, {2, 3}, {2, 5}, {2, 6},
    {3, 4}, {3, 5}, {3, 6}, {4, 5}, {5, 6}
};

typedef struct No {
    int vertice;                /* o vizinho */
    struct No *prox;            /* próximo vizinho da lista */
} No;

/* ------------------------------------------------------------------ */
/* Versão "limpa", idêntica à do slide.                                */
/* ------------------------------------------------------------------ */
void inserir_fim(No **inicio, int v) {
    No *novo = (No *) malloc(sizeof(No));
    novo->vertice = v;
    novo->prox = NULL;
    if (*inicio == NULL) {
        *inicio = novo;                         /* lista estava vazia */
    } else {
        No *p = *inicio;
        while (p->prox != NULL) p = p->prox;    /* anda até o último */
        p->prox = novo;
    }
}

void criar_lista(No *adj[N + 1], int dirigido) {
    int i;
    for (i = 0; i <= N; i++) adj[i] = NULL;     /* posição 0 sem uso */
    for (i = 0; i < NARESTAS; i++) {
        int u = ARESTAS[i][0], v = ARESTAS[i][1];
        inserir_fim(&adj[u], v);
        if (!dirigido) inserir_fim(&adj[v], u); /* v também vê u */
    }
}

void imprimir_lista(No *adj[N + 1]) {
    int v;
    for (v = 1; v <= N; v++) {
        No *p = adj[v];
        printf("   %d: ", v);
        if (p == NULL) printf("(sem vizinhos)");
        while (p != NULL) {
            printf("%d%s", p->vertice, p->prox != NULL ? " -> " : "");
            p = p->prox;
        }
        printf("\n");
    }
}

int tamanho(No *p) {
    int t = 0;
    while (p != NULL) { t++; p = p->prox; }
    return t;
}

void liberar_lista(No *adj[N + 1]) {
    int v;
    for (v = 1; v <= N; v++) {
        while (adj[v] != NULL) {
            No *aux = adj[v];
            adj[v] = adj[v]->prox;
            free(aux);
        }
    }
}

int main(void) {
    No *adj[N + 1];
    int v, guardados = 0, esperado;

    printf("1) Lista de adjacencias da rede da filial (%s)\n",
           DIRIGIDO ? "DIRIGIDO" : "NAO DIRIGIDO");
    criar_lista(adj, DIRIGIDO);
    imprimir_lista(adj);

    printf("\n2) O grau sai de graca: e o tamanho de cada lista\n");
    for (v = 1; v <= N; v++)
        printf("   grau(%d) = len(adj[%d]) = %d\n", v, v, tamanho(adj[v]));

    for (v = 1; v <= N; v++) guardados += tamanho(adj[v]);
    esperado = DIRIGIDO ? NARESTAS : 2 * NARESTAS;
    printf("\n3) Vizinhos guardados no total: %d (esperado: %d)\n", guardados, esperado);
    printf("   Celulas usadas: %d (vetor) + %d (vizinhos) = %d   x   matriz: %d\n",
           N, guardados, N + guardados, N * N);

    liberar_lista(adj);         /* devolve cada nó com free */
    return 0;
}
