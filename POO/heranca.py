from abc import ABC, abstractmethod


class Pessoa(ABC):
    @abstractmethod
    def __init__(self):
        self.nome = ''


class Vendedor(Pessoa):
    def __init__(self):
        super().__init__()
        self.matricula = 0


# b = Pessoa()
if __name__ == "__main__":
    a = Vendedor()
    print(a.__dir__())
