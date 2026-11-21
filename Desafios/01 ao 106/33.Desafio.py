# Diga maior e menor valor

n1 = float(input('Digite o 1º número: '))
n2 = float(input('Digite o 2º número: '))
n3 = float(input('Digite o 3º número: '))

num = sorted([n1, n2, n3])  # função lista classificar do menor ao maior

print(
    '\nO maior número é: {}\nO menor número é: {}\nE o número intermédiario é igual a: {}'.format(
        num[2], num[0], num[1]
    )
)
