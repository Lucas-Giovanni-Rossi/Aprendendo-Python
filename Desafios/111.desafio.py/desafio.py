# Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
# Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.

from utilidadesCeV import moeda

preco = int(input('Digite um preço: R$'))
taxa1 = int(input('Qual a taxa de aumento? '))
taxa2 = int(input('Qual a taxa de diminuição? '))

moeda.resumo(preco, taxa1, taxa2)
