#include <stdio.h>
#include <stdlib.h>
#include "fila.h"

void fila_criar(Fila *fila) {
    fila->inicio = NULL;
    fila->fim = NULL;
    fila->tamanho = 0;
}

int fila_esta_vazia(const Fila *fila) {
    return fila->inicio == NULL;
}

int fila_tamanho(const Fila *fila) {
    return fila->tamanho;
}

int fila_enfileirar(Fila *fila, int valor) {
    NoFila *novo = malloc(sizeof(NoFila));
    if (novo == NULL) {
        return 0;
    }

    novo->valor = valor;
    novo->proximo = NULL;

    if (fila->fim == NULL) {
        fila->inicio = novo;
    } else {
        fila->fim->proximo = novo;
    }
    fila->fim = novo;
    fila->tamanho++;
    return 1;
}

int fila_desenfileirar(Fila *fila, int *valor) {
    if (fila_esta_vazia(fila)) {
        return 0;
    }

    NoFila *removido = fila->inicio;
    if (valor != NULL) {
        *valor = removido->valor;
    }

    fila->inicio = removido->proximo;
    if (fila->inicio == NULL) {
        fila->fim = NULL;
    }

    free(removido);
    fila->tamanho--;
    return 1;
}

int fila_consultar_frente(const Fila *fila, int *valor) {
    if (fila_esta_vazia(fila)) {
        return 0;
    }
    if (valor != NULL) {
        *valor = fila->inicio->valor;
    }
    return 1;
}

void fila_exibir(const Fila *fila) {
    if (fila_esta_vazia(fila)) {
        printf("[vazia]\n");
        return;
    }

    NoFila *atual = fila->inicio;
    while (atual != NULL) {
        printf("%d", atual->valor);
        if (atual->proximo != NULL) {
            printf(" ");
        }
        atual = atual->proximo;
    }
    printf("\n");
}

void fila_destruir(Fila *fila) {
    int ignorado;
    while (fila_desenfileirar(fila, &ignorado)) {
        /* cada chamada libera um no */
    }
}
