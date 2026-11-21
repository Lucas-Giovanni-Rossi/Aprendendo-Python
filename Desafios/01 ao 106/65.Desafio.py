# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.


qtd = int(input('Quantos números deseja digitar? '))

contador = soma = 0
lista = []

while True:
    while contador < qtd:
        contador += 1
        numero = int(input(f'Digite o {contador}º número: '))
        lista.append(numero)
        soma += numero

    continuar = input('\nDeseja digitar mais número? [S/N] ').strip().upper()[0]

    while True:
        if continuar == 'S':
            mais = int(input('Quantos números deseja digitar? '))
            qtd += mais
            break
        elif continuar == 'N':
            break
        else:
            continuar = input('Opção invalida ! Digite [S/N]: ').strip().upper()[0]

    if continuar == 'N':
        break

media = soma / qtd
print('=-' * 20)
print(f'Voce inseriu {contador} números onde a média é igual a: {media:.2f}')
lista.sort()
print(f'O menor valor inserido foi: {lista[0]}')
lista.reverse()
print(f'E o maior valor inserido foi: {lista[0]}')
