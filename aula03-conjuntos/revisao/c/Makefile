CC = gcc
CFLAGS = -Wall -Wextra -std=c11

.PHONY: all clean

all: contigua encadeada demo_pilha demo_fila

contigua: main_contigua.c lista_contigua.c lista_contigua.h
	$(CC) $(CFLAGS) -o contigua main_contigua.c lista_contigua.c

encadeada: main_encadeada.c lista_encadeada.c lista_encadeada.h
	$(CC) $(CFLAGS) -o encadeada main_encadeada.c lista_encadeada.c

demo_pilha: demo_pilha.c pilha.c pilha.h
	$(CC) $(CFLAGS) -o demo_pilha pilha.c demo_pilha.c

demo_fila: demo_fila.c fila.c fila.h
	$(CC) $(CFLAGS) -o demo_fila fila.c demo_fila.c

clean:
	rm -f contigua encadeada demo_pilha demo_fila
