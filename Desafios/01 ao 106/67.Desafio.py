# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

print(f'{"=" * 40} TABUADA {"=" * 40}')

while True:
    numero = int(input('Quer ver a tabuada de qual valor? '))
    if numero < 0:
        break

    for tabuada in range(0, 11):
        print('{} x {:2} = {}'.format(numero, tabuada, numero * tabuada))

    print('=' * 80)

print('Programa encerrado. Volte sempre.')
