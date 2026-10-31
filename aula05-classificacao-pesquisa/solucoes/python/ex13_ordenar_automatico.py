"""
ex13_ordenar_automatico.py — Aula 5, Exercício 13 (solução de referência)

Um ordenador que escolhe o algoritmo sozinho, com as regras do exercício:
  1. até 32 elementos ................................ Insertion Sort
  2. faixa pequena: max - min <= 2 * len(v) ......... Counting Sort
  3. caso contrário .................................. Merge Sort

É a mesma ideia do Timsort do Python: usar o algoritmo certo para cada
situação (ele usa Insertion Sort em trechos pequenos e Merge Sort para
juntá-los).

Só usa a biblioteca padrão — cole direto no onlineide.pro/playground/python
"""
import random


def insertion_sort(v):
    v = list(v)
    for i in range(1, len(v)):
        chave, j = v[i], i - 1
        while j >= 0 and v[j] > chave:
            v[j + 1] = v[j]
            j -= 1
        v[j + 1] = chave
    return v


def counting_sort(v):
    menor = min(v)
    contagem = [0] * (max(v) - menor + 1)
    for x in v:
        contagem[x - menor] += 1            # desloca para começar em 0
    saida = []
    for deslocado, quantos in enumerate(contagem):
        saida.extend([deslocado + menor] * quantos)
    return saida


def merge_sort(v):
    if len(v) <= 1:
        return list(v)
    meio = len(v) // 2
    esq, dir = merge_sort(v[:meio]), merge_sort(v[meio:])
    resultado, i, j = [], 0, 0
    while i < len(esq) and j < len(dir):
        if esq[i] <= dir[j]:
            resultado.append(esq[i]); i += 1
        else:
            resultado.append(dir[j]); j += 1
    return resultado + esq[i:] + dir[j:]


def ordenar(v):
    """Devolve (lista ordenada, nome do algoritmo escolhido)."""
    if len(v) <= 32:
        return insertion_sort(v), "Insertion Sort"
    if max(v) - min(v) <= 2 * len(v):
        return counting_sort(v), "Counting Sort"
    return merge_sort(v), "Merge Sort"


def main():
    gerador = random.Random(2026)
    testes = [
        ("4 numeros", [5, 2, 9, 1]),
        ("1.000 paginas de 1 a 30", [gerador.randint(1, 30) for _ in range(1000)]),
        ("1.000 numeros de 1 a 1.000.000", [gerador.randint(1, 1_000_000) for _ in range(1000)]),
    ]
    for nome, dados in testes:
        resultado, algoritmo = ordenar(dados)
        certo = "ok" if resultado == sorted(dados) else "ERRO"
        print(f"   {nome:<32} -> {algoritmo:<15} [{certo}]")


if __name__ == "__main__":
    main()
