"""
ex07_tem_ciclo.py — Solução do Exercício 7 (Aula 7)

Um grafo NÃO dirigido tem ciclo se, durante a DFS, encontramos um vizinho
JÁ MARCADO que não é o pai do vértice atual (o pai não conta: é só a
aresta pela qual chegamos). Essa aresta "fecha" o ciclo.

Sem ciclo e conexo = árvore; sem ciclo e desconexo = floresta.
"""


def criar_lista(n, arestas):
    adj = [[] for _ in range(n + 1)]
    for (u, v) in arestas:
        adj[u].append(v)
        adj[v].append(u)
    return adj


def dfs_ciclo(adj, u, pai, marcado):
    marcado[u] = True
    for v in adj[u]:
        if not marcado[v]:
            achou = dfs_ciclo(adj, v, u, marcado)
            if achou:
                return achou
        elif v != pai:
            return (u, v)               # v já visitado e não é o pai: ciclo!
    return None


def tem_ciclo(adj, n):
    marcado = [False] * (n + 1)
    for v in range(1, n + 1):           # testa todas as componentes
        if not marcado[v]:
            achou = dfs_ciclo(adj, v, 0, marcado)
            if achou:
                return achou
    return None


def testar(nome, n, arestas):
    achou = tem_ciclo(criar_lista(n, arestas), n)
    if achou:
        print(f"{nome:<28} tem ciclo: sim (fechado pela aresta {achou[0]}-{achou[1]})")
    else:
        print(f"{nome:<28} tem ciclo: nao")


def main():
    testar("1) rede da filial", 6, [(1, 2), (1, 6), (2, 3), (2, 5), (2, 6),
                                    (3, 4), (3, 5), (3, 6), (4, 5), (5, 6)])
    arvore = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6)]
    testar("2) arvore com 6 vertices", 6, arvore)
    testar("3) floresta (duas arvores)", 7, [(1, 2), (2, 3), (4, 5), (5, 6), (5, 7)])
    testar("4) arvore + aresta 4-6", 6, arvore + [(4, 6)])


if __name__ == "__main__":
    main()
