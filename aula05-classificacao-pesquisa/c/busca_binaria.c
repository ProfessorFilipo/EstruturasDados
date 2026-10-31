/*
 * busca_binaria.c
 *
 * Estruturas de Dados — Aula 5 — Bloco 2 (Pesquisa binária)
 * Slides 07 a 13 · versão em C de python/busca_binaria.py
 *
 * Cada comparação olha o elemento do MEIO e descarta a metade que não pode
 * conter o alvo. No pior caso: floor(log2 n) + 1 comparações -> O(log n).
 *
 * Dois pré-requisitos:
 *   1. o vetor precisa estar ORDENADO pelo campo procurado;
 *   2. o acesso por índice precisa ser O(1) — vetor / lista CONTÍGUA (Aula 1).
 *
 * As partes 1 e 2 usam dados fixos: a saída é idêntica à da versão em Python.
 *
 * Arquivo único, só <stdio.h> — cole direto no onlineide.pro/playground/c
 */
#include <stdio.h>

/* ------------------------------------------------------------------ */
/* Versão "limpa", idêntica à do slide 10 — para referência.           */
/* ------------------------------------------------------------------ */
int busca_binaria(const int v[], int n, int alvo) {
    int inicio = 0, fim = n - 1;
    while (inicio <= fim) {
        int meio = inicio + (fim - inicio) / 2;
        if (v[meio] == alvo) return meio;
        if (v[meio] < alvo) inicio = meio + 1;
        else                fim = meio - 1;
    }
    return -1;
}

/* ------------------------------------------------------------------ */
/* A mesma busca, contando comparações e (se mostrar != 0) cada passo. */
/* ------------------------------------------------------------------ */
int busca_binaria_contando(const int v[], int n, int alvo, int mostrar, int *comparacoes) {
    int inicio = 0, fim = n - 1;
    *comparacoes = 0;
    while (inicio <= fim) {
        int meio = inicio + (fim - inicio) / 2;
        (*comparacoes)++;                          /* olhamos v[meio] */
        if (mostrar) {
            printf("   inicio=%2d  meio=%2d  fim=%2d   v[meio]=%d\n", inicio, meio, fim, v[meio]);
        }
        if (v[meio] == alvo) return meio;
        if (v[meio] < alvo) inicio = meio + 1;     /* descarta a metade da esquerda */
        else                fim = meio - 1;        /* descarta a metade da direita  */
    }
    return -1;
}

/* Parte 3: um vetor "virtual" com v[i] = 101 + i, que não ocupa memória
 * (o mesmo papel do range() na versão em Python). Usa long long porque
 * n chega a 1 bilhão. Devolve o número de comparações. */
int busca_binaria_virtual(long long n, long long alvo) {
    long long inicio = 0, fim = n - 1;
    int comparacoes = 0;
    while (inicio <= fim) {
        long long meio = inicio + (fim - inicio) / 2;
        long long valor = 101 + meio;
        comparacoes++;
        if (valor == alvo) break;
        if (valor < alvo) inicio = meio + 1;
        else              fim = meio - 1;
    }
    return comparacoes;
}

/* Raiz quadrada aproximada pelo método de Newton, sem usar <math.h>. */
static double raiz(double x) {
    double r = x > 1.0 ? x : 1.0;
    for (int i = 0; i < 100; i++) {
        r = 0.5 * (r + x / r);
    }
    return r;
}

/* Escreve x em buf com ponto separando os milhares: 1000000 -> 1.000.000 */
static void com_pontos(long long x, char *buf) {
    char tmp[32];
    int n = sprintf(tmp, "%lld", x), k = 0;
    for (int i = 0; i < n; i++) {
        buf[k++] = tmp[i];
        if ((n - i - 1) % 3 == 0 && i < n - 1) buf[k++] = '.';
    }
    buf[k] = '\0';
}

int main(void) {
    /* 16 IDs do histórico: ordenados (FIFO) e com lacunas (cancelamentos) */
    const int ids[] = {101, 104, 105, 109, 112, 113, 118, 121,
                       125, 126, 130, 134, 137, 141, 142, 150};
    const int n = (int)(sizeof ids / sizeof ids[0]);
    int comp, pos;

    /* Troque o alvo e rode de novo! */
    const int ALVO = 137;

    printf("1) RASTREIO: buscando %d entre %d IDs\n", ALVO, n);
    pos = busca_binaria_contando(ids, n, ALVO, 1, &comp);
    printf("   -> posicao %d, %d comparacoes\n", pos, comp);
    if (pos != busca_binaria(ids, n, ALVO)) printf("   (erro: versoes diferentes!)\n");

    printf("\n2) RASTREIO: buscando 119 (foi cancelado)\n");
    pos = busca_binaria_contando(ids, n, 119, 1, &comp);
    printf("   -> posicao %d (inicio passou do fim), %d comparacoes\n", pos, comp);

    printf("\n3) PIOR CASO: SEQUENCIAL x SALTOS (AULA 4) x BINARIA\n");
    printf("%15s %15s %9s %8s\n", "n", "sequencial", "saltos", "binaria");
    const long long tamanhos[] = {1000LL, 1000000LL, 1000000000LL};
    for (int t = 0; t < 3; t++) {
        long long tam = tamanhos[t];
        int binaria = busca_binaria_virtual(tam, 101 + tam);      /* alvo ausente */
        long long saltos = (long long)(2.0 * raiz((double)tam) + 0.5);   /* n/m + m com m = raiz(n) */
        char a[32], b[32];
        com_pontos(tam, a);
        com_pontos(saltos, b);
        printf("%15s %15s %9s %8d\n", a, a, b, binaria);
    }

    printf("\nDobrar n custa so +1 comparacao na binaria: O(log n)\n");
    return 0;
}
