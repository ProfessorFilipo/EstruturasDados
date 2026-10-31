"""
merge_sort.py

Estruturas de Dados — Aula 5 — Bloco 4 (Merge Sort)
Slides 16 a 20

0) RECURSÃO DE BOLSO: uma função que chama a si mesma com um problema
   menor, até chegar ao CASO BASE. Cada chamada em andamento fica na
   PILHA DE CHAMADAS — a Pilha (LIFO) da Aula 2: a última chamada a
   entrar é a primeira a devolver o resultado.

1) INTERCALAR (merge): duas filas já ordenadas viram uma só. Compara as
   FRENTES e desenfileira a menor — as operações da Fila da Aula 2.
   Custo: Theta(n1 + n2).

2) MERGE SORT: divide o vetor ao meio até sobrar 1 elemento (que já está
   ordenado) e intercala as metades na volta.
   log2(n) níveis x n de trabalho por nível -> Theta(n log n) em TODOS
   os casos. É estável e usa memória extra O(n).

Só usa a biblioteca padrão — cole direto no onlineide.pro/playground/python
"""
import math
import random
from collections import deque

comparacoes = 0   # contador global de comparações do merge sort


def fmt(x):
    """Formata inteiros no padrão brasileiro: 1234567 -> 1.234.567"""
    return f"{x:,}".replace(",", ".")


# ------------------------------------------------------------------
# Versões "limpas", idênticas às dos slides 16 e 19 — para referência.
# ------------------------------------------------------------------
def soma_paginas(paginas):
    if len(paginas) == 0:       # caso base
        return 0
    return paginas[0] + soma_paginas(paginas[1:])


def merge_sort(v):
    if len(v) <= 1:                 # caso base
        return v
    meio = len(v) // 2
    esq = merge_sort(v[:meio])      # ordena a esquerda
    dir = merge_sort(v[meio:])      # ordena a direita
    return intercalar(esq, dir)


def intercalar(esq, dir):
    resultado, i, j = [], 0, 0
    while i < len(esq) and j < len(dir):
        if esq[i] <= dir[j]:        # <= : estável
            resultado.append(esq[i]); i += 1
        else:
            resultado.append(dir[j]); j += 1
    return resultado + esq[i:] + dir[j:]


# ------------------------------------------------------------------
# As mesmas ideias, agora mostrando cada passo e contando comparações.
# ------------------------------------------------------------------
def soma_paginas_rastreada(paginas, nivel=0):
    """Mesma soma recursiva, imprimindo cada chamada e cada devolução.
    O recuo do texto mostra a profundidade da pilha de chamadas."""
    recuo = "   " * nivel
    print(f"{recuo}chamou soma_paginas({paginas})")
    if len(paginas) == 0:                               # caso base
        print(f"{recuo}devolve 0")
        return 0
    total = paginas[0] + soma_paginas_rastreada(paginas[1:], nivel + 1)
    print(f"{recuo}devolve {total}")
    return total


def intercalar_filas(fila_a, fila_b):
    """Intercala duas filas ordenadas usando só a frente de cada uma."""
    resultado = []
    while fila_a and fila_b:
        if fila_a[0] <= fila_b[0]:                      # compara as frentes
            resultado.append(fila_a.popleft())          # desenfileira de A
        else:
            resultado.append(fila_b.popleft())          # desenfileira de B
    resultado.extend(fila_a)                            # sobrou alguém?
    resultado.extend(fila_b)
    return resultado


def intercalar_contando(esq, dir):
    """Igual a intercalar(), somando 1 no contador a cada comparação."""
    global comparacoes
    resultado = []
    i = j = 0
    while i < len(esq) and j < len(dir):
        comparacoes += 1
        if esq[i] <= dir[j]:
            resultado.append(esq[i])
            i += 1
        else:
            resultado.append(dir[j])
            j += 1
    resultado.extend(esq[i:])
    resultado.extend(dir[j:])
    return resultado


def merge_sort_contando(v, nivel=0, mostrar=False):
    """Igual a merge_sort(); se mostrar=True, imprime cada intercalação."""
    if len(v) <= 1:                                     # caso base
        return v
    meio = len(v) // 2
    esq = merge_sort_contando(v[:meio], nivel + 1, mostrar)
    dir = merge_sort_contando(v[meio:], nivel + 1, mostrar)
    junto = intercalar_contando(esq, dir)
    if mostrar:
        print("   " * nivel + f"intercala {esq} + {dir} -> {junto}")
    return junto


def main():
    global comparacoes

    print("0) RECURSAO DE BOLSO")
    print("total =", soma_paginas_rastreada([12, 5, 8]))

    print("\n1) INTERCALAR DUAS FILAS ORDENADAS (duas impressoras)")
    a, b = deque([2, 5, 9]), deque([3, 4, 12])
    print(f"   A = {list(a)}   B = {list(b)}")
    print("   ->", intercalar_filas(a, b))

    print("\n2) MERGE SORT PASSO A PASSO (recuo = profundidade da pilha)")
    paginas = [12, 5, 8, 3, 20, 1, 9, 6]
    comparacoes = 0
    print("   resultado:", merge_sort_contando(paginas, mostrar=True))
    print(f"   {comparacoes} comparacoes  (n log2 n = {len(paginas) * 3})")

    print("\n3) CRESCIMENTO: merge sort x n log2 n")
    gerador = random.Random(2026)
    anterior = None
    print(f"{'n':>7} {'comparacoes':>12} {'n*log2(n)':>10} {'razao':>6}")
    for n in (1000, 2000, 4000):
        v = [gerador.randint(1, 1_000_000) for _ in range(n)]
        comparacoes = 0
        ordenado = merge_sort_contando(v)
        assert ordenado == merge_sort(v) == sorted(v)   # confere com a versão limpa
        razao = f"x{comparacoes / anterior:.1f}".replace(".", ",") if anterior else "-"
        print(f"{n:>7} {fmt(comparacoes):>12} {fmt(round(n * math.log2(n))):>10} {razao:>6}")
        anterior = comparacoes
    print("\nDobrou n -> comparacoes x2,2 (e nao x4): Theta(n log n)")


if __name__ == "__main__":
    main()
