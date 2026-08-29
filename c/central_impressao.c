#include <stdio.h>
#include <stdlib.h>
#include "fila.h"
#include "pilha.h"

static void exigir(int condicao, const char *mensagem) {
    if (!condicao) {
        fprintf(stderr, "Erro: %s\n", mensagem);
        exit(EXIT_FAILURE);
    }
}

static int processar_proximo(Fila *espera, Pilha *historico) {
    int trabalho;
    if (!fila_desenfileirar(espera, &trabalho)) {
        return 0;
    }
    exigir(pilha_empilhar(historico, trabalho), "historico cheio");
    printf("Trabalho processado: %d\n", trabalho);
    return 1;
}

int main(void) {
    Fila espera;
    Pilha historico;
    int valor;

    fila_criar(&espera);
    pilha_criar(&historico);

    exigir(fila_enfileirar(&espera, 101), "nao foi possivel criar o trabalho 101");
    exigir(fila_enfileirar(&espera, 102), "nao foi possivel criar o trabalho 102");
    exigir(fila_enfileirar(&espera, 103), "nao foi possivel criar o trabalho 103");

    exigir(processar_proximo(&espera, &historico), "fila vazia");
    exigir(processar_proximo(&espera, &historico), "fila vazia");
    exigir(fila_enfileirar(&espera, 104), "nao foi possivel criar o trabalho 104");

    printf("Fila de espera: ");
    fila_exibir(&espera);
    printf("Historico - topo para base: ");
    pilha_exibir(&historico);

    exigir(fila_consultar_frente(&espera, &valor), "fila vazia");
    printf("Proximo trabalho: %d\n", valor);
    exigir(pilha_consultar_topo(&historico, &valor), "historico vazio");
    printf("Ultimo trabalho processado: %d\n", valor);

    fila_destruir(&espera);
    return 0;
}
