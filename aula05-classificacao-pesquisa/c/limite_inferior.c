/*
 * limite_inferior.c
 *
 * Estruturas de Dados — Aula 5 — Bloco 6 (Limite inferior)
 * Slides 27 e 28 · versão em C de python/limite_inferior.py
 *
 * Todo algoritmo que ordena COMPARANDO elementos joga o jogo de "adivinhar
 * o número" da Aula 4: entre as n! ordens possíveis, ele precisa descobrir
 * qual é a certa, e cada comparação é uma pergunta de sim/não.
 *
 * Com k perguntas dá para separar no máximo 2^k respostas. Para separar
 * n! ordens:  2^k >= n!   ->   k >= log2(n!)  ~  n log2 n
 * Logo, NENHUMA ordenação por comparação vence Omega(n log n) no pior caso.
 *
 *   1) testa TODAS as ordens de 3 e 4 elementos (saída idêntica à do Python);
 *   2) compara log2(n!) com n log2 n e com o Merge Sort medido (os vetores
 *      embaralhados vêm de um gerador próprio, então a coluna "merge" difere
 *      um pouco da do Python).
 *
 * Os logaritmos são calculados sem <math.h> (assim não é preciso -lm).
 *
 * Arquivo único, só <stdio.h> — cole direto no onlineide.pro/playground/c
 */
#include <stdio.h>

#define N_MAX 10000

/* ------------------------------------------------------------------ */
/* Logaritmo sem <math.h>: reduz x ao intervalo [1, 2] e usa a série   */
/* ln(x) = 2 (z + z^3/3 + z^5/5 + ...), com z = (x - 1) / (x + 1).     */
/* ------------------------------------------------------------------ */
static const double LN2 = 0.69314718055994530942;

static double log2_aprox(double x) {
    int expoente = 0;
    while (x >= 2.0) { x /= 2.0; expoente++; }
    while (x < 1.0)  { x *= 2.0; expoente--; }
    double z = (x - 1.0) / (x + 1.0), z2 = z * z, termo = z, soma = 0.0;
    for (int k = 1; k < 80; k += 2) {
        soma += termo / k;
        termo *= z2;
    }
    return expoente + 2.0 * soma / LN2;
}

/* log2(n!) = log2(2) + log2(3) + ... + log2(n), sem calcular n! */
static double log2_fatorial(int n) {
    double s = 0.0;
    for (int k = 2; k <= n; k++) s += log2_aprox((double)k);
    return s;
}

static long teto(double x) {
    long t = (long)x;
    return (t < x) ? t + 1 : t;
}

/* ------------------------------------------------------------------ */
/* Os dois algoritmos, contando comparações (ordenam uma cópia).       */
/* ------------------------------------------------------------------ */
static long insertion_comparacoes(const int origem[], int n) {
    int v[16];
    long comp = 0;
    for (int i = 0; i < n; i++) v[i] = origem[i];
    for (int i = 1; i < n; i++) {
        int chave = v[i], j = i - 1;
        while (j >= 0) {
            comp++;
            if (!(v[j] > chave)) break;
            v[j + 1] = v[j];
            j--;
        }
        v[j + 1] = chave;
    }
    return comp;
}

static int auxiliar[N_MAX];

/* Merge Sort no lugar (com vetor auxiliar global); devolve as comparações. */
static long merge_comparacoes(int v[], int n) {
    if (n <= 1) return 0;
    int meio = n / 2;
    long comp = merge_comparacoes(v, meio) + merge_comparacoes(v + meio, n - meio);
    int i = 0, j = meio, k = 0;
    while (i < meio && j < n) {
        comp++;
        auxiliar[k++] = (v[i] <= v[j]) ? v[i++] : v[j++];
    }
    while (i < meio) auxiliar[k++] = v[i++];
    while (j < n)    auxiliar[k++] = v[j++];
    for (k = 0; k < n; k++) v[k] = auxiliar[k];
    return comp;
}

/* ------------------------------------------------------------------ */
/* Força bruta: gera todas as permutações de v[0..n-1] (por trocas).   */
/* ------------------------------------------------------------------ */
static long pior_insertion, pior_merge, total_ordens;

static void testar_todas(int v[], int k, int n) {
    if (k == n) {                                  /* uma ordem completa */
        int copia[16];
        for (int i = 0; i < n; i++) copia[i] = v[i];
        long ci = insertion_comparacoes(v, n);
        long cm = merge_comparacoes(copia, n);
        if (ci > pior_insertion) pior_insertion = ci;
        if (cm > pior_merge) pior_merge = cm;
        total_ordens++;
        return;
    }
    for (int i = k; i < n; i++) {
        int t = v[k]; v[k] = v[i]; v[i] = t;       /* escolhe quem fica na posição k */
        testar_todas(v, k + 1, n);
        t = v[k]; v[k] = v[i]; v[i] = t;           /* desfaz a troca */
    }
}

/* Gerador pseudoaleatório (congruencial linear) com semente fixa. */
static unsigned long long semente = 2026ULL;

static unsigned int proximo_aleatorio(void) {
    semente = semente * 6364136223846793005ULL + 1442695040888963407ULL;
    return (unsigned int)(semente >> 33);
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
    printf("1) FORCA BRUTA: pior caso entre todas as ordens possiveis\n");
    printf("   (limite = log2(n!) arredondado para cima)\n");
    const int ns[] = {3, 4};                       /* experimente {3, 4, 5, 6} (até 8) */
    for (int t = 0; t < (int)(sizeof ns / sizeof ns[0]); t++) {
        int n = ns[t], v[16];
        for (int i = 0; i < n; i++) v[i] = 101 + i;            /* trabalhos 101, 102, ... */
        pior_insertion = pior_merge = total_ordens = 0;
        testar_todas(v, 0, n);
        printf("   n=%d: %2ld ordens | limite = %ld | insertion = %ld | merge = %ld\n",
               n, total_ordens, teto(log2_fatorial(n)), pior_insertion, pior_merge);
    }

    printf("\n2) O LIMITE log2(n!) CRESCE COMO n log2 n\n");
    printf("%7s %10s %10s %8s\n", "n", "log2(n!)", "n*log2(n)", "merge");
    static int v[N_MAX];
    const int tamanhos[] = {10, 100, 1000, 10000};
    for (int t = 0; t < 4; t++) {
        int n = tamanhos[t];
        for (int i = 0; i < n; i++) v[i] = i;
        for (int i = n - 1; i > 0; i--) {          /* embaralha (Fisher-Yates) */
            int j = (int)(proximo_aleatorio() % (unsigned int)(i + 1));
            int x = v[i]; v[i] = v[j]; v[j] = x;
        }
        long medido = merge_comparacoes(v, n);
        imprimir_com_pontos(n, 7);
        printf(" ");
        imprimir_com_pontos(teto(log2_fatorial(n)), 10);
        printf(" ");
        imprimir_com_pontos((long)(n * log2_aprox((double)n) + 0.5), 10);
        printf(" ");
        imprimir_com_pontos(medido, 8);
        printf("\n");
    }
    printf("\nMerge Sort fica colado no limite: e assintoticamente otimo.\n");
    return 0;
}
