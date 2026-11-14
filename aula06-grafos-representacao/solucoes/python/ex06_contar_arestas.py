"""
ex06_contar_arestas.py — Solução do Exercício 6 (Aula 6)

Contar as arestas de um grafo a partir da matriz de adjacências e
detectar laços (arestas de um vértice para ele mesmo).

  - dígrafo:       cada 1 da matriz é uma seta    -> |E| = total de 1s
  - não dirigido:  cada aresta aparece duas vezes (M[u][v] e M[v][u]),
                   EXCETO o laço, que ocupa só a diagonal M[v][v].
                   Por isso contamos só o triângulo de cima, com a diagonal.
"""


def criar_matriz(n, arestas, dirigido):
    m = [[0] * (n + 1) for _ in range(n + 1)]
    for (u, v) in arestas:
        m[u][v] = 1
        if not dirigido:
            m[v][u] = 1
    return m


def contar_arestas(m, n, dirigido):
    total = 0
    for i in range(1, n + 1):
        inicio = 1 if dirigido else i   # não dirigido: só j >= i
        for j in range(inicio, n + 1):
            total += m[i][j]
    return total


def tem_laco(m, n):
    for v in range(1, n + 1):
        if m[v][v] == 1:
            return True
    return False


def relatorio(nome, m, n, dirigido):
    print(f"{nome}: {contar_arestas(m, n, dirigido)} aresta(s),"
          f" laco? {'sim' if tem_laco(m, n) else 'nao'}")


def main():
    filial = [(1, 2), (1, 6), (2, 3), (2, 5), (2, 6),
              (3, 4), (3, 5), (3, 6), (4, 5), (5, 6)]

    relatorio("1) rede da filial (nao dirigido)", criar_matriz(6, filial, False), 6, False)
    relatorio("2) mesmas arestas como digrafo  ", criar_matriz(6, filial, True), 6, True)

    com_laco = filial + [(4, 4)]        # o roteador 4 ganhou um cabo de loopback
    relatorio("3) filial + laco em 4           ", criar_matriz(6, com_laco, False), 6, False)

    ida_e_volta = [(1, 2), (2, 1), (2, 3)]   # 1 <-> 2 conta como DUAS setas
    relatorio("4) digrafo 1->2, 2->1, 2->3     ", criar_matriz(3, ida_e_volta, True), 3, True)


if __name__ == "__main__":
    main()
