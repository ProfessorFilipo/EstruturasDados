"""
estruturas.py

Estruturas de Dados — Aula 4 — Atividade prática: Campo Minado
Este arquivo já vem pronto: você não precisa alterá-lo.

As estruturas das aulas anteriores, com a mesma interface:

    Pilha     [Aula 2]  contígua: os dados ficam lado a lado em uma list
    Fila      [Aula 2]  encadeada: nós ligados por referências (início e fim)
    Conjunto  [Aula 3]  sem duplicatas e sem posição (sem usar o set())

e um ContadorOperacoes [Aula 4], usado para medir o custo das jogadas.

Regra da atividade: no núcleo do jogo (tabuleiro.py), não use set(),
collections.deque nem queue.Queue — use só estas estruturas.
"""


class Pilha:
    """TAD Pilha contígua com capacidade fixa. O topo é o fim da list.
    Todas as operações são O(1)."""

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
        """Cópia dos valores, do topo para a base. Custo: O(n)."""
        return list(reversed(self._dados))


class NoFila:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class Fila:
    """TAD Fila encadeada, com referências para o início e o fim.
    Enfileirar e desenfileirar são O(1) graças à referência 'fim'."""

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
        if self.inicio is None:      # removeu o último nó
            self.fim = None
        self._tamanho -= 1
        return removido.valor

    def consultar_frente(self):
        if self.esta_vazia():
            raise IndexError("fila vazia")
        return self.inicio.valor

    def valores(self):
        """Cópia dos valores, do início ao fim. Custo: O(n)."""
        resultado = []
        atual = self.inicio
        while atual is not None:
            resultado.append(atual.valor)
            atual = atual.proximo
        return resultado


class Conjunto:
    """TAD Conjunto sobre uma list (sem usar o set() do Python).

    pertence() percorre os elementos um a um: O(k), onde k é a
    quantidade de elementos. Se receber um ContadorOperacoes, conta
    cada comparação feita em "comparacoes_conjunto" — assim dá para
    ver no contador o custo escondido de cada consulta.
    """

    def __init__(self, contador=None):
        self._dados = []
        self._contador = contador

    def pertence(self, valor):
        """Custo: O(k). Usamos um laço explícito, e não 'valor in lista',
        para deixar visível (e contável) cada comparação."""
        for elemento in self._dados:
            if self._contador is not None:
                self._contador.incrementar("comparacoes_conjunto")
            if elemento == valor:
                return True
        return False

    def inserir(self, valor):
        """Insere se ainda não existir. Custo: O(k) por causa do pertence().
        Devolve True se inseriu, False se o valor já estava lá."""
        if self.pertence(valor):
            return False
        self._dados.append(valor)
        return True

    def remover(self, valor):
        """Remove o valor, se existir. Custo: O(k).
        Como o Conjunto não tem posição, podemos trocar o removido pelo
        último elemento e encurtar a list: não há deslocamentos."""
        for i in range(len(self._dados)):
            if self._contador is not None:
                self._contador.incrementar("comparacoes_conjunto")
            if self._dados[i] == valor:
                self._dados[i] = self._dados[-1]
                self._dados.pop()
                return True
        return False

    def tamanho(self):
        return len(self._dados)

    def valores(self):
        """Cópia dos valores (sem ordem definida). Custo: O(k)."""
        return list(self._dados)


class ContadorOperacoes:
    """Conta operações por categoria, por exemplo "celulas_visitadas".

    As categorias aparecem no relatório na ordem em que foram usadas
    pela primeira vez.
    """

    def __init__(self):
        self._contagens = {}

    def incrementar(self, nome, quantidade=1):
        self._contagens[nome] = self._contagens.get(nome, 0) + quantidade

    def registrar_maximo(self, nome, valor):
        """Guarda o maior valor já visto (ex.: tamanho máximo da fila)."""
        if valor > self._contagens.get(nome, 0):
            self._contagens[nome] = valor

    def valor(self, nome):
        return self._contagens.get(nome, 0)

    def zerar(self):
        self._contagens = {}

    def acumular(self, outro):
        """Soma as contagens de 'outro' a este contador (os máximos
        ficam com o maior valor). Usado para somar cada jogada ao total
        da partida."""
        for nome, valor in outro.itens():
            if nome.startswith("tamanho_max"):
                self.registrar_maximo(nome, valor)
            else:
                self.incrementar(nome, valor)

    def itens(self):
        return list(self._contagens.items())

    def total(self):
        return sum(v for n, v in self._contagens.items() if not n.startswith("tamanho_max"))

    def relatorio(self):
        if not self._contagens:
            return "(nenhuma operacao contada)"
        largura = max(len(nome) for nome in self._contagens)
        linhas = [f"{nome.replace('_', ' '):<{largura}}  {valor:>8}"
                  for nome, valor in self._contagens.items()]
        return "\n".join(linhas)
