from time import sleep

# Importações criadas localmente
from funções import arquivoExiste, criarArquivo, lerArquivo, newcadastro
from inputs import inputint, inputnome
from interfase import cabeçalho, menu

# Verifica se o banco de dados em txt existe e se não existir cria.
arq = 'banco de dados.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    # Cabeçalho e Menu do sistema.
    cabeçalho('MENU DO SISTEMA v3.0')
    resp = menu(['Ver pessoas', 'Cadastrar nova pessoa', 'Sair do sistema'])

    # Mostra ao usurio uma tabela dos dados.
    if resp == 1:
        lerArquivo(arq)

    # Cadastrar um novo dado.
    elif resp == 2:
        cabeçalho('NOVO CADASTRO')
        nome = inputnome('Nome: ')
        idade = inputint('Idade: ')
        newcadastro(arq, nome, idade)

    # Encerrar o programa.
    elif resp == 3:
        cabeçalho('Até logo... Volte sempre!')
        break

    # Erro de opção inválida.
    else:
        print(f'❌ ERRO! <\033[31m{resp}\033[m> não é um opcção válida.')

    # Pequena espera paro o usuario ler.
    sleep(2)
