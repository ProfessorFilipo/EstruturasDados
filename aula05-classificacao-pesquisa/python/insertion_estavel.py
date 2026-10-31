"""
insertion_estavel.py

Estruturas de Dados — Aula 5 — Bloco 3 (Insertion Sort revisitado)
Slides 14 e 15

O Insertion Sort da Aula 4, agora ordenando trabalhos (id, paginas)
pelo número de páginas. Duas lições:

1) ESTABILIDADE: trabalhos com o mesmo número de páginas continuam na
   ordem de chegada (a justiça da fila FIFO). Isso acontece porque só
   deslocamos quem é ESTRITAMENTE maior que a chave ( > , não >= ).

2) CRESCIMENTO: dobrar n multiplica as comparações por ~4 -> Theta(n^2)
   no caso médio. Para ordenar 10.000 trabalhos, é caro demais.

Só usa a biblioteca padrão — cole direto no onlineide.pro/playground/python
"""
import random

PAGINAS = 1   # trabalho[1] -> quantidade de páginas


def fmt(x):
    """Formata inteiros no padrão brasileiro: 1234567 -> 1.234.567"""
    return f"{x:,}".replace(",", ".")


def insertion_sort_por_paginas(v):
    """Ordena v (lista de tuplas (id, paginas)) pelas páginas, no lugar.
    Devolve o número de comparações."""
    comparacoes = 0
    for i in range(1, len(v)):
        chave = v[i]
        j = i - 1
        while j >= 0:
            comparacoes += 1
            if not (v[j][PAGINAS] > chave[PAGINAS]):   # > mantém a estabilidade
                break
            v[j + 1] = v[j]                            # desloca para a direita
            j -= 1
        v[j + 1] = chave                               # encaixa
    return comparacoes


def gerar_trabalhos(n, gerador):
    """n trabalhos com IDs crescentes e páginas aleatórias de 1 a 30."""
    return [(101 + i, gerador.randint(1, 30)) for i in range(n)]


def main():
    print("1) ESTABILIDADE: 8 trabalhos ordenados por paginas")
    fila = [(101, 12), (102, 3), (104, 12), (105, 7),
            (107, 3), (108, 20), (110, 7), (111, 1)]
    print("   antes: ", fila)
    insertion_sort_por_paginas(fila)
    print("   depois:", fila)
    print("   empates (3, 7 e 12 paginas) mantem a ordem de chegada dos IDs")

    print("\n2) CRESCIMENTO: paginas aleatorias")
    gerador = random.Random(2026)
    anterior = None
    print(f"{'n':>7} {'comparacoes':>13} {'razao':>7}")
    for n in (500, 1000, 2000):
        comp = insertion_sort_por_paginas(gerar_trabalhos(n, gerador))
        razao = f"x{comp / anterior:.1f}".replace(".", ",") if anterior else "-"
        print(f"{n:>7} {fmt(comp):>13} {razao:>7}")
        anterior = comp
    print("\nDobrou n -> comparacoes x4: Theta(n^2)")


if __name__ == "__main__":
    main()
