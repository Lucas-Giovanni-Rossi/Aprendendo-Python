# Listas (PARTE 2) ´listas dentro de listas

galera = [['João', 19], ['Maria', 13], ['Ana', 24], ['Joaquim', 25]]

for p in galera:
    print(f'{p[0]} tem {p[1]} anos')


print('-=-' * 30)

galera2 = []
idade2 = []
for p in range(0, 3):
    galera2.append(input('Nome: '))
    idade2.append(int(input('Idade: ')))
    galera2.append(idade2[:])
    idade2.clear()

print(galera2)
