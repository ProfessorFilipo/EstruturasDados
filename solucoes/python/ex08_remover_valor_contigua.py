"""
ex08_remover_valor_contigua.py — solução

Estende o TAD ListaContigua (do repositório) com remover_valor(),
reaproveitando buscar() + remover() já existentes.
"""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "python"))

from lista_contigua import ListaContigua


def remover_valor(lista, valor):
    """Retorna True se removeu, False se o valor não existia na lista.
    Funciona para qualquer TAD Lista que implemente buscar() e
    remover() por posição — não só ListaContigua."""
    pos = lista.buscar(valor)
    if pos == -1:
        return False
    lista.remover(pos)
    return True


if __name__ == "__main__":
    l = ListaContigua()
    for v in [10, 20, 30, 20]:  # 20 repetido, de proposito
        l.inserir_fim(v)

    print(f"antes: {l}")

    removeu = remover_valor(l, 20)
    print(f"\nremover_valor(20) -> {'removeu' if removeu else 'nao encontrado'}")
    print(f"depois (so a PRIMEIRA ocorrencia de 20 deve sair): {l}")

    removeu_inexistente = remover_valor(l, 999)
    status = "removeu" if removeu_inexistente else "nao encontrado"
    print(f"\nremover_valor(999) -> {status} (esperado: nao encontrado)")
