from rich import print


class Diario:
    def __init__(self, senha='1234'):
        self.__segredos = []
        self.__senha = senha.strip()

    def escrever(self, msg):
        if isinstance(msg, str) and len(msg) > 0:
            self.__segredos.append(msg.strip())

    def ler(self, senha=None):
        if senha != self.__senha:
            raise PermissionError('Senha inválida!.')
        else:
            print('[green]Diário Liberado[/]')
            for secret in self.__segredos:
                print(f'- {secret}')

    @property
    def senha(self):
        raise PermissionError('Ninguém tem acesso para ver a senha.')

    @senha.setter
    def senha(self, novasenha):
        self.__senha = novasenha
