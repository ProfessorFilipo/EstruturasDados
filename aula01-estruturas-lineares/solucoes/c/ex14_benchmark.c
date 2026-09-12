/*
 * ex14_benchmark.c — solução
 *
 * Mede o tempo de inserir 10.000 elementos no início e no fim, para uma
 * estrutura contígua e para uma encadeada, e compara com a previsão da
 * tabela de complexidade (Exercício 4).
 *
 * Nota de organização: assim como no Exercício 12, este arquivo evita
 * incluir lista_contigua.h e lista_encadeada.h ao mesmo tempo (os dois
 * reutilizam os mesmos nomes de função) — usa implementações mínimas
 * próprias, com a mesma lógica das do repositório, só para medir o
 * comportamento assintótico de cada uma.
 */
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define N 10000

/* ---- versão contígua mínima (mesma lógica de lista_contigua.c) ---- */

typedef struct {
    int *dados;
    int tamanho;
    int capacidade;
} ArrayBench;

void array_criar(ArrayBench *a, int capacidade) {
    a->dados = malloc(capacidade * sizeof(int));
    a->tamanho = 0;
    a->capacidade = capacidade;
}

void array_inserir_inicio(ArrayBench *a, int valor) {
    for (int i = a->tamanho; i > 0; i--) {
        a->dados[i] = a->dados[i - 1];
    }
    a->dados[0] = valor;
    a->tamanho++;
}

void array_inserir_fim(ArrayBench *a, int valor) {
    a->dados[a->tamanho] = valor;
    a->tamanho++;
}

void array_destruir(ArrayBench *a) {
    free(a->dados);
}

/* ---- versão encadeada mínima (mesma lógica de lista_encadeada.c) ---- */

typedef struct NoBench {
    int valor;
    struct NoBench *proximo;
} NoBench;

typedef struct {
    NoBench *inicio;
    NoBench *fim;
} EncadeadaBench;

void encadeada_criar(EncadeadaBench *lista) {
    lista->inicio = NULL;
    lista->fim = NULL;
}

void encadeada_inserir_inicio(EncadeadaBench *lista, int valor) {
    NoBench *novo = malloc(sizeof(NoBench));
    novo->valor = valor;
    novo->proximo = lista->inicio;
    lista->inicio = novo;
    if (lista->fim == NULL) {
        lista->fim = novo;
    }
}

void encadeada_inserir_fim(EncadeadaBench *lista, int valor) {
    NoBench *novo = malloc(sizeof(NoBench));
    novo->valor = valor;
    novo->proximo = NULL;
    if (lista->inicio == NULL) {
        lista->inicio = novo;
    } else {
        lista->fim->proximo = novo;
    }
    lista->fim = novo;
}

void encadeada_destruir(EncadeadaBench *lista) {
    NoBench *atual = lista->inicio;
    while (atual != NULL) {
        NoBench *proximo = atual->proximo;
        free(atual);
        atual = proximo;
    }
}

/* ---- medição ---- */

int main(void) {
    clock_t inicio, fim;
    double tempo_array_inicio, tempo_array_fim;
    double tempo_encadeada_inicio, tempo_encadeada_fim;

    ArrayBench a1;
    array_criar(&a1, N);
    inicio = clock();
    for (int i = 0; i < N; i++) {
        array_inserir_inicio(&a1, i);
    }
    fim = clock();
    tempo_array_inicio = (double)(fim - inicio) / CLOCKS_PER_SEC;
    array_destruir(&a1);

    ArrayBench a2;
    array_criar(&a2, N);
    inicio = clock();
    for (int i = 0; i < N; i++) {
        array_inserir_fim(&a2, i);
    }
    fim = clock();
    tempo_array_fim = (double)(fim - inicio) / CLOCKS_PER_SEC;
    array_destruir(&a2);

    EncadeadaBench e1;
    encadeada_criar(&e1);
    inicio = clock();
    for (int i = 0; i < N; i++) {
        encadeada_inserir_inicio(&e1, i);
    }
    fim = clock();
    tempo_encadeada_inicio = (double)(fim - inicio) / CLOCKS_PER_SEC;
    encadeada_destruir(&e1);

    EncadeadaBench e2;
    encadeada_criar(&e2);
    inicio = clock();
    for (int i = 0; i < N; i++) {
        encadeada_inserir_fim(&e2, i);
    }
    fim = clock();
    tempo_encadeada_fim = (double)(fim - inicio) / CLOCKS_PER_SEC;
    encadeada_destruir(&e2);

    printf("Inserindo %d elementos:\n\n", N);
    printf("%-30s %10s\n", "operacao", "tempo (s)");
    printf("%-30s %10.6f\n", "contigua  - inserir no inicio", tempo_array_inicio);
    printf("%-30s %10.6f\n", "contigua  - inserir no fim", tempo_array_fim);
    printf("%-30s %10.6f\n", "encadeada - inserir no inicio", tempo_encadeada_inicio);
    printf("%-30s %10.6f\n", "encadeada - inserir no fim", tempo_encadeada_fim);

    printf("\nO esperado pela tabela de complexidade (Exercicio 4):\n");
    printf("- 'contigua - inserir no inicio' deve ser a mais lenta (O(n) por insercao -> O(n^2) no total)\n");
    printf("- as outras tres devem ser proximas entre si e bem mais rapidas (O(1) por insercao -> O(n) no total)\n");

    return 0;
}
