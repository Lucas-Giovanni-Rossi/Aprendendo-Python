# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.


def titulo(msg, cor=0):
    cores = (
        '\033[m',  # 0 - sem cor
        '\033[0;30;41m',  # 1 - vermelho
        '\033[0;30;42m',  # 2 - verde
        '\033[0;30;44m',  # 3 - azul
        '\033[0;30;45m',  # 4 - roxo
    )
    tam = len(msg) + 4
    print(cores[cor] + '~' * tam)
    print(f'  {msg}  ')
    print('~' * tam + cores[0])


def ajuda(comando):
    titulo(f"Acessando o manual do comando '{comando}'", 3)
    print('\033[7m')  # modo invertido
    help(comando)
    print('\033[m')


# Programa principal
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    cmd = input('Função ou Biblioteca > ').strip()

    if cmd.upper() == 'FIM':
        titulo('ATÉ LOGO!', 1)
        break

    ajuda(cmd)
