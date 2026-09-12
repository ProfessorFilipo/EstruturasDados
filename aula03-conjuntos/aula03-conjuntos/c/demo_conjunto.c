/*
 * demo_conjunto.c
 *
 * Estruturas de Dados — Aula 3 — Bloco 4 (Conjuntos: implementação)
 *
 * TAD Conjunto simples sobre array — sem duplicatas, sem posição.
 * Arquivo único, só <stdio.h> — cole direto no onlineide.pro/playground/c
 */
#include <stdio.h>

#define CAPACIDADE 20

typedef struct {
    int dados[CAPACIDADE];
    int tamanho;
} Conjunto;

void conjunto_criar(Conjunto *c) {
    c->tamanho = 0;
}

int conjunto_pertence(const Conjunto *c, int valor) {
    for (int i = 0; i < c->tamanho; i++) {
        if (c->dados[i] == valor) {
            return 1;
        }
    }
    return 0;
}

int conjunto_inserir(Conjunto *c, int valor) {
    if (conjunto_pertence(c, valor)) {
        return 0; /* ja existe -- Conjunto nao duplica */
    }
    if (c->tamanho >= CAPACIDADE) {
        return 0; /* cheio */
    }
    c->dados[c->tamanho] = valor;
    c->tamanho++;
    return 1;
}

int conjunto_remover(Conjunto *c, int valor) {
    for (int i = 0; i < c->tamanho; i++) {
        if (c->dados[i] == valor) {
            c->dados[i] = c->dados[c->tamanho - 1];
            c->tamanho--;
            return 1;
        }
    }
    return 0;
}

void conjunto_uniao(const Conjunto *a, const Conjunto *b, Conjunto *resultado) {
    conjunto_criar(resultado);
    for (int i = 0; i < a->tamanho; i++) {
        conjunto_inserir(resultado, a->dados[i]);
    }
    for (int i = 0; i < b->tamanho; i++) {
        conjunto_inserir(resultado, b->dados[i]);
    }
}

void conjunto_intersecao(const Conjunto *a, const Conjunto *b, Conjunto *resultado) {
    conjunto_criar(resultado);
    for (int i = 0; i < a->tamanho; i++) {
        if (conjunto_pertence(b, a->dados[i])) {
            conjunto_inserir(resultado, a->dados[i]);
        }
    }
}

void conjunto_diferenca(const Conjunto *a, const Conjunto *b, Conjunto *resultado) {
    conjunto_criar(resultado);
    for (int i = 0; i < a->tamanho; i++) {
        if (!conjunto_pertence(b, a->dados[i])) {
            conjunto_inserir(resultado, a->dados[i]);
        }
    }
}

void conjunto_imprimir(const Conjunto *c) {
    printf("{");
    for (int i = 0; i < c->tamanho; i++) {
        printf("%d", c->dados[i]);
        if (i < c->tamanho - 1) {
            printf(", ");
        }
    }
    printf("}\n");
}

int main(void) {
    Conjunto a, b, uniao, intersecao, diferenca;
    conjunto_criar(&a);
    conjunto_criar(&b);

    int valores_a[] = {1, 2, 3, 4};
    for (int i = 0; i < 4; i++) {
        conjunto_inserir(&a, valores_a[i]);
    }

    int valores_b[] = {3, 4, 5, 6};
    for (int i = 0; i < 4; i++) {
        conjunto_inserir(&b, valores_b[i]);
    }

    printf("A = ");
    conjunto_imprimir(&a);
    printf("B = ");
    conjunto_imprimir(&b);

    printf("\npertence(A, 2)  = %d\n", conjunto_pertence(&a, 2));
    printf("pertence(A, 99) = %d\n", conjunto_pertence(&a, 99));

    conjunto_inserir(&a, 2); /* ja existe -- nao duplica */
    printf("\napos inserir(A, 2) de novo: ");
    conjunto_imprimir(&a);

    conjunto_remover(&a, 1);
    printf("apos remover(A, 1):         ");
    conjunto_imprimir(&a);
    conjunto_inserir(&a, 1); /* volta ao estado original para as proximas operacoes */

    conjunto_uniao(&a, &b, &uniao);
    conjunto_intersecao(&a, &b, &intersecao);
    conjunto_diferenca(&a, &b, &diferenca);

    printf("\nA uniao B      = ");
    conjunto_imprimir(&uniao);
    printf("A intersecao B = ");
    conjunto_imprimir(&intersecao);
    printf("A diferenca B  = ");
    conjunto_imprimir(&diferenca);

    return 0;
}
