/*
 * busca_saltos.c
 *
 * Estruturas de Dados — Aula 4 — Bloco 6 (Derivadas)
 * Slides 42 a 45 · Apostila, capítulo 11
 *
 * Busca por saltos em um vetor ORDENADO de tamanho n:
 *   fase 1: salta de m em m posições (acesso por índice é O(1) — Aula 1),
 *           olhando o último elemento de cada bloco, até achar o bloco
 *           que pode conter o valor;
 *   fase 2: faz busca linear só dentro desse bloco.
 *
 * No pior caso: cerca de n/m saltos + m comparações dentro do bloco.
 *     T(m) = n/m + m
 * Derivando (regra da potência, com n/m = n * m^-1):
 *     T'(m) = -n/m^2 + 1 = 0   ->   m = raiz(n)
 *
 * Este programa testa vários tamanhos de bloco m, mede o pior caso de
 * cada um e confere que o melhor m fica mesmo perto de raiz(n).
 *
 * Arquivo único, só <stdio.h> (não precisa de -lm) —
 * cole direto no onlineide.pro/playground/c
 */
#include <stdio.h>

#define TAMANHO_MAX 1000000

static int v[TAMANHO_MAX]; /* vetor ordenado 0, 1, 2, ..., n-1 */

static int minimo(int a, int b) {
    return a < b ? a : b;
}

/* Procura 'alvo' no vetor ordenado v[0..n-1] usando blocos de tamanho m.
 * Devolve a posição (ou -1) e guarda em *comparacoes quantas foram feitas. */
int busca_por_saltos(const int vet[], int n, int alvo, int m, long *comparacoes) {
    int inicio = 0;
    *comparacoes = 0;

    /* Fase 1: pula blocos inteiros enquanto o ÚLTIMO elemento do bloco
     * ainda for menor que o alvo (então o alvo não pode estar nele). */
    while (inicio < n) {
        int fim_do_bloco = minimo(inicio + m, n) - 1;
        (*comparacoes)++;
        if (!(vet[fim_do_bloco] < alvo)) {
            break;               /* o alvo, se existir, está neste bloco */
        }
        inicio += m;
    }

    /* Fase 2: busca linear dentro do bloco encontrado. */
    int limite = minimo(inicio + m, n);
    for (int i = inicio; i < limite; i++) {
        (*comparacoes)++;
        if (vet[i] == alvo) {
            return i;
        }
    }
    return -1;
}

/* Comparações no pior caso para blocos de tamanho m.
 * O pior caso é procurar o último elemento de um bloco que fica no fim
 * do vetor: fazemos todos os saltos e percorremos o bloco inteiro.
 * Há dois candidatos — o último elemento do vetor e o último elemento do
 * último bloco completo (quando o bloco final é mais curto) — e ficamos
 * com o maior dos dois. */
long pior_caso(int n, int m) {
    long c1 = 0, c2 = 0;
    busca_por_saltos(v, n, v[n - 1], m, &c1);
    int ultimo_bloco_completo = (n / m) * m - 1;
    if (ultimo_bloco_completo >= 0 && ultimo_bloco_completo < n - 1) {
        busca_por_saltos(v, n, v[ultimo_bloco_completo], m, &c2);
    }
    return c1 > c2 ? c1 : c2;
}

/* Raiz quadrada inteira (o maior r com r*r <= n), sem usar <math.h>. */
static int raiz_inteira(int n) {
    int r = 0;
    while ((long)(r + 1) * (r + 1) <= n) {
        r++;
    }
    return r;
}

/* Imprime um inteiro com ponto separando os milhares: 1000000 -> 1.000.000 */
static void imprimir_com_pontos(long x) {
    if (x >= 1000) {
        imprimir_com_pontos(x / 1000);
        printf(".%03ld", x % 1000);
    } else {
        printf("%ld", x);
    }
}

/* Imprime T(m) = n/m + m: inteiro quando m divide n, senão com 1 casa. */
static void imprimir_formula(int n, int m) {
    if (n % m == 0) {
        printf("%11ld", (long)(n / m) + m);
    } else {
        /* uma casa decimal, com vírgula, sem usar ponto flutuante */
        long decimos = (10L * n + m / 2) / m + 10L * m;
        printf("%9ld,%ld", decimos / 10, decimos % 10);
    }
}

void analisar(int n, const int valores_de_m[], int quantidade, int primeiro, int ultimo) {
    printf("\nn = ");
    imprimir_com_pontos(n);
    printf("   (busca linear, pior caso: ");
    imprimir_com_pontos(n);
    printf(" comparacoes)\n");

    printf("%9s %18s %11s\n", "m", "pior caso medido", "n/m + m");
    for (int k = 0; k < quantidade; k++) {
        int m = valores_de_m[k];
        printf("%9d %18ld ", m, pior_caso(n, m));
        imprimir_formula(n, m);
        printf("\n");
    }

    long menor = -1;
    int melhor_primeiro = 0, melhor_ultimo = 0, empatados = 0;
    for (int m = primeiro; m <= ultimo; m++) {
        long custo = pior_caso(n, m);
        if (menor == -1 || custo < menor) {
            menor = custo;
            melhor_primeiro = m;
            melhor_ultimo = m;
            empatados = 1;
        } else if (custo == menor) {
            melhor_ultimo = m;
            empatados++;
        }
    }
    int r = raiz_inteira(n);
    printf("Testando todos os m de %d a %d:\n", primeiro, ultimo);
    printf("  menor pior caso = %ld comparacoes\n", menor);
    printf("  obtido com m de %d a %d (%d valores empatados)\n",
           melhor_primeiro, melhor_ultimo, empatados);
    printf("  raiz(%d) = %d   ->   2 * raiz(n) = %d\n", n, r, 2 * r);
}

int main(void) {
    for (int i = 0; i < TAMANHO_MAX; i++) {
        v[i] = i;
    }

    printf("BUSCA POR SALTOS - comparacoes no pior caso (vetor ordenado)\n");
    printf("Modelo: T(m) = n/m + m   ->   T'(m) = -n/m^2 + 1 = 0   ->   m = raiz(n)\n");

    /* Exemplo dos slides 42 e 43 */
    int m_exemplo[] = {1, 10, 25, 50, 100, 200, 400, 1000};
    analisar(10000, m_exemplo, 8, 1, 1000);

    /* Exercício 9 (slides 44 e 45) */
    int m_400[] = {5, 10, 20, 40, 80};
    analisar(400, m_400, 5, 1, 400);
    int m_milhao[] = {500, 1000, 2000};
    analisar(1000000, m_milhao, 3, 900, 1100);

    printf("\nPerceba: perto de raiz(n) varios m empatam. No fundo do \"vale\" a\n");
    printf("curva e quase plana - exatamente onde a derivada vale zero.\n");
    return 0;
}
