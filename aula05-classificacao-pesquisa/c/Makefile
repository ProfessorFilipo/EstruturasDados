CC = cc
CFLAGS = -std=c11 -Wall -Wextra -pedantic

PROGRAMAS = busca_sequencial busca_binaria insertion_estavel merge_sort \
            quick_sort limite_inferior counting_radix

.PHONY: all clean

all: $(PROGRAMAS)

busca_sequencial: busca_sequencial.c
	$(CC) $(CFLAGS) busca_sequencial.c -o busca_sequencial

busca_binaria: busca_binaria.c
	$(CC) $(CFLAGS) busca_binaria.c -o busca_binaria

insertion_estavel: insertion_estavel.c
	$(CC) $(CFLAGS) insertion_estavel.c -o insertion_estavel

merge_sort: merge_sort.c
	$(CC) $(CFLAGS) merge_sort.c -o merge_sort

quick_sort: quick_sort.c
	$(CC) $(CFLAGS) quick_sort.c -o quick_sort

limite_inferior: limite_inferior.c
	$(CC) $(CFLAGS) limite_inferior.c -o limite_inferior

counting_radix: counting_radix.c
	$(CC) $(CFLAGS) counting_radix.c -o counting_radix

clean:
	rm -f $(PROGRAMAS)
