"""
p3_lista_adjacencias.py

Estruturas de Dados — Aula 6 — Prática P3 (Lista de adjacências)
Slides 22 (teoria) e 30 (prática)

Lista de adjacências: um vetor com uma posição por vértice; em cada
posição, a lista dos vizinhos daquele vértice.

    1: 2 -> 6
    2: 1 -> 3 -> 5 -> 6
    ...

Em Python, cada lista de vizinhos é uma list comum. Na versão em C
(c/p3_lista_adjacencias.c) cada uma é uma LISTA ENCADEADA, como na Aula 1 e
no livro de Ascencio & Araújo (p. 377).

Espaço: n posições no vetor + 2 x |E| vizinhos guardados -> O(V + E).

Só usa a biblioteca padrão — cole direto no onlineide.pro/playground/python
"""

N = 6
ARESTAS = [(1, 2), (1, 6), (2, 3), (2, 5), (2, 6),
           (3, 4), (3, 5), (3, 6), (4, 5), (5, 6)]

DIRIGIDO = False


# ------------------------------------------------------------------
# Versão "limpa", idêntica à do slide.
# ------------------------------------------------------------------
def criar_lista(n, arestas, dirigido):
    adj = [[] for _ in range(n + 1)]    # posição 0 sem uso, como no livro
    for (u, v) in arestas:
        adj[u].append(v)
        if not dirigido:
            adj[v].append(u)            # não dirigido: v também vê u
    return adj


def imprimir_lista(adj, n):
    for v in range(1, n + 1):
        vizinhos = " -> ".join(str(x) for x in adj[v])
        print(f"   {v}: {vizinhos if vizinhos else '(sem vizinhos)'}")


def main():
    tipo = "DIRIGIDO" if DIRIGIDO else "NAO DIRIGIDO"
    print(f"1) Lista de adjacencias da rede da filial ({tipo})")
    adj = criar_lista(N, ARESTAS, DIRIGIDO)
    imprimir_lista(adj, N)

    print("\n2) O grau sai de graca: e o tamanho de cada lista")
    for v in range(1, N + 1):
        print(f"   grau({v}) = len(adj[{v}]) = {len(adj[v])}")

    guardados = sum(len(adj[v]) for v in range(1, N + 1))
    esperado = len(ARESTAS) if DIRIGIDO else 2 * len(ARESTAS)
    print(f"\n3) Vizinhos guardados no total: {guardados} (esperado: {esperado})")
    print(f"   Celulas usadas: {N} (vetor) + {guardados} (vizinhos) = {N + guardados}"
          f"   x   matriz: {N * N}")


if __name__ == "__main__":
    main()
