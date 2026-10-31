/*
 * ex08_quick_mediana_tres.c — Aula 5, Exercício 8 (solução de referência)
 *
 * Quicksort com a partição da aula, com o pivô escolhido de dois jeitos:
 * o último elemento, ou a mediana de três (v[inicio], v[meio], v[fim]),
 * levada para o fim antes de particionar.
 *
 * O vetor "aleatório" vem de um gerador próprio: os números diferem um
 * pouco dos do Python; a linha "ja ordenado / pivo = ultimo" é idêntica
 * (124.750 = n(n-1)/2).
 *
 * Arquivo único, só <stdio.h> — cole direto no onlineide.pro/playground/c
 */
#include <stdio.h>

#define N 500

static long comparacoes = 0;

static void trocar(int v[], int a, int b) { int t = v[a]; v[a] = v[b]; v[b] = t; }

static int indice_mediana_de_tres(const int v[], int inicio, int fim) {
    int meio = inicio + (fim - inicio) / 2;
    int a = v[inicio], b = v[meio], c = v[fim];
    if ((a <= b && b <= c) || (c <= b && b <= a)) return meio;
    if ((b <= a && a <= c) || (c <= a && a <= b)) return inicio;
    return fim;
}

/* estrategia: 0 = pivô é o último; 1 = mediana de três */
static int particionar(int v[], int inicio, int fim, int estrategia) {
    if (estrategia == 1) trocar(v, indice_mediana_de_tres(v, inicio, fim), fim);
    int pivo = v[fim], i = inicio;
    for (int j = inicio; j < fim; j++) {
        comparacoes++;
        if (v[j] < pivo) { trocar(v, i, j); i++; }
    }
    trocar(v, i, fim);
    return i;
}

static void quick_sort(int v[], int inicio, int fim, int estrategia) {
    if (inicio < fim) {
        int p = particionar(v, inicio, fim, estrategia);
        quick_sort(v, inicio, p - 1, estrategia);
        quick_sort(v, p + 1, fim, estrategia);
    }
}

static long contar(const int dados[], int estrategia) {
    static int v[N];
    for (int i = 0; i < N; i++) v[i] = dados[i];
    comparacoes = 0;
    quick_sort(v, 0, N - 1, estrategia);
    for (int i = 1; i < N; i++) if (v[i - 1] > v[i]) printf("(erro: nao ordenou!)\n");
    return comparacoes;
}

static unsigned long long semente = 2026ULL;
static unsigned int proximo_aleatorio(void) {
    semente = semente * 6364136223846793005ULL + 1442695040888963407ULL;
    return (unsigned int)(semente >> 33);
}

static void com_pontos(long x, char *buf) {
    char tmp[32];
    int n = sprintf(tmp, "%ld", x), k = 0;
    for (int i = 0; i < n; i++) {
        buf[k++] = tmp[i];
        if ((n - i - 1) % 3 == 0 && i < n - 1) buf[k++] = '.';
    }
    buf[k] = '\0';
}

int main(void) {
    static int aleatorio[N], ordenado[N], inverso[N];
    for (int i = 0; i < N; i++) aleatorio[i] = ordenado[i] = 1 + (int)(proximo_aleatorio() % 1000000u);
    quick_sort(ordenado, 0, N - 1, 1);                       /* prepara o vetor ordenado */
    for (int i = 0; i < N; i++) inverso[i] = ordenado[N - 1 - i];

    const char *nomes[] = {"aleatorio", "ja ordenado", "ordem inversa"};
    const int *cenarios[] = {aleatorio, ordenado, inverso};
    printf("Comparacoes do Quicksort com n = %d\n", N);
    printf("   %-14s %14s %16s\n", "cenario", "pivo = ultimo", "mediana de tres");
    for (int c = 0; c < 3; c++) {
        char a[32], b[32];
        com_pontos(contar(cenarios[c], 0), a);
        com_pontos(contar(cenarios[c], 1), b);
        printf("   %-14s %14s %16s\n", nomes[c], a, b);
    }
    return 0;
}
