# Conta bancaria simples
from rich import print


class ContaBancaria:
    """Classe:
    Cria conta bancaria e permite saques e depositos
    """

    def __init__(self, id, nome, saldo=0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f'Conta de {self.titular} criada com sucesso.\nNúmero de registro: {self.id}.\nSaldo: {self.saldo}')

    def __str__(self):
        return f'A conta {self.id} é de {self.titular} e tem R${self.saldo:,.2f} de saldo.'

    def depositar(self, valor):
        self.saldo += valor
        print(f'Deposito de R${valor:,.2f} autorizado na conta {self.id}')

    def sacar(self, valor):
        if valor > self.saldo:
            print(f'Saque negado por Saldo Insuficiente. Saldo atual de R${self.saldo:,.2f}')
        else:
            self.saldo -= valor
            print(f'Saque de [green]R${valor:,.2f}[/] autorizado na conta {self.id}')


c1 = ContaBancaria(10, 'Gustavo', 3000)
c1.depositar(500)
c1.sacar(10)
