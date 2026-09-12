CC = gcc
CFLAGS = -Wall -Wextra -std=c11

.PHONY: all clean

all: memoria contigua encadeada

memoria: memoria_ponteiros.c
	$(CC) $(CFLAGS) -o memoria memoria_ponteiros.c

contigua: main_contigua.c lista_contigua.c lista_contigua.h
	$(CC) $(CFLAGS) -o contigua main_contigua.c lista_contigua.c

encadeada: main_encadeada.c lista_encadeada.c lista_encadeada.h
	$(CC) $(CFLAGS) -o encadeada main_encadeada.c lista_encadeada.c

clean:
	rm -f memoria contigua encadeada
