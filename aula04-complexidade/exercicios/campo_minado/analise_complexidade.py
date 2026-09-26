"""
analise_complexidade.py

Estruturas de Dados — Aula 4 — Atividade prática: Campo Minado
Este arquivo já vem pronto: você não precisa alterá-lo.

Mede, com o contador de operações, o custo das técnicas usadas no jogo e
compara cada uma com uma alternativa mais ingênua. Use a saída para
responder à Parte D do enunciado.

Rode só depois de completar os TODOs de tabuleiro.py:
    python analise_complexidade.py
"""
from estruturas import Conjunto, ContadorOperacoes, Fila
from tabuleiro import NIVEIS, Tabuleiro

SEMENTE = 2026   # semente fixa: os números saem iguais a cada execução


def titulo(texto):
    print("\n" + texto)
    print("-" * len(texto))


def abrir_tabuleiro_vazio(n, estrategia):
    """Tabuleiro n x n SEM minas: um clique no canto abre tudo.
    É o pior caso da abertura em cascata. Devolve o contador da jogada."""
    tab = Tabuleiro(n, n, 0)
    tab.estrategia = estrategia
    tab.definir_minas([])
    tab.revelar(0, 0)
    return tab.contador


def abrir_marcando_ao_retirar(n):
    """Versão ERRADA da abertura: marca a célula só quando ela SAI da fila.
    Uma célula pode então entrar na fila várias vezes (uma por vizinha
    que a enxergou antes de ela ser aberta). Devolve quantas entradas."""
    tab = Tabuleiro(n, n, 0)
    abertas = [False] * tab.total_celulas
    fila = Fila()
    fila.enfileirar(0)
    entradas = 1
    while not fila.esta_vazia():
        atual = fila.desenfileirar()
        if abertas[atual]:
            continue                      # já tinha sido aberta: trabalho jogado fora
        abertas[atual] = True
        for vizinha in tab.vizinhos(atual):
            if not abertas[vizinha]:
                fila.enfileirar(vizinha)
                entradas += 1
    return entradas


def numeros_perguntando_a_cada_celula(tab):
    """Versão INGÊNUA do cálculo dos números: para cada célula, pergunta
    ao Conjunto de minas se cada vizinha é mina. Devolve (numeros,
    comparações feitas no Conjunto)."""
    contador = ContadorOperacoes()
    minas = Conjunto(contador)
    for mina in tab.minas.valores():
        minas.inserir(mina)
    contador.zerar()                      # só queremos medir as consultas
    numeros = [0] * tab.total_celulas
    for i in range(tab.total_celulas):
        for vizinha in tab.vizinhos(i):
            if minas.pertence(vizinha):
                numeros[i] += 1
    return numeros, contador.valor("comparacoes_conjunto")


def tabuleiro_sorteado(nivel):
    """Tabuleiro do nível com as minas já sorteadas (clique no centro)."""
    linhas, colunas, minas = NIVEIS[nivel]
    tab = Tabuleiro(linhas, colunas, minas, semente=SEMENTE)
    centro = tab.indice(linhas // 2, colunas // 2)
    tab.contador.zerar()
    tab._posicionar_minas(centro)
    return tab


def main():
    print("ANALISE DE COMPLEXIDADE DO CAMPO MINADO")
    print("(L = linhas, C = colunas, k = minas)")

    titulo("1) Abertura em cascata no pior caso: tabuleiro N x N sem minas")
    print(f"{'N':>4} {'celulas':>8} | {'FILA':^27} | {'PILHA':^27}")
    print(f"{'':>4} {'(N^2)':>8} | {'entradas':>8} {'vizinhos':>9} {'tam.max':>8} |"
          f" {'entradas':>8} {'vizinhos':>9} {'tam.max':>8}")
    for n in (10, 20, 40, 80):
        linha = f"{n:>4} {n * n:>8} |"
        for estrategia in ("fila", "pilha"):
            c = abrir_tabuleiro_vazio(n, estrategia)
            linha += (f" {c.valor('entradas_estrutura'):>8} {c.valor('vizinhos_examinados'):>9}"
                      f" {c.valor('tamanho_max_estrutura'):>8} |")
        print(linha.rstrip(" |"))
    print("Cada celula entra UMA vez na estrutura: o trabalho cresce como L*C.")
    print("Dobrar N quadruplica as celulas -> quadruplica as operacoes: Theta(L*C).")

    titulo("2) Marcar ao COLOCAR na fila x marcar ao RETIRAR da fila")
    print(f"{'N':>4} {'celulas':>8} {'marcando ao colocar':>21} {'marcando ao retirar':>21}")
    for n in (10, 20, 40):
        certa = abrir_tabuleiro_vazio(n, "fila").valor("entradas_estrutura")
        errada = abrir_marcando_ao_retirar(n)
        print(f"{n:>4} {n * n:>8} {certa:>21} {errada:>21}")
    print("Marcando so ao retirar, cada celula entra na fila varias vezes.")

    titulo("3) Calculo dos numeros: percorrer as minas x perguntar a cada celula")
    print(f"{'nivel':>8} {'L x C':>7} {'k':>4} {'percorrendo minas':>18} {'perguntando':>12}"
          f" {'mesmo resultado?':>17}")
    for nivel in NIVEIS:
        tab = tabuleiro_sorteado(nivel)
        copia = Tabuleiro(tab.linhas, tab.colunas, tab.num_minas)
        copia.definir_minas(tab.minas.valores())
        copia.numeros = [0] * copia.total_celulas   # recalcula do zero, medindo
        copia.contador.zerar()
        copia._calcular_numeros()
        rapido = copia.contador.valor("vizinhos_examinados")
        numeros, lento = numeros_perguntando_a_cada_celula(tab)
        iguais = "sim" if numeros == copia.numeros else "NAO"
        print(f"{nivel:>8} {tab.linhas:>3}x{tab.colunas:<3} {tab.num_minas:>4} {rapido:>18}"
              f" {lento:>12} {iguais:>17}")
    print("Percorrendo as minas: no maximo 8 passos por mina -> O(k).")
    print("Perguntando a cada celula: ate 8*L*C consultas de custo O(k) -> O(L*C*k).")

    titulo("4) Sorteio das minas com o Conjunto (sem repeticao)")
    print(f"{'nivel':>8} {'k':>4} {'sorteios':>9} {'comparacoes no Conjunto':>24} {'k^2/2':>7}")
    for nivel in NIVEIS:
        tab = tabuleiro_sorteado(nivel)
        k = tab.num_minas
        print(f"{nivel:>8} {k:>4} {tab.contador.valor('sorteios'):>9}"
              f" {tab.contador.valor('comparacoes_conjunto'):>24} {k * k // 2:>7}")
    print("Cada insercao consulta o Conjunto de minas (O(k)): para k grande, o total")
    print("cresce como k^2/2. Para k pequeno, pesam mais as consultas as celulas")
    print("protegidas do primeiro clique (ate 9 comparacoes por sorteio).")

    titulo("5) Fila x Pilha: as mesmas celulas, em ordens diferentes")
    tab_fila = Tabuleiro(*NIVEIS["dificil"], semente=SEMENTE)
    tab_pilha = Tabuleiro(*NIVEIS["dificil"], semente=SEMENTE)
    tab_pilha.estrategia = "pilha"
    ordem_fila = tab_fila.revelar(8, 15)
    ordem_pilha = tab_pilha.revelar(8, 15)
    print(f"celulas abertas com Fila:  {len(ordem_fila)}")
    print(f"celulas abertas com Pilha: {len(ordem_pilha)}")
    print(f"mesmo conjunto de celulas? {'sim' if sorted(ordem_fila) == sorted(ordem_pilha) else 'NAO'}")
    print(f"mesma ordem?               {'sim' if ordem_fila == ordem_pilha else 'nao'}")
    print(f"primeiras 8 (Fila):  {ordem_fila[:8]}")
    print(f"primeiras 8 (Pilha): {ordem_pilha[:8]}")

    titulo("6) Verificar a vitoria: varrer o tabuleiro x manter um contador")
    print(f"{'nivel':>8} {'varrendo (por jogada)':>22} {'com contador':>13}")
    for nivel, (linhas, colunas, _) in NIVEIS.items():
        print(f"{nivel:>8} {linhas * colunas:>22} {1:>13}")
    print("O contador de celulas seguras restantes responde em O(1).")


if __name__ == "__main__":
    try:
        main()
    except NotImplementedError as erro:
        print(f"\nFalta implementar: {erro}")
        print("Complete os TODOs de tabuleiro.py antes de rodar a analise.")
