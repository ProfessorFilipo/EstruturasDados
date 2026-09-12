CC = gcc
CFLAGS = -Wall -Wextra -std=c11

.PHONY: all clean

all: demo_conjunto

demo_conjunto: demo_conjunto.c
	$(CC) $(CFLAGS) -o demo_conjunto demo_conjunto.c

clean:
	rm -f demo_conjunto
