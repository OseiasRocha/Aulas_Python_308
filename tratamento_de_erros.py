import io

try:
    arq = open('asndas.txt', 'a+')
    linhas = arq.readlines()
    arq.close()
    print(linhas)
except FileNotFoundError:
    print('Arquivo não encontrado')
except io.UnsupportedOperation:
    print('Operação não suportada')
finally:
    print('Finalmente')


try:
    arq = open('asndas.txt', 'w')
    arq.close()
    arq.write('Olá mundo3')
except io.UnsupportedOperation:
    print('Operação não suportada')
except ValueError:
    print('Tentou escrever em um arquivo fechado')
