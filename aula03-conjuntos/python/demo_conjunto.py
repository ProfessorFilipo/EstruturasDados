"""
demo_conjunto.py

Estruturas de Dados — Aula 3 — Bloco 4 (Conjuntos: implementação)

O set() nativo do Python já resolve tudo isso por baixo dos panos —
mesma sequência de operações que acabamos de ver em C.
Sem nenhum import — cole direto no onlineide.pro/playground/python
"""

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("A =", a)
print("B =", b)

print("\npertence(A, 2)  =", 2 in a)
print("pertence(A, 99) =", 99 in a)

a.add(2)  # ja existe -- nao duplica
print("\napos inserir(A, 2) de novo:", a)

a.remove(1)
print("apos remover(A, 1):        ", a)
a.add(1)  # volta ao estado original para as proximas operacoes

print("\nA uniao B      =", a | b)
print("A intersecao B =", a & b)
print("A diferenca B  =", a - b)
