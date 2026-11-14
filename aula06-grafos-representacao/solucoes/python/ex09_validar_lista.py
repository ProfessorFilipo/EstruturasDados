"""
ex09_validar_lista.py — Solução do Exercício 9 (Aula 6)

Numa lista de adjacências de um grafo NÃO dirigido, se v está na lista de
u, então u TEM de estar na lista de v. Uma lista "torta" é um erro comum
quando se monta a estrutura à mão (ou quando o código esquece a segunda
inserção). A função devolve todos os pares quebrados.
"""


def esta_na_lista(lista, x):
    for y in lista:
        if y == x:
            return True
    return False


def validar(adj, n):
    quebrados = []
    for u in range(1, n + 1):
        for v in adj[u]:
            if not esta_na_lista(adj[v], u):
                quebrados.append((u, v))    # u vê v, mas v não vê u
    return quebrados


def relatorio(nome, adj, n):
    q = validar(adj, n)
    if not q:
        print(f"{nome}: lista consistente")
    else:
        for (u, v) in q:
            print(f"{nome}: {v} esta na lista de {u}, mas {u} NAO esta na lista de {v}")


def main():
    filial = [[], [2, 6], [1, 3, 5, 6], [2, 4, 5, 6], [3, 5], [2, 3, 4, 6], [1, 2, 3, 5]]
    relatorio("1) rede da filial", filial, 6)

    torta = [[], [2, 4], [1, 3], [2], [1, 3]]
    relatorio("2) lista do enunciado", torta, 4)

    esqueceu = [[], [2, 3], [], [1]]        # o código esqueceu adj[v].append(u) em 1-2
    relatorio("3) segunda insercao esquecida", esqueceu, 3)


if __name__ == "__main__":
    main()
