"""
p3_componentes.py

Estruturas de Dados — Aula 7 — Prática P3 (Componentes conexas)
Slide 16 (teoria) e 33 (prática)

Dia de tempestade na filial: os cabos 3-4 e 4-5 romperam e chegaram três
roteadores novos (7, 8 e 9) — só o 7 e o 8 já foram ligados entre si.
Quantas "ilhas" (componentes conexas) a rede tem agora? Quem conversa
com quem?

Ideia: percorra os vértices; sempre que encontrar um ainda NÃO marcado,
ele começa uma ilha nova — rode uma DFS a partir dele para marcar a ilha
inteira. Número de ilhas = número de vezes que a DFS foi disparada.

Custo: cada vértice e cada aresta são vistos uma vez -> O(V + E).

Só usa a biblioteca padrão — cole direto no onlineide.pro/playground/python
"""

N = 9
ARESTAS = [(1, 2), (1, 6), (2, 3), (2, 5), (2, 6),
           (3, 5), (3, 6), (5, 6),          # 3-4 e 4-5 romperam
           (7, 8)]                          # roteadores novos


def criar_lista(n, arestas):
    adj = [[] for _ in range(n + 1)]
    for (u, v) in arestas:
        adj[u].append(v)
        adj[v].append(u)
    return adj


def dfs(adj, u, marcado, ilha):
    marcado[u] = True
    ilha.append(u)
    for v in adj[u]:
        if not marcado[v]:
            dfs(adj, v, marcado, ilha)


# ------------------------------------------------------------------
# Versão "limpa", idêntica à do slide.
# ------------------------------------------------------------------
def componentes(adj, n):
    marcado = [False] * (n + 1)
    ilhas = []
    for v in range(1, n + 1):
        if not marcado[v]:              # v começa uma ilha nova
            ilha = []
            dfs(adj, v, marcado, ilha)  # marca a ilha inteira
            ilhas.append(sorted(ilha))
    return ilhas


def main():
    adj = criar_lista(N, ARESTAS)
    print(f"1) Rede depois da tempestade: {N} roteadores, {len(ARESTAS)} cabos")
    for v in range(1, N + 1):
        print(f"   {v}: {adj[v] if adj[v] else '(isolado)'}")

    ilhas = componentes(adj, N)
    print(f"\n2) Componentes conexas encontradas: {len(ilhas)}")
    for i, ilha in enumerate(ilhas, start=1):
        print(f"   ilha {i}: {ilha}")

    print("\n3) Perguntas rapidas")
    ilha_de = [0] * (N + 1)
    for i, ilha in enumerate(ilhas, start=1):
        for v in ilha:
            ilha_de[v] = i
    for (a, b) in [(1, 5), (1, 4), (7, 8), (8, 9)]:
        resp = "sim" if ilha_de[a] == ilha_de[b] else "nao"
        print(f"   {a} alcanca {b}? {resp}")
    print(f"   cabos minimos para reconectar tudo: {len(ilhas) - 1}"
          " (um cabo liga duas ilhas)")


if __name__ == "__main__":
    main()
