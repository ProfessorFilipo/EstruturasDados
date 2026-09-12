"""TAD Fila implementado com nos ligados por referencias."""


class NoFila:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self._tamanho = 0

    def esta_vazia(self):
        return self.inicio is None

    def tamanho(self):
        return self._tamanho

    def enfileirar(self, valor):
        novo = NoFila(valor)
        if self.fim is None:
            self.inicio = novo
        else:
            self.fim.proximo = novo
        self.fim = novo
        self._tamanho += 1

    def desenfileirar(self):
        if self.esta_vazia():
            raise IndexError("fila vazia")
        removido = self.inicio
        self.inicio = removido.proximo
        if self.inicio is None:
            self.fim = None
        self._tamanho -= 1
        return removido.valor

    def consultar_frente(self):
        if self.esta_vazia():
            raise IndexError("fila vazia")
        return self.inicio.valor

    def valores(self):
        resultado = []
        atual = self.inicio
        while atual is not None:
            resultado.append(atual.valor)
            atual = atual.proximo
        return resultado

    def exibir(self):
        valores = self.valores()
        print(" ".join(map(str, valores)) if valores else "[vazia]")


if __name__ == "__main__":
    f = Fila()
    f.enfileirar(101)
    f.enfileirar(102)
    f.exibir()
