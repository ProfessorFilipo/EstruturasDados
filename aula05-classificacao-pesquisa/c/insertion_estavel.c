/*
 * insertion_estavel.c
 *
 * Estruturas de Dados — Aula 5 — Bloco 3 (Insertion Sort revisitado)
 * Slides 14 e 15 · versão em C de python/insertion_estavel.py
 *
 * O Insertion Sort da Aula 4, agora ordenando trabalhos (id, paginas)
 * pelo número de páginas. Duas lições:
 *
 * 1) ESTABILIDADE: trabalhos com o mesmo número de páginas continuam na
 *    ordem de chegada (a justiça da fila FIFO), porque só deslocamos quem
 *    é ESTRITAMENTE maior que a chave ( > , não >= ).
 * 2) CRESCIMENTO: dobrar n multiplica as comparações por ~4 -> Theta(n^2).
 *
 * A parte 1 usa dados fixos (saída idêntica à do Python). Na parte 2 os
 * dados são sorteados por um gerador próprio: os números diferem um pouco
 * dos do Python, mas a razão de ~4 aparece do mesmo jeito.
 *
 * Arquivo único, só <stdio.h> — cole direto no onlineide.pro/playground/c
 */
#include <stdio.h>

#define N_MAX 2000

typedef struct {
    int id;
    int paginas;
} Trabalho;

/* Ordena v pelas páginas, no lugar. Devolve o número de comparações. */
long insertion_sort_por_paginas(Trabalho v[], int n) {
    long comparacoes = 0;
    for (int i = 1; i < n; i++) {
        Trabalho chave = v[i];
        int j = i - 1;
        while (j >= 0) {
            comparacoes++;
            if (!(v[j].paginas > chave.paginas)) {   /* > mantém a estabilidade */
                break;
            }
            v[j + 1] = v[j];                         /* desloca para a direita */
            j--;
        }
        v[j + 1] = chave;                            /* encaixa */
    }
    return comparacoes;
}

static void imprimir_trabalhos(const Trabalho v[], int n) {
    printf("[");
    for (int i = 0; i < n; i++) {
        printf("(%d, %d)%s", v[i].id, v[i].paginas, i < n - 1 ? ", " : "");
    }
    printf("]\n");
}

/* Gerador pseudoaleatório (congruencial linear) com semente fixa. */
static unsigned long long semente = 2026ULL;

static unsigned int proximo_aleatorio(void) {
    semente = semente * 6364136223846793005ULL + 1442695040888963407ULL;
    return (unsigned int)(semente >> 33);
}

/* Imprime x com ponto separando os milhares, alinhado à direita em 'largura'. */
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
    printf("1) ESTABILIDADE: 8 trabalhos ordenados por paginas\n");
    Trabalho fila[] = {{101, 12}, {102, 3}, {104, 12}, {105, 7},
                       {107, 3}, {108, 20}, {110, 7}, {111, 1}};
    printf("   antes:  ");
    imprimir_trabalhos(fila, 8);
    insertion_sort_por_paginas(fila, 8);
    printf("   depois: ");
    imprimir_trabalhos(fila, 8);
    printf("   empates (3, 7 e 12 paginas) mantem a ordem de chegada dos IDs\n");

    printf("\n2) CRESCIMENTO: paginas aleatorias\n");
    printf("%7s %13s %7s\n", "n", "comparacoes", "razao");
    static Trabalho v[N_MAX];
    const int tamanhos[] = {500, 1000, 2000};
    long anterior = 0;
    for (int t = 0; t < 3; t++) {
        int n = tamanhos[t];
        for (int i = 0; i < n; i++) {
            v[i].id = 101 + i;
            v[i].paginas = 1 + (int)(proximo_aleatorio() % 30u);
        }
        long comp = insertion_sort_por_paginas(v, n);
        printf("%7d ", n);
        imprimir_com_pontos(comp, 13);
        if (anterior > 0) {
            long decimos = (10 * comp + anterior / 2) / anterior;   /* razão com 1 casa */
            printf("    x%ld,%ld\n", decimos / 10, decimos % 10);
        } else {
            printf("%8s\n", "-");
        }
        anterior = comp;
    }
    printf("\nDobrou n -> comparacoes x4: Theta(n^2)\n");
    return 0;
}
