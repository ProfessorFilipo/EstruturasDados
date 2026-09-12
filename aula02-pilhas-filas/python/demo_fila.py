from fila import Fila


def mostrar(rotulo, fila):
    valores = fila.valores()
    estado = " ".join(map(str, valores)) if valores else "[vazia]"
    print(f"{rotulo:<25} {estado}")


f = Fila()
mostrar("0. fila criada:", f)
f.enfileirar(101)
mostrar("1. enfileirar(101):", f)
f.enfileirar(102)
mostrar("2. enfileirar(102):", f)
f.enfileirar(103)
mostrar("3. enfileirar(103):", f)
print(f"4. consultar_frente():    {f.consultar_frente()} (a fila nao muda)")
print(f"5. desenfileirar():       removeu {f.desenfileirar()}")
mostrar("6. estado final:", f)
