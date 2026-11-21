#Operadores Aritméticos

''' 1º : ()
    2º : **
    3º : *  /  //  %
    4º : +  - '''

n1 = int(input('Um valor inteiro:'))
n2 = int(input('segundo valor'))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
print('A soma é: {} \n' \
'A multiplicação é: {} \n' \
'A divisão é: {:.2f} \n' \
'A divisão inteira é: {} \n' \
'A potência é: {}'.format(s,m,d,di,e))
