CC = cc
CFLAGS = -std=c11 -Wall -Wextra -pedantic

.PHONY: all test clean

all: demo_pilha demo_fila central_impressao testes

demo_pilha: demo_pilha.c pilha.c pilha.h
	$(CC) $(CFLAGS) pilha.c demo_pilha.c -o demo_pilha

demo_fila: demo_fila.c fila.c fila.h
	$(CC) $(CFLAGS) fila.c demo_fila.c -o demo_fila

central_impressao: central_impressao.c pilha.c pilha.h fila.c fila.h
	$(CC) $(CFLAGS) pilha.c fila.c central_impressao.c -o central_impressao

testes: testes.c pilha.c pilha.h fila.c fila.h
	$(CC) $(CFLAGS) pilha.c fila.c testes.c -o testes

test: testes
	./testes

clean:
	rm -f demo_pilha demo_fila central_impressao testes
