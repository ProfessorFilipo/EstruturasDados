/*
 * ex10_amigos_em_comum.c — Solução do Exercício 10 (Aula 6)
 *
 *   - amigos_em_comum(u, v): quem está na lista de u E na de v
 *   - sugerir_amizade(u): entre os NÃO amigos de u, quem tem mais amigos
 *     em comum com u (empate: o de menor número)
 *
 * Lista de adjacências para percorrer os amigos; matriz para testar
 * "x é amigo de v?" em O(1).
 * Saída idêntica à da versão em Python. Só <stdio.h>.
 */
#include <stdio.h>

#define N 8
#define NAMIZADES 12

static const char *NOMES[N + 1] = {"", "Ana", "Bruno", "Carla", "Davi",
                                   "Elisa", "Fabio", "Gabi", "Hugo"};
static const int AMIZADES[NAMIZADES][2] = {
    {1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 5}, {3, 5}, {3, 6},
    {4, 5}, {4, 6}, {5, 7}, {6, 7}, {7, 8}
};

int viz[N + 1][N], grau[N + 1];         /* lista de adjacências contígua */
int m[N + 1][N + 1];                    /* matriz de adjacências */

void montar(void) {
    int i;
    for (i = 0; i < NAMIZADES; i++) {
        int u = AMIZADES[i][0], v = AMIZADES[i][1];
        viz[u][grau[u]++] = v;
        viz[v][grau[v]++] = u;
        m[u][v] = m[v][u] = 1;
    }
}

/* grava os amigos em comum em comuns[] e devolve quantos são */
int amigos_em_comum(int u, int v, int comuns[]) {
    int k, qtd = 0;
    for (k = 0; k < grau[u]; k++) {     /* percorre os amigos de u... */
        int x = viz[u][k];
        if (m[x][v] == 1) comuns[qtd++] = x;   /* ...e testa na matriz: O(1) */
    }
    return qtd;
}

int sugerir_amizade(int u, int *melhor_qtd) {
    int v, melhor = 0, comuns[N];
    *melhor_qtd = -1;
    for (v = 1; v <= N; v++) {
        int qtd;
        if (v == u || m[u][v] == 1) continue;   /* é o próprio u ou já é amigo */
        qtd = amigos_em_comum(u, v, comuns);
        if (qtd > *melhor_qtd) { melhor = v; *melhor_qtd = qtd; }
    }
    return melhor;
}

void imprimir_nomes(const int lista[], int n) {
    int i;
    if (n == 0) { printf("(ninguem)"); return; }
    for (i = 0; i < n; i++) printf("%s%s", i > 0 ? ", " : "", NOMES[lista[i]]);
}

int main(void) {
    int pares[3][2] = {{1, 5}, {2, 4}, {1, 8}};
    int comuns[N], i, u;

    montar();
    printf("1) Amigos em comum\n");
    for (i = 0; i < 3; i++) {
        int a = pares[i][0], b = pares[i][1];
        int qtd = amigos_em_comum(a, b, comuns);
        printf("   %s e %s: ", NOMES[a], NOMES[b]);
        imprimir_nomes(comuns, qtd);
        printf("\n");
    }

    printf("\n2) Sugestao de amizade (quem tem mais amigos em comum)\n");
    for (u = 1; u <= N; u++) {
        int qtd, v = sugerir_amizade(u, &qtd);
        printf("   para %-6s-> %-6s (%d em comum)\n", NOMES[u], NOMES[v], qtd);
    }
    return 0;
}
