/*
 * p4_dijkstra.c
 *
 * Estruturas de Dados — Aula 7 — Prática P4 (Caminho mínimo — Dijkstra)
 * Slides 21 a 25 (teoria) e 34 (prática) · versão em C de python/p4_dijkstra.py
 *
 * Cada cabo da rede da filial tem uma LATÊNCIA (ms) — os mesmos pesos do
 * exemplo do livro de Ascencio & Araújo (p. 409). Qual é a rota mais RÁPIDA
 * do roteador 1 até cada um dos outros?
 *
 * Dijkstra, versão simples O(V^2):
 *   1. dist[origem] = 0; todos os outros = INF
 *   2. repita: escolha o vértice ABERTO com a menor dist e FECHE-o;
 *              RELAXE cada vizinho v: se dist[u] + peso < dist[v], melhore v
 * Só funciona com pesos NÃO NEGATIVOS.
 *
 * A saída é idêntica à da versão em Python.
 * Arquivo único, só <stdio.h> — cole direto no onlineide.pro/playground/c
 */
#include <stdio.h>

#define N 6
#define ORIGEM 1
#define INF 1000000000                  /* "infinito": maior que qualquer rota */

static const int GRAU[N + 1]    = {0, 2, 4, 4, 2, 4, 4};
static const int VIZ[N + 1][4]  = {     /* vizinhos, na ordem do livro */
    {0}, {6, 2}, {6, 5, 3, 1}, {6, 5, 4, 2}, {5, 3}, {6, 4, 3, 2}, {5, 3, 2, 1}
};
static const int PESO[N + 1][4] = {     /* latência (ms) do cabo correspondente */
    {0}, {7, 2}, {4, 3, 9, 2}, {3, 4, 5, 9}, {3, 5}, {1, 3, 4, 3}, {1, 3, 4, 7}
};

/* ------------------------------------------------------------------ */
/* Versão "limpa", idêntica à do slide.                                */
/* ------------------------------------------------------------------ */
void dijkstra(int s, int dist[], int pai[]) {
    int fechado[N + 1] = {0};
    int r, v, k;
    for (v = 0; v <= N; v++) { dist[v] = INF; pai[v] = 0; }
    dist[s] = 0;
    for (r = 0; r < N; r++) {
        int u = -1;                     /* acha o aberto com menor dist: O(V) */
        for (v = 1; v <= N; v++)
            if (!fechado[v] && (u == -1 || dist[v] < dist[u])) u = v;
        if (dist[u] == INF) break;      /* o resto é inalcançável */
        fechado[u] = 1;
        for (k = 0; k < GRAU[u]; k++) { /* relaxamento */
            int w = VIZ[u][k], peso = PESO[u][k];
            if (!fechado[w] && dist[u] + peso < dist[w]) {
                dist[w] = dist[u] + peso;
                pai[w] = u;
            }
        }
    }
}

int caminho(const int pai[], int destino, int c[]) {
    int tmp[N + 1], t = 0, i;
    tmp[t++] = destino;
    while (pai[tmp[t - 1]] != 0) { tmp[t] = pai[tmp[t - 1]]; t++; }
    for (i = 0; i < t; i++) c[i] = tmp[t - 1 - i];
    return t;
}

void imprime_dist(int d, int largura) {
    if (d == INF) printf("%*s", largura, "INF");
    else printf("%*d", largura, d);
}

/* O mesmo Dijkstra, imprimindo a tabela de cada rodada. */
void dijkstra_passo_a_passo(int s, int dist[], int pai[]) {
    int fechado[N + 1] = {0};
    int r, v, k;
    for (v = 0; v <= N; v++) { dist[v] = INF; pai[v] = 0; }
    dist[s] = 0;
    printf("   rodada fecha |");
    for (v = 1; v <= N; v++) printf("%5d", v);
    printf("\n   inicio       |");
    for (v = 1; v <= N; v++) imprime_dist(dist[v], 5);
    printf("\n");
    for (r = 1; r <= N; r++) {
        int u = -1;
        for (v = 1; v <= N; v++)
            if (!fechado[v] && (u == -1 || dist[v] < dist[u])) u = v;
        if (dist[u] == INF) break;
        fechado[u] = 1;
        for (k = 0; k < GRAU[u]; k++) {
            int w = VIZ[u][k], peso = PESO[u][k];
            if (!fechado[w] && dist[u] + peso < dist[w]) {
                dist[w] = dist[u] + peso;
                pai[w] = u;
            }
        }
        printf("   %6d %5d |", r, u);
        for (v = 1; v <= N; v++) imprime_dist(dist[v], 5);
        printf("\n");
    }
}

/* BFS ignorando os pesos (só para comparar com o Dijkstra). */
void bfs_saltos(int s, int pai[]) {
    int marcado[N + 1] = {0}, fila[N], ini = 0, fim = 0, v, k;
    for (v = 0; v <= N; v++) pai[v] = 0;
    fila[fim++] = s;
    marcado[s] = 1;
    while (ini < fim) {
        int u = fila[ini++];
        for (k = 0; k < GRAU[u]; k++) {
            int w = VIZ[u][k];
            if (!marcado[w]) { marcado[w] = 1; pai[w] = u; fila[fim++] = w; }
        }
    }
}

int peso_de(int a, int b) {
    int k;
    for (k = 0; k < GRAU[a]; k++) if (VIZ[a][k] == b) return PESO[a][k];
    return INF;
}

/* escreve "1 -> 2 -> 5" em buf */
void caminho_str(char *buf, const int c[], int t) {
    int i, n = 0;
    buf[0] = '\0';
    for (i = 0; i < t; i++) n += sprintf(buf + n, "%s%d", i > 0 ? " -> " : "", c[i]);
}

int main(void) {
    int dist[N + 1], pai[N + 1], d2[N + 1], p2[N + 1], pai_bfs[N + 1], c[N + 1];
    int v, t, i, total;
    char s[64];

    printf("1) Dijkstra a partir do roteador %d (latencias em ms)\n", ORIGEM);
    dijkstra_passo_a_passo(ORIGEM, dist, pai);
    dijkstra(ORIGEM, d2, p2);                       /* confere com a versão limpa */
    for (v = 1; v <= N; v++) if (d2[v] != dist[v] || p2[v] != pai[v]) return 1;

    printf("\n2) Rota mais rapida ate cada roteador (seguindo pai[])\n");
    for (v = 1; v <= N; v++) {
        t = caminho(pai, v, c);
        caminho_str(s, c, t);
        printf("   ate %d: %-20s ", v, s);
        imprime_dist(dist[v], 3);
        printf(" ms\n");
    }

    printf("\n3) Menos saltos (BFS) x menor latencia (Dijkstra), ate o roteador 3\n");
    bfs_saltos(ORIGEM, pai_bfs);
    t = caminho(pai_bfs, 3, c);
    caminho_str(s, c, t);
    for (total = 0, i = 0; i + 1 < t; i++) total += peso_de(c[i], c[i + 1]);
    printf("   BFS:      %-18s%d saltos, %d ms\n", s, t - 1, total);
    t = caminho(pai, 3, c);
    caminho_str(s, c, t);
    for (total = 0, i = 0; i + 1 < t; i++) total += peso_de(c[i], c[i + 1]);
    printf("   Dijkstra: %-18s%d saltos, %d ms\n", s, t - 1, total);
    return 0;
}
