/*
 * ex12_contigua_para_encadeada.c — solução
 *
 * Converte uma ListaContigua (do repositório) em uma lista encadeada
 * equivalente.
 *
 * Nota de organização: este arquivo usa apenas lista_contigua.h — não
 * lista_encadeada.h. Os dois cabeçalhos do repositório reutilizam os
 * mesmos nomes de função (lista_criar, lista_tamanho, etc.) para tipos
 * diferentes, o que é normal quando cada um é usado em seu próprio
 * programa, mas colide se os dois forem incluídos e linkados juntos no
 * mesmo executável. Por isso, o lado "encadeado" da conversão usa aqui
 * uma struct e funções próprias (No/Encadeada), com nomes que não
 * colidem — o comportamento é idêntico ao de lista_encadeada.c.
 */
#include <stdio.h>
#include <stdlib.h>
#include "lista_contigua.h"

typedef struct No {
    int valor;
    struct No *proximo;
} No;

typedef struct {
    No *inicio;
    No *fim;
} Encadeada;

void encadeada_criar(Encadeada *lista) {
    lista->inicio = NULL;
    lista->fim = NULL;
}

void encadeada_inserir_fim(Encadeada *lista, int valor) {
    No *novo = malloc(sizeof(No));
    novo->valor = valor;
    novo->proximo = NULL;
    if (lista->inicio == NULL) {
        lista->inicio = novo;
    } else {
        lista->fim->proximo = novo;
    }
    lista->fim = novo;
}

void encadeada_percorrer(const Encadeada *lista) {
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

void encadeada_destruir(Encadeada *lista) {
    No *atual = lista->inicio;
    while (atual != NULL) {
        No *proximo = atual->proximo;
        free(atual);
        atual = proximo;
    }
    lista->inicio = NULL;
    lista->fim = NULL;
}

/* a conversão em si: só usa a interface pública de ListaContigua */
void contigua_para_encadeada(const ListaContigua *origem, Encadeada *destino) {
    encadeada_criar(destino);
    for (int i = 0; i < lista_tamanho(origem); i++) {
        int valor;
        lista_obter(origem, i, &valor);
        encadeada_inserir_fim(destino, valor);
    }
}

int main(void) {
    ListaContigua c;
    lista_criar(&c);
    lista_inserir_fim(&c, 5);
    lista_inserir_fim(&c, 10);
    lista_inserir_fim(&c, 15);

    Encadeada e;
    contigua_para_encadeada(&c, &e);

    printf("contigua:  ");
    lista_percorrer(&c);

    printf("\nencadeada: ");
    encadeada_percorrer(&e);

    encadeada_destruir(&e);
    return 0;
}
