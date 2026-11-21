def inputint(msg):
    while True:
        try:
            n = input(msg).strip()
            n = int(n)
        except (ValueError, TypeError):
            print(f'❌ ERRO! <\033[31m{n}\033[m> não é um número inteiro válido.')
        except KeyboardInterrupt:
            print('\n\033[31mUsuário não digitou entrada do processo!\033[m')
            return 0
        else:
            return n


def inputfloat(msg):
    while True:
        try:
            n = input(msg).replace(',', '.').strip()
            n = float(n)
        except (ValueError, TypeError):
            print(f'❌ ERRO! <\033[31m{n}\033[m> não é um número real válido.')
        except KeyboardInterrupt:
            print('\n\033[31mUsuário não digitou entrada do processo!\033[m')
            return 0
        else:
            return n
