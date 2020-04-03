import time


def Log(func):
    def wraper():
        a = func()
        print(f'A função retornou: {a}')
    return wraper


def decorador(func):
    def wraper():
        print('Antes')
        tempo_inicial = time.perf_counter()
        func()
        tempo_final = time.perf_counter()
        resultado = tempo_final - tempo_inicial
        print('Depois')
        print(
            f'A função {func.__name__} foi executada em : {resultado:.3f} segundos')
    return wraper


# @decorador
@Log
def funcao():
    a = 0
    for _ in range(1000000):
        a += 1
    if a > 100:
        return False
    else:
        return True


funcao()
