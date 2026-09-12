"""Arquivo inicial da atividade. Complete apenas os trechos TODO.

Implemente um Conjunto do zero (sem usar o set() nativo do Python) —
a mesma lógica que você acabou de ver em C.
"""


class Conjunto:
    def __init__(self):
        self._dados = []

    def pertence(self, valor):
        # TODO 1
        raise NotImplementedError

    def inserir(self, valor):
        # TODO 2: nao inserir se o valor ja pertence ao conjunto
        raise NotImplementedError

    def remover(self, valor):
        # TODO 3
        raise NotImplementedError

    def valores(self):
        # TODO 4: retornar os valores armazenados (qualquer ordem)
        raise NotImplementedError


def uniao(a, b):
    # TODO 5
    raise NotImplementedError


def intersecao(a, b):
    # TODO 6
    raise NotImplementedError


def diferenca(a, b):
    # TODO 7
    raise NotImplementedError


def main():
    turma_manha = Conjunto()
    for aluno in (10, 20, 30, 40):
        turma_manha.inserir(aluno)

    turma_tarde = Conjunto()
    for aluno in (30, 40, 50, 60):
        turma_tarde.inserir(aluno)

    print("Turma da manha:", turma_manha.valores())
    print("Turma da tarde:", turma_tarde.valores())

    print("\naluno 20 esta na turma da manha?", turma_manha.pertence(20))
    print("aluno 99 esta na turma da manha?", turma_manha.pertence(99))

    turma_manha.inserir(20)  # ja existe -- nao deve duplicar
    print("\napos inserir 20 de novo:", turma_manha.valores())

    turma_manha.remover(10)
    print("apos remover 10:", turma_manha.valores())
    turma_manha.inserir(10)  # volta ao estado original

    print("\nalunos em pelo menos uma turma:", uniao(turma_manha, turma_tarde).valores())
    print("alunos nas duas turmas:        ", intersecao(turma_manha, turma_tarde).valores())
    print("alunos so na turma da manha:   ", diferenca(turma_manha, turma_tarde).valores())


if __name__ == "__main__":
    main()
