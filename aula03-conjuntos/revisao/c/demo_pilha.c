#include <stdio.h>
#include "pilha.h"

static void mostrar_estado(const char *rotulo, const Pilha *pilha) {
    printf("%-25s ", rotulo);
    pilha_exibir(pilha);
}

int main(void) {
    Pilha pilha;
    int valor;
    pilha_criar(&pilha);

    mostrar_estado("0. pilha criada:", &pilha);
    pilha_empilhar(&pilha, 10);
    mostrar_estado("1. empilhar(10):", &pilha);
    pilha_empilhar(&pilha, 20);
    mostrar_estado("2. empilhar(20):", &pilha);

    pilha_consultar_topo(&pilha, &valor);
    printf("3. consultar_topo():      %d (a pilha nao muda)\n", valor);

    pilha_desempilhar(&pilha, &valor);
    printf("4. desempilhar():         removeu %d\n", valor);
    mostrar_estado("5. estado final:", &pilha);
    return 0;
}
