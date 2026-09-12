/*
 * ex01_troca_ponteiros.c — solução
 *
 * Troca o valor de duas variáveis usando apenas ponteiros.
 */
#include <stdio.h>

void trocar(int *p1, int *p2) {
    int temp = *p1;
    *p1 = *p2;
    *p2 = temp;
}

int main(void) {
    int a = 10;
    int b = 99;

    printf("antes:  a = %d, b = %d\n", a, b);
    trocar(&a, &b);
    printf("depois: a = %d, b = %d\n", a, b);

    return 0;
}
