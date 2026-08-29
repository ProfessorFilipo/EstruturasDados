"""TAD Pilha sobre a list contigua e dinamica do Python."""


class Pilha:
    def __init__(self, capacidade=20):
        self._dados = []
        self._capacidade = capacidade

    def esta_vazia(self):
        return len(self._dados) == 0

    def esta_cheia(self):
        return len(self._dados) == self._capacidade

    def tamanho(self):
        return len(self._dados)

    def empilhar(self, valor):
        if self.esta_cheia():
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

    def exibir(self):
        valores = self.valores_do_topo_para_base()
        print(" ".join(map(str, valores)) if valores else "[vazia]")


if __name__ == "__main__":
    p = Pilha()
    p.empilhar(10)
    p.empilhar(20)
    p.exibir()
