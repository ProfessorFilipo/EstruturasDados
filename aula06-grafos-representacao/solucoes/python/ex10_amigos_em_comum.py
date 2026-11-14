"""
ex10_amigos_em_comum.py — Solução do Exercício 10 (Aula 6)

Rede de amizades (grafo não dirigido) em lista de adjacências.
  - amigos_em_comum(u, v): vértices que estão na lista de u E na de v
  - sugerir_amizade(u): entre quem NÃO é amigo de u (e não é o próprio u),
    quem tem MAIS amigos em comum com u. Empate: o de menor número.

Para testar "é amigo?" em O(1), montamos também a matriz de adjacências:
cada representação faz o que faz melhor.
"""

NOMES = ["", "Ana", "Bruno", "Carla", "Davi", "Elisa", "Fabio", "Gabi", "Hugo"]
N = 8
AMIZADES = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 5), (3, 5), (3, 6),
            (4, 5), (4, 6), (5, 7), (6, 7), (7, 8)]


def montar(n, arestas):
    adj = [[] for _ in range(n + 1)]
    m = [[0] * (n + 1) for _ in range(n + 1)]
    for (u, v) in arestas:
        adj[u].append(v)
        adj[v].append(u)
        m[u][v] = m[v][u] = 1
    return adj, m


def amigos_em_comum(adj, m, u, v):
    comuns = []
    for x in adj[u]:                    # percorre os amigos de u...
        if m[x][v] == 1:                # ...e testa na matriz se x é amigo de v: O(1)
            comuns.append(x)
    return comuns


def sugerir_amizade(adj, m, n, u):
    melhor, melhor_qtd = 0, -1
    for v in range(1, n + 1):
        if v == u or m[u][v] == 1:
            continue                    # é o próprio u ou já é amigo
        qtd = len(amigos_em_comum(adj, m, u, v))
        if qtd > melhor_qtd:
            melhor, melhor_qtd = v, qtd
    return melhor, melhor_qtd


def nomes(lista):
    return ", ".join(NOMES[x] for x in lista) if lista else "(ninguem)"


def main():
    adj, m = montar(N, AMIZADES)
    print("1) Amigos em comum")
    for (u, v) in [(1, 5), (2, 4), (1, 8)]:
        print(f"   {NOMES[u]} e {NOMES[v]}: {nomes(amigos_em_comum(adj, m, u, v))}")

    print("\n2) Sugestao de amizade (quem tem mais amigos em comum)")
    for u in range(1, N + 1):
        v, qtd = sugerir_amizade(adj, m, N, u)
        print(f"   para {NOMES[u]:<6}-> {NOMES[v]:<6} ({qtd} em comum)")


if __name__ == "__main__":
    main()
