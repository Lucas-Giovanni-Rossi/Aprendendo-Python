# Escreva um programa que leia um número N inteiro qualquer e
# mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8

print(f'{"=" * 40}\n{">>> SEQUÊNCIA DE FIBONACCI <<<".center(40)}\n{"=" * 40}')  # aprendi com chatgpt

termo = int(input('Quantos termos deseja mostrar? '))

contador = 0
n1 = 0
n2 = 1

while contador < termo:
    contador += 1
    print(n1, end=' → ' if contador != termo else ' → Fim.')
    n1, n2 = n2, n1 + n2
