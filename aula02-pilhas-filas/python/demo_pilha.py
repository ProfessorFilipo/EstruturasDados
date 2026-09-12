from pilha import Pilha


def mostrar(rotulo, pilha):
    valores = pilha.valores_do_topo_para_base()
    estado = " ".join(map(str, valores)) if valores else "[vazia]"
    print(f"{rotulo:<25} {estado}")


p = Pilha()
mostrar("0. pilha criada:", p)
p.empilhar(10)
mostrar("1. empilhar(10):", p)
p.empilhar(20)
mostrar("2. empilhar(20):", p)
print(f"3. consultar_topo():      {p.consultar_topo()} (a pilha nao muda)")
print(f"4. desempilhar():         removeu {p.desempilhar()}")
mostrar("5. estado final:", p)
