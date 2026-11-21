# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e
# o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
"""considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1."""

print('~' * 50)
print('CAIXA ELETRÔNICO 24 HORAS'.center(50))
print('~' * 50)

sacar = int(input('Qual valor deseja sacar: R$'))
total = sacar
totalced50 = 0
totalced20 = 0
totalced10 = 0
totalced1 = 0
ced50 = 50
ced20 = 20
ced10 = 10
ced1 = 1

while True:
    if total >= ced50 and totalced50 <= 100:  # limitei a 50 cedulas pois tava chato qualquer valor a ced de 50 comia tudo.
        total -= ced50
        totalced50 += 1
    elif total >= ced20:
        total -= ced20
        totalced20 += 1
    elif total >= ced10:
        total -= ced10
        totalced10 += 1
    elif total >= ced1:
        total -= ced1
        totalced1 += 1

    if total == 0:
        break

print('~' * 50)

if totalced50 != 0:
    print(f'Você ira sacar {totalced50} cedulas de R$50,00')
if totalced20 != 0:
    print(f'Você ira sacar {totalced20} cedulas de R$20,00')
if totalced10 != 0:
    print(f'Você ira sacar {totalced10} cedulas de R$10,00')
if totalced1 != 0:
    print(f'Você ira sacar {totalced1} cedulas de R$1,00')

print('\nTenha um bom dia! Volte sempre!')
