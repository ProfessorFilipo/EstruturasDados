#ifndef PILHA_H
#define PILHA_H

#define PILHA_CAPACIDADE 20

typedef struct {
    int dados[PILHA_CAPACIDADE];
    int topo;
} Pilha;

void pilha_criar(Pilha *pilha);
int pilha_esta_vazia(const Pilha *pilha);
int pilha_esta_cheia(const Pilha *pilha);
int pilha_tamanho(const Pilha *pilha);
int pilha_empilhar(Pilha *pilha, int valor);
int pilha_desempilhar(Pilha *pilha, int *valor);
int pilha_consultar_topo(const Pilha *pilha, int *valor);
void pilha_exibir(const Pilha *pilha);

#endif
