"""
contagem_operacoes.py

Estruturas de Dados — Aula 4 — Bloco 2 (Contar operações)
Slides 06 a 08 · Apostila, capítulo 2

Conta os passos executados por duas funções simples e compara o
resultado com a fórmula que obtivemos no papel:

    soma de um vetor ............. T(n) = 3n + 4
    busca linear, pior caso ...... T(n) = 3n + 3   (valor ausente)
    busca linear, melhor caso .... T(n) = 4        (valor na posição 0)

Modelo de custo usado na aula: cada instrução simples executada custa
1 passo — uma atribuição, um teste do laço, um incremento, um comando
do corpo do laço ou um return.

Sem nenhum import — cole direto no onlineide.pro/playground/python
"""

passos = 0  # contador global de passos


def testar(condicao):
    """Conta 1 passo cada vez que um teste é avaliado e devolve o
    resultado do teste. Assim, "while testar(i < n)" conta cada
    avaliação de i < n."""
    global passos
    passos += 1
    return condicao


def soma(v, n):
    """Mesma soma do slide 06.

    Em Python, o jeito natural seria "for x in v: total += x". Aqui
    usamos while para deixar cada passo visível — a contagem é a mesma
    da versão em C.
    """
    global passos
    total = 0                 # executa 1 vez
    passos += 1
    i = 0                     # executa 1 vez
    passos += 1
    while testar(i < n):      # teste: executa n + 1 vezes
        total = total + v[i]  # executa n vezes
        passos += 1
        i = i + 1             # executa n vezes
        passos += 1
    passos += 1               # return: executa 1 vez
    return total


def buscar(dados, tamanho, valor):
    """Mesma lógica de lista_buscar() da Aula 1: devolve a posição de
    'valor' ou -1 se ele não estiver na lista."""
    global passos
    i = 0                            # executa 1 vez
    passos += 1
    while testar(i < tamanho):       # teste: até n + 1 vezes
        if testar(dados[i] == valor):  # comparação: até n vezes
            passos += 1              # return i: no máximo 1 vez
            return i
        i = i + 1                    # incremento: até n vezes
        passos += 1
    passos += 1                      # return -1: no máximo 1 vez
    return -1


def imprimir_cabecalho():
    print(f"{'n':>8} {'passos contados':>17} {'formula':>9}")


def imprimir_linha(n, contados, formula):
    situacao = "confere" if contados == formula else "DIFERENTE!"
    print(f"{n:>8} {contados:>17} {formula:>9}   {situacao}")


def main():
    global passos
    tamanhos = [10, 100, 1000]
    v = list(range(1000))  # vetor com os valores 0, 1, 2, ..., 999

    print("Modelo de custo: cada instrucao simples executada = 1 passo")

    print("\n1) SOMA DE UM VETOR                            formula: T(n) = 3n + 4")
    imprimir_cabecalho()
    for n in tamanhos:
        passos = 0
        soma(v, n)
        imprimir_linha(n, passos, 3 * n + 4)

    print("\n2) BUSCA LINEAR - PIOR CASO (valor ausente)    formula: T(n) = 3n + 3")
    imprimir_cabecalho()
    for n in tamanhos:
        passos = 0
        buscar(v, n, -1)  # -1 nao esta no vetor
        imprimir_linha(n, passos, 3 * n + 3)

    print("\n3) BUSCA LINEAR - MELHOR CASO (valor na posicao 0)   formula: T(n) = 4")
    imprimir_cabecalho()
    for n in tamanhos:
        passos = 0
        buscar(v, n, 0)  # 0 esta na posicao 0
        imprimir_linha(n, passos, 4)

    print("\nObserve: no pior caso, os passos crescem junto com n (crescimento linear).")
    print("No melhor caso, ficam constantes, nao importa o tamanho da lista.")


if __name__ == "__main__":
    main()
