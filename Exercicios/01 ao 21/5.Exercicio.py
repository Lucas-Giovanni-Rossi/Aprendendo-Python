#Manipulando cadeias de texto

frase = '   Aprenda Python com o curso   '

#alguns testes
print(frase[3]) # uma letra
print(frase[3:13]) # um intervalo
print(frase[:13]) # Intervalo sem falar o inicio
print(frase[3:]) # intervalo sem o final
print(frase[2::3],'\n') # intervalo pulando 3 letras

#testes de informação
print(len(frase)) # conta quantos caracteres tem na frase
print(frase.count('o')) # conta quantas letras "o" tem na frase
print(frase.count('o',5,21)) # conta quantas letras "o" tem dentro de um intervalo da frase
print(frase.find('deo')) # em que momento começou 'deo'
print(frase.find('android'),'\n') # teste de caso não existe a str

#testes de tru ou false
print('Curso' in frase) # há palavra 'curso' na frase?
print('Android' in frase,'\n') # há palavra 'Android' na frase?


#testes de tranformação
print(frase.replace('Python','Android')) #substituição de valor
print(frase.upper()) # tudo maiusculo
print(frase.lower()) # tudo em minusculo
print(frase.capitalize()) # só o 1 caractere em maisculo e resto minusculo
print(frase.title()) # coloca em maisculo 1 letra de cada palavra e demais minusculo
print(frase.strip()) # remove todos espaços inuteis
print(frase.lstrip()) # remove so os espaços da esquerda
print(frase.rstrip()) # remove do os espaços da direira
print(len(frase.strip()),'\n') # remove todos espaços inuteis e depois contas os caracteres sem os espaços

#testes de divisão
print(frase.split())  
dividido = frase.split()  
print(dividido[0])

#teste de junção após dividir
juntar = frase.split()
print('-'.join(juntar))

#teste de print grande com 3 """"
print("""\nA tecnologia faz parte do nosso dia a dia e muda a forma como vivemos e nos comunicamos.
Com apenas alguns cliques, podemos acessar informações de qualquer lugar do mundo.
Isso facilita o aprendizado, o trabalho e até o entretenimento.
No entanto, também é importante usar a tecnologia com equilíbrio e responsabilidade.
Assim, conseguimos aproveitar seus benefícios sem deixar de valorizar a vida fora das telas. 📱🌍""")