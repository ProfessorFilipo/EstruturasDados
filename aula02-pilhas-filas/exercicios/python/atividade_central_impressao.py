"""Arquivo inicial da atividade. Complete apenas os trechos TODO."""


class Pilha:
    def __init__(self, capacidade=20):
        self._dados = []
        self._capacidade = capacidade

    def esta_vazia(self):
        # TODO 1
        raise NotImplementedError

    def empilhar(self, valor):
        # TODO 2: verificar a capacidade e inserir no topo
        raise NotImplementedError

    def desempilhar(self):
        # TODO 3: tratar pilha vazia, remover e retornar o topo
        raise NotImplementedError

    def consultar_topo(self):
        # TODO 4: consultar sem remover
        raise NotImplementedError

    def valores_do_topo_para_base(self):
        # TODO 5
        raise NotImplementedError


class NoFila:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def esta_vazia(self):
        # TODO 6
        raise NotImplementedError

    def enfileirar(self, valor):
        # TODO 7: ligar o novo no ao fim
        raise NotImplementedError

    def desenfileirar(self):
        # TODO 8: remover o inicio e atualizar o fim se a fila ficar vazia
        raise NotImplementedError

    def consultar_frente(self):
        # TODO 9: consultar sem remover
        raise NotImplementedError

    def valores(self):
        # TODO 10: percorrer sem modificar a fila
        raise NotImplementedError


def processar_proximo(espera, historico):
    # TODO 11: retirar da fila, empilhar no historico e imprimir
    raise NotImplementedError


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
