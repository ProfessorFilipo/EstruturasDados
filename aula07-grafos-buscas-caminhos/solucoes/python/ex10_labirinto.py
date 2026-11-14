"""
ex10_labirinto.py — Solução do Exercício 10 (Aula 7)

O labirinto é um grafo IMPLÍCITO: cada casa livre é um vértice e há
aresta entre casas vizinhas (cima, baixo, esquerda, direita). Não é
preciso montar lista nem matriz de adjacências — os vizinhos são
calculados na hora.

A BFS a partir da entrada E dá o MENOR número de passos até a saída S, e
pai[] permite desenhar o caminho com '*'.
Cada casa (linha, coluna) vira o número linha * COLUNAS + coluna.
"""
from collections import deque

LAB = ["##########",
       "#E.....#.#",
       "#.##.###.#",
       "#.#..#...#",
       "#.#.####.#",
       "#...#..#.#",
       "###.#.##.#",
       "#.....#..#",
       "#.###...S#",
       "##########"]
LINHAS, COLUNAS = len(LAB), len(LAB[0])
MOVIMENTOS = [(-1, 0), (1, 0), (0, -1), (0, 1)]     # cima, baixo, esquerda, direita


def acha(letra):
    for i in range(LINHAS):
        for j in range(COLUNAS):
            if LAB[i][j] == letra:
                return i * COLUNAS + j
    return -1


def bfs_labirinto(inicio):
    dist = [-1] * (LINHAS * COLUNAS)
    pai = [-1] * (LINHAS * COLUNAS)
    dist[inicio] = 0
    fila = deque([inicio])
    while fila:
        u = fila.popleft()
        i, j = divmod(u, COLUNAS)
        for (di, dj) in MOVIMENTOS:     # os vizinhos são calculados na hora
            ni, nj = i + di, j + dj
            v = ni * COLUNAS + nj
            if LAB[ni][nj] != "#" and dist[v] == -1:
                dist[v] = dist[u] + 1
                pai[v] = u
                fila.append(v)
    return dist, pai


def main():
    e, s = acha("E"), acha("S")
    dist, pai = bfs_labirinto(e)
    if dist[s] == -1:
        print("Nao ha caminho da entrada ate a saida.")
        return
    print(f"Menor caminho de E ate S: {dist[s]} passos")
    print(f"Casas alcancaveis a partir de E: {sum(1 for d in dist if d != -1)}\n")
    grade = [list(linha) for linha in LAB]
    u = pai[s]
    while u != e:                       # marca o caminho, de trás para frente
        i, j = divmod(u, COLUNAS)
        grade[i][j] = "*"
        u = pai[u]
    for linha in grade:
        print("   " + "".join(linha))


if __name__ == "__main__":
    main()
