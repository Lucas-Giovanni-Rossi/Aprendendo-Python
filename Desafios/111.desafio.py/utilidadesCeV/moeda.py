def aumentar(preço=0, taxa=0, formate=False):
    res = preço + (preço * taxa / 100)
    return res if formate is False else moeda(res)


def diminuir(preço=0, taxa=0, formate=False):
    res = preço - (preço * taxa / 100)
    return res if formate is False else moeda(res)


def metade(preço=0, formate=False):
    res = preço / 2
    return res if formate is False else moeda(res)


def dobro(preço=0, formate=False):
    res = preço * 2
    return res if formate is False else moeda(res)


def moeda(preço=0, moeda='R$', formate=False):
    resp = f'{moeda}{preço:.2f}'
    if moeda == 'R$':
        resp = resp.replace('.', ',')
    return resp


def resumo(preço=0, taxa1=0, taxa2=0):
    print('=' * 40)
    print(f'{"RESUMO DO VALOR":^40}')
    print('=' * 40)
    print(f'{"Preço analisado:"}\t\t{moeda(preço)}')
    print(f'{"Dobro do preço:"}\t\t\t{dobro(preço, True)}')
    print(f'{"Metade do preço:"}\t\t{metade(preço, True)}')
    print(f'{f"Aumento de {taxa1}%:"}\t\t\t{aumentar(preço, taxa1, True)}')
    print(f'{f"Dimnuição de {taxa2}%"}\t\t\t{diminuir(preço, taxa2, True)}')
    print('=' * 40)
