# Achar posições da letra A inicial e final

frase = input('Digite uma frase: ').upper().strip()

x = frase.count('A')
a1 = frase.find('A')+1
a2 = frase.rfind('A')+1


print('A letra "a" aparece {} vezes.\nA primeira letra "a" aparece na posição: {}\n' \
'a última letra "a" aparece na posicão: {}'.format(x,a1,a2))