# Vamos criar um menu em Python, usando modularização.

from inputs import inputint


def linha(tam=42):
    return print('=' * tam)


def cabeçalho(txt):
    linha()
    print(txt.center(42))
    linha()


def menu(lista):
    c = 1
    for item in lista:
        print(f'{c} → {item}')
        c += 1
    linha()
    opc = inputint('Digite uma opção: ')
    return opc
