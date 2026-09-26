"""
crescimento_funcoes.py

Estruturas de Dados — Aula 4 — Bloco 6 (Famílias de funções)
Slides 37 e 38 · Apostila, capítulo 10

1) Valor de cada família de funções para n = 10, 20, 50, 100 e 1000.
2) Tempo de execução se cada operação levasse 1 nanossegundo.
3) Quanto um computador 1000 vezes mais rápido realmente ajuda.

Números muito grandes aparecem em notação científica:
    4,0 x 10^13  significa  4,0 vezes 10 elevado a 13.

Só usa a biblioteca padrão — cole direto no onlineide.pro/playground/python
"""
import math

# Cada família: (nome exibido, função que calcula o valor para um n).
# Os inteiros do Python não têm limite de tamanho, então 2^1000 e 1000!
# são calculados exatamente.
FAMILIAS = [
    ("log2 n",   lambda n: math.log2(n)),
    ("raiz n",   lambda n: math.sqrt(n)),
    ("n",        lambda n: n),
    ("n log2 n", lambda n: n * math.log2(n)),
    ("n^2",      lambda n: n ** 2),
    ("n^3",      lambda n: n ** 3),
    ("2^n",      lambda n: 2 ** n),
    ("n!",       lambda n: math.factorial(n)),
]

SEGUNDOS_POR_ANO = 365.25 * 24 * 3600


def com_virgula(texto):
    """Troca o ponto decimal por vírgula (padrão brasileiro)."""
    return texto.replace(".", ",")


def cientifica(valor):
    """Formata um número positivo como 'm,m x 10^e'.
    Funciona até para inteiros enormes, como 1000! (com 2568 dígitos)."""
    expoente = math.floor(math.log10(valor))
    mantissa = valor / 10 ** expoente  # Python divide inteiros enormes com precisão
    if mantissa >= 9.95:             # evita "10,0 x 10^e" por arredondamento
        mantissa /= 10
        expoente += 1
    return com_virgula(f"{mantissa:.1f}") + f" x 10^{expoente}"


def formatar_valor(valor):
    """Números pequenos por extenso; números grandes em notação científica."""
    if isinstance(valor, float) and valor < 1000:
        return com_virgula(f"{valor:.1f}")
    if valor < 10_000_000:
        return f"{round(valor):,}".replace(",", ".")  # 1.000.000
    return cientifica(valor)


def formatar_tempo(nanossegundos):
    """Converte uma quantidade de nanossegundos para a unidade mais legível."""
    segundos = nanossegundos / 1e9
    if nanossegundos < 1e3:
        return f"{nanossegundos:.0f} ns"
    if nanossegundos < 1e6:
        return com_virgula(f"{nanossegundos / 1e3:.1f}") + " us"
    if nanossegundos < 1e9:
        return com_virgula(f"{nanossegundos / 1e6:.1f}") + " ms"
    if segundos < 60:
        return com_virgula(f"{segundos:.1f}") + " s"
    if segundos < 3600:
        return com_virgula(f"{segundos / 60:.1f}") + " min"
    if segundos < 86400:
        return com_virgula(f"{segundos / 3600:.1f}") + " h"
    if segundos < SEGUNDOS_POR_ANO:
        return com_virgula(f"{segundos / 86400:.0f}") + " dias"
    anos = segundos / SEGUNDOS_POR_ANO
    if anos < 1_000_000:
        return f"{anos:,.0f}".replace(",", ".") + " anos"
    return cientifica(anos) + " anos"


def maior_n_possivel(funcao, orcamento):
    """Maior n tal que funcao(n) <= orcamento (a função precisa ser crescente).
    Primeiro dobra n até estourar o orçamento; depois faz busca binária."""
    alto = 1
    while funcao(alto * 2) <= orcamento:
        alto *= 2
    baixo, alto = alto, alto * 2     # a resposta está entre baixo e alto
    while alto - baixo > 1:
        meio = (baixo + alto) // 2
        if funcao(meio) <= orcamento:
            baixo = meio
        else:
            alto = meio
    return baixo


def main():
    tamanhos = [10, 20, 50, 100, 1000]

    print("1) VALOR DE CADA FAMILIA DE FUNCOES")
    print(f"{'f(n)':>9}" + "".join(f"{'n = ' + str(n):>16}" for n in tamanhos))
    for nome, funcao in FAMILIAS:
        linha = f"{nome:>9}"
        for n in tamanhos:
            linha += f"{formatar_valor(funcao(n)):>16}"
        print(linha)

    print("\n2) TEMPO DE EXECUCAO SE CADA OPERACAO LEVASSE 1 NANOSSEGUNDO")
    print("   (ns = nanossegundo, us = microssegundo, ms = milissegundo)")
    tamanhos_tempo = [10, 20, 50, 100]
    print(f"{'f(n)':>9}" + "".join(f"{'n = ' + str(n):>20}" for n in tamanhos_tempo))
    for nome, funcao in FAMILIAS:
        if nome in ("n", "n^2", "n^3", "2^n", "n!"):
            linha = f"{nome:>9}"
            for n in tamanhos_tempo:
                linha += f"{formatar_tempo(float(funcao(n))):>20}"
            print(linha)
    print("   Para comparar: a idade do universo e de cerca de 1,4 x 10^10 anos.")

    print("\n3) UM COMPUTADOR 1000 VEZES MAIS RAPIDO AJUDA QUANTO?")
    print("   Maior n que cabe em 1 segundo, a 1 ns por operacao (10^9 operacoes),")
    print("   e o mesmo com uma maquina 1000 vezes mais rapida (10^12 operacoes).")
    print(f"{'f(n)':>9} {'hoje':>18} {'1000x mais rapido':>20} {'ganho':>10}")
    for nome, funcao in FAMILIAS:
        if nome in ("log2 n", "raiz n"):
            continue  # crescem tao devagar que o n "cabivel" e astronomico
        hoje = maior_n_possivel(funcao, 10 ** 9)
        rapido = maior_n_possivel(funcao, 10 ** 12)
        razao = rapido / hoje
        if razao >= 2:
            ganho = f"x {razao:,.0f}".replace(",", ".") if razao >= 100 else "x " + com_virgula(f"{razao:.1f}")
        else:
            ganho = f"+ {rapido - hoje}"
        print(f"{nome:>9} {formatar_valor(hoje):>18} {formatar_valor(rapido):>20} {ganho:>10}")
    print("   Moral: para 2^n e n!, hardware melhor quase nao muda nada;")
    print("   o que muda o jogo e escolher um algoritmo de familia menor.")


if __name__ == "__main__":
    main()
