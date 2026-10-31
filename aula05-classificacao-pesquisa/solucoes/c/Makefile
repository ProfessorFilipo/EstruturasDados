CC = cc
CFLAGS = -std=c11 -Wall -Wextra -pedantic

PROGRAMAS = ex03 ex07 ex08 ex13

.PHONY: all clean

all: $(PROGRAMAS)

ex03: ex03_buscar_primeira.c
	$(CC) $(CFLAGS) ex03_buscar_primeira.c -o ex03

ex07: ex07_merge_sort_estavel.c
	$(CC) $(CFLAGS) ex07_merge_sort_estavel.c -o ex07

ex08: ex08_quick_mediana_tres.c
	$(CC) $(CFLAGS) ex08_quick_mediana_tres.c -o ex08

ex13: ex13_ordenar_automatico.c
	$(CC) $(CFLAGS) ex13_ordenar_automatico.c -o ex13

clean:
	rm -f $(PROGRAMAS)
