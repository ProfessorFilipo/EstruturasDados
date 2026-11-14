"""
ex09_rota_cidades.py — Solução do Exercício 9 (Aula 7)

Dijkstra O(V^2) com nomes: a rota mais rápida de Porto Alegre até cada
cidade da Região Metropolitana. Os tempos (minutos) são ILUSTRATIVOS — servem
para o exercício, não para planejar viagem.
"""

INF = 10**9
CIDADES = ["", "Porto Alegre", "Canoas", "Esteio", "Sapucaia do Sul",
           "Sao Leopoldo", "Novo Hamburgo", "Cachoeirinha", "Gravatai"]
N = 8
ESTRADAS = [(1, 2, 20), (1, 7, 25), (2, 3, 12), (2, 7, 15), (3, 4, 8),
            (4, 5, 10), (5, 6, 15), (7, 8, 12), (8, 6, 50), (3, 5, 22)]


def criar_lista(n, arestas):
    adj = [[] for _ in range(n + 1)]
    for (u, v, w) in arestas:
        adj[u].append((v, w))
        adj[v].append((u, w))
    return adj


def dijkstra(adj, n, s):
    dist = [INF] * (n + 1)
    pai = [0] * (n + 1)
    fechado = [False] * (n + 1)
    dist[s] = 0
    for _ in range(n):
        u = -1
        for v in range(1, n + 1):
            if not fechado[v] and (u == -1 or dist[v] < dist[u]):
                u = v
        if dist[u] == INF:
            break
        fechado[u] = True
        for (v, w) in adj[u]:
            if not fechado[v] and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                pai[v] = u
    return dist, pai


def rota(pai, destino):
    c = [destino]
    while pai[c[-1]] != 0:
        c.append(pai[c[-1]])
    return c[::-1]


def main():
    adj = criar_lista(N, ESTRADAS)
    origem = 1
    dist, pai = dijkstra(adj, N, origem)
    print(f"Rotas mais rapidas a partir de {CIDADES[origem]} (tempos ilustrativos)\n")
    ordem = sorted(range(1, N + 1), key=lambda v: dist[v])
    for v in ordem:
        if v == origem:
            continue
        print(f"{CIDADES[v]:<16}{dist[v]:>4} min   " +
              " -> ".join(CIDADES[x] for x in rota(pai, v)))


if __name__ == "__main__":
    main()
