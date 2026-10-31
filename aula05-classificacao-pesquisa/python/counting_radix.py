"""
counting_radix.py

Estruturas de Dados — Aula 5 — Bloco 7 (Ordenação sem comparação)
Slides 29 a 31

O limite Omega(n log n) vale para quem COMPARA elementos. Se as chaves
são inteiros numa faixa pequena (páginas de 1 a k), dá para ordenar sem
comparar nada:

1) COUNTING SORT
   a) CONTAR quantos trabalhos têm 1, 2, ..., k páginas (um histograma);
   b) ACUMULAR: onde começa o bloco de cada número de páginas;
   c) POSICIONAR cada trabalho no seu bloco, na ordem de chegada.
   Custo: Theta(n + k). Estável. Memória extra: O(n + k).

2) RADIX SORT: ordena IDs dígito a dígito (unidade, dezena, centena),
   com um counting sort estável (k = 10) em cada passada.
   Custo: Theta(d * (n + 10)) para d dígitos.

Só usa a biblioteca padrão — cole direto no onlineide.pro/playground/python
"""
import random


def fmt(x):
    """Formata inteiros no padrão brasileiro: 1234567 -> 1.234.567"""
    return f"{x:,}".replace(",", ".")


def counting_sort(trabalhos, chave, k, mostrar=False):
    """Ordena trabalhos pela função chave(t), que devolve um inteiro de 0 a k.
    Devolve (nova lista, operações simples). Não compara trabalhos entre si."""
    ops = 0
    contagem = [0] * (k + 1)
    for t in trabalhos:                      # a) contar
        contagem[chave(t)] += 1
        ops += 1
    inicio = [0] * (k + 1)
    for p in range(1, k + 1):                # b) acumular
        inicio[p] = inicio[p - 1] + contagem[p - 1]
        ops += 1
    saida = [None] * len(trabalhos)
    for t in trabalhos:                      # c) posicionar (ordem de chegada)
        saida[inicio[chave(t)]] = t
        inicio[chave(t)] += 1
        ops += 1
    if mostrar:
        print(f"   {'contagem (1..k):':<19}{contagem[1:]}")
        acumulado = [0] * (k + 1)
        for p in range(1, k + 1):
            acumulado[p] = acumulado[p - 1] + contagem[p - 1]
        print(f"   {'bloco comeca em:':<19}{acumulado[1:]}")
    return saida, ops


def merge_comparacoes(v):
    """Comparações do Merge Sort (para a corrida)."""
    if len(v) <= 1:
        return v, 0
    meio = len(v) // 2
    esq, c1 = merge_comparacoes(v[:meio])
    dir, c2 = merge_comparacoes(v[meio:])
    junto, i, j, comp = [], 0, 0, c1 + c2
    while i < len(esq) and j < len(dir):
        comp += 1
        if esq[i] <= dir[j]:
            junto.append(esq[i])
            i += 1
        else:
            junto.append(dir[j])
            j += 1
    return junto + esq[i:] + dir[j:], comp


def radix_sort(ids, digitos, mostrar=False):
    """Ordena inteiros não negativos com 'digitos' dígitos."""
    divisor = 1
    nomes = ["unidade", "dezena", "centena", "milhar"]
    for d in range(digitos):
        ids, _ = counting_sort(ids, lambda x: (x // divisor) % 10, 9)
        if mostrar:
            print(f"   por {nomes[d]:<8} {ids}")
        divisor *= 10
    return ids


def main():
    print("1) COUNTING SORT: 12 trabalhos com 1 a 6 paginas")
    paginas = [3, 1, 4, 1, 5, 2, 6, 5, 3, 5, 1, 2]
    trabalhos = [(101 + i, p) for i, p in enumerate(paginas)]
    print(f"   {'paginas:':<19}{paginas}")
    ordenados, _ = counting_sort(trabalhos, lambda t: t[1], 6, mostrar=True)
    print(f"   {'ordenado:':<19}{[t[1] for t in ordenados]}")
    print(f"   {'IDs com 1 pagina:':<19}{[t[0] for t in ordenados if t[1] == 1]}"
          "  (ordem de chegada: estavel)")

    gerador = random.Random(2026)
    n, k = 100_000, 30
    print(f"\n2) CORRIDA: n = {fmt(n)} trabalhos com 1 a {fmt(k)} paginas")
    pags = [gerador.randint(1, k) for _ in range(n)]
    _, ops = counting_sort(pags, lambda p: p, k)
    _, comp = merge_comparacoes(pags)
    print(f"   counting sort: {fmt(ops):>9} operacoes simples (2n + k)")
    print(f"   merge sort:    {fmt(comp):>9} comparacoes (~n log2 n)")

    print("\n3) RADIX SORT: IDs de 3 digitos, um digito por passada")
    ids = [512, 137, 905, 254, 731, 618, 220]
    print(f"   {'entrada':<12} {ids}")
    radix_sort(ids, 3, mostrar=True)


if __name__ == "__main__":
    main()
