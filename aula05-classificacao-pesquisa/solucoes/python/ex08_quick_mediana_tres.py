"""
ex08_quick_mediana_tres.py — Aula 5, Exercício 8 (solução de referência)

Quicksort com a partição da aula, escolhendo o pivô de dois jeitos:
  - "ultimo": o último elemento (como no slide 23);
  - "mediana": a mediana de três entre v[inicio], v[meio] e v[fim], que é
    levada para o fim antes de particionar.

Com o vetor já ordenado (ou invertido), o último elemento é sempre o maior
(ou o menor) — o pior pivô possível. A mediana de três pega o elemento do
MEIO, que nesses casos é exatamente a mediana: a partição divide ao meio.

Só usa a biblioteca padrão — cole direto no onlineide.pro/playground/python
"""
import random

comparacoes = 0


def fmt(x):
    return f"{x:,}".replace(",", ".")


def indice_mediana_de_tres(v, inicio, fim):
    meio = (inicio + fim) // 2
    a, b, c = v[inicio], v[meio], v[fim]
    if a <= b <= c or c <= b <= a:
        return meio
    if b <= a <= c or c <= a <= b:
        return inicio
    return fim


def particionar(v, inicio, fim, estrategia):
    global comparacoes
    if estrategia == "mediana":
        k = indice_mediana_de_tres(v, inicio, fim)
        v[k], v[fim] = v[fim], v[k]          # leva o pivô escolhido para o fim
    pivo, i = v[fim], inicio
    for j in range(inicio, fim):
        comparacoes += 1
        if v[j] < pivo:
            v[i], v[j] = v[j], v[i]
            i += 1
    v[i], v[fim] = v[fim], v[i]
    return i


def quick_sort(v, inicio, fim, estrategia):
    if inicio < fim:
        p = particionar(v, inicio, fim, estrategia)
        quick_sort(v, inicio, p - 1, estrategia)
        quick_sort(v, p + 1, fim, estrategia)


def contar(dados, estrategia):
    global comparacoes
    comparacoes = 0
    v = list(dados)
    quick_sort(v, 0, len(v) - 1, estrategia)
    assert v == sorted(dados)
    return comparacoes


def main():
    gerador = random.Random(2026)
    n = 500
    aleatorio = [gerador.randint(1, 1_000_000) for _ in range(n)]
    cenarios = [("aleatorio", aleatorio), ("ja ordenado", sorted(aleatorio)),
                ("ordem inversa", sorted(aleatorio, reverse=True))]
    print(f"Comparacoes do Quicksort com n = {n}")
    print(f"   {'cenario':<14} {'pivo = ultimo':>14} {'mediana de tres':>16}")
    for nome, dados in cenarios:
        print(f"   {nome:<14} {fmt(contar(dados, 'ultimo')):>14} {fmt(contar(dados, 'mediana')):>16}")


if __name__ == "__main__":
    main()
