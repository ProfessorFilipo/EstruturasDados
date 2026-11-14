"""
ex06_graus_separacao.py — Solução do Exercício 6 (Aula 7)

Graus de separação numa rede de amizades: a BFS a partir de uma pessoa dá,
para cada outra, o MENOR número de "pulos" de amizade até ela.
  - dist == 1: amigos
  - dist == 2: amigos de amigos (boas sugestões de amizade)
  - pai[]:     a cadeia de apresentações

É a mesma rede do Exercício 10 da Aula 6.
"""
from collections import deque

NOMES = ["", "Ana", "Bruno", "Carla", "Davi", "Elisa", "Fabio", "Gabi", "Hugo"]
N = 8
AMIZADES = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 5), (3, 5), (3, 6),
            (4, 5), (4, 6), (5, 7), (6, 7), (7, 8)]


def criar_lista(n, arestas):
    adj = [[] for _ in range(n + 1)]
    for (u, v) in arestas:
        adj[u].append(v)
        adj[v].append(u)
    return adj


def bfs(adj, n, s):
    dist = [-1] * (n + 1)               # -1 também serve de "não marcado"
    pai = [0] * (n + 1)
    dist[s] = 0
    fila = deque([s])
    while fila:
        u = fila.popleft()
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                pai[v] = u
                fila.append(v)
    return dist, pai


def cadeia(pai, destino):
    c = [destino]
    while pai[c[-1]] != 0:
        c.append(pai[c[-1]])
    return c[::-1]


def main():
    adj = criar_lista(N, AMIZADES)
    origem = 1
    dist, pai = bfs(adj, N, origem)

    print(f"1) Graus de separacao a partir de {NOMES[origem]}")
    for v in range(1, N + 1):
        print(f"   {NOMES[v]:<6} {dist[v]}")

    print(f"\n2) Amigos de amigos de {NOMES[origem]} (sugestoes):",
          ", ".join(NOMES[v] for v in range(1, N + 1) if dist[v] == 2))

    longe = max(range(1, N + 1), key=lambda v: dist[v])
    print(f"\n3) Pessoa mais distante: {NOMES[longe]} ({dist[longe]} graus)")
    print("   cadeia de apresentacoes:", " -> ".join(NOMES[v] for v in cadeia(pai, longe)))


if __name__ == "__main__":
    main()
