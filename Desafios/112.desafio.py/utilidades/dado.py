def leiadinheiro(msg):
    while True:
        n = input(msg).strip().replace(',', '.')

        if n.count('.') > 1:
            print(f'❌ ERRO! <\033[31m{n}\033[m> não é um número válido.')
        else:
            if n.replace('.', '').isdigit():
                return float(n)
            else:
                print(f'❌ ERRO! <\033[31m{n}\033[m> não é um número válido.')
