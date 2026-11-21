#devolva 1º e ultimo nome da pessoa

nome = input('Qual o seu nome completo? ').strip()

pri = nome.split()[0].capitalize()
ult = nome.split()[-1].capitalize() #separa e o -1 faz pegar o ultimo da lista e depois capitaliza para ficar bonito

print('Seu nome completo é: {}\n' \
    'Seu primeiro nome é: {}\n' \
    'Seu ultimo nome é: {}'.format(nome.title(),pri,ult))