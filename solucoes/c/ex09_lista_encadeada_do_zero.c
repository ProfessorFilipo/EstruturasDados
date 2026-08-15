/*
 * ex09_lista_encadeada_do_zero.c — solução
 *
 * Implementação independente (não usa lista_encadeada.h/.c do
 * repositório) de uma lista encadeada mínima, com inserir_inicio e
 * percorrer, exatamente como o Exercício 9 pede.
 */
#include <stdio.h>
#include <stdlib.h>

typedef struct No {
    int valor;
    struct No *proximo;
} No;

typedef struct {
    No *inicio;
} ListaEncadeada;

void inserir_inicio(ListaEncadeada *lista, int valor) {
    No *novo = malloc(sizeof(No));
    novo->valor = valor;
    novo->proximo = lista->inicio;
    lista->inicio = novo;
}

void percorrer(const ListaEncadeada *lista) {
    No *atual = lista->inicio;
    while (atual != NULL) {
        printf("%d", atual->valor);
        if (atual->proximo != NULL) {
            printf(", ");
        }
        atual = atual->proximo;
    }
    printf("\n");
}

int main(void) {
    ListaEncadeada l;
    l.inicio = NULL;

    inserir_inicio(&l, 10);
    inserir_inicio(&l, 20);
    inserir_inicio(&l, 30);

    printf("esperado: 30, 20, 10\n");
    printf("obtido:   ");
    percorrer(&l);

    /* libera a memoria dos nos antes de encerrar */
    No *atual = l.inicio;
    while (atual != NULL) {
        No *proximo = atual->proximo;
        free(atual);
        atual = proximo;
    }

    return 0;
}
