dic = {1: 10, 2: 20, 3: 30, 4: 40}
tupla = (1, 2, 3, 4, 5)
lista = []

for i in range(10):
    lista.append(i)

print(lista)

lista2 = [i*3 for i in dic.values()]
print(lista2)
