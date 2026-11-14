"""
p1_matriz_adjacencias.py

Estruturas de Dados — Aula 6 — Prática P1 (Matriz de adjacências)
Slides 21 (teoria) e 28 (prática)

A "rede da filial": 6 roteadores ligados por 10 cabos. É o mesmo grafo
do livro de Ascencio & Araújo (cap. 8, p. 391), que vamos usar nas duas aulas.

Matriz de adjacências M (n x n):
    M[u][v] = 1  se existe a aresta (u, v)
    M[u][v] = 0  caso contrário
Os vértices são numerados de 1 a n, como no livro: a linha 0 e a coluna 0
existem na memória, mas ficam sem uso.

Experimente: troque DIRIGIDO = False por True e rode de novo.

Só usa a biblioteca padrão — cole direto no onlineide.pro/playground/python
"""

N = 6                                   # número de vértices (roteadores)
ARESTAS = [(1, 2), (1, 6), (2, 3), (2, 5), (2, 6),
           (3, 4), (3, 5), (3, 6), (4, 5), (5, 6)]

DIRIGIDO = False                        # True: cada par (u, v) vira a seta u -> v


# ------------------------------------------------------------------
# Versão "limpa", idêntica à do slide.
# ------------------------------------------------------------------
def criar_matriz(n, arestas, dirigido):
    m = [[0] * (n + 1) for _ in range(n + 1)]   # (n+1) x (n+1), tudo 0
    for (u, v) in arestas:
        m[u][v] = 1
        if not dirigido:
            m[v][u] = 1                 # não dirigido: vale nos dois sentidos
    return m


def imprimir_matriz(m, n):
    print("      " + " ".join(f"{j:>2}" for j in range(1, n + 1)))
    for i in range(1, n + 1):
        linha = " ".join(f"{m[i][j]:>2}" for j in range(1, n + 1))
        print(f"   {i:>2} {linha}")


def eh_simetrica(m, n):
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if m[i][j] != m[j][i]:
                return False
    return True


def contar_uns(m, n):
    total = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            total += m[i][j]
    return total


def main():
    tipo = "DIRIGIDO" if DIRIGIDO else "NAO DIRIGIDO"
    print(f"1) Grafo {tipo}: {N} vertices e {len(ARESTAS)} arestas")
    m = criar_matriz(N, ARESTAS, DIRIGIDO)
    imprimir_matriz(m, N)

    print("\n2) A matriz e simetrica (M[i][j] == M[j][i])?",
          "sim" if eh_simetrica(m, N) else "nao")

    uns = contar_uns(m, N)
    if DIRIGIDO:
        print(f"3) Quantidade de 1s: {uns} = |E| (cada seta marca 1 posicao)")
    else:
        print(f"3) Quantidade de 1s: {uns} = 2 x |E| (cada aresta marca 2 posicoes)")

    print("\n4) Consultas diretas, custo O(1):")
    for (u, v) in [(2, 5), (1, 4), (5, 2)]:
        resposta = "sim" if m[u][v] == 1 else "nao"
        print(f"   existe aresta {u} -> {v}?  M[{u}][{v}] = {m[u][v]}  ({resposta})")

    print(f"\n5) Memoria: a matriz tem {N} x {N} = {N * N} celulas uteis,"
          f" mas so {uns} guardam 1.")


if __name__ == "__main__":
    main()
