"""
p2_graus.py

Estruturas de Dados — Aula 6 — Prática P2 (Grau dos vértices)
Slides 13 e 14 (teoria) e 29 (prática)

Na matriz de adjacências:
  - grafo NÃO dirigido: grau(v) = soma da linha v
  - dígrafo: grau de SAÍDA(v)   = soma da linha v   (setas que saem de v)
             grau de ENTRADA(v) = soma da coluna v  (setas que chegam em v)

Lema do aperto de mãos: num grafo não dirigido, a soma dos graus é 2 x |E|,
porque cada aresta tem duas pontas.

Só usa a biblioteca padrão — cole direto no onlineide.pro/playground/python
"""

N = 6
ARESTAS = [(1, 2), (1, 6), (2, 3), (2, 5), (2, 6),
           (3, 4), (3, 5), (3, 6), (4, 5), (5, 6)]


def criar_matriz(n, arestas, dirigido):
    m = [[0] * (n + 1) for _ in range(n + 1)]
    for (u, v) in arestas:
        m[u][v] = 1
        if not dirigido:
            m[v][u] = 1
    return m


# ------------------------------------------------------------------
# Versões "limpas", idênticas às do slide.
# ------------------------------------------------------------------
def grau(m, n, v):                      # soma da linha v
    return sum(m[v][j] for j in range(1, n + 1))


def grau_saida(m, n, v):                # soma da linha v
    return sum(m[v][j] for j in range(1, n + 1))


def grau_entrada(m, n, v):              # soma da coluna v
    return sum(m[i][v] for i in range(1, n + 1))


def main():
    # ---------------- Parte 1: grafo não dirigido ----------------
    m = criar_matriz(N, ARESTAS, dirigido=False)
    print("1) Rede da filial (NAO DIRIGIDO): grau de cada roteador")
    soma = 0
    maior = 0
    for v in range(1, N + 1):
        g = grau(m, N, v)
        soma += g
        maior = max(maior, g)
        print(f"   grau({v}) = {g}  " + "#" * g)
    print(f"   soma dos graus = {soma}   2 x |E| = 2 x {len(ARESTAS)} = {2 * len(ARESTAS)}")
    print("   aperto de maos confere?", "sim" if soma == 2 * len(ARESTAS) else "NAO")
    mais_ligados = [v for v in range(1, N + 1) if grau(m, N, v) == maior]
    print(f"   roteadores mais conectados (grau {maior}): {mais_ligados}")

    # ---------------- Parte 2: o mesmo desenho como dígrafo ----------------
    d = criar_matriz(N, ARESTAS, dirigido=True)
    print("\n2) Mesmas arestas como DIGRAFO (cada par (u, v) vira u -> v)")
    print("   vertice  saida  entrada")
    soma_saida = soma_entrada = 0
    fontes, sumidouros = [], []
    for v in range(1, N + 1):
        gs, ge = grau_saida(d, N, v), grau_entrada(d, N, v)
        soma_saida += gs
        soma_entrada += ge
        if ge == 0:
            fontes.append(v)            # ninguém aponta para v
        if gs == 0:
            sumidouros.append(v)        # v não aponta para ninguém
        print(f"   {v:>7}  {gs:>5}  {ge:>7}")
    print(f"   soma das saidas = {soma_saida}, soma das entradas = {soma_entrada}"
          f", |E| = {len(ARESTAS)}")
    print(f"   fontes (entrada 0): {fontes}    sumidouros (saida 0): {sumidouros}")


if __name__ == "__main__":
    main()
