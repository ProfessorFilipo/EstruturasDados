#include <stdio.h>
#include <stdlib.h>

#define CAPACIDADE 20

typedef struct {
    int dados[CAPACIDADE];
    int topo;
} Pilha;

typedef struct NoFila {
    int valor;
    struct NoFila *proximo;
} NoFila;

typedef struct {
    NoFila *inicio;
    NoFila *fim;
} Fila;

void pilha_criar(Pilha *pilha) {
    pilha->topo = -1;
}

int pilha_esta_vazia(const Pilha *pilha) {
    /* TODO 1 */
    (void)pilha;
    return 1;
}

int pilha_empilhar(Pilha *pilha, int valor) {
    /* TODO 2: verificar limite, incrementar topo e armazenar */
    (void)pilha;
    (void)valor;
    return 0;
}

int pilha_desempilhar(Pilha *pilha, int *valor) {
    /* TODO 3: tratar pilha vazia, devolver valor e decrementar topo */
    (void)pilha;
    (void)valor;
    return 0;
}

int pilha_consultar_topo(const Pilha *pilha, int *valor) {
    /* TODO 4: consultar sem remover */
    (void)pilha;
    (void)valor;
    return 0;
}

void pilha_exibir(const Pilha *pilha) {
    /* TODO 5: percorrer do topo para a base */
    (void)pilha;
    printf("[TODO]\n");
}

void fila_criar(Fila *fila) {
    fila->inicio = NULL;
    fila->fim = NULL;
}

int fila_esta_vazia(const Fila *fila) {
    /* TODO 6 */
    (void)fila;
    return 1;
}

int fila_enfileirar(Fila *fila, int valor) {
    /* TODO 7: alocar e ligar um novo no ao fim */
    (void)fila;
    (void)valor;
    return 0;
}

int fila_desenfileirar(Fila *fila, int *valor) {
    /* TODO 8: remover o inicio, usar free e atualizar o fim */
    (void)fila;
    (void)valor;
    return 0;
}

int fila_consultar_frente(const Fila *fila, int *valor) {
    /* TODO 9: consultar sem remover */
    (void)fila;
    (void)valor;
    return 0;
}

void fila_exibir(const Fila *fila) {
    /* TODO 10: percorrer do inicio ao fim */
    (void)fila;
    printf("[TODO]\n");
}

void fila_destruir(Fila *fila) {
    int ignorado;
    while (fila_desenfileirar(fila, &ignorado)) {
    }
}

int processar_proximo(Fila *espera, Pilha *historico) {
    /* TODO 11: desenfileirar, empilhar e imprimir */
    (void)espera;
    (void)historico;
    return 0;
}

int main(void) {
    Fila espera;
    Pilha historico;
    int valor;

    fila_criar(&espera);
    pilha_criar(&historico);

    fila_enfileirar(&espera, 101);
    fila_enfileirar(&espera, 102);
    fila_enfileirar(&espera, 103);
    processar_proximo(&espera, &historico);
    processar_proximo(&espera, &historico);
    fila_enfileirar(&espera, 104);

    printf("Fila de espera: ");
    fila_exibir(&espera);
    printf("Historico - topo para base: ");
    pilha_exibir(&historico);
    if (fila_consultar_frente(&espera, &valor)) {
        printf("Proximo trabalho: %d\n", valor);
    }
    if (pilha_consultar_topo(&historico, &valor)) {
        printf("Ultimo trabalho processado: %d\n", valor);
    }

    fila_destruir(&espera);
    return 0;
}
