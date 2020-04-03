import heranca
import copy


class Venda():
    def __init__(self):
        self.ID = 0
        self.Vendedor = heranca.Vendedor()

    def executa_venda(self, vendedor, cliente='a'):
        self.Vendedor = vendedor


if __name__ == "__main__":
    vend = heranca.Vendedor()
    vend.matricula = 100
    a = Venda()
    a.executa_venda(vend)

    print(a.Vendedor.matricula)
