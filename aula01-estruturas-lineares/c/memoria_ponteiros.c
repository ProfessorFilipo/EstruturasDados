/*
 * memoria_ponteiros.c
 *
 * Estruturas de Dados — Aula 1 — Bloco 2 (Nivelamento)
 *
 * Demonstra o conceito de ponteiro em C: uma variável que guarda o
 * ENDEREÇO de outra variável, em vez do valor diretamente.
 */
#include <stdio.h>

int main(void) {
    int x = 42;
    int *p = &x; /* p guarda o ENDEREÇO de x */

    printf("x               = %d\n", x);
    printf("&x (endereco)   = %p\n", (void *)&x);
    printf("p               = %p\n", (void *)p);
    printf("*p (valor de x através de p) = %d\n", *p);

    /* alterar *p altera x indiretamente, pois apontam para o mesmo endereço */
    *p = 100;
    printf("\napos '*p = 100':\n");
    printf("x               = %d\n", x);

    return 0;
}
