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

void pilha_criar(Pilha *p) { p->topo = -1; }
int pilha_esta_vazia(const Pilha *p) { return p->topo == -1; }

int pilha_empilhar(Pilha *p, int valor) {
    if (p->topo == CAPACIDADE - 1) return 0;
    p->dados[++p->topo] = valor;
    return 1;
}

int pilha_desempilhar(Pilha *p, int *valor) {
    if (pilha_esta_vazia(p)) return 0;
    if (valor != NULL) *valor = p->dados[p->topo];
    p->topo--;
    return 1;
}

int pilha_consultar_topo(const Pilha *p, int *valor) {
    if (pilha_esta_vazia(p)) return 0;
    if (valor != NULL) *valor = p->dados[p->topo];
    return 1;
}

void pilha_exibir(const Pilha *p) {
    for (int i = p->topo; i >= 0; i--) {
        printf("%d%s", p->dados[i], i > 0 ? " " : "");
    }
    printf("\n");
}

void fila_criar(Fila *f) { f->inicio = NULL; f->fim = NULL; }
int fila_esta_vazia(const Fila *f) { return f->inicio == NULL; }

int fila_enfileirar(Fila *f, int valor) {
    NoFila *novo = malloc(sizeof(NoFila));
    if (novo == NULL) return 0;
    novo->valor = valor;
    novo->proximo = NULL;
    if (f->fim == NULL) f->inicio = novo;
    else f->fim->proximo = novo;
    f->fim = novo;
    return 1;
}

int fila_desenfileirar(Fila *f, int *valor) {
    if (fila_esta_vazia(f)) return 0;
    NoFila *removido = f->inicio;
    if (valor != NULL) *valor = removido->valor;
    f->inicio = removido->proximo;
    if (f->inicio == NULL) f->fim = NULL;
    free(removido);
    return 1;
}

int fila_consultar_frente(const Fila *f, int *valor) {
    if (fila_esta_vazia(f)) return 0;
    if (valor != NULL) *valor = f->inicio->valor;
    return 1;
}

void fila_exibir(const Fila *f) {
    for (NoFila *atual = f->inicio; atual != NULL; atual = atual->proximo) {
        printf("%d%s", atual->valor, atual->proximo != NULL ? " " : "");
    }
    printf("\n");
}

void fila_destruir(Fila *f) {
    int ignorado;
    while (fila_desenfileirar(f, &ignorado)) { }
}

int processar_proximo(Fila *espera, Pilha *historico) {
    int trabalho;
    if (!fila_desenfileirar(espera, &trabalho)) return 0;
    if (!pilha_empilhar(historico, trabalho)) return 0;
    printf("Trabalho processado: %d\n", trabalho);
    return 1;
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
    printf("Fila de espera: "); fila_exibir(&espera);
    printf("Historico - topo para base: "); pilha_exibir(&historico);
    fila_consultar_frente(&espera, &valor);
    printf("Proximo trabalho: %d\n", valor);
    pilha_consultar_topo(&historico, &valor);
    printf("Ultimo trabalho processado: %d\n", valor);
    fila_destruir(&espera);
    return 0;
}
