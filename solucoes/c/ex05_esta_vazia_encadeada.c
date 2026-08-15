/*
 * ex05_esta_vazia_encadeada.c — solução
 *
 * Estende o TAD ListaEncadeada (do repositório) com esta_vazia().
 * Compile junto com lista_encadeada.c — veja o Makefile desta pasta.
 */
#include <stdio.h>
#include "lista_encadeada.h"

int esta_vazia(const ListaEncadeada *lista) {
    return lista_tamanho(lista) == 0;
}

int main(void) {
    ListaEncadeada l;
    lista_criar(&l);

    printf("lista recem-criada, esta_vazia = %d\n", esta_vazia(&l));

    lista_inserir_fim(&l, 42);
    printf("apos inserir um elemento, esta_vazia = %d\n", esta_vazia(&l));

    int removido;
    lista_remover(&l, 0, &removido);
    printf("apos remover o unico elemento, esta_vazia = %d\n", esta_vazia(&l));

    lista_destruir(&l);
    return 0;
}
