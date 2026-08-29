#ifndef FILA_H
#define FILA_H

typedef struct NoFila {
    int valor;
    struct NoFila *proximo;
} NoFila;

typedef struct {
    NoFila *inicio;
    NoFila *fim;
    int tamanho;
} Fila;

void fila_criar(Fila *fila);
int fila_esta_vazia(const Fila *fila);
int fila_tamanho(const Fila *fila);
int fila_enfileirar(Fila *fila, int valor);
int fila_desenfileirar(Fila *fila, int *valor);
int fila_consultar_frente(const Fila *fila, int *valor);
void fila_exibir(const Fila *fila);
void fila_destruir(Fila *fila);

#endif
