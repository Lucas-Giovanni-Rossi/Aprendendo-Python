# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)


def leiaInt(msg):
    while True:
        n = input(msg).strip()
        if n.isnumeric():
            return int(n)
        else:
            print('ERRO! Digite um numero inteiro válido.')


# Principal
numero = leiaInt('Digite um número: ')
print(f'Você digitou o número {numero}.')
