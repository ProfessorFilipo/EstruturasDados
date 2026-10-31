/*
 * ex07_merge_sort_estavel.c — Aula 5, Exercício 7 (solução de referência)
 *
 * Merge Sort de trabalhos (id, paginas) pelas páginas. É estável porque, no
 * empate, a intercalação tira primeiro da metade ESQUERDA (o <=).
 * O resultado é comparado com o do Insertion Sort estável da aula.
 *
 * Arquivo único — cole direto no onlineide.pro/playground/c
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    int id;
    int paginas;
} Trabalho;

void merge_sort_por_paginas(Trabalho v[], int n) {
    if (n <= 1) return;
    int meio = n / 2;
    merge_sort_por_paginas(v, meio);
    merge_sort_por_paginas(v + meio, n - meio);
    Trabalho *aux = malloc(n * sizeof(Trabalho));
    if (aux == NULL) { fprintf(stderr, "memoria insuficiente\n"); exit(1); }
    int i = 0, j = meio, k = 0;
    while (i < meio && j < n)
        aux[k++] = (v[i].paginas <= v[j].paginas) ? v[i++] : v[j++];   /* <= : estável */
    while (i < meio) aux[k++] = v[i++];
    while (j < n)    aux[k++] = v[j++];
    memcpy(v, aux, n * sizeof(Trabalho));
    free(aux);
}

void insertion_sort_por_paginas(Trabalho v[], int n) {
    for (int i = 1; i < n; i++) {
        Trabalho chave = v[i];
        int j = i - 1;
        while (j >= 0 && v[j].paginas > chave.paginas) {
            v[j + 1] = v[j];
            j--;
        }
        v[j + 1] = chave;
    }
}

static int iguais(const Trabalho a[], const Trabalho b[], int n) {
    for (int i = 0; i < n; i++)
        if (a[i].id != b[i].id || a[i].paginas != b[i].paginas) return 0;
    return 1;
}

static void imprimir(const Trabalho v[], int n) {
    printf("[");
    for (int i = 0; i < n; i++) printf("(%d, %d)%s", v[i].id, v[i].paginas, i < n - 1 ? ", " : "]\n");
}

static unsigned long long semente = 2026ULL;
static unsigned int proximo_aleatorio(void) {
    semente = semente * 6364136223846793005ULL + 1442695040888963407ULL;
    return (unsigned int)(semente >> 33);
}

int main(void) {
    Trabalho fila[] = {{101, 12}, {102, 3}, {104, 12}, {105, 7},
                       {107, 3}, {108, 20}, {110, 7}, {111, 1}};
    Trabalho copia[8];
    memcpy(copia, fila, sizeof fila);
    printf("1) OS 8 TRABALHOS DA DEMO 3\n   merge:     ");
    merge_sort_por_paginas(fila, 8);
    imprimir(fila, 8);
    printf("   insertion: ");
    insertion_sort_por_paginas(copia, 8);
    imprimir(copia, 8);
    printf("   iguais? %s\n", iguais(fila, copia, 8) ? "sim" : "NAO");

    printf("\n2) 1.000 TRABALHOS COM PAGINAS ALEATORIAS\n");
    static Trabalho a[1000], b[1000];
    for (int i = 0; i < 1000; i++) {
        a[i].id = b[i].id = 101 + i;
        a[i].paginas = b[i].paginas = 1 + (int)(proximo_aleatorio() % 30u);
    }
    merge_sort_por_paginas(a, 1000);
    insertion_sort_por_paginas(b, 1000);
    printf("   igual ao Insertion Sort? %s\n", iguais(a, b, 1000) ? "sim" : "NAO");
    return 0;
}
