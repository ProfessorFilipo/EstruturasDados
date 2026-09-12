"""
ex10_lista_encadeada_do_zero.py — solução

Implementação independente (não importa lista_encadeada.py do
repositório) de uma lista encadeada mínima, com inserir_inicio e
percorrer, exatamente como o Exercício 10 pede.
"""


class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class ListaEncadeada:
    def __init__(self):
        self.inicio = None

    def inserir_inicio(self, valor):
        novo = No(valor)
        novo.proximo = self.inicio
        self.inicio = novo

    def percorrer(self):
        valores = []
        atual = self.inicio
        while atual is not None:
            valores.append(str(atual.valor))
            atual = atual.proximo
        print(", ".join(valores))


if __name__ == "__main__":
    l = ListaEncadeada()
    l.inserir_inicio(10)
    l.inserir_inicio(20)
    l.inserir_inicio(30)

    print("esperado: 30, 20, 10")
    print("obtido:   ", end="")
    l.percorrer()
