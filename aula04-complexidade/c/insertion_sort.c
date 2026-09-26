/*
 * insertion_sort.c
 *
 * Estruturas de Dados — Aula 4 — Bloco 5 (Casos e Insertion Sort)
 * Slides 29 a 36 · Apostila, capítulo 9
 *
 * 1) Rastreia o Insertion Sort em {5, 2, 4, 6, 1, 3}, passada por passada.
 * 2) Conta as comparações em três cenários:
 *      vetor já ordenado -> melhor caso: n - 1 comparações   -> Theta(n)
 *      ordem aleatória   -> caso médio:  cerca de n^2 / 4    -> Theta(n^2)
 *      ordem inversa     -> pior caso:   n(n - 1) / 2        -> Theta(n^2)
 *
 * Conta como "comparação" cada avaliação de  v[j] > chave.
 * (Theta é a letra grega Θ, usada na notação vista em aula.)
 *
 * Arquivo único, só <stdio.h> — cole direto no onlineide.pro/playground/c
 */
#include <stdio.h>

#define TAMANHO_MAX 1000

/* ------------------------------------------------------------------ */
/* Versão "limpa", idêntica à do slide 29 — para referência.           */
/* ------------------------------------------------------------------ */
void insertion_sort(int v[], int n) {
    for (int i = 1; i < n; i++) {
        int chave = v[i];
        int j = i - 1;
        while (j >= 0 && v[j] > chave) {
            v[j + 1] = v[j]; /* desloca para a direita */
            j--;
        }
        v[j + 1] = chave;
    }
}

/* ------------------------------------------------------------------ */
/* Mesma lógica, agora contando comparações e deslocamentos.          */
/* ------------------------------------------------------------------ */
typedef struct {
    long comparacoes;
    long deslocamentos;
} Contagem;

static void imprimir_vetor(const int v[], int n) {
    printf("{");
    for (int i = 0; i < n; i++) {
        printf("%d%s", v[i], i < n - 1 ? ", " : "");
    }
    printf("}");
}

/* Se 'mostrar' for diferente de 0, imprime o vetor ao final de cada passada. */
void insertion_sort_contando(int v[], int n, Contagem *total, int mostrar) {
    total->comparacoes = 0;
    total->deslocamentos = 0;

    for (int i = 1; i < n; i++) {
        int chave = v[i];
        int j = i - 1;
        long comparacoes_passada = 0;
        long deslocamentos_passada = 0;

        while (j >= 0) {
            comparacoes_passada++;   /* vamos avaliar v[j] > chave */
            if (!(v[j] > chave)) {
                break;               /* achou o lugar da chave */
            }
            v[j + 1] = v[j];         /* desloca para a direita */
            deslocamentos_passada++;
            j--;
        }
        v[j + 1] = chave;

        total->comparacoes += comparacoes_passada;
        total->deslocamentos += deslocamentos_passada;

        if (mostrar) {
            printf("passada %d  chave = %d  ->  ", i, chave);
            imprimir_vetor(v, n);
            printf("   comparacoes: %ld   deslocamentos: %ld\n",
                   comparacoes_passada, deslocamentos_passada);
        }
    }
}

/* ------------------------------------------------------------------ */
/* Gerador de números pseudoaleatórios simples (congruencial linear).  */
/* Usamos este em vez de rand() porque rand() gera sequências          */
/* diferentes em cada compilador; este gera sempre os mesmos números,  */
/* então a saída do programa é igual em qualquer máquina.              */
/* ------------------------------------------------------------------ */
static unsigned long long semente = 42ULL;

static unsigned int proximo_aleatorio(void) {
    semente = semente * 6364136223846793005ULL + 1442695040888963407ULL;
    return (unsigned int)(semente >> 33);
}

/* Embaralhamento de Fisher-Yates: cada ordem tem a mesma chance. */
static void embaralhar(int v[], int n) {
    for (int i = n - 1; i > 0; i--) {
        int j = (int)(proximo_aleatorio() % (unsigned int)(i + 1));
        int temporario = v[i];
        v[i] = v[j];
        v[j] = temporario;
    }
}

static long comparacoes_ordenado(int n) {
    static int v[TAMANHO_MAX];
    Contagem c;
    for (int i = 0; i < n; i++) {
        v[i] = i;                    /* 0, 1, 2, ..., n-1 */
    }
    insertion_sort_contando(v, n, &c, 0);
    return c.comparacoes;
}

static long comparacoes_invertido(int n) {
    static int v[TAMANHO_MAX];
    Contagem c;
    for (int i = 0; i < n; i++) {
        v[i] = n - 1 - i;            /* n-1, ..., 2, 1, 0 */
    }
    insertion_sort_contando(v, n, &c, 0);
    return c.comparacoes;
}

static double comparacoes_aleatorio(int n, int rodadas) {
    static int v[TAMANHO_MAX];
    Contagem c;
    long soma = 0;
    for (int r = 0; r < rodadas; r++) {
        for (int i = 0; i < n; i++) {
            v[i] = i;
        }
        embaralhar(v, n);
        insertion_sort_contando(v, n, &c, 0);
        soma += c.comparacoes;
    }
    return (double)soma / rodadas;   /* média das rodadas */
}

int main(void) {
    int exemplo[] = {5, 2, 4, 6, 1, 3};
    int n_exemplo = (int)(sizeof(exemplo) / sizeof(exemplo[0]));
    Contagem c;

    int tamanhos[] = {10, 100, 1000};
    int rodadas[] = {200, 50, 10};   /* quantos vetores aleatórios por tamanho */
    int quantidade = (int)(sizeof(tamanhos) / sizeof(tamanhos[0]));

    printf("1) INSERTION SORT PASSO A PASSO\n");
    printf("vetor inicial:              ");
    imprimir_vetor(exemplo, n_exemplo);
    printf("\n");
    insertion_sort_contando(exemplo, n_exemplo, &c, 1);
    printf("total: %ld comparacoes e %ld deslocamentos\n",
           c.comparacoes, c.deslocamentos);

    printf("\n2) COMPARACOES POR CENARIO\n");
    printf("%8s %12s %13s %12s\n", "n", "ordenado", "aleatorio(*)", "invertido");
    for (int k = 0; k < quantidade; k++) {
        int n = tamanhos[k];
        printf("%8d %12ld %13.0f %12ld\n", n,
               comparacoes_ordenado(n),
               comparacoes_aleatorio(n, rodadas[k]),
               comparacoes_invertido(n));
    }
    printf("(*) media de varios vetores embaralhados\n");

    printf("\nFormulas:  ordenado = n - 1   |   aleatorio ~ n^2/4   |   invertido = n(n-1)/2\n");
    printf("Melhor caso: Theta(n)     Caso medio e pior caso: Theta(n^2)\n");
    return 0;
}
