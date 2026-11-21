# A pessoa tem 'SILVA' no nome

nome = input('Digite seu nome completo: ')

#faz uma lista, transforma em maiusculo e verifica se alguma é 'SILVA'
silva = 'SILVA' in nome.upper().split()

print('Seu nome te Silva? ',silva)