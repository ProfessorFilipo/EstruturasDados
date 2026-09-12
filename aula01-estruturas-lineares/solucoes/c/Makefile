CC = gcc
CFLAGS = -Wall -Wextra -std=c11
BASE = ../../c

.PHONY: all clean

all: ex01 ex05_contigua ex05_encadeada ex06 ex08 ex09 ex11 ex12 ex13 ex14

ex01: ex01_troca_ponteiros.c
	$(CC) $(CFLAGS) -o ex01 ex01_troca_ponteiros.c

ex05_contigua: ex05_esta_vazia_contigua.c $(BASE)/lista_contigua.c
	$(CC) $(CFLAGS) -I$(BASE) -o ex05_contigua ex05_esta_vazia_contigua.c $(BASE)/lista_contigua.c

ex05_encadeada: ex05_esta_vazia_encadeada.c $(BASE)/lista_encadeada.c
	$(CC) $(CFLAGS) -I$(BASE) -o ex05_encadeada ex05_esta_vazia_encadeada.c $(BASE)/lista_encadeada.c

ex06: ex06_lista_contigua_do_zero.c
	$(CC) $(CFLAGS) -o ex06 ex06_lista_contigua_do_zero.c

ex08: ex08_remover_valor_contigua.c $(BASE)/lista_contigua.c
	$(CC) $(CFLAGS) -I$(BASE) -o ex08 ex08_remover_valor_contigua.c $(BASE)/lista_contigua.c

ex09: ex09_lista_encadeada_do_zero.c
	$(CC) $(CFLAGS) -o ex09 ex09_lista_encadeada_do_zero.c

ex11: ex11_inverter_encadeada.c $(BASE)/lista_encadeada.c
	$(CC) $(CFLAGS) -I$(BASE) -o ex11 ex11_inverter_encadeada.c $(BASE)/lista_encadeada.c

ex12: ex12_contigua_para_encadeada.c $(BASE)/lista_contigua.c
	$(CC) $(CFLAGS) -I$(BASE) -o ex12 ex12_contigua_para_encadeada.c $(BASE)/lista_contigua.c

ex13: ex13_remover_duplicatas_encadeada.c $(BASE)/lista_encadeada.c
	$(CC) $(CFLAGS) -I$(BASE) -o ex13 ex13_remover_duplicatas_encadeada.c $(BASE)/lista_encadeada.c

ex14: ex14_benchmark.c
	$(CC) $(CFLAGS) -O2 -o ex14 ex14_benchmark.c

clean:
	rm -f ex01 ex05_contigua ex05_encadeada ex06 ex08 ex09 ex11 ex12 ex13 ex14
