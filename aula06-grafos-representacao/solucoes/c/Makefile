CC = cc
CFLAGS = -std=c11 -Wall -Wextra -pedantic

PROGRAMAS = ex06 ex07 ex08 ex09 ex10

.PHONY: all clean

all: $(PROGRAMAS)

ex06: ex06_contar_arestas.c
	$(CC) $(CFLAGS) ex06_contar_arestas.c -o ex06

ex07: ex07_completo_regular.c
	$(CC) $(CFLAGS) ex07_completo_regular.c -o ex07

ex08: ex08_grafo_transposto.c
	$(CC) $(CFLAGS) ex08_grafo_transposto.c -o ex08

ex09: ex09_validar_lista.c
	$(CC) $(CFLAGS) ex09_validar_lista.c -o ex09

ex10: ex10_amigos_em_comum.c
	$(CC) $(CFLAGS) ex10_amigos_em_comum.c -o ex10

clean:
	rm -f $(PROGRAMAS)
