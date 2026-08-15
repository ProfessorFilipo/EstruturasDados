"""
lista_encadeada.py

Estruturas de Dados — Aula 1
TAD Lista implementado com nós ligados por referências (estrutura
encadeada, lista simplesmente encadeada) — o equivalente em Python aos
ponteiros usados na versão em C.
"""


class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class ListaEncadeada:
    def __init__(self):
        self.inicio = None
        self.fim = None  # mantido para permitir inserir_fim em O(1)
        self._tamanho = 0

    def inserir_inicio(self, valor):
        """Insere 'valor' no início da lista. Custo: O(1)."""
        novo = No(valor)
        novo.proximo = self.inicio
        self.inicio = novo
        if self.fim is None:
            self.fim = novo  # lista estava vazia
        self._tamanho += 1

    def inserir_fim(self, valor):
        """Insere 'valor' no fim da lista. Custo: O(1), graças a self.fim."""
        novo = No(valor)
        if self.inicio is None:
            self.inicio = novo
        else:
            self.fim.proximo = novo
        self.fim = novo
        self._tamanho += 1

    def inserir(self, pos, valor):
        """Insere 'valor' na posição 'pos' (0 <= pos <= tamanho).
        Custo: O(n) no pior caso."""
        if pos < 0 or pos > self._tamanho:
            raise IndexError("posição inválida")
        if pos == 0:
            self.inserir_inicio(valor)
            return
        if pos == self._tamanho:
            self.inserir_fim(valor)
            return

        anterior = self._no_em(pos - 1)
        novo = No(valor)
        novo.proximo = anterior.proximo
        anterior.proximo = novo
        self._tamanho += 1

    def remover(self, pos):
        """Remove e retorna o valor da posição 'pos'. Custo: O(n)."""
        if pos < 0 or pos >= self._tamanho:
            raise IndexError("posição inválida")

        if pos == 0:
            removido = self.inicio
            self.inicio = removido.proximo
            if self.inicio is None:
                self.fim = None
        else:
            anterior = self._no_em(pos - 1)
            removido = anterior.proximo
            anterior.proximo = removido.proximo
            if removido is self.fim:
                self.fim = anterior

        self._tamanho -= 1
        return removido.valor

    def buscar(self, valor):
        """Retorna o índice da primeira ocorrência de 'valor', ou -1 se
        não encontrado. Custo: O(n)."""
        atual = self.inicio
        pos = 0
        while atual is not None:
            if atual.valor == valor:
                return pos
            atual = atual.proximo
            pos += 1
        return -1

    def obter(self, pos):
        """Retorna o valor da posição 'pos'. Custo: O(n)."""
        return self._no_em(pos).valor

    def tamanho(self):
        """Retorna a quantidade de elementos. Custo: O(1)."""
        return self._tamanho

    def percorrer(self):
        """Imprime todos os elementos, na ordem. Custo: O(n)."""
        atual = self.inicio
        pos = 0
        while atual is not None:
            print(f"[{pos}] = {atual.valor}")
            atual = atual.proximo
            pos += 1

    def _no_em(self, pos):
        """Função auxiliar interna: retorna o nó na posição 'pos'."""
        if pos < 0 or pos >= self._tamanho:
            raise IndexError("posição inválida")
        atual = self.inicio
        for _ in range(pos):
            atual = atual.proximo
        return atual

    def __repr__(self):
        valores = []
        atual = self.inicio
        while atual is not None:
            valores.append(atual.valor)
            atual = atual.proximo
        return f"ListaEncadeada({valores})"


if __name__ == "__main__":
    l = ListaEncadeada()
    l.inserir_fim(10)
    l.inserir_fim(20)
    l.inserir_fim(30)
    l.inserir_inicio(5)
    l.inserir(2, 99)  # insere 99 no meio

    print(f"Lista apos as insercoes (tamanho = {l.tamanho()}):")
    l.percorrer()

    print(f"\nposicao de 99: {l.buscar(99)}")
    print(f"elemento na posicao 0: {l.obter(0)}")

    removido = l.remover(2)
    print(f"\nremovido da posicao 2: {removido}")
    print(f"Lista apos a remocao (tamanho = {l.tamanho()}):")
    l.percorrer()
