# traga o tipo primitivo do que foi digitado

valor = input('Digite algo para mim:')

print('O tipo prmitivo deste valor é:',type(valor))
print('Só tem espaços?',valor.isspace())
print('É um número?',valor.isnumeric())
print('É alfabetico?',valor.isalpha())
print('É alfanumerico?',valor.isalnum())
print('Esta em letras maiusculos?',valor.isupper())
print('Esta em letras minusculas?',valor.islower())
print('Esta capitalizada?',valor.istitle())