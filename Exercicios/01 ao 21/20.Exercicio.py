# Funções em Python (Criação)

# Adapatada a um parametro
def titulo(txt):  # Def é criação de uma função usado para rotinas dentro do programa principal
    print('-=' * 30)
    print(txt)
    print('-=' * 30)


# Programa principal
titulo('Qualquer  coisa.')
titulo('Aprenda python')


# Testes
def soma(a, b):  # sem um parametro
    print(f'A = {a}, B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')


# Não pode ter menos que 2 ou mais que 2 parametros se não da erro
soma(4, 5)
soma(b=5, a=4)


def s(*valores):  # Empacotamento de paramentro
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} é igual a: {s}')


# Não pode ter menos que 2 ou mais que 2 parametros se não da erro
s(4, 5)
s(1, 10, 5, 6)


def contador(*num):  # Empacotar parametros
    tam = len(num)
    print(f'Recebi os valores em {num} e são ao todo {tam} números.')


contador(4, 5, 4, 0, 5)
contador(1, 10)
contador(0)


def dobra(lst):  # Usando listas
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 8, 5, 1, 2, 6, 7]
print(valores)  # Original
dobra(valores)  # Dobrou
print(valores)
dobra(valores)  # Dobrou
print(valores)
