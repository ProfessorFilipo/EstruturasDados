"""
busca_binaria.py

Estruturas de Dados — Aula 5 — Bloco 2 (Pesquisa binária)
Slides 07 a 13

O jogo de "adivinhar de 1 a 100" da Aula 4, agora com IDs de trabalhos.
Cada comparação olha o elemento do MEIO e descarta a metade que não pode
conter o alvo. No pior caso: floor(log2 n) + 1 comparações -> O(log n).

Dois pré-requisitos:
  1. o vetor precisa estar ORDENADO pelo campo procurado
     (o histórico da Central sai da fila FIFO já ordenado por ID);
  2. o acesso por índice precisa ser O(1) — lista CONTÍGUA (Aula 1).
     Numa lista encadeada, obter(meio) custa O(n) e a vantagem some.

Só usa a biblioteca padrão — cole direto no onlineide.pro/playground/python
"""
import math


def fmt(x):
    """Formata inteiros no padrão brasileiro: 1234567 -> 1.234.567"""
    return f"{x:,}".replace(",", ".")


# ------------------------------------------------------------------
# Versão "limpa", idêntica à do slide 10 — para referência.
# ------------------------------------------------------------------
def busca_binaria(v, alvo):
    inicio, fim = 0, len(v) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if v[meio] == alvo:
            return meio        # achou
        if v[meio] < alvo:
            inicio = meio + 1  # descarta esquerda
        else:
            fim = meio - 1     # descarta direita
    return -1                  # intervalo vazio


# ------------------------------------------------------------------
# A mesma busca, contando comparações e (opcionalmente) mostrando cada passo.
# ------------------------------------------------------------------
def busca_binaria_contando(v, alvo, mostrar=False):
    """Procura 'alvo' no vetor ORDENADO v.
    Devolve a tupla (posicao, comparacoes); posicao = -1 se não achar."""
    inicio, fim = 0, len(v) - 1
    comparacoes = 0
    while inicio <= fim:
        meio = (inicio + fim) // 2
        comparacoes += 1                        # olhamos v[meio]
        if mostrar:
            print(f"   inicio={inicio:>2}  meio={meio:>2}  fim={fim:>2}"
                  f"   v[meio]={v[meio]}")
        if v[meio] == alvo:
            return meio, comparacoes
        if v[meio] < alvo:
            inicio = meio + 1                   # descarta a metade da esquerda
        else:
            fim = meio - 1                      # descarta a metade da direita
    return -1, comparacoes


def main():
    # 16 IDs do histórico: ordenados (FIFO) e com lacunas (cancelamentos)
    ids = [101, 104, 105, 109, 112, 113, 118, 121,
           125, 126, 130, 134, 137, 141, 142, 150]

    # Troque o alvo e rode de novo!
    ALVO = 137

    print("1) RASTREIO: buscando", ALVO, "entre", len(ids), "IDs")
    pos, comp = busca_binaria_contando(ids, ALVO, mostrar=True)
    assert pos == busca_binaria(ids, ALVO)      # confere com a versão limpa
    print(f"   -> posicao {pos}, {comp} comparacoes")

    print("\n2) RASTREIO: buscando 119 (foi cancelado)")
    pos, comp = busca_binaria_contando(ids, 119, mostrar=True)
    print(f"   -> posicao {pos} (inicio passou do fim), {comp} comparacoes")

    print("\n3) PIOR CASO: SEQUENCIAL x SALTOS (AULA 4) x BINARIA")
    print(f"{'n':>15} {'sequencial':>15} {'saltos':>9} {'binaria':>8}")
    for n in (1_000, 1_000_000, 1_000_000_000):
        ids_grandes = range(101, 101 + n)       # range não ocupa memória
        _, comp = busca_binaria_contando(ids_grandes, 101 + n)   # alvo ausente
        saltos = round(2 * math.sqrt(n))        # n/m + m com m = raiz(n)
        print(f"{fmt(n):>15} {fmt(n):>15} {fmt(saltos):>9} {comp:>8}")

    print("\nDobrar n custa so +1 comparacao na binaria: O(log n)")


if __name__ == "__main__":
    main()
