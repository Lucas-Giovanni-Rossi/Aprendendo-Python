#Dia olá para o mundo e depois pergunte para usuarios algumas informações

nome = input('Qual é o seu nome?')
print('Olá',nome,'!','Prazer em te conhecer?')

dia = input(nome + ' ,Qual dia você nasceu?')
mês = input(nome + ' ,Qual mês você nasceu?')
ano = input(nome + ' ,Qual ano você nasceu?')

print('Hm..',nome,',então você nasceu em',dia, 'de', mês, 'no ano de',ano,'certo?!')

peso = input(nome + ' ,Qual é o seu peso?')

print('Obrigado pelas informações!!')
print('Seu nome é ' + nome + ', nasceu em ' + dia + '/' + mês + '/'+ ano +' e pesa ' + peso + ' kilos, Certo?')
