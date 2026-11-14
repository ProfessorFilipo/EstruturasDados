CC = cc
CFLAGS = -std=c11 -Wall -Wextra -pedantic

PROGRAMAS = p1_bfs p2_dfs p3_componentes p4_dijkstra

.PHONY: all clean

all: $(PROGRAMAS)

p1_bfs: p1_bfs.c
	$(CC) $(CFLAGS) p1_bfs.c -o p1_bfs

p2_dfs: p2_dfs.c
	$(CC) $(CFLAGS) p2_dfs.c -o p2_dfs

p3_componentes: p3_componentes.c
	$(CC) $(CFLAGS) p3_componentes.c -o p3_componentes

p4_dijkstra: p4_dijkstra.c
	$(CC) $(CFLAGS) p4_dijkstra.c -o p4_dijkstra

clean:
	rm -f $(PROGRAMAS)
