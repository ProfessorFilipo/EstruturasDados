"""
p4_comparando_representacoes.py

Estruturas de Dados — Aula 6 — Prática P4 (Matriz x Lista)
Slides 23 (teoria) e 31 (prática)

Três perguntas para decidir entre matriz e lista de adjacências:
  1. "u e v são vizinhos?"   matriz: O(1)       lista: O(grau(u))
  2. "quem são os vizinhos?" matriz: O(V)       lista: O(grau(u))
  3. "quanta memória?"       matriz: V x V      lista: V + 2 x E

E duas conversões, para provar que as duas guardam o MESMO grafo.

Só usa a biblioteca padrão — cole direto no onlineide.pro/playground/python
"""

N = 6
ARESTAS = [(1, 2), (1, 6), (2, 3), (2, 5), (2, 6),
           (3, 4), (3, 5), (3, 6), (4, 5), (5, 6)]


def fmt(x):
    """Formata inteiros no padrão brasileiro: 1234567 -> 1.234.567"""
    return f"{x:,}".replace(",", ".")


def criar_matriz(n, arestas):
    m = [[0] * (n + 1) for _ in range(n + 1)]
    for (u, v) in arestas:
        m[u][v] = m[v][u] = 1
    return m


def criar_lista(n, arestas):
    adj = [[] for _ in range(n + 1)]
    for (u, v) in arestas:
        adj[u].append(v)
        adj[v].append(u)
    return adj


# ------------------------------------------------------------------
# Versões "limpas", idênticas às do slide.
# ------------------------------------------------------------------
def vizinhos_matriz(m, n, u, v):
    return m[u][v] == 1                 # um acesso direto: O(1)


def vizinhos_lista(adj, u, v):
    for x in adj[u]:                    # percorre a lista de u: O(grau(u))
        if x == v:
            return True
    return False


def matriz_para_lista(m, n):
    adj = [[] for _ in range(n + 1)]
    for u in range(1, n + 1):
        for v in range(1, n + 1):       # varre a linha inteira: O(V) por vértice
            if m[u][v] == 1:
                adj[u].append(v)
    return adj


def lista_para_matriz(adj, n):
    m = [[0] * (n + 1) for _ in range(n + 1)]
    for u in range(1, n + 1):
        for v in adj[u]:
            m[u][v] = 1
    return m


# Versão da busca na lista que conta os passos (para a demonstração).
def vizinhos_lista_contando(adj, u, v):
    passos = 0
    for x in adj[u]:
        passos += 1
        if x == v:
            return True, passos
    return False, passos


def main():
    m = criar_matriz(N, ARESTAS)
    adj = criar_lista(N, ARESTAS)

    print("1) 'u e v sao vizinhos?' nas duas representacoes")
    for (u, v) in [(2, 6), (1, 4), (4, 5)]:
        r_m = vizinhos_matriz(m, N, u, v)
        r_l, passos = vizinhos_lista_contando(adj, u, v)
        assert r_m == r_l == vizinhos_lista(adj, u, v)
        print(f"   ({u},{v}): {'sim' if r_m else 'nao'}"
              f"   matriz: 1 acesso   lista: {passos} passo(s)")

    print("\n2) Convertendo uma na outra")
    adj2 = matriz_para_lista(m, N)
    m2 = lista_para_matriz(adj, N)
    for v in range(1, N + 1):
        print(f"   {v}: {adj2[v]}")
    print("   matriz -> lista -> matriz volta igual?",
          "sim" if lista_para_matriz(adj2, N) == m else "nao")
    print("   lista -> matriz confere com a original?", "sim" if m2 == m else "nao")

    print("\n3) Memoria (celulas) em tres cenarios")
    cenarios = [
        ("rede da filial", 6, 10),
        ("campus (1 cabo por PC)", 1_000, 1_500),
        ("rede social (50 amigos)", 1_000_000, 25_000_000),
    ]
    print(f"   {'cenario':<26}{'matriz V x V':>20}{'lista V + 2E':>16}")
    for nome, v, e in cenarios:
        print(f"   {nome:<26}{fmt(v * v):>20}{fmt(v + 2 * e):>16}")
    print("   -> grafo ESPARSO (poucas arestas): lista. Grafo DENSO: matriz.")


if __name__ == "__main__":
    main()
