lista = [3, 13, 5, 7, 7, 9]
lista_pares = list(map(lambda num: num % 2 == 0, lista))
# if all(lista_pares):
#     print('Todos são pares')
# else:
#     print('Alguns não são pares')
#     print('Adicionando 1 aos ímpares')
#     lista = [i+1 if i % 2 != 0 else i for i in lista]
#     print(lista)
print(lista_pares)
if any(lista_pares):
    print('Pelo menos um é par')
else:
    print('Nenhum é par')
