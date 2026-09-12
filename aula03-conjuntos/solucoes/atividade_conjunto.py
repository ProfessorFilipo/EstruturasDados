"""Solucao de referencia da atividade da Aula 3."""


class Conjunto:
    def __init__(self):
        self._dados = []

    def pertence(self, valor):
        return valor in self._dados

    def inserir(self, valor):
        if self.pertence(valor):
            return False
        self._dados.append(valor)
        return True

    def remover(self, valor):
        if not self.pertence(valor):
            return False
        self._dados.remove(valor)
        return True

    def valores(self):
        return list(self._dados)


def uniao(a, b):
    resultado = Conjunto()
    for valor in a.valores():
        resultado.inserir(valor)
    for valor in b.valores():
        resultado.inserir(valor)
    return resultado


def intersecao(a, b):
    resultado = Conjunto()
    for valor in a.valores():
        if b.pertence(valor):
            resultado.inserir(valor)
    return resultado


def diferenca(a, b):
    resultado = Conjunto()
    for valor in a.valores():
        if not b.pertence(valor):
            resultado.inserir(valor)
    return resultado


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
