"""
limite_inferior.py

Estruturas de Dados — Aula 5 — Bloco 6 (Limite inferior)
Slides 27 e 28

Todo algoritmo que ordena COMPARANDO elementos está jogando o jogo de
"adivinhar o número" da Aula 4: entre as n! ordens possíveis (Aula 4:
3 trabalhos chegam à fila de 3! = 6 formas), ele precisa descobrir qual
é a certa, e cada comparação é uma pergunta de sim/não.

Com k perguntas de sim/não dá para separar no máximo 2^k respostas.
Para separar n! ordens:  2^k >= n!   ->   k >= log2(n!)  ~  n log2 n
Logo, NENHUMA ordenação por comparação vence Omega(n log n) no pior caso.

Este programa:
  1) testa TODAS as ordens de 3 e 4 elementos e mostra o maior número
     de comparações do Insertion Sort e do Merge Sort;
  2) compara log2(n!) com n log2 n e com o Merge Sort medido.

Só usa a biblioteca padrão — cole direto no onlineide.pro/playground/python
"""
import itertools
import math
import random


def fmt(x):
    """Formata inteiros no padrão brasileiro: 1234567 -> 1.234.567"""
    return f"{x:,}".replace(",", ".")


def insertion_comparacoes(v):
    v = list(v)
    comp = 0
    for i in range(1, len(v)):
        chave, j = v[i], i - 1
        while j >= 0:
            comp += 1
            if not (v[j] > chave):
                break
            v[j + 1] = v[j]
            j -= 1
        v[j + 1] = chave
    return comp


def merge_comparacoes(v):
    """Devolve (lista ordenada, comparações) do Merge Sort."""
    if len(v) <= 1:
        return list(v), 0
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


def log2_fatorial(n):
    """log2(n!) = log2(1) + log2(2) + ... + log2(n), sem calcular n!."""
    return sum(math.log2(k) for k in range(2, n + 1))


def main():
    print("1) FORCA BRUTA: pior caso entre todas as ordens possiveis")
    print("   (limite = log2(n!) arredondado para cima)")
    for n in (3, 4):
        ordens = list(itertools.permutations(range(101, 101 + n)))   # trabalhos 101, 102, ...
        pior_ins = max(insertion_comparacoes(o) for o in ordens)
        pior_mer = max(merge_comparacoes(list(o))[1] for o in ordens)
        limite = math.ceil(log2_fatorial(n))
        print(f"   n={n}: {len(ordens):>2} ordens | limite = {limite}"
              f" | insertion = {pior_ins} | merge = {pior_mer}")

    print("\n2) O LIMITE log2(n!) CRESCE COMO n log2 n")
    gerador = random.Random(2026)
    print(f"{'n':>7} {'log2(n!)':>10} {'n*log2(n)':>10} {'merge':>8}")
    for n in (10, 100, 1000, 10000):
        v = list(range(n))
        gerador.shuffle(v)
        _, medido = merge_comparacoes(v)
        print(f"{fmt(n):>7} {fmt(math.ceil(log2_fatorial(n))):>10}"
              f" {fmt(round(n * math.log2(n))):>10} {fmt(medido):>8}")
    print("\nMerge Sort fica colado no limite: e assintoticamente otimo.")


if __name__ == "__main__":
    main()
