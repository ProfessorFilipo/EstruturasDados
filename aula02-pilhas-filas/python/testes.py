import unittest

from fila import Fila
from pilha import Pilha


class TestPilha(unittest.TestCase):
    def test_lifo_e_limites(self):
        p = Pilha(capacidade=2)
        self.assertTrue(p.esta_vazia())
        p.empilhar(10)
        p.empilhar(20)
        self.assertEqual(p.consultar_topo(), 20)
        self.assertEqual(p.desempilhar(), 20)
        self.assertEqual(p.desempilhar(), 10)
        with self.assertRaises(IndexError):
            p.desempilhar()


class TestFila(unittest.TestCase):
    def test_fifo_e_ultimo_no(self):
        f = Fila()
        f.enfileirar(101)
        f.enfileirar(102)
        self.assertEqual(f.consultar_frente(), 101)
        self.assertEqual(f.desenfileirar(), 101)
        self.assertEqual(f.desenfileirar(), 102)
        self.assertIsNone(f.inicio)
        self.assertIsNone(f.fim)
        with self.assertRaises(IndexError):
            f.desenfileirar()


if __name__ == "__main__":
    unittest.main()
