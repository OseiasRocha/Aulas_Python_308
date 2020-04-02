import copy

dic = {'nome': 'Oseias', 'idade': 24, 'sexo': 'M'}

for key, value in dic.items():
    print(f'A chave {key} contém o valor {value}')

dic.update({3: 12323.12312})

print(dic)
dic.pop('sexo')
print(dic)
dic2 = copy.deepcopy(dic)
dic.update({5: 10})
print(dic2)
