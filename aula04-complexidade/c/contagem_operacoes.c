/*
 * contagem_operacoes.c
 *
 * Estruturas de Dados — Aula 4 — Bloco 2 (Contar operações)
 * Slides 06 a 08 · Apostila, capítulo 2
 *
 * Conta os passos executados por duas funções simples e compara o
 * resultado com a fórmula que obtivemos no papel:
 *
 *   soma de um vetor ............. T(n) = 3n + 4
 *   busca linear, pior caso ...... T(n) = 3n + 3   (valor ausente)
 *   busca linear, melhor caso .... T(n) = 4        (valor na posição 0)
 *
 * Modelo de custo usado na aula: cada instrução simples executada custa
 * 1 passo — uma atribuição, um teste do laço, um incremento, um comando
 * do corpo do laço ou um return.
 *
 * Arquivo único, só <stdio.h> — cole direto no onlineide.pro/playground/c
 */
#include <stdio.h>

#define TAMANHO_MAX 1000

static long passos = 0; /* contador global de passos */

/* Conta 1 passo cada vez que um teste é avaliado e devolve o resultado
 * do teste. Assim, "while (testar(i < n))" conta cada avaliação de i < n. */
static int testar(int condicao) {
    passos++;
    return condicao;
}

/* Mesma soma do slide 06. O for foi reescrito como while apenas para
 * deixar cada passo visível — a contagem é idêntica à do for:
 *
 *     int total = 0;
 *     for (int i = 0; i < n; i++) {
 *         total = total + v[i];
 *     }
 *     return total;
 */
int soma(const int v[], int n) {
    int total = 0;              passos++;  /* executa 1 vez            */
    int i = 0;                  passos++;  /* executa 1 vez            */
    while (testar(i < n)) {                /* teste: executa n + 1 vezes */
        total = total + v[i];   passos++;  /* executa n vezes          */
        i++;                    passos++;  /* executa n vezes          */
    }
    passos++;                              /* return: executa 1 vez    */
    return total;
}

/* Mesma lógica de lista_buscar() da Aula 1 (aula01-estruturas-lineares/
 * c/lista_contigua.c), com o for reescrito como while pelo mesmo motivo. */
int buscar(const int dados[], int tamanho, int valor) {
    int i = 0;                  passos++;  /* executa 1 vez                */
    while (testar(i < tamanho)) {          /* teste: até n + 1 vezes       */
        if (testar(dados[i] == valor)) {   /* comparação: até n vezes      */
            passos++;                      /* return i: no máximo 1 vez    */
            return i;
        }
        i++;                    passos++;  /* incremento: até n vezes      */
    }
    passos++;                              /* return -1: no máximo 1 vez   */
    return -1;
}

static void imprimir_cabecalho(void) {
    printf("%8s %17s %9s\n", "n", "passos contados", "formula");
}

static void imprimir_linha(int n, long contados, long formula) {
    printf("%8d %17ld %9ld   %s\n", n, contados, formula,
           contados == formula ? "confere" : "DIFERENTE!");
}

int main(void) {
    static int v[TAMANHO_MAX];
    int tamanhos[] = {10, 100, 1000};
    int quantidade = (int)(sizeof(tamanhos) / sizeof(tamanhos[0]));

    /* vetor com os valores 0, 1, 2, ..., n-1 */
    for (int i = 0; i < TAMANHO_MAX; i++) {
        v[i] = i;
    }

    printf("Modelo de custo: cada instrucao simples executada = 1 passo\n");

    printf("\n1) SOMA DE UM VETOR                            formula: T(n) = 3n + 4\n");
    imprimir_cabecalho();
    for (int k = 0; k < quantidade; k++) {
        int n = tamanhos[k];
        passos = 0;
        soma(v, n);
        imprimir_linha(n, passos, 3L * n + 4);
    }

    printf("\n2) BUSCA LINEAR - PIOR CASO (valor ausente)    formula: T(n) = 3n + 3\n");
    imprimir_cabecalho();
    for (int k = 0; k < quantidade; k++) {
        int n = tamanhos[k];
        passos = 0;
        buscar(v, n, -1); /* -1 nao esta no vetor */
        imprimir_linha(n, passos, 3L * n + 3);
    }

    printf("\n3) BUSCA LINEAR - MELHOR CASO (valor na posicao 0)   formula: T(n) = 4\n");
    imprimir_cabecalho();
    for (int k = 0; k < quantidade; k++) {
        int n = tamanhos[k];
        passos = 0;
        buscar(v, n, 0); /* 0 esta na posicao 0 */
        imprimir_linha(n, passos, 4);
    }

    printf("\nObserve: no pior caso, os passos crescem junto com n (crescimento linear).\n");
    printf("No melhor caso, ficam constantes, nao importa o tamanho da lista.\n");
    return 0;
}
