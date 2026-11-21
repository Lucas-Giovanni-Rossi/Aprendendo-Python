# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

qtd = int(input('Quantos alunos deseja cadastrar: '))

temp = []
alunos = []

total = 1
while total <= qtd:
    print('~' * 10, f'{total}º aluno', '~' * 10)
    temp.append(input('Nome: ').strip().capitalize())
    temp.append(float(input('A1: ')))
    temp.append(float(input('A2: ')))
    alunos.append(temp[:])
    temp.clear()
    total += 1

print()
print(f'{"RA":<3}{"Aluno":^15}{"Média":>4}')
print('-' * 30)

for i, l in enumerate(alunos):  # noqa: E741
    print(f'{i + 1:<3}{l[0]:^15}{((l[1] + l[2]) / 2):>4.1f}')
print('-' * 30)

while True:
    RA = int(input('Digite o RA para mais informações ou "000" para encerrar: '))

    if RA < 0 or RA > len(alunos):
        print('RA inválido! Tente novamente.')
        print('~' * 30)
        continue

    if RA == 0:
        break

    RA -= 1
    print('~' * 30)
    print(f'Nome: {alunos[RA][0]}')
    print(f'Nota da A1: {alunos[RA][1]}')
    print(f'Nota da A2: {alunos[RA][2]}')
    print(f'Média Final: {(alunos[RA][1] + alunos[RA][2]) / 2}')
