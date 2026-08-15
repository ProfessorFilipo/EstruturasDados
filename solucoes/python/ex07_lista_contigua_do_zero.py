"""
ex07_lista_contigua_do_zero.py — solução

Implementação independente (não importa lista_contigua.py do
repositório) de uma lista contígua mínima, com inserir_fim e buscar,
exatamente como o Exercício 7 pede.
"""


class ListaContigua:
    def __init__(self):
        self._dados = []

    def inserir_fim(self, valor):
        self._dados.append(valor)

    def buscar(self, valor):
        for i, v in enumerate(self._dados):
            if v == valor:
                return i
        return -1


if __name__ == "__main__":
    l = ListaContigua()
    l.inserir_fim(10)
    l.inserir_fim(20)
    l.inserir_fim(30)

    print(f"buscar(20) = {l.buscar(20)} (esperado: 1)")
    print(f"buscar(99) = {l.buscar(99)} (esperado: -1)")
