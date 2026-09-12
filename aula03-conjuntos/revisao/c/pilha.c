#include <stdio.h>
#include "pilha.h"

void pilha_criar(Pilha *pilha) {
    pilha->topo = -1;
}

int pilha_esta_vazia(const Pilha *pilha) {
    return pilha->topo == -1;
}

int pilha_esta_cheia(const Pilha *pilha) {
    return pilha->topo == PILHA_CAPACIDADE - 1;
}

int pilha_tamanho(const Pilha *pilha) {
    return pilha->topo + 1;
}

int pilha_empilhar(Pilha *pilha, int valor) {
    if (pilha_esta_cheia(pilha)) {
        return 0;
    }
    pilha->topo++;
    pilha->dados[pilha->topo] = valor;
    return 1;
}

int pilha_desempilhar(Pilha *pilha, int *valor) {
    if (pilha_esta_vazia(pilha)) {
        return 0;
    }
    if (valor != NULL) {
        *valor = pilha->dados[pilha->topo];
    }
    pilha->topo--;
    return 1;
}

int pilha_consultar_topo(const Pilha *pilha, int *valor) {
    if (pilha_esta_vazia(pilha)) {
        return 0;
    }
    if (valor != NULL) {
        *valor = pilha->dados[pilha->topo];
    }
    return 1;
}

void pilha_exibir(const Pilha *pilha) {
    if (pilha_esta_vazia(pilha)) {
        printf("[vazia]\n");
        return;
    }
    for (int i = pilha->topo; i >= 0; i--) {
        printf("%d", pilha->dados[i]);
        if (i > 0) {
            printf(" ");
        }
    }
    printf("\n");
}
