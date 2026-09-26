"""
busca_saltos.py

Estruturas de Dados — Aula 4 — Bloco 6 (Derivadas)
Slides 42 a 45 · Apostila, capítulo 11

Busca por saltos em um vetor ORDENADO de tamanho n:
  fase 1: salta de m em m posições (acesso por índice é O(1) — Aula 1),
          olhando o último elemento de cada bloco, até achar o bloco
          que pode conter o valor;
  fase 2: faz busca linear só dentro desse bloco.

No pior caso: cerca de n/m saltos + m comparações dentro do bloco.
    T(m) = n/m + m
Derivando (regra da potência, com n/m = n * m^-1):
    T'(m) = -n/m^2 + 1 = 0   ->   m = raiz(n)

Este programa testa vários tamanhos de bloco m, mede o pior caso de
cada um e confere que o melhor m fica mesmo perto de raiz(n).

Só usa a biblioteca padrão — cole direto no onlineide.pro/playground/python
"""
import math


def busca_por_saltos(v, alvo, m):
    """Procura 'alvo' no vetor ordenado v usando blocos de tamanho m.
    Devolve a tupla (posicao, comparacoes); posicao = -1 se não achar."""
    n = len(v)
    comparacoes = 0
    inicio = 0

    # Fase 1: pula blocos inteiros enquanto o ÚLTIMO elemento do bloco
    # ainda for menor que o alvo (então o alvo não pode estar nele).
    while inicio < n:
        fim_do_bloco = min(inicio + m, n) - 1
        comparacoes += 1
        if not (v[fim_do_bloco] < alvo):
            break                    # o alvo, se existir, está neste bloco
        inicio += m

    # Fase 2: busca linear dentro do bloco encontrado.
    for i in range(inicio, min(inicio + m, n)):
        comparacoes += 1
        if v[i] == alvo:
            return i, comparacoes
    return -1, comparacoes


def pior_caso(v, m):
    """Comparações no pior caso para blocos de tamanho m.

    O pior caso é procurar o último elemento de um bloco que fica no fim
    do vetor: fazemos todos os saltos e percorremos o bloco inteiro.
    Há dois candidatos — o último elemento do vetor e o último elemento
    do último bloco completo (quando o bloco final é mais curto) — e
    ficamos com o maior dos dois.
    """
    n = len(v)
    candidatos = [n - 1]
    ultimo_bloco_completo = (n // m) * m - 1
    if 0 <= ultimo_bloco_completo < n - 1:
        candidatos.append(ultimo_bloco_completo)
    return max(busca_por_saltos(v, v[i], m)[1] for i in candidatos)


def formula(n, m):
    """T(m) = n/m + m, escrita como texto (inteiro quando m divide n)."""
    valor = n / m + m
    if valor == int(valor):
        return str(int(valor))
    return f"{valor:.1f}".replace(".", ",")


def com_pontos(x):
    """Formata um inteiro com ponto nos milhares: 1000000 -> 1.000.000"""
    return f"{x:,}".replace(",", ".")


def analisar(n, valores_de_m, faixa_de_busca):
    v = list(range(n))  # vetor ordenado 0, 1, 2, ..., n-1
    print(f"\nn = {com_pontos(n)}   (busca linear, pior caso: {com_pontos(n)} comparacoes)")
    print(f"{'m':>9} {'pior caso medido':>18} {'n/m + m':>11}")
    for m in valores_de_m:
        print(f"{m:>9} {pior_caso(v, m):>18} {formula(n, m):>11}")

    primeiro, ultimo = faixa_de_busca
    resultados = {m: pior_caso(v, m) for m in range(primeiro, ultimo + 1)}
    menor = min(resultados.values())
    melhores = [m for m, custo in resultados.items() if custo == menor]
    print(f"Testando todos os m de {primeiro} a {ultimo}:")
    print(f"  menor pior caso = {menor} comparacoes")
    print(f"  obtido com m de {melhores[0]} a {melhores[-1]}"
          f" ({len(melhores)} valores empatados)")
    print(f"  raiz({n}) = {math.isqrt(n)}   ->   2 * raiz(n) = {2 * math.isqrt(n)}")


def main():
    print("BUSCA POR SALTOS - comparacoes no pior caso (vetor ordenado)")
    print("Modelo: T(m) = n/m + m   ->   T'(m) = -n/m^2 + 1 = 0   ->   m = raiz(n)")

    # Exemplo dos slides 42 e 43
    analisar(10_000, [1, 10, 25, 50, 100, 200, 400, 1000], (1, 1000))

    # Exercício 9 (slides 44 e 45)
    analisar(400, [5, 10, 20, 40, 80], (1, 400))
    analisar(1_000_000, [500, 1000, 2000], (900, 1100))

    print("\nPerceba: perto de raiz(n) varios m empatam. No fundo do \"vale\" a")
    print("curva e quase plana - exatamente onde a derivada vale zero.")


if __name__ == "__main__":
    main()
