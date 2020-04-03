import pickle
import json


class Pessoa:
    ID = 0

    def __init__(self, dados=False):
        self._nome = ''
        self._data_nascimento = ''
        self._sexo = ''
        self._lista = [1, 2, 3, 4]
        Pessoa.ID += 1
        self._ID = Pessoa.ID
        if dados:
            self.__dict__ = json.load(dados)

    @staticmethod
    def printa_id():
        print('teste', Pessoa.ID)

    def setNome(self, nome):
        self._nome = nome

    def setSexo(self, sexo):
        self._sexo = sexo

    def setDataNasc(self, data_nasc):
        self._data_nascimento = data_nasc

    def getNome(self):
        return self._nome

    def getSexo(self):
        return self._sexo

    def getDataNasc(self):
        return self._data_nascimento

    def __str__(self):
        return f'Nome: {self._nome} \nSexo: {self._sexo} \nData de Nascimento: {self._data_nascimento}'

    def __iter__(self):
        return iter(self._lista)


pessoa = Pessoa()
pessoa.setNome('Oseias')
pessoa.setSexo('m')
pessoa.setDataNasc('03/09/1995')

arq = open('arquivo_com_pickle.txt', 'wb')
pickle.dump(pessoa, arq)
arq.close()

arq = open('arquivo_json.json', 'w')
json.dump(pessoa.__dict__, arq)
arq.close()

arq = open('arquivo_json.json', 'r')
teste = Pessoa(arq)
arq.close()
print(teste, type(teste))
