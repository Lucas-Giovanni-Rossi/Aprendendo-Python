# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.                                  ]
# Ex:
# escreva(‘Olá, Mundo!’) Saída:
# ~~~~~~~~~
# Olá, Mundo!
# ~~~~~~~~~
def escreva(msg):
    tam = len(msg) + 6
    print('~' * tam)
    print(msg.center(tam))
    print('~' * tam)


escreva('Lucas Rossi')
escreva('Aprendendo Python')
escreva('Eu você e o zubumafuuuu uuu!')
escreva('Olá Mundo !!! To de volta')
