/*
 * ex13_ordenar_automatico.c — Aula 5, Exercício 13 (solução de referência)
 *
 * Um ordenador que escolhe o algoritmo sozinho:
 *   1. até 32 elementos ................................ Insertion Sort
 *   2. faixa pequena: max - min <= 2 * n ............... Counting Sort
 *   3. caso contrário .................................. Merge Sort
 * Ordena v no lugar e devolve o nome do algoritmo escolhido.
 *
 * Arquivo único — cole direto no onlineide.pro/playground/c
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static void insertion_sort(int v[], int n) {
    for (int i = 1; i < n; i++) {
        int chave = v[i], j = i - 1;
        while (j >= 0 && v[j] > chave) { v[j + 1] = v[j]; j--; }
        v[j + 1] = chave;
    }
}

static void counting_sort(int v[], int n, int menor, int maior) {
    int faixa = maior - menor + 1;
    int *contagem = calloc((size_t)faixa, sizeof(int));          /* começa zerado */
    if (contagem == NULL) { fprintf(stderr, "memoria insuficiente\n"); exit(1); }
    for (int i = 0; i < n; i++) contagem[v[i] - menor]++;          /* desloca para começar em 0 */
    int k = 0;
    for (int d = 0; d < faixa; d++)
        while (contagem[d]-- > 0) v[k++] = d + menor;
    free(contagem);
}

static void merge_sort(int v[], int n) {
    if (n <= 1) return;
    int meio = n / 2;
    merge_sort(v, meio);
    merge_sort(v + meio, n - meio);
    int *aux = malloc(n * sizeof(int));
    if (aux == NULL) { fprintf(stderr, "memoria insuficiente\n"); exit(1); }
    int i = 0, j = meio, k = 0;
    while (i < meio && j < n) aux[k++] = (v[i] <= v[j]) ? v[i++] : v[j++];
    while (i < meio) aux[k++] = v[i++];
    while (j < n)    aux[k++] = v[j++];
    memcpy(v, aux, n * sizeof(int));
    free(aux);
}

const char *ordenar(int v[], int n) {
    if (n <= 32) { insertion_sort(v, n); return "Insertion Sort"; }
    int menor = v[0], maior = v[0];
    for (int i = 1; i < n; i++) {
        if (v[i] < menor) menor = v[i];
        if (v[i] > maior) maior = v[i];
    }
    if ((long)maior - menor <= 2L * n) { counting_sort(v, n, menor, maior); return "Counting Sort"; }
    merge_sort(v, n);
    return "Merge Sort";
}

static unsigned long long semente = 2026ULL;
static unsigned int proximo_aleatorio(void) {
    semente = semente * 6364136223846793005ULL + 1442695040888963407ULL;
    return (unsigned int)(semente >> 33);
}

static int esta_ordenado(const int v[], int n) {
    for (int i = 1; i < n; i++) if (v[i - 1] > v[i]) return 0;
    return 1;
}

int main(void) {
    int quatro[] = {5, 2, 9, 1};
    static int paginas[1000], grandes[1000];
    for (int i = 0; i < 1000; i++) paginas[i] = 1 + (int)(proximo_aleatorio() % 30u);
    for (int i = 0; i < 1000; i++) grandes[i] = 1 + (int)(proximo_aleatorio() % 1000000u);

    const char *nomes[] = {"4 numeros", "1.000 paginas de 1 a 30", "1.000 numeros de 1 a 1.000.000"};
    int *testes[] = {quatro, paginas, grandes};
    const int tamanhos[] = {4, 1000, 1000};
    for (int t = 0; t < 3; t++) {
        const char *algoritmo = ordenar(testes[t], tamanhos[t]);
        printf("   %-32s -> %-15s [%s]\n", nomes[t], algoritmo,
               esta_ordenado(testes[t], tamanhos[t]) ? "ok" : "ERRO");
    }
    return 0;
}
