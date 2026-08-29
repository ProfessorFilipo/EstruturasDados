/*
 * ex11_inverter_encadeada.c — solução
 *
 * Inverte uma ListaEncadeada (do repositório) religando os nós
 * já existentes, sem alocar nenhum nó novo.
 * Compile junto com lista_encadeada.c — veja o Makefile desta pasta.
 */
#include <stdio.h>
#include "lista_encadeada.h"

void inverter(ListaEncadeada *lista) {
    No *anterior = NULL;
    No *atual = lista->inicio;

    lista->fim = lista->inicio; /* o antigo inicio vira o novo fim */

    while (atual != NULL) {
        No *proximo = atual->proximo; /* guarda o resto da lista antes de sobrescrever */
        atual->proximo = anterior;    /* inverte a seta deste no */
        anterior = atual;             /* avanca 'anterior' */
        atual = proximo;              /* avanca 'atual' */
    }

    lista->inicio = anterior; /* o ultimo no visitado vira o novo inicio */
}

int main(void) {
    ListaEncadeada l;
    lista_criar(&l);

    lista_inserir_fim(&l, 10);
    lista_inserir_fim(&l, 20);
    lista_inserir_fim(&l, 30);

    printf("antes:    ");
    lista_percorrer(&l);

    inverter(&l);

    printf("\nesperado: 30, 20, 10\n");
    printf("depois:   ");
    lista_percorrer(&l);

    /* confirma que 'fim' tambem ficou consistente apos a inversao */
    int ultimo;
    lista_obter(&l, lista_tamanho(&l) - 1, &ultimo);
    printf("\nlista->fim aponta para o valor %d (deve ser 10)\n", ultimo);

    lista_destruir(&l);
    return 0;
}
