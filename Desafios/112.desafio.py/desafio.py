# Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado.
# Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(),
# mas com uma validação de dados para aceitar apenas valores que seja monetários.

from utilidades import dado, moeda

preco = dado.leiadinheiro('Digite um preço: R$')
taxa1 = dado.leiadinheiro('Qual a taxa de aumento? ')
taxa2 = dado.leiadinheiro('Qual a taxa de diminuição? ')

moeda.resumo(preco, taxa1, taxa2)
