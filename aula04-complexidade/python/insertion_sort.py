"""
insertion_sort.py

Estruturas de Dados — Aula 4 — Bloco 5 (Casos e Insertion Sort)
Slides 29 a 36 · Apostila, capítulo 9

1) Rastreia o Insertion Sort em [5, 2, 4, 6, 1, 3], passada por passada.
2) Conta as comparações em três cenários:
     vetor já ordenado -> melhor caso: n - 1 comparações   -> Theta(n)
     ordem aleatória   -> caso médio:  cerca de n^2 / 4    -> Theta(n^2)
     ordem inversa     -> pior caso:   n(n - 1) / 2        -> Theta(n^2)

Conta como "comparação" cada avaliação de  v[j] > chave.
(Theta é a letra grega Θ, usada na notação vista em aula.)

Só usa a biblioteca padrão — cole direto no onlineide.pro/playground/python
"""
import random


def insertion_sort(v):
    """Versão "limpa", idêntica à do slide 29 — para referência."""
    for i in range(1, len(v)):
        chave = v[i]
        j = i - 1
        while j >= 0 and v[j] > chave:
            v[j + 1] = v[j]  # desloca para a direita
            j -= 1
        v[j + 1] = chave


def insertion_sort_contando(v, mostrar=False):
    """Mesma lógica, contando comparações e deslocamentos.

    Ordena v no lugar e devolve a tupla (comparacoes, deslocamentos).
    Se mostrar=True, imprime o vetor ao final de cada passada.
    """
    comparacoes = 0
    deslocamentos = 0

    for i in range(1, len(v)):
        chave = v[i]
        j = i - 1
        comparacoes_passada = 0
        deslocamentos_passada = 0

        while j >= 0:
            comparacoes_passada += 1   # vamos avaliar v[j] > chave
            if not (v[j] > chave):
                break                  # achou o lugar da chave
            v[j + 1] = v[j]            # desloca para a direita
            deslocamentos_passada += 1
            j -= 1
        v[j + 1] = chave

        comparacoes += comparacoes_passada
        deslocamentos += deslocamentos_passada

        if mostrar:
            print(f"passada {i}  chave = {chave}  ->  {v}"
                  f"   comparacoes: {comparacoes_passada}"
                  f"   deslocamentos: {deslocamentos_passada}")

    return comparacoes, deslocamentos


def comparacoes_ordenado(n):
    v = list(range(n))               # 0, 1, 2, ..., n-1
    comparacoes, _ = insertion_sort_contando(v)
    return comparacoes


def comparacoes_invertido(n):
    v = list(range(n - 1, -1, -1))   # n-1, ..., 2, 1, 0
    comparacoes, _ = insertion_sort_contando(v)
    return comparacoes


def comparacoes_aleatorio(n, rodadas, gerador):
    """Média de comparações em 'rodadas' vetores embaralhados."""
    soma = 0
    for _ in range(rodadas):
        v = list(range(n))
        gerador.shuffle(v)           # embaralha: cada ordem tem a mesma chance
        comparacoes, _ = insertion_sort_contando(v)
        soma += comparacoes
    return soma / rodadas


def main():
    # Semente fixa: os "aleatórios" saem sempre iguais, então a saída
    # do programa se repete a cada execução.
    gerador = random.Random(42)

    print("1) INSERTION SORT PASSO A PASSO")
    exemplo = [5, 2, 4, 6, 1, 3]
    print(f"vetor inicial:              {exemplo}")
    comparacoes, deslocamentos = insertion_sort_contando(exemplo, mostrar=True)
    print(f"total: {comparacoes} comparacoes e {deslocamentos} deslocamentos")

    print("\n2) COMPARACOES POR CENARIO")
    print(f"{'n':>8} {'ordenado':>12} {'aleatorio(*)':>13} {'invertido':>12}")
    rodadas = {10: 200, 100: 50, 1000: 10}  # vetores aleatórios por tamanho
    for n in (10, 100, 1000):
        media = comparacoes_aleatorio(n, rodadas[n], gerador)
        print(f"{n:>8} {comparacoes_ordenado(n):>12} {media:>13.0f}"
              f" {comparacoes_invertido(n):>12}")
    print("(*) media de varios vetores embaralhados")

    print("\nFormulas:  ordenado = n - 1   |   aleatorio ~ n^2/4   |   invertido = n(n-1)/2")
    print("Melhor caso: Theta(n)     Caso medio e pior caso: Theta(n^2)")


if __name__ == "__main__":
    main()
