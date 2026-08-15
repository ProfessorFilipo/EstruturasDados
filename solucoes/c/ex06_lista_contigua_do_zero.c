/*
 * ex06_lista_contigua_do_zero.c — solução
 *
 * Implementação independente (não usa lista_contigua.h/.c do
 * repositório) de uma lista contígua mínima, com inserir_fim e buscar,
 * exatamente como o Exercício 6 pede.
 */
#include <stdio.h>

#define CAPACIDADE_MAX 100

typedef struct {
    int dados[CAPACIDADE_MAX];
    int tamanho;
} ListaContigua;

void inserir_fim(ListaContigua *lista, int valor) {
    lista->dados[lista->tamanho] = valor;
    lista->tamanho++;
}

int buscar(const ListaContigua *lista, int valor) {
    for (int i = 0; i < lista->tamanho; i++) {
        if (lista->dados[i] == valor) {
            return i;
        }
    }
    return -1;
}

int main(void) {
    ListaContigua l;
    l.tamanho = 0;

    inserir_fim(&l, 10);
    inserir_fim(&l, 20);
    inserir_fim(&l, 30);

    printf("buscar(20) = %d (esperado: 1)\n", buscar(&l, 20));
    printf("buscar(99) = %d (esperado: -1)\n", buscar(&l, 99));

    return 0;
}
