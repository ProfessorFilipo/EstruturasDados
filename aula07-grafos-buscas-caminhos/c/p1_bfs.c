/*
 * p1_bfs.c
 *
 * Estruturas de Dados — Aula 7 — Prática P1 (Busca em largura — BFS)
 * Slides 05 a 09 (teoria) e 31 (prática) · versão em C de python/p1_bfs.py
 *
 * Quantos SALTOS separam o roteador 1 de cada um dos outros? A BFS explora
 * o grafo em "ondas", organizadas por uma FILA (Aula 2). Como cada vértice
 * entra na fila no máximo uma vez, um vetor de N posições basta para ela.
 *
 * A lista de adjacências é CONTÍGUA (um vetor de vizinhos por vértice) e
 * está na MESMA ordem do livro de Ascencio & Araújo (p. 391).
 *
 * Custo: O(V + E). A saída é idêntica à da versão em Python.
 * Arquivo único, só <stdio.h> — cole direto no onlineide.pro/playground/c
 */
#include <stdio.h>

#define N 6
#define ORIGEM 1                        /* troque e rode de novo! */

/* posição 0 sem uso, como no livro */
static const int GRAU[N + 1]   = {0, 2, 4, 4, 2, 4, 4};
static const int ADJ[N + 1][4] = {
    {0},
    {6, 2},                             /* vizinhos de 1 */
    {5, 3, 1, 6},                       /* vizinhos de 2 */
    {6, 5, 4, 2},                       /* vizinhos de 3 */
    {5, 3},                             /* vizinhos de 4 */
    {6, 4, 3, 2},                       /* vizinhos de 5 */
    {5, 3, 2, 1}                        /* vizinhos de 6 */
};

/* ------------------------------------------------------------------ */
/* Versão "limpa", idêntica à do slide.                                */
/* ------------------------------------------------------------------ */
void bfs(int s, int dist[], int pai[]) {
    int marcado[N + 1] = {0};
    int fila[N], ini = 0, fim = 0;      /* fila em vetor: tira em ini, põe em fim */
    int v, k;
    for (v = 0; v <= N; v++) { dist[v] = -1; pai[v] = 0; }
    fila[fim++] = s;
    marcado[s] = 1;
    dist[s] = 0;
    while (ini < fim) {                 /* enquanto a fila não está vazia */
        int u = fila[ini++];            /* tira o primeiro da fila */
        for (k = 0; k < GRAU[u]; k++) {
            int w = ADJ[u][k];
            if (!marcado[w]) {          /* vizinho novo? */
                marcado[w] = 1;
                dist[w] = dist[u] + 1;  /* um salto a mais que u */
                pai[w] = u;             /* chegamos em w vindo de u */
                fila[fim++] = w;        /* entra no fim da fila */
            }
        }
    }
}

/* Reconstrói o caminho origem -> destino seguindo pai[] de trás para frente.
 * Grava em c[] e devolve o tamanho. */
int caminho(const int pai[], int destino, int c[]) {
    int tmp[N + 1], t = 0, i;
    tmp[t++] = destino;
    while (pai[tmp[t - 1]] != 0) { tmp[t] = pai[tmp[t - 1]]; t++; }
    for (i = 0; i < t; i++) c[i] = tmp[t - 1 - i];  /* inverte */
    return t;
}

/* escreve um vetor no formato de lista do Python ("[6, 2]") em buf */
void vetor_str(char *buf, const int v[], int ini, int fim) {
    int i, n = sprintf(buf, "[");
    for (i = ini; i < fim; i++) n += sprintf(buf + n, "%s%d", i > ini ? ", " : "", v[i]);
    sprintf(buf + n, "]");
}

/* A mesma BFS, mostrando cada passo (para a demonstração). */
void bfs_passo_a_passo(int s, int dist[], int pai[], int ordem[]) {
    int marcado[N + 1] = {0};
    int fila[N], ini = 0, fim = 0, nordem = 0, v, k;
    char sviz[64], sfila[64], sent[16];
    for (v = 0; v <= N; v++) { dist[v] = -1; pai[v] = 0; }
    fila[fim++] = s;
    marcado[s] = 1;
    dist[s] = 0;
    vetor_str(sfila, fila, ini, fim);
    printf("   inicio: marca %d, dist[%d] = 0, fila = %s\n", s, s, sfila);
    while (ini < fim) {
        int u = fila[ini++], n = 0;
        ordem[nordem++] = u;
        sent[0] = '\0';
        for (k = 0; k < GRAU[u]; k++) {
            int w = ADJ[u][k];
            if (!marcado[w]) {
                marcado[w] = 1;
                dist[w] = dist[u] + 1;
                pai[w] = u;
                fila[fim++] = w;
                n += sprintf(sent + n, "%s%d", n > 0 ? " " : "", w);
            }
        }
        if (n == 0) sprintf(sent, "-");
        vetor_str(sviz, ADJ[u], 0, GRAU[u]);
        vetor_str(sfila, fila, ini, fim);
        printf("   tira %d | vizinhos %-12s | entram: %-5s | fila = %s\n", u, sviz, sent, sfila);
    }
}

int main(void) {
    int dist[N + 1], pai[N + 1], ordem[N], d2[N + 1], p2[N + 1], c[N + 1];
    int v, i, t;

    printf("1) BFS a partir do roteador %d, passo a passo\n", ORIGEM);
    bfs_passo_a_passo(ORIGEM, dist, pai, ordem);
    bfs(ORIGEM, d2, p2);                            /* confere com a versão limpa */
    for (v = 1; v <= N; v++) if (d2[v] != dist[v] || p2[v] != pai[v]) return 1;
    printf("   ordem de visita:");
    for (i = 0; i < N; i++) printf(" %d", ordem[i]);
    printf("\n");

    printf("\n2) Distancia (saltos) e pai de cada vertice\n");
    printf("   vertice: ");
    for (v = 1; v <= N; v++) printf("%s%2d", v > 1 ? " " : "", v);
    printf("\n   dist:    ");
    for (v = 1; v <= N; v++) printf("%s%2d", v > 1 ? " " : "", dist[v]);
    printf("\n   pai:     ");
    for (v = 1; v <= N; v++) printf("%s%2d", v > 1 ? " " : "", pai[v]);
    printf("\n");

    printf("\n3) Caminho com MENOS saltos ate cada roteador (seguindo pai[])\n");
    for (v = 1; v <= N; v++) {
        char s[64];
        int n = 0;
        t = caminho(pai, v, c);
        for (i = 0; i < t; i++) n += sprintf(s + n, "%s%d", i > 0 ? " -> " : "", c[i]);
        printf("   ate %d: %-20s (%d salto(s))\n", v, s, dist[v]);
    }
    return 0;
}
