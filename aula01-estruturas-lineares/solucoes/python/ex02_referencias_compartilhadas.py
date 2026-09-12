"""
ex02_referencias_compartilhadas.py — solução
"""

original = [1, 2, 3]

# 1. mesma_lista aponta para o MESMO objeto que original
mesma_lista = original
print(f"mesma_lista is original: {mesma_lista is original}")  # True

# 2. copia é um objeto NOVO, com os mesmos valores
copia = original.copy()
print(f"copia is original: {copia is original}")  # False

# 3. modificar mesma_lista também altera original, porque são o
#    mesmo objeto na memória — não existem duas listas aqui, só um
#    objeto com dois nomes apontando para ele.
mesma_lista.append(4)
print(f"original apos mesma_lista.append(4): {original}")  # [1, 2, 3, 4]

# 4. modificar copia NÃO afeta original, porque copy() criou um
#    objeto totalmente separado.
copia.append(999)
print(f"original apos copia.append(999): {original}")  # continua [1, 2, 3, 4]
print(f"copia: {copia}")  # [1, 2, 3, 4, 999]
