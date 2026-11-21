# Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional)
# indicando se será mostrado ou não na tela o processo de cálculo do fatorial.


def fatorial(numero, show=False):
    """Função de fatoração
    Args:
        numero (int): Número a ser fatorado
        show (bool, optional): Se True, mostra a conta. Se False, mostra só o resultado.
    """
    fatorial = 1
    for i in range(numero, 0, -1):
        if show:
            print(i, end=' x ' if i > 1 else ' = ')
        fatorial *= i
    print(fatorial)


num = int(input('Digite um número para fatorar: '))
show = input('Quer mostrar a conta? [S/N] ').strip().upper()

show = True if show == 'S' else False

fatorial(num, show)
