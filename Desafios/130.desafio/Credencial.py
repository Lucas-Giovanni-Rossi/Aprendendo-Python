from hashlib import sha256

from rich import print


class Credencial:
    def __init__(self):
        self.__hash = None

    @property
    def senha(self):
        return self.__hash

    @senha.setter
    def senha(self, chave):
        # Aceita apenas letras, apenas números ou ambos (sem vazio, espaços ou símbolos)
        if not chave or not chave.isalnum():
            raise ValueError('[red]Senha inválida. Use apenas letras, números ou ambos.[/]')

        self.__hash = sha256(chave.encode('utf-8')).hexdigest()

    def validar(self, chave):
        usuario = sha256(chave.encode('utf-8')).hexdigest()
        if usuario == self.__hash:
            print('Senha confere.')
            return True
        else:
            print('[red]Senha errada![/]')
            return False


c = Credencial()

try:
    c.senha = input('Digite sua senha: ').strip()
except Exception as e:
    print(f'{e}')

print(f'Minha senha codificado é:\n[green]{c}[/]')

c.validar('1234')
