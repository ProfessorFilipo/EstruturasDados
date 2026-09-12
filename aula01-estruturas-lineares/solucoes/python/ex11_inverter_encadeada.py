"""
ex11_inverter_encadeada.py — solução

Inverte uma ListaEncadeada (do repositório) religando os nós já
existentes, sem criar nenhum nó novo.
"""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "python"))

from lista_encadeada import ListaEncadeada


def inverter(lista):
    anterior = None
    atual = lista.inicio

    lista.fim = lista.inicio  # o antigo inicio vira o novo fim

    while atual is not None:
        proximo = atual.proximo  # guarda o resto da lista antes de sobrescrever
        atual.proximo = anterior  # inverte a seta deste no
        anterior = atual  # avanca 'anterior'
        atual = proximo  # avanca 'atual'

    lista.inicio = anterior  # o ultimo no visitado vira o novo inicio


if __name__ == "__main__":
    l = ListaEncadeada()
    l.inserir_fim(10)
    l.inserir_fim(20)
    l.inserir_fim(30)

    print(f"antes:    {l}")
    inverter(l)
    print("esperado: ListaEncadeada([30, 20, 10])")
    print(f"depois:   {l}")

    print(f"\nl.fim aponta para o valor {l.fim.valor} (deve ser 10)")
