from fila import Fila
from pilha import Pilha


def processar_proximo(espera, historico):
    if espera.esta_vazia():
        return False
    trabalho = espera.desenfileirar()
    historico.empilhar(trabalho)
    print(f"Trabalho processado: {trabalho}")
    return True


espera = Fila()
historico = Pilha()

for trabalho in (101, 102, 103):
    espera.enfileirar(trabalho)

processar_proximo(espera, historico)
processar_proximo(espera, historico)
espera.enfileirar(104)

print("Fila de espera:", *espera.valores())
print("Historico - topo para base:", *historico.valores_do_topo_para_base())
print("Proximo trabalho:", espera.consultar_frente())
print("Ultimo trabalho processado:", historico.consultar_topo())
