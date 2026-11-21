# Estruturas de repetição

contador = 0  # inicializa o contador

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Blocos por passos: '))

for c in range(i, f + 1, p):
    print(c)
    contador += 1
print('Você deu {} passos para alcançar o fim: '.format(contador))
print('Parabéns!')
