/*
 * ex13_remover_duplicatas_encadeada.c — solução
 *
 * Remove valores duplicados de uma ListaEncadeada (do repositório),
 * mantendo apenas a primeira ocorrência de cada valor.
 * Compile junto com lista_encadeada.c — veja o Makefile desta pasta.
 *
 * Duas versões, como sugerido no enunciado:
 *  - remover_duplicatas_simples: usa um array auxiliar (alocado do
 *    tamanho da lista) para lembrar quais valores já viu. Mais fácil
 *    de entender, gasta memória extra proporcional ao tamanho da lista.
 *  - remover_duplicatas_sem_auxiliar: não usa nenhuma estrutura extra,
 *    mas paga um custo maior (compara cada nó com todos os anteriores,
 *    O(n²) no pior caso, igual à primeira versão em termos de tempo —
 *    a diferença real entre as duas está no espaço extra usado).
 */
#include <stdio.h>
#include <stdlib.h>
#include "lista_encadeada.h"

void remover_duplicatas_simples(ListaEncadeada *lista) {
    int n = lista_tamanho(lista);
    if (n == 0) {
        return;
    }
    int *vistos = malloc(n * sizeof(int));
    int qtd_vistos = 0;

    int pos = 0;
    while (pos < lista_tamanho(lista)) {
        int valor;
        lista_obter(lista, pos, &valor);

        int ja_visto = 0;
        for (int i = 0; i < qtd_vistos; i++) {
            if (vistos[i] == valor) {
                ja_visto = 1;
                break;
            }
        }

        if (ja_visto) {
            lista_remover(lista, pos, NULL); /* não avança 'pos': o próximo elemento ocupa esta posição agora */
        } else {
            vistos[qtd_vistos++] = valor;
            pos++;
        }
    }

    free(vistos);
}

void remover_duplicatas_sem_auxiliar(ListaEncadeada *lista) {
    No *atual = lista->inicio;
    while (atual != NULL) {
        No *comparador = atual;
        while (comparador->proximo != NULL) {
            if (comparador->proximo->valor == atual->valor) {
                /* encontrou uma duplicata do valor de 'atual' mais à
                 * frente na lista: remove pela posição, via a API
                 * pública, para manter 'fim' e o contador consistentes */
                int pos = 0;
                No *busca = lista->inicio;
                while (busca != comparador->proximo) {
                    busca = busca->proximo;
                    pos++;
                }
                lista_remover(lista, pos, NULL);
            } else {
                comparador = comparador->proximo;
            }
        }
        atual = atual->proximo;
    }
}

static void imprimir_lista(const char *rotulo, ListaEncadeada *lista) {
    printf("%s", rotulo);
    int n = lista_tamanho(lista);
    for (int i = 0; i < n; i++) {
        int valor;
        lista_obter(lista, i, &valor);
        printf("%d", valor);
        if (i < n - 1) {
            printf(", ");
        }
    }
}

int main(void) {
    ListaEncadeada l1;
    lista_criar(&l1);
    int valores[] = {5, 3, 5, 8, 3, 9};
    for (int i = 0; i < 6; i++) {
        lista_inserir_fim(&l1, valores[i]);
    }

    imprimir_lista("antes:                      ", &l1);
    remover_duplicatas_simples(&l1);
    imprimir_lista("\ndepois (versao simples):    ", &l1);
    printf("\nesperado:                    5, 3, 8, 9\n");
    lista_destruir(&l1);

    ListaEncadeada l2;
    lista_criar(&l2);
    for (int i = 0; i < 6; i++) {
        lista_inserir_fim(&l2, valores[i]);
    }
    remover_duplicatas_sem_auxiliar(&l2);
    imprimir_lista("\ndepois (sem auxiliar):       ", &l2);
    printf("\nesperado:                    5, 3, 8, 9\n");
    lista_destruir(&l2);

    return 0;
}
