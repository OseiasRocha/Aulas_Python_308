def triplica(num):
    return num * 3


string1 = 'Oi'
string2 = 'Olá'
string3 = 'Tchau'

string1, string2, string3 = tuple(map(str.lower,
                                      (string1, string2, string3)))
print(string1, string2, string3, '\n\n')

lista = [1, 2, 3, 4, 5]
lista = list(map(triplica, lista))
print(lista)
