# Evolução do desafio DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.


print('=-' * 10, ' Este programa lê termos de uma PA ', '=-' * 10)

# Loop para reiniciar a PA
while True:
    termo = int(input('PRIMEIRO TERMO: '))
    razao = int(input('RAZÃO: '))

    qtd = 10
    contador = 0

    # Loop para inserir mais termos
    while qtd != 0:
        # Lopp para calcular a PA
        while contador < qtd:
            contador += 1
            print(termo, end=' = PAUSA' if contador == qtd else ' → ')
            termo += razao
        mais = int(input('\nQuantos termos deseja a mais? '))

        if mais != 0:
            qtd += mais
        else:
            qtd = 0
            print(f'\nProgressão finalizada com {contador} termos mostrados. ')

    continuar = input('\nDigite qualquer teclar para ler uma nova PA ou "Sair" para encerrar. ').strip().upper()

    print('-=' * 30, '\n')

    # Encerro o loop
    if continuar == 'SAIR':
        break

print('Fim do programa. Volte sempre!')
