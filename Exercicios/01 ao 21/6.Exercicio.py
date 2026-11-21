# Condição (Parte 1) - Simples e Composta

tempo = int(input('Quantos anos tem seu carro? '))

if tempo <= 3:
    print('\nVocê tem um carro novo!')
else:
    print('Você tem um carro mais usado...')
print('=====FIM=====\n')

#simplificado:

print('Carro novo' if tempo<=3 else 'Carro velho')
print('=====FIM=====\n')

# ===============================================================

nome = input('Qual seu nome? ').upper().strip()

if nome == 'GUSTAVO':
    print('Que nome feio você tem...')
else:
    print('Que nome lindo você tem!')
print('Bom dia {}!'.format(nome))
