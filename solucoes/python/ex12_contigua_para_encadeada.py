"""
ex12_contigua_para_encadeada.py — solução

Converte uma ListaContigua já preenchida em uma nova ListaEncadeada
equivalente, usando só a interface pública das duas (tamanho/obter/
inserir_fim) — sem tocar em nenhum detalhe interno das classes.

Em Python, diferente de C, isso não tem nenhum problema de nomes: as
duas classes podem ser importadas e usadas juntas sem conflito.
"""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "python"))

from lista_contigua import ListaContigua
from lista_encadeada import ListaEncadeada


def contigua_para_encadeada(origem):
    destino = ListaEncadeada()
    for i in range(origem.tamanho()):
        destino.inserir_fim(origem.obter(i))
    return destino


if __name__ == "__main__":
    c = ListaContigua()
    for v in [5, 10, 15]:
        c.inserir_fim(v)

    e = contigua_para_encadeada(c)

    print(f"contigua:  {c}")
    print(f"encadeada: {e}")
