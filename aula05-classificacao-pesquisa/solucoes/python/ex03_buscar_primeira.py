"""
ex03_buscar_primeira.py — Aula 5, Exercício 3 (solução de referência)

Busca binária que devolve a PRIMEIRA ocorrência de um valor num vetor
ordenado com repetições. Continua O(log n): quando acha o alvo, guarda a
posição e continua procurando à ESQUERDA, porque pode haver outro igual
antes dele.

Só usa a biblioteca padrão — cole direto no onlineide.pro/playground/python
"""


def buscar_primeira(v, alvo):
    """Devolve (posicao da primeira ocorrência ou -1, comparacoes)."""
    inicio, fim = 0, len(v) - 1
    resposta, comparacoes = -1, 0
    while inicio <= fim:
        meio = (inicio + fim) // 2
        comparacoes += 1
        if v[meio] == alvo:
            resposta = meio          # achou... mas pode haver outro antes
            fim = meio - 1           # continua procurando à esquerda
        elif v[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return resposta, comparacoes


def main():
    paginas = [1, 3, 3, 3, 7, 7, 9, 12, 12, 12, 12, 20]
    print("paginas ordenadas:", paginas)
    esperado = {12: 7, 3: 1, 1: 0, 20: 11, 5: -1}
    for alvo, certo in esperado.items():
        pos, comp = buscar_primeira(paginas, alvo)
        situacao = "ok" if pos == certo else f"ERRO (esperado {certo})"
        print(f"   alvo {alvo:>2}: posicao {pos:>2}, {comp} comparacoes  [{situacao}]")


if __name__ == "__main__":
    main()
