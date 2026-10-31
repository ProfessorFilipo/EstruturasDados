/*
 * ex03_buscar_primeira.c — Aula 5, Exercício 3 (solução de referência)
 *
 * Busca binária que devolve a PRIMEIRA ocorrência de um valor num vetor
 * ordenado com repetições. Continua O(log n): quando acha o alvo, guarda a
 * posição e continua procurando à ESQUERDA.
 *
 * Arquivo único, só <stdio.h> — cole direto no onlineide.pro/playground/c
 */
#include <stdio.h>

int buscar_primeira(const int v[], int n, int alvo, int *comparacoes) {
    int inicio = 0, fim = n - 1, resposta = -1;
    *comparacoes = 0;
    while (inicio <= fim) {
        int meio = inicio + (fim - inicio) / 2;
        (*comparacoes)++;
        if (v[meio] == alvo) {
            resposta = meio;          /* achou... mas pode haver outro antes */
            fim = meio - 1;           /* continua procurando à esquerda */
        } else if (v[meio] < alvo) {
            inicio = meio + 1;
        } else {
            fim = meio - 1;
        }
    }
    return resposta;
}

int main(void) {
    const int paginas[] = {1, 3, 3, 3, 7, 7, 9, 12, 12, 12, 12, 20};
    const int n = (int)(sizeof paginas / sizeof paginas[0]);
    const int alvos[] = {12, 3, 1, 20, 5}, esperados[] = {7, 1, 0, 11, -1};
    printf("paginas ordenadas: [");
    for (int i = 0; i < n; i++) printf("%d%s", paginas[i], i < n - 1 ? ", " : "]\n");
    for (int t = 0; t < 5; t++) {
        int comp, pos = buscar_primeira(paginas, n, alvos[t], &comp);
        printf("   alvo %2d: posicao %2d, %d comparacoes  [%s]\n", alvos[t], pos, comp,
               pos == esperados[t] ? "ok" : "ERRO");
    }
    return 0;
}
