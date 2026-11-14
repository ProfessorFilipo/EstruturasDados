/*
 * ex08_dois_times.c — Solução do Exercício 8 (Aula 7)
 *
 * Dois times sem rivais juntos = grafo de rivalidades BIPARTIDO.
 * BFS pintando: cada vizinho recebe o time oposto ao de quem o descobriu;
 * dois vizinhos no MESMO time tornam a divisão impossível.
 *
 * Saída idêntica à da versão em Python. Só <stdio.h>.
 */
#include <stdio.h>

#define MAX 8

typedef struct {
    int n;
    int viz[MAX][MAX];
    int grau[MAX];
} Grafo;

void criar_lista(Grafo *g, int n, const int arestas[][2], int na) {
    int i;
    g->n = n;
    for (i = 0; i <= n; i++) g->grau[i] = 0;
    for (i = 0; i < na; i++) {
        int u = arestas[i][0], v = arestas[i][1];
        g->viz[u][g->grau[u]++] = v;
        g->viz[v][g->grau[v]++] = u;
    }
}

/* devolve 1 se deu certo (times em time[]); 0 com o conflito em *a, *b */
int dividir(const Grafo *g, int time[], int *a, int *b) {
    int s, v, k;
    for (v = 0; v <= g->n; v++) time[v] = -1;      /* -1 = ainda sem time */
    for (s = 1; s <= g->n; s++) {                  /* cada componente começa do zero */
        int fila[MAX], ini = 0, fim = 0;
        if (time[s] != -1) continue;
        time[s] = 0;
        fila[fim++] = s;
        while (ini < fim) {
            int u = fila[ini++];
            for (k = 0; k < g->grau[u]; k++) {
                int w = g->viz[u][k];
                if (time[w] == -1) {
                    time[w] = 1 - time[u];         /* time oposto */
                    fila[fim++] = w;
                } else if (time[w] == time[u]) {
                    *a = u; *b = w;                /* rivais no mesmo time */
                    return 0;
                }
            }
        }
    }
    return 1;
}

void imprimir_time(const char *rotulo, const int time[], int n, int qual) {
    int v, primeiro = 1;
    printf("   %s: [", rotulo);
    for (v = 1; v <= n; v++)
        if (time[v] == qual) { printf("%s%d", primeiro ? "" : ", ", v); primeiro = 0; }
    printf("]\n");
}

void testar(const char *nome, int n, const int arestas[][2], int na) {
    Grafo g;
    int time[MAX], a, b;
    criar_lista(&g, n, arestas, na);
    printf("%s\n", nome);
    if (!dividir(&g, time, &a, &b)) {
        printf("   impossivel: os rivais %d e %d cairiam no mesmo time\n", a, b);
    } else {
        imprimir_time("time A", time, n, 0);
        imprimir_time("time B", time, n, 1);
    }
}

int main(void) {
    static const int rivais[7][2] = {           /* a última só entra no teste 2 */
        {1, 2}, {1, 4}, {2, 3}, {3, 6}, {4, 5}, {5, 6}, {1, 3}
    };
    testar("1) turma com 6 alunos", 6, rivais, 6);
    testar("2) mesma turma + rivalidade 1-3", 6, rivais, 7);
    testar("3) turma com 7 alunos, 7 isolado", 7, rivais, 6);
    return 0;
}
