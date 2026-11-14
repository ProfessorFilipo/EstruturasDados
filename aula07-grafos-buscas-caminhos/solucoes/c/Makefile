CC = cc
CFLAGS = -std=c11 -Wall -Wextra -pedantic

PROGRAMAS = ex06 ex07 ex08 ex09 ex10

.PHONY: all clean

all: $(PROGRAMAS)

ex06: ex06_graus_separacao.c
	$(CC) $(CFLAGS) ex06_graus_separacao.c -o ex06

ex07: ex07_tem_ciclo.c
	$(CC) $(CFLAGS) ex07_tem_ciclo.c -o ex07

ex08: ex08_dois_times.c
	$(CC) $(CFLAGS) ex08_dois_times.c -o ex08

ex09: ex09_rota_cidades.c
	$(CC) $(CFLAGS) ex09_rota_cidades.c -o ex09

ex10: ex10_labirinto.c
	$(CC) $(CFLAGS) ex10_labirinto.c -o ex10

clean:
	rm -f $(PROGRAMAS)
