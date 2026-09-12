/*
 * lista_encadeada.c
 *
 * Estruturas de Dados — Aula 1
 * Implementação do TAD Lista com nós ligados por ponteiros.
 */
#include <stdio.h>
#include <stdlib.h>
#include "lista_encadeada.h"

/* Função auxiliar interna: retorna um ponteiro para o nó na posição
 * 'pos' (0 <= pos < tamanho), ou NULL se a posição for inválida. */
static No *no_em(const ListaEncadeada *lista, int pos) {
    if (pos < 0 || pos >= lista->tamanho) {
        return NULL;
    }
    No *atual = lista->inicio;
    for (int i = 0; i < pos; i++) {
        atual = atual->proximo;
    }
    return atual;
}

void lista_criar(ListaEncadeada *lista) {
    lista->inicio = NULL;
    lista->fim = NULL;
    lista->tamanho = 0;
}

int lista_inserir_inicio(ListaEncadeada *lista, int valor) {
    No *novo = malloc(sizeof(No));
    if (novo == NULL) {
        return 0; /* memória insuficiente */
    }
    novo->valor = valor;
    novo->proximo = lista->inicio;
    lista->inicio = novo;
    if (lista->fim == NULL) {
        lista->fim = novo; /* lista estava vazia: novo nó também é o fim */
    }
    lista->tamanho++;
    return 1;
}

int lista_inserir_fim(ListaEncadeada *lista, int valor) {
    No *novo = malloc(sizeof(No));
    if (novo == NULL) {
        return 0; /* memória insuficiente */
    }
    novo->valor = valor;
    novo->proximo = NULL;

    if (lista->inicio == NULL) {
        lista->inicio = novo;
    } else {
        lista->fim->proximo = novo;
    }
    lista->fim = novo;
    lista->tamanho++;
    return 1;
}

int lista_inserir(ListaEncadeada *lista, int pos, int valor) {
    if (pos < 0 || pos > lista->tamanho) {
        return 0; /* posição inválida */
    }
    if (pos == 0) {
        return lista_inserir_inicio(lista, valor);
    }
    if (pos == lista->tamanho) {
        return lista_inserir_fim(lista, valor);
    }

    No *anterior = no_em(lista, pos - 1);
    No *novo = malloc(sizeof(No));
    if (novo == NULL) {
        return 0; /* memória insuficiente */
    }
    novo->valor = valor;
    novo->proximo = anterior->proximo;
    anterior->proximo = novo;
    lista->tamanho++;
    return 1;
}

int lista_remover(ListaEncadeada *lista, int pos, int *valor_removido) {
    if (pos < 0 || pos >= lista->tamanho) {
        return 0; /* posição inválida */
    }

    No *removido;
    if (pos == 0) {
        removido = lista->inicio;
        lista->inicio = removido->proximo;
        if (lista->inicio == NULL) {
            lista->fim = NULL; /* lista ficou vazia */
        }
    } else {
        No *anterior = no_em(lista, pos - 1);
        removido = anterior->proximo;
        anterior->proximo = removido->proximo;
        if (removido == lista->fim) {
            lista->fim = anterior;
        }
    }

    if (valor_removido != NULL) {
        *valor_removido = removido->valor;
    }
    free(removido);
    lista->tamanho--;
    return 1;
}

int lista_buscar(const ListaEncadeada *lista, int valor) {
    No *atual = lista->inicio;
    int pos = 0;
    while (atual != NULL) {
        if (atual->valor == valor) {
            return pos;
        }
        atual = atual->proximo;
        pos++;
    }
    return -1;
}

int lista_obter(const ListaEncadeada *lista, int pos, int *valor) {
    No *no = no_em(lista, pos);
    if (no == NULL) {
        return 0; /* posição inválida */
    }
    *valor = no->valor;
    return 1;
}

int lista_tamanho(const ListaEncadeada *lista) {
    return lista->tamanho;
}

void lista_percorrer(const ListaEncadeada *lista) {
    No *atual = lista->inicio;
    int pos = 0;
    while (atual != NULL) {
        printf("[%d] = %d\n", pos, atual->valor);
        atual = atual->proximo;
        pos++;
    }
}

void lista_destruir(ListaEncadeada *lista) {
    No *atual = lista->inicio;
    while (atual != NULL) {
        No *proximo = atual->proximo;
        free(atual);
        atual = proximo;
    }
    lista->inicio = NULL;
    lista->fim = NULL;
    lista->tamanho = 0;
}
