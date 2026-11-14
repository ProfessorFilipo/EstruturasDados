"""
p4_dijkstra.py

Estruturas de Dados — Aula 7 — Prática P4 (Caminho mínimo — Dijkstra)
Slides 21 a 25 (teoria) e 34 (prática)

Agora cada cabo da rede da filial tem uma LATÊNCIA (em ms) — os mesmos
pesos do exemplo do livro de Ascencio & Araújo (p. 409). Qual é a rota
mais RÁPIDA do roteador 1 até cada um dos outros?

Dijkstra, versão simples O(V^2):
  1. dist[origem] = 0; todos os outros = INF (infinito)
  2. repita: escolha o vértice ABERTO com a menor dist e FECHE-o
             (a distância dele não muda mais);
             RELAXE cada vizinho v:  se dist[u] + peso < dist[v], melhore v
Funciona com pesos NÃO NEGATIVOS. É o mesmo princípio usado pelo protocolo
de roteamento OSPF ("Shortest Path First").

O livro usa uma lista de prioridades (heap) para achar o menor mais rápido:
O((V + E) log V). Aqui, para ficar simples, procuramos o menor varrendo o
vetor: O(V) por rodada, O(V^2) no total.

Só usa a biblioteca padrão — cole direto no onlineide.pro/playground/python
"""
from collections import deque

N = 6
INF = 10**9                             # "infinito": maior que qualquer rota
ADJ = [[],                              # (vizinho, latência em ms)
       [(6, 7), (2, 2)],
       [(6, 4), (5, 3), (3, 9), (1, 2)],
       [(6, 3), (5, 4), (4, 5), (2, 9)],
       [(5, 3), (3, 5)],
       [(6, 1), (4, 3), (3, 4), (2, 3)],
       [(5, 1), (3, 3), (2, 4), (1, 7)]]

ORIGEM = 1


# ------------------------------------------------------------------
# Versão "limpa", idêntica à do slide.
# ------------------------------------------------------------------
def dijkstra(adj, n, s):
    dist = [INF] * (n + 1)
    pai = [0] * (n + 1)
    fechado = [False] * (n + 1)
    dist[s] = 0
    for _ in range(n):
        u = -1                          # acha o aberto com menor dist: O(V)
        for v in range(1, n + 1):
            if not fechado[v] and (u == -1 or dist[v] < dist[u]):
                u = v
        if dist[u] == INF:
            break                       # o resto é inalcançável
        fechado[u] = True
        for (v, peso) in adj[u]:        # relaxamento
            if not fechado[v] and dist[u] + peso < dist[v]:
                dist[v] = dist[u] + peso
                pai[v] = u
    return dist, pai


def caminho(pai, destino):
    c = [destino]
    while pai[c[-1]] != 0:
        c.append(pai[c[-1]])
    return c[::-1]


def mostra(d):
    return "INF" if d == INF else str(d)


# O mesmo Dijkstra, imprimindo a tabela de cada rodada (para a demonstração).
def dijkstra_passo_a_passo(adj, n, s):
    dist = [INF] * (n + 1)
    pai = [0] * (n + 1)
    fechado = [False] * (n + 1)
    dist[s] = 0
    print("   rodada fecha |" + "".join(f"{v:>5}" for v in range(1, n + 1)))
    print("   inicio       |" + "".join(f"{mostra(dist[v]):>5}" for v in range(1, n + 1)))
    for r in range(1, n + 1):
        u = -1
        for v in range(1, n + 1):
            if not fechado[v] and (u == -1 or dist[v] < dist[u]):
                u = v
        if dist[u] == INF:
            break
        fechado[u] = True
        for (v, peso) in adj[u]:
            if not fechado[v] and dist[u] + peso < dist[v]:
                dist[v] = dist[u] + peso
                pai[v] = u
        print(f"   {r:>6} {u:>5} |" + "".join(f"{mostra(dist[v]):>5}" for v in range(1, n + 1)))
    return dist, pai


def bfs_saltos(adj, n, s):
    """BFS ignorando os pesos (só para comparar com o Dijkstra)."""
    marcado = [False] * (n + 1)
    pai = [0] * (n + 1)
    fila = deque([s])
    marcado[s] = True
    while fila:
        u = fila.popleft()
        for (v, _) in adj[u]:
            if not marcado[v]:
                marcado[v] = True
                pai[v] = u
                fila.append(v)
    return pai


def custo(adj, c):
    total = 0
    for a, b in zip(c, c[1:]):
        total += dict(adj[a])[b]
    return total


def main():
    print(f"1) Dijkstra a partir do roteador {ORIGEM} (latencias em ms)")
    dist, pai = dijkstra_passo_a_passo(ADJ, N, ORIGEM)
    assert (dist, pai) == dijkstra(ADJ, N, ORIGEM)

    print("\n2) Rota mais rapida ate cada roteador (seguindo pai[])")
    for v in range(1, N + 1):
        c = caminho(pai, v)
        print(f"   ate {v}: {' -> '.join(str(x) for x in c):<20} {mostra(dist[v]):>3} ms")

    print("\n3) Menos saltos (BFS) x menor latencia (Dijkstra), ate o roteador 3")
    c_bfs = caminho(bfs_saltos(ADJ, N, ORIGEM), 3)
    c_dij = caminho(pai, 3)
    print(f"   BFS:      {' -> '.join(str(x) for x in c_bfs):<18}"
          f"{len(c_bfs) - 1} saltos, {custo(ADJ, c_bfs)} ms")
    print(f"   Dijkstra: {' -> '.join(str(x) for x in c_dij):<18}"
          f"{len(c_dij) - 1} saltos, {custo(ADJ, c_dij)} ms")


if __name__ == "__main__":
    main()
