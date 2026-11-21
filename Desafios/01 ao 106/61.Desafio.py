# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
# Progressão Aritmética v2.0

print('=-' * 10, ' Este programa lê os 10 primeiros termos de uma PA ', '=-' * 10)

while True:
    termo = int(input('PRIMEIRO TERMO: '))
    razao = int(input('RAZÃO: '))

    contador = 0

    while contador < 10:
        contador += 1
        print(termo, end=' = Acabou!' if contador == 10 else ' → ')
        termo += razao

    print(f'\nEsses são os {contador} primeiros termos encontrados. ')

    continuar = input('\nDigite qualque teclar para continuar ou "Sair" para encerrar. ').strip().upper()

    print('-=' * 30, '\n')

    if continuar == 'SAIR':
        break

print('Fim do programa. Volte sempre!')
