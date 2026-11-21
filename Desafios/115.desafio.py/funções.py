# Vamos ver como fazer acesso a arquivos usando o Python
from os.path import dirname, join

from interfase import cabeçalho


def arquivoExiste(nome):
    caminho = join(dirname(__file__), nome)  # usei chatGPT porque tava procurando noo lugar errado.

    try:
        with open(caminho, 'r'):  # noqa: UP015
            return True
    except FileNotFoundError:
        return False


def criarArquivo(nome):
    caminho = join(dirname(__file__), nome)

    try:
        with open(caminho, 'w'):
            pass
    except Exception as erro:
        print(f'Erro ao criar arquivo: {erro}')
    else:
        print('Arquivo criado com sucesso!')


def lerArquivo(nome):
    caminho = join(dirname(__file__), nome)

    try:
        with open(caminho, 'rt') as a:  # noqa: UP015
            cabeçalho('PESSOAS CADASTRADAS')
            for linha in a:
                dado = linha.split(';')
                dado[1] = dado[1].replace('\n', '')
                print(f'{dado[0]:<33}{dado[1]:>3} anos')
    except Exception as erro:
        print(f'Erro ao ler arquivo: {erro}')


def newcadastro(arq, nome, idade):
    caminho = join(dirname(__file__), arq)

    try:
        with open(caminho, 'at') as a:  # noqa: UP015
            a.write(f'{nome};{idade}\n')
    except Exception as erro:
        print(f'Erro ao abrir arquivo : {erro}')
