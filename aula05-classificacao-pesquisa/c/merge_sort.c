/*
 * merge_sort.c
 *
 * Estruturas de Dados — Aula 5 — Bloco 4 (Merge Sort)
 * Slides 16 a 20 · versão em C de python/merge_sort.py
 *
 * 0) RECURSÃO DE BOLSO: uma função que chama a si mesma com um problema
 *    menor, até chegar ao CASO BASE. Cada chamada em andamento fica na
 *    PILHA DE CHAMADAS — a Pilha (LIFO) da Aula 2.
 * 1) INTERCALAR: duas filas já ordenadas viram uma só, comparando só as
 *    FRENTES (as operações da Fila da Aula 2). Custo: Theta(n1 + n2).
 * 2) MERGE SORT: divide ao meio até sobrar 1 elemento e intercala na volta.
 *    log2(n) níveis x n por nível -> Theta(n log n) em TODOS os casos.
 *
 * Em C, o vetor auxiliar da intercalação precisa ser criado com malloc e
 * liberado com free: é aqui que a memória extra O(n) fica visível.
 *
 * As partes 0, 1 e 2 usam dados fixos (saída idêntica à do Python). Na
 * parte 3 os dados vêm de um gerador próprio: os números diferem um pouco,
 * mas a razão de ~2,2 aparece do mesmo jeito.
 *
 * Arquivo único — cole direto no onlineide.pro/playground/c
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* ------------------------------------------------------------------ */
/* Versões "limpas", equivalentes às dos slides 16 e 19.               */
/* ------------------------------------------------------------------ */
int soma_paginas(const int paginas[], int n) {
    if (n == 0) return 0;                        /* caso base */
    return paginas[0] + soma_paginas(paginas + 1, n - 1);
}

void merge_sort(int v[], int n) {
    if (n <= 1) return;              /* caso base */
    int meio = n / 2;
    merge_sort(v, meio);             /* esquerda  */
    merge_sort(v + meio, n - meio);  /* direita   */
    int *aux = malloc(n * sizeof(int)); /* O(n) */
    if (aux == NULL) { fprintf(stderr, "memoria insuficiente\n"); exit(1); }
    int i = 0, j = meio, k = 0;
    while (i < meio && j < n)
        aux[k++] = (v[i] <= v[j]) ? v[i++] : v[j++];
    while (i < meio) aux[k++] = v[i++];
    while (j < n)    aux[k++] = v[j++];
    memcpy(v, aux, n * sizeof(int));
    free(aux);
}

/* ------------------------------------------------------------------ */
/* Auxiliares de impressão                                             */
/* ------------------------------------------------------------------ */
static void imprimir_lista(const int v[], int n) {
    printf("[");
    for (int i = 0; i < n; i++) printf("%d%s", v[i], i < n - 1 ? ", " : "");
    printf("]");
}

static void recuo(int nivel) {
    for (int i = 0; i < nivel; i++) printf("   ");
}

static void imprimir_com_pontos(long x, int largura) {
    char tmp[32], buf[40];
    int n = sprintf(tmp, "%ld", x), k = 0;
    for (int i = 0; i < n; i++) {
        buf[k++] = tmp[i];
        if ((n - i - 1) % 3 == 0 && i < n - 1) buf[k++] = '.';
    }
    buf[k] = '\0';
    printf("%*s", largura, buf);
}

/* ------------------------------------------------------------------ */
/* As mesmas ideias, mostrando cada passo e contando comparações.      */
/* ------------------------------------------------------------------ */
int soma_paginas_rastreada(const int paginas[], int n, int nivel) {
    recuo(nivel);
    printf("chamou soma_paginas(");
    imprimir_lista(paginas, n);
    printf(")\n");
    if (n == 0) {                                /* caso base */
        recuo(nivel);
        printf("devolve 0\n");
        return 0;
    }
    int total = paginas[0] + soma_paginas_rastreada(paginas + 1, n - 1, nivel + 1);
    recuo(nivel);
    printf("devolve %d\n", total);
    return total;
}

/* Intercala duas filas ordenadas usando só a frente de cada uma. */
void intercalar_filas(const int a[], int na, const int b[], int nb, int saida[]) {
    int frente_a = 0, frente_b = 0, k = 0;
    while (frente_a < na && frente_b < nb) {
        if (a[frente_a] <= b[frente_b]) saida[k++] = a[frente_a++];   /* desenfileira de A */
        else                            saida[k++] = b[frente_b++];   /* desenfileira de B */
    }
    while (frente_a < na) saida[k++] = a[frente_a++];                 /* sobrou alguém? */
    while (frente_b < nb) saida[k++] = b[frente_b++];
}

static long comparacoes = 0;   /* contador global de comparações */

void merge_sort_contando(int v[], int n, int nivel, int mostrar) {
    if (n <= 1) return;
    int meio = n / 2;
    merge_sort_contando(v, meio, nivel + 1, mostrar);
    merge_sort_contando(v + meio, n - meio, nivel + 1, mostrar);
    if (mostrar) {
        recuo(nivel);
        printf("intercala ");
        imprimir_lista(v, meio);
        printf(" + ");
        imprimir_lista(v + meio, n - meio);
    }
    int *aux = malloc(n * sizeof(int));
    if (aux == NULL) { fprintf(stderr, "memoria insuficiente\n"); exit(1); }
    int i = 0, j = meio, k = 0;
    while (i < meio && j < n) {
        comparacoes++;
        aux[k++] = (v[i] <= v[j]) ? v[i++] : v[j++];
    }
    while (i < meio) aux[k++] = v[i++];
    while (j < n)    aux[k++] = v[j++];
    memcpy(v, aux, n * sizeof(int));
    free(aux);
    if (mostrar) {
        printf(" -> ");
        imprimir_lista(v, n);
        printf("\n");
    }
}

/* Gerador pseudoaleatório (congruencial linear) com semente fixa. */
static unsigned long long semente = 2026ULL;

static unsigned int proximo_aleatorio(void) {
    semente = semente * 6364136223846793005ULL + 1442695040888963407ULL;
    return (unsigned int)(semente >> 33);
}

int main(void) {
    printf("0) RECURSAO DE BOLSO\n");
    const int tres[] = {12, 5, 8};
    int total = soma_paginas_rastreada(tres, 3, 0);
    printf("total = %d\n", total);
    if (total != soma_paginas(tres, 3)) printf("(erro: versoes diferentes!)\n");

    printf("\n1) INTERCALAR DUAS FILAS ORDENADAS (duas impressoras)\n");
    const int a[] = {2, 5, 9}, b[] = {3, 4, 12};
    int unica[6];
    printf("   A = ");
    imprimir_lista(a, 3);
    printf("   B = ");
    imprimir_lista(b, 3);
    printf("\n   -> ");
    intercalar_filas(a, 3, b, 3, unica);
    imprimir_lista(unica, 6);
    printf("\n");

    printf("\n2) MERGE SORT PASSO A PASSO (recuo = profundidade da pilha)\n");
    int paginas[] = {12, 5, 8, 3, 20, 1, 9, 6};
    comparacoes = 0;
    merge_sort_contando(paginas, 8, 0, 1);
    printf("   resultado: ");
    imprimir_lista(paginas, 8);
    printf("\n   %ld comparacoes  (n log2 n = %d)\n", comparacoes, 8 * 3);

    printf("\n3) CRESCIMENTO: merge sort x n log2 n\n");
    printf("%7s %12s %10s %6s\n", "n", "comparacoes", "n*log2(n)", "razao");
    static int v[4000], copia[4000];
    const int tamanhos[] = {1000, 2000, 4000};
    const long nlogn[] = {9966, 21932, 47863};   /* n * log2(n), arredondado */
    long anterior = 0;
    for (int t = 0; t < 3; t++) {
        int n = tamanhos[t];
        for (int i = 0; i < n; i++) v[i] = copia[i] = 1 + (int)(proximo_aleatorio() % 1000000u);
        comparacoes = 0;
        merge_sort_contando(v, n, 0, 0);
        merge_sort(copia, n);                        /* confere com a versão limpa */
        if (memcmp(v, copia, n * sizeof(int)) != 0) printf("(erro: versoes diferentes!)\n");
        printf("%7d ", n);
        imprimir_com_pontos(comparacoes, 12);
        printf(" ");
        imprimir_com_pontos(nlogn[t], 10);
        if (anterior > 0) {
            long decimos = (10 * comparacoes + anterior / 2) / anterior;
            printf("   x%ld,%ld\n", decimos / 10, decimos % 10);
        } else {
            printf("%7s\n", "-");
        }
        anterior = comparacoes;
    }
    printf("\nDobrou n -> comparacoes x2,2 (e nao x4): Theta(n log n)\n");
    return 0;
}
