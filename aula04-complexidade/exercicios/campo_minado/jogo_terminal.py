"""
jogo_terminal.py

Estruturas de Dados — Aula 4 — Atividade prática: Campo Minado
Este arquivo já vem pronto: você não precisa alterá-lo.

Interface de TEXTO do Campo Minado. Funciona em qualquer terminal e
também em IDEs online, porque só usa print() e input().

Como jogar: digite um comando e tecle Enter.
    r 3 5   revela a célula da linha 3, coluna 5
    b 3 5   marca/desmarca uma bandeira na linha 3, coluna 5
    d       desfaz a última bandeira (a Pilha só deixa desfazer o topo)
    h       mostra as últimas jogadas (topo da Pilha primeiro)
    o       mostra as operações contadas na última jogada
    a       alterna a abertura em cascata entre Fila e Pilha
    ?       ajuda
    s       sai da partida

Símbolos:  # fechada   F bandeira   . vazia (0)   1-8 minas em volta
           * mina   X mina que explodiu   ! bandeira no lugar errado

Este arquivo não tem regras do jogo: ele só lê comandos, chama os
métodos do Tabuleiro e desenha o resultado.
"""
import time

from ranking import Ranking
from tabuleiro import (BANDEIRA, DERROTA, ERRO, EXPLODIU, JOGANDO, MINA,
                       NIVEIS, OCULTA, VITORIA, Tabuleiro)

SIMBOLOS = {OCULTA: "#", BANDEIRA: "F", MINA: "*", EXPLODIU: "X", ERRO: "!", 0: "."}

NOMES_NIVEIS = {"facil": "Facil", "medio": "Medio", "dificil": "Dificil"}

AJUDA = """Comandos (linha e coluna comecam em 1):
  r L C   revela a celula da linha L, coluna C      ex.: r 3 5
  b L C   marca/desmarca bandeira na linha L, coluna C
  d       desfaz a ultima bandeira
  h       mostra as ultimas jogadas (topo da pilha primeiro)
  o       mostra as operacoes contadas na ultima jogada
  a       alterna a abertura em cascata entre Fila e Pilha
  ?       mostra esta ajuda
  s       sai da partida
Simbolos: # fechada  F bandeira  . vazia  1-8 minas em volta
          * mina  X mina que explodiu  ! bandeira errada"""


def simbolo(codigo):
    """Converte o código de mapa_visivel() no caractere exibido."""
    return SIMBOLOS.get(codigo, str(codigo))


def desenhar(tab):
    """Imprime o tabuleiro com os números das linhas e das colunas."""
    mapa = tab.mapa_visivel()
    print()
    print("    " + "".join(f"{c + 1:>3}" for c in range(tab.colunas)))
    for linha in range(tab.linhas):
        # as células da linha ocupam um trecho contíguo da lista [Aula 1]
        trecho = mapa[linha * tab.colunas:(linha + 1) * tab.colunas]
        celulas = "".join(f"{simbolo(codigo):>3}" for codigo in trecho)
        print(f"{linha + 1:>3} {celulas}")
    print(f"Minas restantes: {tab.minas_restantes()}    "
          f"Abertura em cascata: {tab.estrategia.upper()}")


def ler(mensagem):
    """input() que devolve None se a entrada terminar (Ctrl+D / fim do arquivo)."""
    try:
        return input(mensagem)
    except EOFError:
        return None


def interpretar(texto, tab):
    """Converte o texto digitado em (comando, linha, coluna).
    Linha e coluna voltam já convertidas para começar em 0.
    Em caso de erro, devolve ("erro", mensagem, None)."""
    partes = texto.strip().lower().split()
    if not partes:
        return "erro", "Digite um comando (? para ajuda).", None
    comando = partes[0]
    if comando in ("d", "h", "o", "a", "?", "s"):
        return comando, None, None
    if comando in ("r", "b"):
        if len(partes) != 3 or not partes[1].isdigit() or not partes[2].isdigit():
            return "erro", f"Use: {comando} LINHA COLUNA   (ex.: {comando} 3 5)", None
        linha, coluna = int(partes[1]) - 1, int(partes[2]) - 1
        if not (0 <= linha < tab.linhas and 0 <= coluna < tab.colunas):
            return "erro", (f"Posicao fora do tabuleiro: linhas 1 a {tab.linhas}, "
                            f"colunas 1 a {tab.colunas}."), None
        return comando, linha, coluna
    return "erro", "Comando desconhecido (? para ajuda).", None


def escolher_nivel():
    print("\nEscolha o nivel:")
    opcoes = list(NIVEIS)
    for numero, nivel in enumerate(opcoes, start=1):
        linhas, colunas, minas = NIVEIS[nivel]
        print(f"  {numero}) {NOMES_NIVEIS[nivel]:<8} {linhas} x {colunas}, {minas} minas")
    while True:
        resposta = ler("Nivel (1, 2 ou 3): ")
        if resposta is None:
            return None
        if resposta.strip() in ("1", "2", "3"):
            return opcoes[int(resposta) - 1]
        print("Opcao invalida.")


def mostrar_ranking(ranking, nivel):
    recordes = ranking.melhores(nivel)
    print(f"\nRANKING - {NOMES_NIVEIS[nivel]}")
    if not recordes:
        print("  (ainda sem recordes)")
    for posicao, (tempo, nome) in enumerate(recordes, start=1):
        print(f"  {posicao:>2}. {tempo:>7.1f} s   {nome}")


def executar(comando, linha, coluna, tab):
    """Executa um comando de jogo. Devolve False se o jogador quer sair."""
    if comando == "r":
        tab.revelar(linha, coluna)
    elif comando == "b":
        if not tab.alternar_bandeira(linha, coluna):
            print("Nao da para marcar uma celula ja aberta.")
    elif comando == "d":
        desfeita = tab.desfazer()
        if desfeita is None:
            print("Nada a desfazer: so a bandeira do topo da pilha pode ser desfeita")
            print("(revelar nao tem volta).")
        else:
            print(f"Bandeira desfeita na linha {desfeita[0] + 1}, coluna {desfeita[1] + 1}.")
    elif comando == "h":
        jogadas = tab.ultimas_jogadas(5)
        print("Ultimas jogadas (a mais recente primeiro):" if jogadas else "Nenhuma jogada ainda.")
        for acao, l, c in jogadas:
            print(f"  {acao:<9} linha {l + 1}, coluna {c + 1}")
    elif comando == "o":
        print("Operacoes contadas na ultima jogada:")
        print(tab.contador.relatorio())
    elif comando == "a":
        tab.estrategia = "pilha" if tab.estrategia == "fila" else "fila"
        print(f"Abertura em cascata agora usa: {tab.estrategia.upper()}")
    elif comando == "?":
        print(AJUDA)
    elif comando == "s":
        return False
    return True


def jogar_partida(nivel, ranking):
    tab = Tabuleiro(*NIVEIS[nivel])
    print(f"\nNovo jogo: {NOMES_NIVEIS[nivel]}. Digite ? para ver os comandos.")
    inicio = None
    while tab.estado == JOGANDO:
        desenhar(tab)
        texto = ler("> ")
        if texto is None:
            return False                       # a entrada acabou
        comando, linha, coluna = interpretar(texto, tab)
        if comando == "erro":
            print(linha)                       # aqui 'linha' traz a mensagem de erro
            continue
        if comando == "r" and inicio is None:
            inicio = time.monotonic()          # o relógio começa no primeiro clique
        try:
            if not executar(comando, linha, coluna, tab):
                return True
        except NotImplementedError as erro:
            print(f"\nFalta implementar: {erro}")
            print("Complete esse TODO e rode de novo.")
            return False

    desenhar(tab)
    tempo = time.monotonic() - inicio if inicio is not None else 0.0
    if tab.estado == DERROTA:
        print(f"\nBOOM! Voce encontrou uma mina. Tempo: {tempo:.1f} s")
    elif tab.estado == VITORIA:
        print(f"\nPARABENS! Voce abriu todas as celulas seguras em {tempo:.1f} s.")
        if ranking.entraria(nivel, tempo):
            nome = ler("Seu tempo entrou no ranking! Seu nome: ")
            posicao = ranking.registrar(nivel, nome, tempo)
            if not ranking.salvar():
                print("(Nao foi possivel gravar o arquivo do ranking neste ambiente.)")
            print(f"Voce ficou em {posicao}o lugar.")
        mostrar_ranking(ranking, nivel)
    print("\nOperacoes contadas na partida inteira:")
    print(tab.contador_partida.relatorio())
    return True


def main():
    print("=== CAMPO MINADO - Estruturas de Dados, Aula 4 ===")
    ranking = Ranking()
    ranking.carregar()
    while True:
        nivel = escolher_nivel()
        if nivel is None:
            break
        if not jogar_partida(nivel, ranking):
            break
        resposta = ler("\nJogar de novo? (s/n): ")
        if resposta is None or resposta.strip().lower() != "s":
            break
    print("Ate a proxima!")


if __name__ == "__main__":
    main()
