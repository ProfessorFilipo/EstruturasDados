/*
 * ex08_remover_valor_contigua.c — solução
 *
 * Estende o TAD ListaContigua (do repositório) com remover_valor(),
 * reaproveitando buscar() + remover() por posição já existentes.
 * Compile junto com lista_contigua.c — veja o Makefile desta pasta.
 */
#include <stdio.h>
#include "lista_contigua.h"

/* Retorna 1 se removeu, 0 se o valor não existia na lista. */
int remover_valor(ListaContigua *lista, int valor) {
    int pos = lista_buscar(lista, valor);
    if (pos == -1) {
        return 0; /* valor não encontrado */
    }
    return lista_remover(lista, pos, NULL);
}

int main(void) {
    ListaContigua l;
    lista_criar(&l);

    lista_inserir_fim(&l, 10);
    lista_inserir_fim(&l, 20);
    lista_inserir_fim(&l, 30);
    lista_inserir_fim(&l, 20); /* valor repetido, de propósito */

    printf("antes:\n");
    lista_percorrer(&l);

    int removeu = remover_valor(&l, 20);
    printf("\nremover_valor(20) -> %s\n", removeu ? "removeu" : "nao encontrado");
    printf("depois (so a PRIMEIRA ocorrencia de 20 deve sair):\n");
    lista_percorrer(&l);

    int removeu_inexistente = remover_valor(&l, 999);
    printf("\nremover_valor(999) -> %s (esperado: nao encontrado)\n",
           removeu_inexistente ? "removeu" : "nao encontrado");

    return 0;
}
