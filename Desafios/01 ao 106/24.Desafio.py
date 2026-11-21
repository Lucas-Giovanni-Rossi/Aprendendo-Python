# Ler nome da cidade e ler se começa ou não com "SANTO"

c = input('Digite o nome da sua cidade: ')

# Primeiro ele sapara as palavras fazendo um lista (retirando espaços), separa apenas 1º palavra
# Coloca tudo em maiusculo e depois verifica se é 'SANTO'

cidade = 'SANTO' in c.upper().split()[0]

print(cidade)