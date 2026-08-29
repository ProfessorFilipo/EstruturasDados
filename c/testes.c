#include <assert.h>
#include <stdio.h>
#include "fila.h"
#include "pilha.h"

static void testar_pilha(void) {
    Pilha p;
    int valor = 0;
    pilha_criar(&p);
    assert(pilha_esta_vazia(&p));
    assert(!pilha_desempilhar(&p, &valor));
    assert(pilha_empilhar(&p, 10));
    assert(pilha_empilhar(&p, 20));
    assert(pilha_tamanho(&p) == 2);
    assert(pilha_consultar_topo(&p, &valor) && valor == 20);
    assert(pilha_desempilhar(&p, &valor) && valor == 20);
    assert(pilha_desempilhar(&p, &valor) && valor == 10);
    assert(pilha_esta_vazia(&p));
}

static void testar_fila(void) {
    Fila f;
    int valor = 0;
    fila_criar(&f);
    assert(fila_esta_vazia(&f));
    assert(!fila_desenfileirar(&f, &valor));
    assert(fila_enfileirar(&f, 101));
    assert(fila_enfileirar(&f, 102));
    assert(fila_tamanho(&f) == 2);
    assert(fila_consultar_frente(&f, &valor) && valor == 101);
    assert(fila_desenfileirar(&f, &valor) && valor == 101);
    assert(fila_desenfileirar(&f, &valor) && valor == 102);
    assert(f.inicio == NULL && f.fim == NULL && f.tamanho == 0);
    fila_destruir(&f);
}

int main(void) {
    testar_pilha();
    testar_fila();
    printf("Todos os testes em C passaram.\n");
    return 0;
}
