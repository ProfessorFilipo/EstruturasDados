/*
 * lista_contigua.c
 *
 * Estruturas de Dados — Aula 1
 * Implementação do TAD Lista sobre um array (estrutura contígua).
 */
#include <stdio.h>
#include "lista_contigua.h"

void lista_criar(ListaContigua *lista) {
    lista->tamanho = 0;
}

int lista_inserir(ListaContigua *lista, int pos, int valor) {
    if (pos < 0 || pos > lista->tamanho) {
        return 0; /* posição inválida */
    }
    if (lista->tamanho >= LISTA_CAPACIDADE_MAX) {
        return 0; /* lista cheia */
    }

    /* desloca os elementos de pos em diante uma posição à frente,
     * de trás para frente para não sobrescrever dados */
    for (int i = lista->tamanho; i > pos; i--) {
        lista->dados[i] = lista->dados[i - 1];
    }

    lista->dados[pos] = valor;
    lista->tamanho++;
    return 1;
}

int lista_inserir_inicio(ListaContigua *lista, int valor) {
    return lista_inserir(lista, 0, valor);
}

int lista_inserir_fim(ListaContigua *lista, int valor) {
    return lista_inserir(lista, lista->tamanho, valor);
}

int lista_remover(ListaContigua *lista, int pos, int *valor_removido) {
    if (pos < 0 || pos >= lista->tamanho) {
        return 0; /* posição inválida */
    }

    if (valor_removido != NULL) {
        *valor_removido = lista->dados[pos];
    }

    /* desloca os elementos seguintes uma posição para trás */
    for (int i = pos; i < lista->tamanho - 1; i++) {
        lista->dados[i] = lista->dados[i + 1];
    }

    lista->tamanho--;
    return 1;
}

int lista_buscar(const ListaContigua *lista, int valor) {
    for (int i = 0; i < lista->tamanho; i++) {
        if (lista->dados[i] == valor) {
            return i;
        }
    }
    return -1;
}

int lista_obter(const ListaContigua *lista, int pos, int *valor) {
    if (pos < 0 || pos >= lista->tamanho) {
        return 0; /* posição inválida */
    }
    *valor = lista->dados[pos];
    return 1;
}

int lista_tamanho(const ListaContigua *lista) {
    return lista->tamanho;
}

void lista_percorrer(const ListaContigua *lista) {
    for (int i = 0; i < lista->tamanho; i++) {
        printf("[%d] = %d\n", i, lista->dados[i]);
    }
}
