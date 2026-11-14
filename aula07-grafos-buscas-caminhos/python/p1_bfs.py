"""
p1_bfs.py

Estruturas de Dados — Aula 7 — Prática P1 (Busca em largura — BFS)
Slides 05 a 09 (teoria) e 31 (prática)

A rede da filial (Aula 6): quantos SALTOS (roteadores no caminho) separam
o roteador 1 de cada um dos outros? A BFS responde explorando o grafo em
"ondas": primeiro os vizinhos (1 salto), depois os vizinhos dos vizinhos
(2 saltos), e assim por diante. Quem organiza as ondas é uma FILA (Aula 2).

A lista de adjacências está na MESMA ordem do livro de Ascencio & Araújo
(p. 391), para você conferir o passo a passo com as ilustrações de lá.

Custo: cada vértice entra na fila uma vez e cada lista é percorrida uma
vez -> O(V + E).

Só usa a biblioteca padrão — cole direto no onlineide.pro/playground/python
"""
from collections import deque           # deque = fila com popleft() em O(1)

N = 6
ADJ = [[],                              # posição 0 sem uso, como no livro
       [6, 2],                          # vizinhos de 1
       [5, 3, 1, 6],                    # vizinhos de 2
       [6, 5, 4, 2],                    # vizinhos de 3
       [5, 3],                          # vizinhos de 4
       [6, 4, 3, 2],                    # vizinhos de 5
       [5, 3, 2, 1]]                    # vizinhos de 6

ORIGEM = 1                              # troque e rode de novo!


# ------------------------------------------------------------------
# Versão "limpa", idêntica à do slide.
# ------------------------------------------------------------------
def bfs(adj, n, s):
    marcado = [False] * (n + 1)
    dist = [-1] * (n + 1)               # -1 = ainda não alcançado
    pai = [0] * (n + 1)                 # 0 = sem pai
    fila = deque([s])
    marcado[s] = True
    dist[s] = 0
    while fila:
        u = fila.popleft()              # tira o primeiro da fila
        for v in adj[u]:
            if not marcado[v]:          # vizinho novo?
                marcado[v] = True
                dist[v] = dist[u] + 1   # um salto a mais que u
                pai[v] = u              # chegamos em v vindo de u
                fila.append(v)          # entra no fim da fila
    return dist, pai


def caminho(pai, destino):
    """Reconstrói o caminho origem -> destino seguindo pai[] de trás para frente."""
    c = [destino]
    while pai[c[-1]] != 0:
        c.append(pai[c[-1]])
    return c[::-1]


# A mesma BFS, mostrando cada passo (para a demonstração).
def bfs_passo_a_passo(adj, n, s):
    marcado = [False] * (n + 1)
    dist = [-1] * (n + 1)
    pai = [0] * (n + 1)
    fila = deque([s])
    marcado[s] = True
    dist[s] = 0
    ordem = []
    print(f"   inicio: marca {s}, dist[{s}] = 0, fila = {list(fila)}")
    while fila:
        u = fila.popleft()
        ordem.append(u)
        novos = []
        for v in adj[u]:
            if not marcado[v]:
                marcado[v] = True
                dist[v] = dist[u] + 1
                pai[v] = u
                fila.append(v)
                novos.append(v)
        entram = " ".join(str(x) for x in novos) if novos else "-"
        viz = str(adj[u])
        print(f"   tira {u} | vizinhos {viz:<12} | entram: {entram:<5} | fila = {list(fila)}")
    return ordem, dist, pai


def main():
    print(f"1) BFS a partir do roteador {ORIGEM}, passo a passo")
    ordem, dist, pai = bfs_passo_a_passo(ADJ, N, ORIGEM)
    assert (dist, pai) == bfs(ADJ, N, ORIGEM)   # confere com a versão limpa
    print("   ordem de visita:", " ".join(str(v) for v in ordem))

    print("\n2) Distancia (saltos) e pai de cada vertice")
    print("   vertice: " + " ".join(f"{v:>2}" for v in range(1, N + 1)))
    print("   dist:    " + " ".join(f"{dist[v]:>2}" for v in range(1, N + 1)))
    print("   pai:     " + " ".join(f"{pai[v]:>2}" for v in range(1, N + 1)))

    print("\n3) Caminho com MENOS saltos ate cada roteador (seguindo pai[])")
    for v in range(1, N + 1):
        c = caminho(pai, v)
        print(f"   ate {v}: {' -> '.join(str(x) for x in c):<20} ({dist[v]} salto(s))")


if __name__ == "__main__":
    main()
