"""
ex14_benchmark.py — solução

Mede o tempo de inserir 10.000 elementos no início e no fim, para a
ListaContigua e a ListaEncadeada do repositório, e compara com a
previsão da tabela de complexidade (Exercício 4).
"""
import sys
import os
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "python"))

from lista_contigua import ListaContigua
from lista_encadeada import ListaEncadeada

N = 10000


def medir(func):
    inicio = time.time()
    func()
    fim = time.time()
    return fim - inicio


def contigua_inicio():
    l = ListaContigua()
    for i in range(N):
        l.inserir_inicio(i)


def contigua_fim():
    l = ListaContigua()
    for i in range(N):
        l.inserir_fim(i)


def encadeada_inicio():
    l = ListaEncadeada()
    for i in range(N):
        l.inserir_inicio(i)


def encadeada_fim():
    l = ListaEncadeada()
    for i in range(N):
        l.inserir_fim(i)


if __name__ == "__main__":
    resultados = {
        "contigua  - inserir no inicio": medir(contigua_inicio),
        "contigua  - inserir no fim": medir(contigua_fim),
        "encadeada - inserir no inicio": medir(encadeada_inicio),
        "encadeada - inserir no fim": medir(encadeada_fim),
    }

    print(f"Inserindo {N} elementos:\n")
    print(f"{'operacao':<32}{'tempo (s)':>10}")
    for nome, tempo in resultados.items():
        print(f"{nome:<32}{tempo:>10.6f}")

    print("\nO esperado pela tabela de complexidade (Exercicio 4):")
    print("- 'contigua - inserir no inicio' deve ser a mais lenta")
    print("  (O(n) por insercao -> O(n^2) no total)")
    print("- as outras tres devem ser bem mais rapidas entre si")
    print("  (O(1) por insercao -> O(n) no total)")
