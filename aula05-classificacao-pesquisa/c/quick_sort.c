/*
 * quick_sort.c
 *
 * Estruturas de Dados — Aula 5 — Bloco 5 (Quicksort)
 * Slides 21 a 26 · versão em C de python/quick_sort.py
 *
 * 1) PARTIÇÃO (esquema de Lomuto): o último elemento é o PIVÔ. Quem é
 *    menor que ele vai para a esquerda; no fim, o pivô vai para a posição
 *    entre os dois grupos — que já é a sua posição FINAL.
 * 2) QUICKSORT: particiona e repete, recursivamente, nos dois lados.
 *    Ordena no próprio vetor (sem vetor auxiliar). Não é estável.
 * 3) CASOS:
 *    caso médio .... ~1,39 n log2 n comparações -> Theta(n log n)
 *    pior caso ..... pivô sempre o maior/menor  -> n(n-1)/2 -> Theta(n^2)
 *                    (vetor JÁ ORDENADO com pivô = último elemento!)
 *    correção ...... pivô aleatório: o pior caso fica improvável.
 *
 * As partes 1 e 2 e a linha ORDENADO usam dados fixos (iguais ao Python).
 * As linhas com dados sorteados diferem um pouco, porque o gerador é outro.
 *
 * Arquivo único, só <stdio.h> — cole direto no onlineide.pro/playground/c
 */
#include <stdio.h>

/* ------------------------------------------------------------------ */
/* Versões "limpas", equivalentes às do slide 23.                      */
/* ------------------------------------------------------------------ */
static void trocar(int v[], int a, int b) {
    int t = v[a];
    v[a] = v[b];
    v[b] = t;
}

int particionar(int v[], int inicio, int fim) {
    int pivo = v[fim];                 /* o último é o pivô */
    int i = inicio;                    /* vaga dos menores  */
    for (int j = inicio; j < fim; j++) {
        if (v[j] < pivo) {
            trocar(v, i, j);
            i++;
        }
    }
    trocar(v, i, fim);                 /* pivô no lugar */
    return i;
}

void quick_sort(int v[], int inicio, int fim) {
    if (inicio < fim) {
        int p = particionar(v, inicio, fim);
        quick_sort(v, inicio, p - 1);
        quick_sort(v, p + 1, fim);
    }
}

/* ------------------------------------------------------------------ */
/* A mesma lógica, contando comparações, mostrando a partição e com a  */
/* opção de sortear o pivô.                                            */
/* ------------------------------------------------------------------ */
static long comparacoes = 0;
static unsigned long long semente = 2026ULL;

static unsigned int proximo_aleatorio(void) {
    semente = semente * 6364136223846793005ULL + 1442695040888963407ULL;
    return (unsigned int)(semente >> 33);
}

static void imprimir_lista(const int v[], int n) {
    printf("[");
    for (int i = 0; i < n; i++) printf("%d%s", v[i], i < n - 1 ? ", " : "");
    printf("]");
}

/* 'n_total' é o tamanho do vetor inteiro, usado só para imprimir. */
int particionar_contando(int v[], int inicio, int fim, int pivo_aleatorio, int mostrar, int n_total) {
    if (pivo_aleatorio) {                          /* sorteia o pivô e o leva para o fim */
        int k = inicio + (int)(proximo_aleatorio() % (unsigned int)(fim - inicio + 1));
        trocar(v, k, fim);
    }
    int pivo = v[fim];
    int i = inicio;                                /* próxima vaga do grupo "menores" */
    for (int j = inicio; j < fim; j++) {
        int x = v[j];
        comparacoes++;
        if (x < pivo) {
            trocar(v, i, j);                       /* manda x para o grupo dos menores */
            i++;
            if (mostrar) { printf("   %2d <  %d  -> esquerda  ", x, pivo); imprimir_lista(v, n_total); printf("\n"); }
        } else if (mostrar) {
            printf("   %2d >= %d  -> fica      ", x, pivo); imprimir_lista(v, n_total); printf("\n");
        }
    }
    trocar(v, i, fim);                             /* pivô entre os dois grupos */
    return i;
}

void quick_sort_contando(int v[], int inicio, int fim, int pivo_aleatorio) {
    if (inicio < fim) {                            /* 0 ou 1 elemento: caso base */
        int p = particionar_contando(v, inicio, fim, pivo_aleatorio, 0, 0);
        quick_sort_contando(v, inicio, p - 1, pivo_aleatorio);
        quick_sort_contando(v, p + 1, fim, pivo_aleatorio);
    }
}

static long contar(const int v[], int n, int pivo_aleatorio) {
    static int copia[1000];
    for (int i = 0; i < n; i++) copia[i] = v[i];
    comparacoes = 0;
    quick_sort_contando(copia, 0, n - 1, pivo_aleatorio);
    return comparacoes;
}

static void imprimir_com_pontos(long x, int largura) {
    char tmp[32], buf[40];
    int n = sprintf(tmp, "%ld", x), k = 0;
    for (int i = 0; i < n; i++) {
        buf[k++] = tmp[i];
        if ((n - i - 1) % 3 == 0 && i < n - 1) buf[k++] = '.';
    }
    buf[k] = '\0';
    printf("%*s", largura, buf);
}

int main(void) {
    printf("1) PARTICAO PASSO A PASSO (pivo = ultimo elemento)\n");
    int paginas[] = {12, 5, 8, 3, 20, 1, 9, 6};
    printf("   inicio:               ");
    imprimir_lista(paginas, 8);
    printf("\n");
    int p = particionar_contando(paginas, 0, 7, 0, 1, 8);
    printf("   pivo %d -> posicao %d:  ", paginas[p], p);
    imprimir_lista(paginas, 8);
    printf("\n");

    printf("\n2) QUICKSORT COMPLETO\n");
    int outra[] = {12, 5, 8, 3, 20, 1, 9, 6};
    quick_sort(outra, 0, 7);
    printf("   resultado: ");
    imprimir_lista(outra, 8);
    printf("\n");

    printf("\n3) MELHOR E PIOR CASO (n = 500)\n");
    enum { N = 500 };
    static int aleatorio[N], ordenado[N];
    for (int i = 0; i < N; i++) aleatorio[i] = ordenado[i] = 1 + (int)(proximo_aleatorio() % 1000000u);
    quick_sort(ordenado, 0, N - 1);               /* a versão limpa prepara o vetor ordenado */
    printf("   aleatorio, pivo = ultimo ...... ");
    imprimir_com_pontos(contar(aleatorio, N, 0), 7);
    printf("\n   ORDENADO,  pivo = ultimo ...... ");
    imprimir_com_pontos(contar(ordenado, N, 0), 7);
    printf("\n   ordenado,  pivo aleatorio ..... ");
    imprimir_com_pontos(contar(ordenado, N, 1), 7);
    printf("\n   n(n-1)/2 = ");
    imprimir_com_pontos((long)N * (N - 1) / 2, 0);
    printf("\n\nVetor ja ordenado + pivo no fim = pior caso Theta(n^2)\n");
    return 0;
}
