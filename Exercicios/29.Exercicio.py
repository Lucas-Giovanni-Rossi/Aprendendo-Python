# Aprendendo capsulamento

from rich import print


def linha():
    print('~-' * 20)


class ContaBancaria:
    """Classe:
    Cria conta bancaria e permite saques e depositos
    """

    def __init__(self, id, nome, saldo=0):
        self.id = id
        self._titular = nome
        self.__saldo = saldo
        print(f'Conta de {self._titular} criada com sucesso.\nNúmero de registro: {self.id}.\nSaldo: {self.__saldo}')

    def __str__(self):  # Dar um print
        linha()
        return f'Estado atual da conta: {self.__dict__}'

    def depositar(self, valor):
        valor = abs(valor)
        self.__saldo += valor
        linha()
        print(f'Deposito de R${valor:,.2f} autorizado na conta {self.id}')

    def sacar(self, valor):
        valor = abs(valor)
        if valor > self.__saldo:
            linha()
            print(f'Saque negado por Saldo Insuficiente. Saldo atual de R${self.__saldo:,.2f}')
        else:
            self.__saldo -= valor
            linha()
            print(f'Saque de [green]R${valor:,.2f}[/] autorizado na conta {self.id}')


c1 = ContaBancaria(111, 'Maria', 5_000)
c1.depositar(-500)
c1.sacar(-100)
c1.__saldo = 0
print(c1)
