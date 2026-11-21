# Conceito de LISTAS
numeros = [3, 7, 12, 25, 8, 19, 42, 5, 30, 16, 4]  # listas são mutaveis
print('Inicio do teste: ', numeros)
print()

numeros[2] = 3  # trocar um item por outro
print('Trocar um valor: ', numeros)
print()

numeros.append(7)  # adiionar um novo valor
print('Adicionar um valor: ', numeros)
print()

numeros.insert(2, 0)  # inserir valores em posição, no caso insera na posição 2 o valor 0
print('Inserir um valor em posição especifica: ', numeros)
print()

numeros.pop(2)  # Elimina um valor na posição indicada (se não tiver nada é o ultimo)
print('Elimina valor na posição indicada: ', numeros)
print()

if 4 in numeros:  # combinar remover apenas se tiver o numero na lista
    numeros.remove(4)  # Procura o primeiro valor indicadp e elimina
    print('Remove valor o primeiro valor indicado: ', numeros)
    print()

numeros.sort()  # ordenar do menor ao maior
print('Crescente:', numeros)
print()

numeros.sort(reverse=True)  # inverter a ordenação
print('Decrescente', numeros)
print()

print(f'Esta lista tem {len(numeros)} itens.')  # teste com len
print()


print('Teste de Lista adicionando: ')
valores = []
valores.append(1)
valores.append(7)
valores.append(45)
for c, v in enumerate(valores):  # enumerate encontra posição de valores
    print(f'Na posição {c} encontrei o valor {v}.')
