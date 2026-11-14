"""
ex07_completo_regular.py — Solução do Exercício 7 (Aula 6)

  - completo: existe aresta entre TODO par de vértices distintos
              (fora da diagonal, a matriz é toda de 1s)
  - regular:  todos os vértices têm o MESMO grau
              (devolve esse grau, ou -1 se não for regular)

Todo grafo completo com n vértices é (n-1)-regular, mas nem todo grafo
regular é completo (veja o ciclo C5, que é 2-regular).
"""


def criar_matriz(n, arestas):
    m = [[0] * (n + 1) for _ in range(n + 1)]
    for (u, v) in arestas:
        m[u][v] = m[v][u] = 1
    return m


def eh_completo(m, n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j and m[i][j] == 0:
                return False            # achou um par sem aresta
    return True


def grau(m, n, v):
    return sum(m[v][j] for j in range(1, n + 1))


def eh_regular(m, n):
    g = grau(m, n, 1)
    for v in range(2, n + 1):
        if grau(m, n, v) != g:
            return -1
    return g


def testar(nome, n, arestas):
    m = criar_matriz(n, arestas)
    r = eh_regular(m, n)
    print(f"{nome:<22} completo? {'sim' if eh_completo(m, n) else 'nao':<4}"
          f" regular? {'sim, grau ' + str(r) if r >= 0 else 'nao'}")


def main():
    testar("rede da filial (6)", 6, [(1, 2), (1, 6), (2, 3), (2, 5), (2, 6),
                                     (3, 4), (3, 5), (3, 6), (4, 5), (5, 6)])
    k4 = [(u, v) for u in range(1, 5) for v in range(u + 1, 5)]
    testar("K4 (completo, 4)", 4, k4)
    testar("ciclo C5 (5)", 5, [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)])
    testar("K4 sem a aresta 1-2", 4, [a for a in k4 if a != (1, 2)])


if __name__ == "__main__":
    main()
