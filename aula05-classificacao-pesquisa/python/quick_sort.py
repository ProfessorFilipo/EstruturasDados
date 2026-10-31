"""
quick_sort.py

Estruturas de Dados — Aula 5 — Bloco 5 (Quicksort)
Slides 21 a 26

1) PARTIÇÃO (esquema de Lomuto): o último elemento é o PIVÔ. Quem é
   menor que ele vai para a esquerda; no fim, o pivô é trocado para a
   posição entre os dois grupos — que já é a sua posição FINAL.
   É como separar dois conjuntos (Aula 3): {x < p} e {x >= p}.

2) QUICKSORT: particiona e repete, recursivamente, nos dois lados.
   Não precisa intercalar e ordena no próprio vetor (sem vetor extra).
   Não é estável.

3) CASOS:
   caso médio .... ~1,39 n log2 n comparações -> Theta(n log n)
   pior caso ..... pivô sempre o maior/menor  -> n(n-1)/2 -> Theta(n^2)
                   (vetor JÁ ORDENADO com pivô = último elemento!)
   correção ...... pivô aleatório: o pior caso fica improvável.

Atenção: no pior caso a recursão empilha n chamadas, e o Python limita a
pilha de chamadas a ~1.000. Por isso usamos n = 500 na parte 3.

Só usa a biblioteca padrão — cole direto no onlineide.pro/playground/python
"""
import random

comparacoes = 0                 # contador global de comparações
gerador = random.Random(2026)   # semente fixa: mesma saída para todos


def fmt(x):
    """Formata inteiros no padrão brasileiro: 1234567 -> 1.234.567"""
    return f"{x:,}".replace(",", ".")


# ------------------------------------------------------------------
# Versões "limpas", idênticas às do slide 23 — para referência.
# ------------------------------------------------------------------
def particionar(v, inicio, fim):
    pivo = v[fim]                  # o último é o pivô
    i = inicio                     # vaga dos menores
    for j in range(inicio, fim):
        if v[j] < pivo:
            v[i], v[j] = v[j], v[i]
            i += 1
    v[i], v[fim] = v[fim], v[i]    # pivô no lugar
    return i


def quick_sort(v, inicio, fim):
    if inicio < fim:
        p = particionar(v, inicio, fim)
        quick_sort(v, inicio, p - 1)
        quick_sort(v, p + 1, fim)


# ------------------------------------------------------------------
# A mesma lógica, contando comparações, mostrando a partição e com a
# opção de sortear o pivô.
# ------------------------------------------------------------------
def particionar_contando(v, inicio, fim, pivo_aleatorio=False, mostrar=False):
    """Particiona v[inicio..fim] e devolve a posição final do pivô."""
    global comparacoes
    if pivo_aleatorio:                       # sorteia o pivô e o leva para o fim
        k = gerador.randint(inicio, fim)
        v[k], v[fim] = v[fim], v[k]
    pivo = v[fim]
    i = inicio                               # próxima vaga do grupo "menores"
    for j in range(inicio, fim):
        comparacoes += 1
        x = v[j]
        if x < pivo:
            v[i], v[j] = v[j], v[i]          # manda x para o grupo dos menores
            i += 1
            if mostrar:
                print(f"   {x:>2} <  {pivo}  -> esquerda  {v}")
        elif mostrar:
            print(f"   {x:>2} >= {pivo}  -> fica      {v}")
    v[i], v[fim] = v[fim], v[i]              # pivô entre os dois grupos
    return i


def quick_sort_contando(v, inicio, fim, pivo_aleatorio=False):
    """Ordena v[inicio..fim] no lugar, contando as comparações."""
    if inicio < fim:                         # 0 ou 1 elemento: caso base
        p = particionar_contando(v, inicio, fim, pivo_aleatorio)
        quick_sort_contando(v, inicio, p - 1, pivo_aleatorio)   # lado dos menores
        quick_sort_contando(v, p + 1, fim, pivo_aleatorio)      # lado dos maiores


def contar(v, pivo_aleatorio=False):
    """Ordena uma cópia de v e devolve quantas comparações foram feitas."""
    global comparacoes
    comparacoes = 0
    copia = list(v)
    quick_sort_contando(copia, 0, len(copia) - 1, pivo_aleatorio)
    assert copia == sorted(v)                # confere o resultado
    return comparacoes


def main():
    print("1) PARTICAO PASSO A PASSO (pivo = ultimo elemento)")
    paginas = [12, 5, 8, 3, 20, 1, 9, 6]
    print(f"   inicio:               {paginas}")
    p = particionar_contando(paginas, 0, len(paginas) - 1, mostrar=True)
    print(f"   pivo {paginas[p]} -> posicao {p}:  {paginas}")

    print("\n2) QUICKSORT COMPLETO")
    paginas = [12, 5, 8, 3, 20, 1, 9, 6]
    quick_sort(paginas, 0, len(paginas) - 1)
    print("   resultado:", paginas)

    print("\n3) MELHOR E PIOR CASO (n = 500)")
    n = 500
    aleatorio = [gerador.randint(1, 1_000_000) for _ in range(n)]
    ordenado = sorted(aleatorio)
    print(f"   aleatorio, pivo = ultimo ...... {fmt(contar(aleatorio)):>7}")
    print(f"   ORDENADO,  pivo = ultimo ...... {fmt(contar(ordenado)):>7}")
    print(f"   ordenado,  pivo aleatorio ..... {fmt(contar(ordenado, True)):>7}")
    print(f"   n(n-1)/2 = {fmt(n * (n - 1) // 2)}")
    print("\nVetor ja ordenado + pivo no fim = pior caso Theta(n^2)")


if __name__ == "__main__":
    main()
