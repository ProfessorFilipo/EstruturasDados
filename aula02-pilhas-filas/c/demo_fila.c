#include <stdio.h>
#include "fila.h"

static void mostrar_estado(const char *rotulo, const Fila *fila) {
    printf("%-25s ", rotulo);
    fila_exibir(fila);
}

int main(void) {
    Fila fila;
    int valor;
    fila_criar(&fila);

    mostrar_estado("0. fila criada:", &fila);
    fila_enfileirar(&fila, 101);
    mostrar_estado("1. enfileirar(101):", &fila);
    fila_enfileirar(&fila, 102);
    mostrar_estado("2. enfileirar(102):", &fila);
    fila_enfileirar(&fila, 103);
    mostrar_estado("3. enfileirar(103):", &fila);

    fila_consultar_frente(&fila, &valor);
    printf("4. consultar_frente():    %d (a fila nao muda)\n", valor);

    fila_desenfileirar(&fila, &valor);
    printf("5. desenfileirar():       removeu %d\n", valor);
    mostrar_estado("6. estado final:", &fila);

    fila_destruir(&fila);
    return 0;
}
