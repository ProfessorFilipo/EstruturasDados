"""
testes.py

Estruturas de Dados — Aula 4 — Atividade prática: Campo Minado
Este arquivo já vem pronto: você não precisa alterá-lo.

Testes automáticos: use para conferir sozinho o seu código.
    python -m unittest -v testes.py        (ou simplesmente: python testes.py)

Cada grupo de testes indica o(s) TODO(s) que ele verifica. No começo,
com o esqueleto, quase todos falham com "NotImplementedError: TODO ...".
Conforme você completa os TODOs, eles passam a dar "ok".

O tabuleiro 5 x 5 usado aqui é o mesmo da Parte A do enunciado.
"""
import os
import tempfile
import unittest

from estruturas import Conjunto, ContadorOperacoes, Fila, Pilha
from ranking import Ranking, inserir_ordenado, ordenar_por_insercao
from tabuleiro import (BANDEIRA, DERROTA, EXPLODIU, JOGANDO, MINA, NIVEIS,
                       OCULTA, VITORIA, Tabuleiro)

# Tabuleiro da Parte A: 5 x 5, minas nas posições (linha, coluna), a
# partir de 1: (1, 4), (2, 2) e (4, 5)  ->  índices 3, 6 e 19.
MINAS_PARTE_A = [3, 6, 19]
NUMEROS_PARTE_A = [
    1, 1, 2, None, 1,
    1, None, 2, 1, 1,
    1, 1, 1, 1, 1,
    0, 0, 0, 1, None,
    0, 0, 0, 1, 1,
]
# Clique na linha 5, coluna 1 (índice 20): ordem em que as células saem
ORDEM_FILA_PARTE_A = [20, 15, 16, 21, 10, 11, 12, 17, 22, 13, 18, 23]
ORDEM_PILHA_PARTE_A = [20, 21, 22, 23, 18, 17, 13, 12, 11, 16, 10, 15]


def tabuleiro_parte_a(estrategia="fila"):
    tab = Tabuleiro(5, 5, 3)
    tab.estrategia = estrategia
    tab.definir_minas(MINAS_PARTE_A)
    return tab


class TestEstruturas(unittest.TestCase):
    """estruturas.py (já pronto — são as estruturas das Aulas 2 e 3)."""

    def test_pilha_lifo_e_limites(self):
        p = Pilha(capacidade=2)
        p.empilhar(10)
        p.empilhar(20)
        self.assertTrue(p.esta_cheia())
        with self.assertRaises(OverflowError):
            p.empilhar(30)
        self.assertEqual(p.valores_do_topo_para_base(), [20, 10])
        self.assertEqual(p.desempilhar(), 20)
        self.assertEqual(p.desempilhar(), 10)
        with self.assertRaises(IndexError):
            p.desempilhar()

    def test_fila_fifo_e_ultimo_no(self):
        f = Fila()
        for v in (101, 102, 103):
            f.enfileirar(v)
        self.assertEqual(f.valores(), [101, 102, 103])
        self.assertEqual([f.desenfileirar() for _ in range(3)], [101, 102, 103])
        self.assertIsNone(f.inicio)
        self.assertIsNone(f.fim)
        with self.assertRaises(IndexError):
            f.desenfileirar()

    def test_conjunto_sem_duplicatas_e_contagem(self):
        contador = ContadorOperacoes()
        c = Conjunto(contador)
        self.assertTrue(c.inserir(5))
        self.assertFalse(c.inserir(5))             # não duplica
        c.inserir(7)
        self.assertEqual(sorted(c.valores()), [5, 7])
        contador.zerar()
        self.assertFalse(c.pertence(99))
        self.assertEqual(contador.valor("comparacoes_conjunto"), 2)  # olhou os 2 elementos
        self.assertTrue(c.remover(5))
        self.assertFalse(c.remover(5))
        self.assertEqual(c.valores(), [7])


class TestEnderecamento(unittest.TestCase):
    """TODOs 1, 2 e 3: indice(), coordenadas() e vizinhos()."""

    def test_indice(self):
        tab = Tabuleiro(4, 7, 1)
        self.assertEqual(tab.indice(0, 0), 0)
        self.assertEqual(tab.indice(0, 6), 6)
        self.assertEqual(tab.indice(1, 0), 7)
        self.assertEqual(tab.indice(3, 6), 27)

    def test_coordenadas_e_ida_e_volta(self):
        tab = Tabuleiro(4, 7, 1)
        self.assertEqual(tab.coordenadas(7), (1, 0))
        for i in range(tab.total_celulas):
            self.assertEqual(tab.indice(*tab.coordenadas(i)), i)

    def test_parte_a_conversoes(self):
        tab = Tabuleiro(5, 5, 3)
        self.assertEqual(tab.indice(3, 4), 19)       # (4, 5) contando a partir de 1
        self.assertEqual(tab.coordenadas(12), (2, 2))

    def test_vizinhos_canto_borda_miolo(self):
        tab = Tabuleiro(3, 3, 1)
        self.assertEqual(tab.vizinhos(0), [1, 3, 4])                    # canto
        self.assertEqual(tab.vizinhos(1), [0, 2, 3, 4, 5])              # borda
        self.assertEqual(tab.vizinhos(4), [0, 1, 2, 3, 5, 6, 7, 8])     # miolo, na ordem de DIRECOES

    def test_vizinhos_nao_atravessam_a_borda(self):
        tab = Tabuleiro(2, 4, 1)
        self.assertEqual(tab.vizinhos(3), [2, 6, 7])   # (0, 3) nao "vaza" para (1, 0)


class TestMinasENumeros(unittest.TestCase):
    """TODOs 4 e 5: _posicionar_minas() e _calcular_numeros()."""

    def test_numeros_da_parte_a(self):
        tab = tabuleiro_parte_a()
        for i, esperado in enumerate(NUMEROS_PARTE_A):
            if esperado is not None:
                self.assertEqual(tab.numeros[i], esperado, f"celula {i}")

    def test_sorteio_sem_repeticao_e_primeiro_clique_seguro(self):
        for semente in range(30):
            tab = Tabuleiro(*NIVEIS["facil"], semente=semente)
            tab._posicionar_minas(40)                     # célula (4, 4), o centro
            minas = tab.minas.valores()
            self.assertEqual(len(minas), 10)
            self.assertEqual(len(minas), len(set(minas)))  # (set só aqui, no teste)
            protegidas = [40] + tab.vizinhos(40)
            for m in minas:
                self.assertNotIn(m, protegidas)
            self.assertTrue(tab.minas_posicionadas)

    def test_numeros_conferem_com_forca_bruta(self):
        tab = Tabuleiro(*NIVEIS["medio"], semente=7)
        tab._posicionar_minas(0)
        minas = tab.minas.valores()
        for i in range(tab.total_celulas):
            esperado = sum(1 for v in tab.vizinhos(i) if v in minas)
            self.assertEqual(tab.numeros[i], esperado)

    def test_calculo_percorre_as_minas(self):
        tab = Tabuleiro(5, 5, 3)
        tab.definir_minas(MINAS_PARTE_A)
        tab.contador.zerar()
        tab.numeros = [0] * 25
        tab._calcular_numeros()
        # minas na borda (5 vizinhas), no miolo (8) e na borda (5):
        # 18 passos, em vez de 25 celulas * 8 vizinhas
        self.assertEqual(tab.contador.valor("vizinhos_examinados"), 18)


class TestAbertura(unittest.TestCase):
    """TODOs 6 e 7: _abrir_a_partir_de() e _revelar()."""

    def test_ordem_com_fila_parte_a(self):
        tab = tabuleiro_parte_a("fila")
        self.assertEqual(tab.revelar(4, 0), ORDEM_FILA_PARTE_A)
        self.assertEqual(tab.celulas_seguras_restantes, 10)

    def test_ordem_com_pilha_parte_a(self):
        tab = tabuleiro_parte_a("pilha")
        self.assertEqual(tab.revelar(4, 0), ORDEM_PILHA_PARTE_A)

    def test_numero_abre_so_a_propria_celula(self):
        tab = tabuleiro_parte_a()
        self.assertEqual(tab.revelar(0, 0), [0])

    def test_mina_e_derrota(self):
        tab = tabuleiro_parte_a()
        self.assertEqual(tab.revelar(1, 1), [6])
        self.assertEqual(tab.estado, DERROTA)
        self.assertEqual(tab.mina_explodida, 6)
        self.assertEqual(tab.mapa_visivel()[6], EXPLODIU)
        self.assertEqual(tab.mapa_visivel()[3], MINA)
        self.assertEqual(tab.revelar(0, 0), [])          # partida encerrada

    def test_vitoria(self):
        tab = tabuleiro_parte_a()
        for i in range(25):
            if i not in MINAS_PARTE_A and not tab.reveladas[i]:
                tab.revelar(*divmod(i, 5))
        self.assertEqual(tab.estado, VITORIA)
        self.assertEqual(tab.mapa_visivel()[19], BANDEIRA)

    def test_celula_ja_aberta_ou_com_bandeira(self):
        tab = tabuleiro_parte_a()
        tab.revelar(0, 0)
        self.assertEqual(tab.revelar(0, 0), [])
        tab.alternar_bandeira(0, 1)
        self.assertEqual(tab.revelar(0, 1), [])

    def test_cascata_nao_abre_bandeiras(self):
        tab = tabuleiro_parte_a()
        tab.alternar_bandeira(4, 2)                      # índice 22, dentro da área vazia
        ordem = tab.revelar(4, 0)
        self.assertNotIn(22, ordem)
        self.assertFalse(tab.reveladas[22])

    def test_primeiro_clique_nunca_e_mina(self):
        for semente in range(100):
            tab = Tabuleiro(*NIVEIS["dificil"], semente=semente)
            tab.revelar(semente % 16, semente % 30)
            self.assertEqual(tab.estado, JOGANDO)

    def test_cada_celula_entra_uma_unica_vez(self):
        for estrategia in ("fila", "pilha"):
            tab = Tabuleiro(12, 12, 0)
            tab.estrategia = estrategia
            tab.definir_minas([])
            tab.revelar(0, 0)
            self.assertEqual(tab.contador.valor("entradas_estrutura"), 144,
                             f"com {estrategia}: marque a celula ao COLOCAR na estrutura")
            self.assertEqual(tab.estado, VITORIA)


class TestBandeirasEHistorico(unittest.TestCase):
    """TODOs 8, 9 e 10: bandeiras, desfazer e últimas jogadas."""

    def test_marcar_e_desmarcar(self):
        tab = tabuleiro_parte_a()
        self.assertTrue(tab.alternar_bandeira(0, 3))
        self.assertEqual(tab.mapa_visivel()[3], BANDEIRA)
        self.assertEqual(tab.minas_restantes(), 2)
        self.assertTrue(tab.alternar_bandeira(0, 3))
        self.assertEqual(tab.mapa_visivel()[3], OCULTA)
        self.assertEqual(tab.minas_restantes(), 3)

    def test_nao_marca_celula_aberta(self):
        tab = tabuleiro_parte_a()
        tab.revelar(0, 0)
        self.assertFalse(tab.alternar_bandeira(0, 0))

    def test_desfazer_so_bandeira_do_topo(self):
        tab = tabuleiro_parte_a()
        tab.alternar_bandeira(0, 3)
        self.assertEqual(tab.desfazer(), (0, 3))
        self.assertEqual(tab.minas_restantes(), 3)
        self.assertIsNone(tab.desfazer())                # histórico vazio
        tab.alternar_bandeira(0, 3)
        tab.revelar(0, 0)                                # agora o topo é um "revelar"
        self.assertIsNone(tab.desfazer())
        self.assertEqual(tab.minas_restantes(), 2)       # a bandeira continua lá

    def test_ultimas_jogadas_topo_primeiro(self):
        tab = tabuleiro_parte_a()
        tab.alternar_bandeira(0, 3)
        tab.revelar(0, 0)
        tab.alternar_bandeira(1, 1)
        self.assertEqual(tab.ultimas_jogadas(2),
                         [("bandeira", 1, 1), ("revelar", 0, 0)])
        self.assertEqual(len(tab.ultimas_jogadas(10)), 3)
        self.assertEqual(tab.historico.tamanho(), 3)     # consultar não remove


class TestRanking(unittest.TestCase):
    """TODOs 11 e 12: inserir_ordenado() e ordenar_por_insercao()."""

    def test_inserir_ordenado(self):
        lista = []
        self.assertEqual(inserir_ordenado(lista, (50.0, "A")), 0)
        self.assertEqual(inserir_ordenado(lista, (30.0, "B")), 0)
        self.assertEqual(inserir_ordenado(lista, (40.0, "C")), 1)
        self.assertEqual(inserir_ordenado(lista, (40.0, "D")), 2)   # empate: o antigo fica na frente
        self.assertEqual([nome for _, nome in lista], ["B", "C", "D", "A"])

    def test_ordenar_por_insercao(self):
        lista = [(9.0, "a"), (3.0, "b"), (5.0, "c"), (3.0, "d")]
        ordenar_por_insercao(lista)
        self.assertEqual(lista, [(3.0, "b"), (3.0, "d"), (5.0, "c"), (9.0, "a")])

    def test_registrar_limita_aos_melhores(self):
        r = Ranking(caminho=os.devnull, maximo=3)
        for tempo in (40, 10, 30, 20):
            r.registrar("facil", f"j{tempo}", tempo)
        self.assertEqual([t for t, _ in r.melhores("facil")], [10, 20, 30])
        self.assertIsNone(r.registrar("facil", "lento", 99))
        self.assertFalse(r.entraria("facil", 50))

    def test_salvar_e_carregar(self):
        with tempfile.TemporaryDirectory() as pasta:
            caminho = os.path.join(pasta, "ranking.txt")
            r = Ranking(caminho)
            r.registrar("medio", "Ana", 88.8)
            r.registrar("medio", "Bia; Ltda", 77.7)
            self.assertTrue(r.salvar())
            outro = Ranking(caminho)
            self.assertTrue(outro.carregar())
            self.assertEqual(outro.melhores("medio"), [(77.7, "Bia  Ltda"), (88.8, "Ana")])


if __name__ == "__main__":
    unittest.main(verbosity=2)
