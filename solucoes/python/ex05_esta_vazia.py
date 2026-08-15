"""
ex05_esta_vazia.py — solução

Em Python não há o problema de colisão de nomes que aparece em C: cada
classe tem seu próprio namespace, então dá para importar as duas
implementações no mesmo arquivo sem conflito.
"""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "python"))

from lista_contigua import ListaContigua
from lista_encadeada import ListaEncadeada


def esta_vazia(lista):
    """Funciona para QUALQUER TAD Lista que implemente tamanho() —
    não precisa saber se é contígua ou encadeada."""
    return lista.tamanho() == 0


if __name__ == "__main__":
    for Classe in (ListaContigua, ListaEncadeada):
        print(f"--- {Classe.__name__} ---")
        l = Classe()
        print(f"lista recem-criada, esta_vazia = {esta_vazia(l)}")

        l.inserir_fim(42)
        print(f"apos inserir um elemento, esta_vazia = {esta_vazia(l)}")

        l.remover(0)
        print(f"apos remover o unico elemento, esta_vazia = {esta_vazia(l)}")
        print()
