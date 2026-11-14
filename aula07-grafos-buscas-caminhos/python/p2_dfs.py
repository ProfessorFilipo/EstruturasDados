"""
p2_dfs.py

Estruturas de Dados — Aula 7 — Prática P2 (Busca em profundidade — DFS)
Slides 13 a 15 (teoria) e 32 (prática)

A DFS explora como quem anda num labirinto: vai sempre em frente pelo
primeiro caminho ainda não visitado e, quando não há mais para onde ir,
VOLTA (backtracking) e tenta o próximo. Quem guarda "para onde voltar" é
uma PILHA (Aula 2) — na versão recursiva, a própria pilha de chamadas.

Mesmo grafo e mesma ordem de vizinhos do livro de Ascencio & Araújo
(p. 378 e 391). Custo: O(V + E), como a BFS.

Só usa a biblioteca padrão — cole direto no onlineide.pro/playground/python
"""

N = 6
ADJ = [[],
       [6, 2],
       [5, 3, 1, 6],
       [6, 5, 4, 2],
       [5, 3],
       [6, 4, 3, 2],
       [5, 3, 2, 1]]

ORIGEM = 1


# ------------------------------------------------------------------
# Versão "limpa", idêntica à do slide (recursiva).
# ------------------------------------------------------------------
def dfs(adj, u, marcado, ordem):
    marcado[u] = True
    ordem.append(u)                     # visita u
    for v in adj[u]:
        if not marcado[v]:
            dfs(adj, v, marcado, ordem) # mergulha em v; ao voltar, segue o laço


# A mesma DFS, com recuo mostrando a profundidade da recursão.
def dfs_passo_a_passo(adj, u, marcado, ordem, nivel=0):
    marcado[u] = True
    ordem.append(u)
    print("   " + "  " * nivel + f"visita {u}")
    for v in adj[u]:
        if not marcado[v]:
            dfs_passo_a_passo(adj, v, marcado, ordem, nivel + 1)
    print("   " + "  " * nivel + f"volta de {u}")


# Versão com PILHA explícita, sem recursão.
def dfs_pilha(adj, n, s):
    marcado = [False] * (n + 1)
    ordem = []
    pilha = [s]
    while pilha:
        u = pilha.pop()                 # tira do TOPO
        if marcado[u]:
            continue                    # já visitado por outro caminho
        marcado[u] = True
        ordem.append(u)
        for v in reversed(adj[u]):      # invertido: o 1o vizinho fica no topo
            if not marcado[v]:
                pilha.append(v)
    return ordem


def main():
    print(f"1) DFS recursiva a partir de {ORIGEM} (o recuo mostra a profundidade)")
    marcado = [False] * (N + 1)
    ordem = []
    dfs_passo_a_passo(ADJ, ORIGEM, marcado, ordem)
    print("   ordem de visita:", " ".join(str(v) for v in ordem))

    marcado2, ordem2 = [False] * (N + 1), []
    dfs(ADJ, ORIGEM, marcado2, ordem2)
    assert ordem2 == ordem              # confere com a versão limpa

    print("\n2) DFS com pilha explicita (sem recursao)")
    ordem3 = dfs_pilha(ADJ, N, ORIGEM)
    print("   ordem de visita:", " ".join(str(v) for v in ordem3))
    print("   mesma ordem da recursiva?", "sim" if ordem3 == ordem else "nao")

    print("\n3) Comparando com a BFS (P1) a partir do mesmo vertice")
    print("   BFS (fila):  1 6 2 5 3 4   -> anda em ondas, por distancia")
    print("   DFS (pilha):", " ".join(str(v) for v in ordem),
          "  -> vai fundo primeiro, depois volta")


if __name__ == "__main__":
    main()
