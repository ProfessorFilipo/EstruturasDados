"""
ex08_dois_times.py — Solução do Exercício 8 (Aula 7)

Dividir a turma em dois times de modo que nenhum par de RIVAIS fique no
mesmo time = descobrir se o grafo de rivalidades é BIPARTIDO.

BFS "pintando" os vértices: a origem recebe o time 0, cada vizinho
recebe o time oposto ao de quem o descobriu. Se algum dia dois vizinhos
estiverem no MESMO time, é impossível (há um ciclo de tamanho ímpar,
como um triângulo de rivais).
"""
from collections import deque


def criar_lista(n, arestas):
    adj = [[] for _ in range(n + 1)]
    for (u, v) in arestas:
        adj[u].append(v)
        adj[v].append(u)
    return adj


def dividir(adj, n):
    """Devolve (time, None) se der certo, ou (None, (u, v)) com o conflito."""
    time = [-1] * (n + 1)               # -1 = ainda sem time
    for s in range(1, n + 1):           # cada componente começa do zero
        if time[s] != -1:
            continue
        time[s] = 0
        fila = deque([s])
        while fila:
            u = fila.popleft()
            for v in adj[u]:
                if time[v] == -1:
                    time[v] = 1 - time[u]   # time oposto
                    fila.append(v)
                elif time[v] == time[u]:
                    return None, (u, v)     # rivais no mesmo time
    return time, None


def testar(nome, n, rivalidades):
    time, conflito = dividir(criar_lista(n, rivalidades), n)
    print(nome)
    if conflito:
        print(f"   impossivel: os rivais {conflito[0]} e {conflito[1]} cairiam no mesmo time")
    else:
        print("   time A:", [v for v in range(1, n + 1) if time[v] == 0])
        print("   time B:", [v for v in range(1, n + 1) if time[v] == 1])


def main():
    rivais = [(1, 2), (1, 4), (2, 3), (3, 6), (4, 5), (5, 6)]
    testar("1) turma com 6 alunos", 6, rivais)
    testar("2) mesma turma + rivalidade 1-3", 6, rivais + [(1, 3)])
    testar("3) turma com 7 alunos, 7 isolado", 7, rivais)


if __name__ == "__main__":
    main()
