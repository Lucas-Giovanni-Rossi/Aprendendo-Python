# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.


def voto(nascimento):
    from datetime import date  # Escopo de importação // economiza memoria

    ano_atual = date.today().year
    idade = ano_atual - nascimento
    print(f'Com {idade} anos o voto é ', end='')

    if idade < 16:
        print('NEGADO.')
    elif 16 <= idade < 18 or idade > 65:
        print('OPCIONAL.')
    else:
        print('OBRIGATÓRIO.')


print('-' * 30)
voto(int(input('Qual o ano de nascimento? ')))
