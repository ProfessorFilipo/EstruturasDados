"""
corrida_ordenacao.py

Estruturas de Dados — Aula 5 — PARA CASA (não é demonstrado em aula)

A corrida dos algoritmos: 2.000 trabalhos da Central de Impressão,
ordenados por número de páginas (de 1 a 30), em três cenários:

    aleatorio ... páginas sorteadas (o caso médio)
    ordenado .... páginas já em ordem crescente
    inverso ..... páginas em ordem decrescente

Corredores:
    Insertion Sort ...... Theta(n) no melhor caso, Theta(n^2) no médio e no pior
    Merge Sort .......... Theta(n log n) sempre
    Quicksort ........... pivô sorteado: n log n em média
    Counting Sort ....... Theta(n + k), sem comparar (k = 30 páginas)
    sorted() do Python .. Timsort (Insertion + Merge), escrito em C

Para cada um, o programa mostra as COMPARAÇÕES (quando o algoritmo compara)
e o TEMPO em milissegundos. O tempo muda de computador para computador —
e até entre duas execuções —, mas a ordem de grandeza se mantém.

Perguntas para pensar:
  1. Por que o Insertion Sort, o mais lento no cenário "aleatorio", fica
     entre os mais rápidos no cenário "ordenado"?
  2. Por que o sorted() vence todo mundo, mesmo sendo n log n?
     (Dica: ele é escrito em C, e "trocar de linguagem" só muda a constante.)
  3. O Quicksort aqui usa pivô sorteado. O que aconteceria no cenário
     "ordenado" com o pivô sempre no último elemento? (Veja quick_sort.py.)
  4. Por que o Quicksort fez cerca de 4 vezes mais comparações que o Merge
     Sort? (Dica: só existem 30 valores diferentes. Na partição da aula,
     todos os elementos IGUAIS ao pivô vão para o mesmo lado.)

Só usa a biblioteca padrão — cole direto no onlineide.pro/playground/python
"""
import random
import time

N = 2000          # quantidade de trabalhos (experimente 500 ou 4000)
K = 30            # páginas de 1 a K

gerador = random.Random(2026)


def fmt(x):
    """Formata inteiros no padrão brasileiro: 1234567 -> 1.234.567"""
    return f"{x:,}".replace(",", ".")


# ---------------------------------------------------------------- corredores
# Cada função ordena uma CÓPIA da lista e devolve (lista_ordenada, comparações).

def insertion_sort(v):
    v = list(v)
    comp = 0
    for i in range(1, len(v)):
        chave, j = v[i], i - 1
        while j >= 0:
            comp += 1
            if not (v[j] > chave):
                break
            v[j + 1] = v[j]
            j -= 1
        v[j + 1] = chave
    return v, comp


def merge_sort(v):
    if len(v) <= 1:
        return list(v), 0
    meio = len(v) // 2
    esq, c1 = merge_sort(v[:meio])
    dir, c2 = merge_sort(v[meio:])
    junto, i, j, comp = [], 0, 0, c1 + c2
    while i < len(esq) and j < len(dir):
        comp += 1
        if esq[i] <= dir[j]:
            junto.append(esq[i])
            i += 1
        else:
            junto.append(dir[j])
            j += 1
    return junto + esq[i:] + dir[j:], comp


def quick_sort(v):
    v = list(v)
    contador = [0]

    def particionar(inicio, fim):
        k = gerador.randint(inicio, fim)          # pivô sorteado
        v[k], v[fim] = v[fim], v[k]
        pivo, i = v[fim], inicio
        for j in range(inicio, fim):
            contador[0] += 1
            if v[j] < pivo:
                v[i], v[j] = v[j], v[i]
                i += 1
        v[i], v[fim] = v[fim], v[i]
        return i

    def ordenar(inicio, fim):
        if inicio < fim:
            p = particionar(inicio, fim)
            ordenar(inicio, p - 1)
            ordenar(p + 1, fim)

    ordenar(0, len(v) - 1)
    return v, contador[0]


def counting_sort(v):
    contagem = [0] * (K + 1)
    for p in v:
        contagem[p] += 1
    saida = []
    for p in range(K + 1):
        saida.extend([p] * contagem[p])
    return saida, None                            # None: não compara nada


def sorted_python(v):
    return sorted(v), None                        # o Python não informa as comparações


CORREDORES = [
    ("Insertion Sort", insertion_sort),
    ("Merge Sort", merge_sort),
    ("Quicksort", quick_sort),
    ("Counting Sort", counting_sort),
    ("sorted() (Timsort)", sorted_python),
]


# ---------------------------------------------------------------- corrida
def correr(nome_cenario, dados):
    print(f"\nCENARIO: {nome_cenario} (n = {fmt(len(dados))}, paginas de 1 a {K})")
    print(f"   {'algoritmo':<20} {'comparacoes':>12} {'tempo (ms)':>11}")
    referencia = sorted(dados)
    for nome, funcao in CORREDORES:
        inicio = time.perf_counter()
        resultado, comp = funcao(dados)
        ms = (time.perf_counter() - inicio) * 1000
        assert resultado == referencia, f"{nome} ordenou errado!"
        comp_txt = fmt(comp) if comp is not None else "-"
        print(f"   {nome:<20} {comp_txt:>12} {ms:>11.1f}")


def main():
    aleatorio = [gerador.randint(1, K) for _ in range(N)]
    correr("aleatorio", aleatorio)
    correr("ordenado", sorted(aleatorio))
    correr("inverso", sorted(aleatorio, reverse=True))
    print("\nTodos ordenaram corretamente. Compare as colunas e responda as")
    print("perguntas do inicio do arquivo.")


if __name__ == "__main__":
    main()
