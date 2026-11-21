# Funções parte 2

# Interactive Help em Python,
"Parar o Interactive Help criei um atahlo com CTR+H+P e abre o terminal interativo, após isso digite help()"

# help(print) = # Tambem da para pedir ajuda deste jeito
print('-' * 30)


# Docstrings
def cont(i, f, p):
    """Contador na tela

    Args:
        i (int): Inicio da contagem
        f (int): final da contagem
        p (int): passos da contagem
    Teste de docstrings
    """
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('Fim!')
    return c


cont(0, 100, 10)
help(cont)


# Parametros opcionais e retorno de resultados
def somar(a=0, b=0, c=0):  # opcionais de "0 a 3" neste caso
    s = a + b + c
    return s  # retornar um valor


um = somar(3, 4.5)  # aplica na variavel
dois = somar(3, 4)
tres = somar(3)
quatro = somar()

print(f'Soma 1 = {um}\nSoma 2 = {dois}\nSoma 3 = {tres}\nSoma 4 = {quatro}')  # injeta em um print personalizado por exemplo
print()


# Escopo de variáveis
def teste():
    global x  # com isso o local deixa de existir e so coonsidera o global assim que for chamado a função
    x = 1  # Variavel local
    n = 10  # Variavel local
    print(f'Na função teste "N" vale {n}')
    print(f'Na função teste "X" vale {x}')


n = 2  # Variavel global
x = 8  # Variavel global
teste()
print(f'\nNo programa principal "N" vale {n}')
print(f'Na programa principal teste "X" vale {x}')
