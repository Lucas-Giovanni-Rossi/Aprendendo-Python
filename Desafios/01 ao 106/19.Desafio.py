#Professor sortear entre 4 alunos para apagar um quadro

import random

a1 = input("Nome do 1º aluno: ")
a2 = input("Nome do 2º aluno: ")
a3 = input("Nome do 3º aluno: ")
a4 = input("Nome do 4º aluno: ")

lista = [a1,a2,a3,a4]

n1 = random.choice(lista)

print('\nO escolhido foi: ',n1)

