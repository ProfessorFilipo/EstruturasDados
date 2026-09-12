"""
memoria_referencias.py

Estruturas de Dados — Aula 1 — Bloco 2 (Nivelamento)

Demonstra que, em Python, toda variável já se comporta como uma
referência a um objeto — não existe um "ponteiro explícito" como em C,
mas o comportamento de compartilhar o mesmo objeto é análogo.
"""

x = 42
p = x  # p recebe uma referência ao mesmo objeto que x referencia

print(f"x = {x}, p = {p}")
print(f"id(x) == id(p): {id(x) == id(p)}")

print()
print("--- com um objeto mutável (lista) o efeito fica mais visível ---")

lista = [1, 2, 3]
outra = lista  # outra referencia O MESMO objeto lista, não uma cópia

outra.append(4)
print(f"lista = {lista}")  # também foi alterada!
print(f"outra = {outra}")
print(f"lista is outra: {lista is outra}")

print()
print("--- para copiar de fato, é preciso pedir explicitamente ---")
copia = lista.copy()
copia.append(999)
print(f"lista = {lista}")
print(f"copia = {copia}")
print(f"lista is copia: {lista is copia}")
