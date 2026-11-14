"""
ex08_grafo_transposto.py — Solução do Exercício 8 (Aula 6)

Numa rede social, "u segue v" é a seta u -> v. A lista de adjacências
responde "quem EU sigo". Para saber "quem ME segue", invertemos todas as
setas: é o grafo TRANSPOSTO. Na matriz, é a matriz transposta (troca linha
por coluna); na lista, cada seta u -> v vira v -> u.

O grau de SAÍDA no transposto é o grau de ENTRADA no original.
"""

N = 5
SEGUE = [(1, 2), (1, 3), (2, 3), (3, 1), (4, 3), (5, 4)]   # u segue v


def criar_lista(n, setas):
    adj = [[] for _ in range(n + 1)]
    for (u, v) in setas:
        adj[u].append(v)
    return adj


def transposto(adj, n):
    t = [[] for _ in range(n + 1)]
    for u in range(1, n + 1):
        for v in adj[u]:
            t[v].append(u)              # u -> v vira v -> u
    return t


def imprimir(adj, n, rotulo):
    for v in range(1, n + 1):
        print(f"   perfil {v} {rotulo}: {adj[v] if adj[v] else '(ninguem)'}")


def main():
    adj = criar_lista(N, SEGUE)
    print("1) Quem cada perfil SEGUE (grafo original)")
    imprimir(adj, N, "segue")

    t = transposto(adj, N)
    print("\n2) Quem SEGUE cada perfil (grafo transposto)")
    imprimir(t, N, "e seguido por")

    mais = max(range(1, N + 1), key=lambda v: len(t[v]))
    print(f"\n3) Perfil mais seguido: {mais} ({len(t[mais])} seguidores)")
    ninguem = [v for v in range(1, N + 1) if not t[v]]
    print(f"   Perfis sem nenhum seguidor: {ninguem}")
    print("   Transpor duas vezes volta ao original?",
          "sim" if transposto(t, N) == [sorted(x) for x in adj] else "nao")


if __name__ == "__main__":
    main()
