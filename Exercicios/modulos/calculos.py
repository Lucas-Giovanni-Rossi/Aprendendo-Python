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
    return fatorial


def media(numero):
    media = sum(numero) / len(numero)
    return media
