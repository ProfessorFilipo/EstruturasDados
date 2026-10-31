"""
ex07_merge_sort_estavel.py — Aula 5, Exercício 7 (solução de referência)

Merge Sort de trabalhos (id, paginas) pelas páginas. É estável porque, no
empate, a intercalação tira primeiro da metade ESQUERDA (o <=), e a
esquerda guarda quem chegou antes.

Só usa a biblioteca padrão — cole direto no onlineide.pro/playground/python
"""
import random

PAGINAS = 1


def merge_sort_por_paginas(trabalhos):
    """Devolve uma NOVA lista ordenada pelas páginas (estável)."""
    if len(trabalhos) <= 1:
        return list(trabalhos)
    meio = len(trabalhos) // 2
    esq = merge_sort_por_paginas(trabalhos[:meio])
    dir = merge_sort_por_paginas(trabalhos[meio:])
    resultado, i, j = [], 0, 0
    while i < len(esq) and j < len(dir):
        if esq[i][PAGINAS] <= dir[j][PAGINAS]:     # <= : empate sai da esquerda
            resultado.append(esq[i]); i += 1
        else:
            resultado.append(dir[j]); j += 1
    return resultado + esq[i:] + dir[j:]


def insertion_sort_por_paginas(trabalhos):
    """O Insertion Sort estável da aula (insertion_estavel.py), numa cópia."""
    v = list(trabalhos)
    for i in range(1, len(v)):
        chave, j = v[i], i - 1
        while j >= 0 and v[j][PAGINAS] > chave[PAGINAS]:
            v[j + 1] = v[j]
            j -= 1
        v[j + 1] = chave
    return v


def main():
    fila = [(101, 12), (102, 3), (104, 12), (105, 7),
            (107, 3), (108, 20), (110, 7), (111, 1)]
    print("1) OS 8 TRABALHOS DA DEMO 3")
    merge = merge_sort_por_paginas(fila)
    print("   merge:    ", merge)
    print("   insertion:", insertion_sort_por_paginas(fila))
    print("   iguais?", merge == insertion_sort_por_paginas(fila))

    print("\n2) 1.000 TRABALHOS COM PAGINAS ALEATORIAS")
    gerador = random.Random(2026)
    muitos = [(101 + i, gerador.randint(1, 30)) for i in range(1000)]
    merge = merge_sort_por_paginas(muitos)
    print("   igual ao Insertion Sort?", merge == insertion_sort_por_paginas(muitos))
    print("   igual ao sorted() (estavel)?", merge == sorted(muitos, key=lambda t: t[PAGINAS]))


if __name__ == "__main__":
    main()
