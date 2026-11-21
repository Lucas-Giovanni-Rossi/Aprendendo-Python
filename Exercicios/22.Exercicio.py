# Modularização
# Criando proprias bibliotecas

from modulos import calculos  # Importe calculo do pacote modulos

num = int(input('Digite um valor para fatoral: '))
fat = calculos.fatorial(num)
teste = [1, 2, 3, 10, 5]

print(f'O fatorial de {num} é igual a {fat}')
print(calculos.media(teste))
