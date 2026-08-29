"""Solucao de referencia da atividade da Aula 2."""


class Pilha:
    def __init__(self, capacidade=20):
        self._dados = []
        self._capacidade = capacidade

    def esta_vazia(self):
        return not self._dados

    def empilhar(self, valor):
        if len(self._dados) == self._capacidade:
            raise OverflowError("pilha cheia")
        self._dados.append(valor)

    def desempilhar(self):
        if self.esta_vazia():
            raise IndexError("pilha vazia")
        return self._dados.pop()

    def consultar_topo(self):
        if self.esta_vazia():
            raise IndexError("pilha vazia")
        return self._dados[-1]

    def valores_do_topo_para_base(self):
        return list(reversed(self._dados))


class NoFila:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def esta_vazia(self):
        return self.inicio is None

    def enfileirar(self, valor):
        novo = NoFila(valor)
        if self.fim is None:
            self.inicio = novo
        else:
            self.fim.proximo = novo
        self.fim = novo

    def desenfileirar(self):
        if self.esta_vazia():
            raise IndexError("fila vazia")
        removido = self.inicio
        self.inicio = removido.proximo
        if self.inicio is None:
            self.fim = None
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


def processar_proximo(espera, historico):
    if espera.esta_vazia():
        return False
    trabalho = espera.desenfileirar()
    historico.empilhar(trabalho)
    print(f"Trabalho processado: {trabalho}")
    return True


def main():
    espera = Fila()
    historico = Pilha()
    for trabalho in (101, 102, 103):
        espera.enfileirar(trabalho)
    processar_proximo(espera, historico)
    processar_proximo(espera, historico)
    espera.enfileirar(104)
    print("Fila de espera:", *espera.valores())
    print("Historico - topo para base:", *historico.valores_do_topo_para_base())
    print("Proximo trabalho:", espera.consultar_frente())
    print("Ultimo trabalho processado:", historico.consultar_topo())


if __name__ == "__main__":
    main()
