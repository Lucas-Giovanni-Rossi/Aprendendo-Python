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
