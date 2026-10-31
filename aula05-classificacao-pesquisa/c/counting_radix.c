/*
 * counting_radix.c
 *
 * Estruturas de Dados — Aula 5 — Bloco 7 (Ordenação sem comparação)
 * Slides 29 a 31 · versão em C de python/counting_radix.py
 *
 * O limite Omega(n log n) vale para quem COMPARA elementos. Se as chaves
 * são inteiros numa faixa pequena (páginas de 1 a k), dá para ordenar sem
 * comparar nada:
 *
 * 1) COUNTING SORT
 *    a) CONTAR quantos trabalhos têm 1, 2, ..., k páginas (um histograma);
 *    b) ACUMULAR: onde começa o bloco de cada número de páginas;
 *    c) POSICIONAR cada trabalho no seu bloco, na ordem de chegada.
 *    Custo: Theta(n + k). Estável. Memória extra: O(n + k).
 *
 * 2) RADIX SORT (LSD, Least Significant Digit): ordena IDs dígito a dígito
 *    (unidade, dezena, centena), com um counting sort estável (k = 10) em
 *    cada passada. Custo: Theta(d * (n + 10)) para d dígitos.
 *
 * As partes 1 e 3 e as operações do counting sort na parte 2 são idênticas
 * às do Python; as comparações do merge sort diferem um pouco, porque os
 * dados sorteados vêm de outro gerador.
 *
 * Arquivo único, só <stdio.h> — cole direto no onlineide.pro/playground/c
 */
#include <stdio.h>

#define N_CORRIDA 100000
#define K_MAX 30

typedef struct {
    int id;
    int paginas;
} Trabalho;

/* ------------------------------------------------------------------ */
/* Counting Sort de trabalhos pelas páginas (de 0 a k).                */
/* Devolve o número de operações simples. Não compara trabalhos.       */
/* ------------------------------------------------------------------ */
long counting_sort(const Trabalho entrada[], int n, int k, Trabalho saida[], int mostrar) {
    int contagem[K_MAX + 1] = {0}, inicio[K_MAX + 1] = {0};
    long ops = 0;
    for (int i = 0; i < n; i++) {                 /* a) contar */
        contagem[entrada[i].paginas]++;
        ops++;
    }
    for (int p = 1; p <= k; p++) {                /* b) acumular */
        inicio[p] = inicio[p - 1] + contagem[p - 1];
        ops++;
    }
    if (mostrar) {
        printf("   %-19s[", "contagem (1..k):");
        for (int p = 1; p <= k; p++) printf("%d%s", contagem[p], p < k ? ", " : "]\n");
        printf("   %-19s[", "bloco comeca em:");
        for (int p = 1; p <= k; p++) printf("%d%s", inicio[p], p < k ? ", " : "]\n");
    }
    for (int i = 0; i < n; i++) {                 /* c) posicionar (ordem de chegada) */
        saida[inicio[entrada[i].paginas]++] = entrada[i];
        ops++;
    }
    return ops;
}

/* Uma passada do Radix Sort: counting sort estável pelo dígito escolhido. */
void counting_por_digito(const int entrada[], int n, int divisor, int saida[]) {
    int contagem[10] = {0}, inicio[10] = {0};
    for (int i = 0; i < n; i++) contagem[(entrada[i] / divisor) % 10]++;
    for (int d = 1; d < 10; d++) inicio[d] = inicio[d - 1] + contagem[d - 1];
    for (int i = 0; i < n; i++) saida[inicio[(entrada[i] / divisor) % 10]++] = entrada[i];
}

static void imprimir_lista(const int v[], int n) {
    printf("[");
    for (int i = 0; i < n; i++) printf("%d%s", v[i], i < n - 1 ? ", " : "");
    printf("]");
}

void radix_sort(int v[], int n, int digitos, int mostrar) {
    const char *nomes[] = {"unidade", "dezena", "centena", "milhar"};
    int aux[64];
    int divisor = 1;
    for (int d = 0; d < digitos; d++) {
        counting_por_digito(v, n, divisor, aux);
        for (int i = 0; i < n; i++) v[i] = aux[i];
        if (mostrar) {
            printf("   por %-8s ", nomes[d]);
            imprimir_lista(v, n);
            printf("\n");
        }
        divisor *= 10;
    }
}

/* ------------------------------------------------------------------ */
/* Merge Sort contando comparações (só para a corrida da parte 2).     */
/* ------------------------------------------------------------------ */
static int auxiliar[N_CORRIDA];

static long merge_comparacoes(int v[], int n) {
    if (n <= 1) return 0;
    int meio = n / 2;
    long comp = merge_comparacoes(v, meio) + merge_comparacoes(v + meio, n - meio);
    int i = 0, j = meio, k = 0;
    while (i < meio && j < n) {
        comp++;
        auxiliar[k++] = (v[i] <= v[j]) ? v[i++] : v[j++];
    }
    while (i < meio) auxiliar[k++] = v[i++];
    while (j < n)    auxiliar[k++] = v[j++];
    for (k = 0; k < n; k++) v[k] = auxiliar[k];
    return comp;
}

/* Gerador pseudoaleatório (congruencial linear) com semente fixa. */
static unsigned long long semente = 2026ULL;

static unsigned int proximo_aleatorio(void) {
    semente = semente * 6364136223846793005ULL + 1442695040888963407ULL;
    return (unsigned int)(semente >> 33);
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

int main(void) {
    printf("1) COUNTING SORT: 12 trabalhos com 1 a 6 paginas\n");
    const int paginas[] = {3, 1, 4, 1, 5, 2, 6, 5, 3, 5, 1, 2};
    Trabalho trabalhos[12], ordenados[12];
    for (int i = 0; i < 12; i++) {
        trabalhos[i].id = 101 + i;
        trabalhos[i].paginas = paginas[i];
    }
    printf("   %-19s", "paginas:");
    imprimir_lista(paginas, 12);
    printf("\n");
    counting_sort(trabalhos, 12, 6, ordenados, 1);
    printf("   %-19s[", "ordenado:");
    for (int i = 0; i < 12; i++) printf("%d%s", ordenados[i].paginas, i < 11 ? ", " : "]\n");
    printf("   %-19s[", "IDs com 1 pagina:");
    int primeiro = 1;
    for (int i = 0; i < 12; i++) {
        if (ordenados[i].paginas == 1) {
            printf("%s%d", primeiro ? "" : ", ", ordenados[i].id);
            primeiro = 0;
        }
    }
    printf("]  (ordem de chegada: estavel)\n");

    const int n = N_CORRIDA, k = K_MAX;
    static Trabalho corrida[N_CORRIDA], saida[N_CORRIDA];
    static int so_paginas[N_CORRIDA];
    printf("\n2) CORRIDA: n = ");
    imprimir_com_pontos(n, 0);
    printf(" trabalhos com 1 a %d paginas\n", k);
    for (int i = 0; i < n; i++) {
        corrida[i].id = 101 + i;
        corrida[i].paginas = 1 + (int)(proximo_aleatorio() % (unsigned int)k);
        so_paginas[i] = corrida[i].paginas;
    }
    long ops = counting_sort(corrida, n, k, saida, 0);
    long comp = merge_comparacoes(so_paginas, n);
    printf("   counting sort: ");
    imprimir_com_pontos(ops, 9);
    printf(" operacoes simples (2n + k)\n   merge sort:    ");
    imprimir_com_pontos(comp, 9);
    printf(" comparacoes (~n log2 n)\n");

    printf("\n3) RADIX SORT: IDs de 3 digitos, um digito por passada\n");
    int ids[] = {512, 137, 905, 254, 731, 618, 220};
    printf("   %-12s ", "entrada");
    imprimir_lista(ids, 7);
    printf("\n");
    radix_sort(ids, 7, 3, 1);
    return 0;
}
