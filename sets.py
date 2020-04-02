lista = [1, 2, 5, 4, 8, 2, 8, 8, 6, 2, 7, 8, 6, 2, 8]
conjunto = set(lista)
print(conjunto)
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {1, 2, 7}

uniao = conjunto1.union(conjunto2)
print(uniao)

diferenca = conjunto1.difference(conjunto2)
diferenca2 = conjunto2.difference(conjunto1)
print(diferenca2)
