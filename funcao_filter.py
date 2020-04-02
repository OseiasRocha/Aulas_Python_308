def pares(num):
    return num % 2 == 0


lista = [1, 2, 3, 4, 5, 6]

lista_pares = list(filter(pares, lista))
print(lista_pares)
