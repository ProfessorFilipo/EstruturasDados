CC = cc
CFLAGS = -std=c11 -Wall -Wextra -pedantic

PROGRAMAS = p1_matriz_adjacencias p2_graus p3_lista_adjacencias \
            p4_comparando_representacoes

.PHONY: all clean

all: $(PROGRAMAS)

p1_matriz_adjacencias: p1_matriz_adjacencias.c
	$(CC) $(CFLAGS) p1_matriz_adjacencias.c -o p1_matriz_adjacencias

p2_graus: p2_graus.c
	$(CC) $(CFLAGS) p2_graus.c -o p2_graus

p3_lista_adjacencias: p3_lista_adjacencias.c
	$(CC) $(CFLAGS) p3_lista_adjacencias.c -o p3_lista_adjacencias

p4_comparando_representacoes: p4_comparando_representacoes.c
	$(CC) $(CFLAGS) p4_comparando_representacoes.c -o p4_comparando_representacoes

clean:
	rm -f $(PROGRAMAS)
