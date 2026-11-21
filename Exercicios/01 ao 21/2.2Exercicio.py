#Tipo primitivos

n = float(input('Digite um número:'))
print(n)
print(type(n))

#Se ter valor True e se nçao tem é False
n1 = bool(input('Digite (ou não) algo no teclado aleatoriamente:'))
print(n1)
print(type(n1))

#Número inteiro
n2 = int(input('Digite um número inteiro:'))
print(n2)
print(type(n2))

#texto ( mas neste caso pode ficar sem a função str)
n3 = str(input('Digite algo no teclado aleatoriamente:'))
print(n3)
print(type(n3))
print(n3.isalpha())