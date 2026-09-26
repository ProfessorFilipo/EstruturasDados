CC = cc
CFLAGS = -std=c11 -Wall -Wextra -pedantic

.PHONY: all clean

all: contagem_operacoes insertion_sort busca_saltos

contagem_operacoes: contagem_operacoes.c
	$(CC) $(CFLAGS) contagem_operacoes.c -o contagem_operacoes

insertion_sort: insertion_sort.c
	$(CC) $(CFLAGS) insertion_sort.c -o insertion_sort

busca_saltos: busca_saltos.c
	$(CC) $(CFLAGS) busca_saltos.c -o busca_saltos

clean:
	rm -f contagem_operacoes insertion_sort busca_saltos
