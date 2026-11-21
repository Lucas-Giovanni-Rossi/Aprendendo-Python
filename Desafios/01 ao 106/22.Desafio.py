# ler nome completo e transformar

nome =  input('Olá, tudo bem?\nVamos fazer alguns teste com seu nome!\nQual o seu nome completo: ').strip()

print('Todas as letras maiúsculas:\n',nome.upper())
print('Todas as letras minúsculas:\n',nome.lower())

caracteres = len(nome) # conta os caracteresS
letras = len(''.join(nome.split())) # conta os caracteres mas primeiro divide para tirar todos os espacos e depois junta tudo sem espaços
nome1 = len(nome.split()[0]) # divide pega o 1 valor da lista e depois conta os caraceteres
capitalize1 = nome.split()[0].capitalize() # divide pega o primeiro valor da lista e capitalize


print('Para escrever seu nome precisa de {} caracteres, porém ele tem apenas {} letras'.format(caracteres,letras))
print('Seu primeiro nome é {} e ele tem {} letras'.format(capitalize1,nome1))

