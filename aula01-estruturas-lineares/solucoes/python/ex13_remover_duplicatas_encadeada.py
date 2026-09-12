"""
ex13_remover_duplicatas_encadeada.py — solução

Remove valores duplicados de uma ListaEncadeada (do repositório),
mantendo apenas a primeira ocorrência de cada valor.

Duas versões, como sugerido no enunciado:
 - remover_duplicatas_simples: usa um set auxiliar para lembrar quais
   valores já viu. Mais fácil de entender, gasta memória extra.
 - remover_duplicatas_sem_auxiliar: não usa nenhuma estrutura extra,
   mas paga um custo maior (compara cada nó com todos os anteriores).
"""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "python"))

from lista_encadeada import ListaEncadeada


def remover_duplicatas_simples(lista):
    vistos = set()
    pos = 0
    while pos < lista.tamanho():
        valor = lista.obter(pos)
        if valor in vistos:
            lista.remover(pos)  # não avança 'pos': o próximo elemento ocupa esta posição agora
        else:
            vistos.add(valor)
            pos += 1


def remover_duplicatas_sem_auxiliar(lista):
    atual = lista.inicio
    while atual is not None:
        comparador = atual
        while comparador.proximo is not None:
            if comparador.proximo.valor == atual.valor:
                # encontrou uma duplicata do valor de 'atual' mais à
                # frente na lista: remove pela posição, via a API
                # pública, para manter 'fim' e o contador consistentes
                pos = 0
                busca = lista.inicio
                while busca is not comparador.proximo:
                    busca = busca.proximo
                    pos += 1
                lista.remover(pos)
            else:
                comparador = comparador.proximo
        atual = atual.proximo


if __name__ == "__main__":
    valores = [5, 3, 5, 8, 3, 9]

    l1 = ListaEncadeada()
    for v in valores:
        l1.inserir_fim(v)
    print(f"antes:                    {l1}")
    remover_duplicatas_simples(l1)
    print(f"depois (versao simples):  {l1}")
    print("esperado:                 ListaEncadeada([5, 3, 8, 9])")

    l2 = ListaEncadeada()
    for v in valores:
        l2.inserir_fim(v)
    remover_duplicatas_sem_auxiliar(l2)
    print(f"\ndepois (sem auxiliar):    {l2}")
    print("esperado:                 ListaEncadeada([5, 3, 8, 9])")
