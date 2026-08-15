"""
lista_contigua.py

Estruturas de Dados — Aula 1
TAD Lista implementado sobre uma estrutura contígua.

Por baixo dos panos, a `list` nativa do Python já É uma estrutura
contígua dinâmica (um array que se realoca sozinho quando necessário).
Esta classe apenas expõe a interface do TAD Lista sobre ela, com os
mesmos nomes de operação usados na versão em C — para deixar visível
que a interface (o que a lista faz) é a mesma, independente da
implementação (como ela faz).
"""


class ListaContigua:
    def __init__(self):
        self._dados = []

    def inserir(self, pos, valor):
        """Insere 'valor' na posição 'pos' (0 <= pos <= tamanho).
        Custo: O(n)."""
        if pos < 0 or pos > len(self._dados):
            raise IndexError("posição inválida")
        self._dados.insert(pos, valor)

    def inserir_inicio(self, valor):
        """Atalho para inserir(0, valor). Custo: O(n)."""
        self.inserir(0, valor)

    def inserir_fim(self, valor):
        """Atalho para inserir(tamanho, valor). Custo: O(1) amortizado."""
        self.inserir(len(self._dados), valor)

    def remover(self, pos):
        """Remove e retorna o elemento da posição 'pos'. Custo: O(n)."""
        if pos < 0 or pos >= len(self._dados):
            raise IndexError("posição inválida")
        return self._dados.pop(pos)

    def buscar(self, valor):
        """Retorna o índice da primeira ocorrência de 'valor', ou -1 se
        não encontrado. Custo: O(n)."""
        try:
            return self._dados.index(valor)
        except ValueError:
            return -1

    def obter(self, pos):
        """Retorna o valor da posição 'pos'. Custo: O(1)."""
        if pos < 0 or pos >= len(self._dados):
            raise IndexError("posição inválida")
        return self._dados[pos]

    def tamanho(self):
        """Retorna a quantidade de elementos. Custo: O(1)."""
        return len(self._dados)

    def percorrer(self):
        """Imprime todos os elementos, na ordem. Custo: O(n)."""
        for i, valor in enumerate(self._dados):
            print(f"[{i}] = {valor}")

    def __repr__(self):
        return f"ListaContigua({self._dados})"


if __name__ == "__main__":
    l = ListaContigua()
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
