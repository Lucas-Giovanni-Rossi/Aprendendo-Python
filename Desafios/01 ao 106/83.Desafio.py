# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

"""FIZ UPGRADE COM CHATE E PROXIMO CONCEITO DA AULA 18"""

exp = input('Digite uma expressão: ')
pilha = []

pares = {')': '(', ']': '[', '}': '{'}

valida = True

for simb in exp:
    if simb in '([{':
        pilha.append(simb)
    elif simb in ')]}':
        if not pilha:
            valida = False
            break
        elif pilha[-1] == pares[simb]:
            pilha.pop()
        else:
            valida = False
            break

if valida and not pilha:
    print('Expressão válida!')
else:
    print('Expressão inválida!')
