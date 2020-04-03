def preenche_lista(lista):
    for i in range(1000000000000000000000000000000000000000000):
        lista.append(i)
    return lista


def preenche_lista_gerador():
    for i in range(1000000000000000000000000000000000000000000):
        yield i


lista = []
# preenche_lista(lista)
print(lista)

lista2 = []
a = preenche_lista_gerador()
for i in a:
    print(i)
