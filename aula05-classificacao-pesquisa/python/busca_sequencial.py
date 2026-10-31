"""
busca_sequencial.py

Estruturas de Dados — Aula 5 — Bloco 1 (Pesquisa sequencial)
Slides 05 e 06

A Central de Impressão da Aula 2 cresceu: o histórico agora guarda
10.000 trabalhos, cada um como uma tupla (id, paginas), na ordem em que
saíram da fila (FIFO). Os IDs crescem; cancelamentos deixam lacunas.

A pesquisa sequencial olha um trabalho de cada vez, do início ao fim:
    melhor caso ... 1 comparação         (o alvo é o primeiro)
    caso médio .... (n + 1) / 2          (a soma de Gauss da Aula 4)
    pior caso ..... n comparações        (o alvo é o último ou não existe)

Ela funciona com QUALQUER ordem e QUALQUER estrutura (lista contígua,
lista encadeada, pilha...). É a única opção quando os dados não estão
ordenados pelo campo procurado — como as páginas, aqui.

Só usa a biblioteca padrão — cole direto no onlineide.pro/playground/python
"""
import random

ID = 0        # trabalho[ID]      -> número do trabalho
PAGINAS = 1   # trabalho[PAGINAS] -> quantidade de páginas


def gerar_historico(n, semente=2026):
    """Devolve uma lista com n trabalhos (id, paginas) em ordem de chegada.
    Semente fixa: todo mundo vê exatamente os mesmos trabalhos."""
    gerador = random.Random(semente)
    historico = []
    id_atual = 101                              # o primeiro ID da Aula 2
    for _ in range(n):
        paginas = gerador.randint(1, 30)
        historico.append((id_atual, paginas))
        id_atual += gerador.randint(1, 3)       # 2 ou 3 = houve cancelamento
    return historico


def busca_sequencial(v, alvo, campo):
    """Procura o primeiro trabalho cujo campo (ID ou PAGINAS) vale 'alvo'.
    Devolve a tupla (posicao, comparacoes); posicao = -1 se não achar."""
    comparacoes = 0
    for i in range(len(v)):
        comparacoes += 1                        # uma comparação por trabalho
        if v[i][campo] == alvo:
            return i, comparacoes
    return -1, comparacoes


def main():
    historico = gerar_historico(10_000)
    print(f"historico: {len(historico)} trabalhos")
    print(f"primeiros: {historico[:3]}")
    print(f"ultimo:    {historico[-1]}")

    # Troque este valor e rode de novo! (de 1 a 30)
    ALVO_PAGINAS = 27

    print("\n1) ALGUM TRABALHO TEVE", ALVO_PAGINAS, "PAGINAS?")
    pos, comp = busca_sequencial(historico, ALVO_PAGINAS, PAGINAS)
    if pos >= 0:
        print(f"   sim: {historico[pos]} na posicao {pos}  ->  {comp} comparacoes")
    else:
        print(f"   nao  ->  {comp} comparacoes")

    print("\n2) O TRABALHO", historico[-1][ID], "(O ULTIMO) FOI IMPRESSO?")
    pos, comp = busca_sequencial(historico, historico[-1][ID], ID)
    print(f"   sim, posicao {pos}  ->  {comp} comparacoes (pior caso)")

    print("\n3) O TRABALHO 100 FOI IMPRESSO?  (nao existe: comecamos no 101)")
    pos, comp = busca_sequencial(historico, 100, ID)
    print(f"   nao  ->  {comp} comparacoes (olhou todos)")

    print("\nMelhor caso: 1   |   medio: (n + 1)/2   |   pior: n   ->   O(n)")


if __name__ == "__main__":
    main()
