/*
 * busca_sequencial.c
 *
 * Estruturas de Dados — Aula 5 — Bloco 1 (Pesquisa sequencial)
 * Slides 05 e 06 · versão em C de python/busca_sequencial.py
 *
 * A Central de Impressão da Aula 2 cresceu: o histórico guarda 10.000
 * trabalhos (id, paginas), na ordem em que saíram da fila (FIFO). Os IDs
 * crescem; cancelamentos deixam lacunas.
 *
 * A pesquisa sequencial olha um trabalho de cada vez, do início ao fim:
 *     melhor caso ... 1 comparação         (o alvo é o primeiro)
 *     caso médio .... (n + 1) / 2          (a soma de Gauss da Aula 4)
 *     pior caso ..... n comparações        (o alvo é o último ou não existe)
 *
 * Os números "aleatórios" vêm de um gerador próprio (congruencial linear):
 * a saída é a mesma em qualquer compilador, mas os trabalhos sorteados NÃO
 * são os mesmos da versão em Python, porque o gerador do Python é outro.
 *
 * Arquivo único, só <stdio.h> — cole direto no onlineide.pro/playground/c
 */
#include <stdio.h>

#define N_TRABALHOS 10000

typedef struct {
    int id;
    int paginas;
} Trabalho;

typedef enum { CAMPO_ID, CAMPO_PAGINAS } Campo;

/* ------------------------------------------------------------------ */
/* Gerador pseudoaleatório (congruencial linear) com semente fixa.     */
/* ------------------------------------------------------------------ */
static unsigned long long semente = 2026ULL;

static unsigned int proximo_aleatorio(void) {
    semente = semente * 6364136223846793005ULL + 1442695040888963407ULL;
    return (unsigned int)(semente >> 33);
}

/* Inteiro sorteado entre a e b (inclusive). */
static int sortear(int a, int b) {
    return a + (int)(proximo_aleatorio() % (unsigned int)(b - a + 1));
}

/* Preenche h[] com n trabalhos em ordem de chegada. */
void gerar_historico(Trabalho h[], int n) {
    int id_atual = 101;                     /* o primeiro ID da Aula 2 */
    for (int i = 0; i < n; i++) {
        h[i].id = id_atual;
        h[i].paginas = sortear(1, 30);
        id_atual += sortear(1, 3);          /* 2 ou 3 = houve cancelamento */
    }
}

static int valor_do_campo(const Trabalho *t, Campo campo) {
    return campo == CAMPO_ID ? t->id : t->paginas;
}

/* Procura o primeiro trabalho cujo campo vale 'alvo'.
 * Devolve a posição (ou -1) e guarda em *comparacoes quantas foram feitas. */
int busca_sequencial(const Trabalho v[], int n, int alvo, Campo campo, long *comparacoes) {
    *comparacoes = 0;
    for (int i = 0; i < n; i++) {
        (*comparacoes)++;                   /* uma comparação por trabalho */
        if (valor_do_campo(&v[i], campo) == alvo) {
            return i;
        }
    }
    return -1;
}

int main(void) {
    static Trabalho historico[N_TRABALHOS];
    long comp;
    int pos;

    gerar_historico(historico, N_TRABALHOS);
    printf("historico: %d trabalhos\n", N_TRABALHOS);
    printf("primeiros: [(%d, %d), (%d, %d), (%d, %d)]\n",
           historico[0].id, historico[0].paginas, historico[1].id, historico[1].paginas,
           historico[2].id, historico[2].paginas);
    printf("ultimo:    (%d, %d)\n", historico[N_TRABALHOS - 1].id, historico[N_TRABALHOS - 1].paginas);

    /* Troque este valor e rode de novo! (de 1 a 30) */
    const int ALVO_PAGINAS = 27;

    printf("\n1) ALGUM TRABALHO TEVE %d PAGINAS?\n", ALVO_PAGINAS);
    pos = busca_sequencial(historico, N_TRABALHOS, ALVO_PAGINAS, CAMPO_PAGINAS, &comp);
    if (pos >= 0) {
        printf("   sim: (%d, %d) na posicao %d  ->  %ld comparacoes\n",
               historico[pos].id, historico[pos].paginas, pos, comp);
    } else {
        printf("   nao  ->  %ld comparacoes\n", comp);
    }

    int ultimo_id = historico[N_TRABALHOS - 1].id;
    printf("\n2) O TRABALHO %d (O ULTIMO) FOI IMPRESSO?\n", ultimo_id);
    pos = busca_sequencial(historico, N_TRABALHOS, ultimo_id, CAMPO_ID, &comp);
    printf("   sim, posicao %d  ->  %ld comparacoes (pior caso)\n", pos, comp);

    printf("\n3) O TRABALHO 100 FOI IMPRESSO?  (nao existe: comecamos no 101)\n");
    busca_sequencial(historico, N_TRABALHOS, 100, CAMPO_ID, &comp);
    printf("   nao  ->  %ld comparacoes (olhou todos)\n", comp);

    printf("\nMelhor caso: 1   |   medio: (n + 1)/2   |   pior: n   ->   O(n)\n");
    return 0;
}
