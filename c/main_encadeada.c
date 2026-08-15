/*
 * main_encadeada.c
 *
 * Demonstração de uso do TAD ListaEncadeada (Aula 1).
 * Compile e execute com: make encadeada && ./encadeada
 */
#include <stdio.h>
#include "lista_encadeada.h"

int main(void) {
    ListaEncadeada l;
    lista_criar(&l);

    lista_inserir_fim(&l, 10);
    lista_inserir_fim(&l, 20);
    lista_inserir_fim(&l, 30);
    lista_inserir_inicio(&l, 5);
    lista_inserir(&l, 2, 99); /* insere 99 no meio */

    printf("Lista apos as insercoes (tamanho = %d):\n", lista_tamanho(&l));
    lista_percorrer(&l);

    int pos = lista_buscar(&l, 99);
    printf("\nposicao de 99: %d\n", pos);

    int valor;
    if (lista_obter(&l, 0, &valor)) {
        printf("elemento na posicao 0: %d\n", valor);
    }

    int removido;
    lista_remover(&l, 2, &removido);
    printf("\nremovido da posicao 2: %d\n", removido);
    printf("Lista apos a remocao (tamanho = %d):\n", lista_tamanho(&l));
    lista_percorrer(&l);

    lista_destruir(&l); /* libera a memoria dos nos */
    return 0;
}
