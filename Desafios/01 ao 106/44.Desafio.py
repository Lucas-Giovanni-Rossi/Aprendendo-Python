# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

"""à vista dinheiro/cheque: 10% de desconto
à vista no cartão: 5% de desconto

em até 2x no cartão: preço formal

3x ou mais no cartão: 20% de juros"""

print('{:=^40}'.format(' Lojas Lucas '))

compra = float(input('Bom dia!!!\nInforme o valor da compra: R$'))

pagamento = int(
    input(
        """Forma de pagamento:
Há vista no dinheiro/pix : [1]
Há vista no cartão:        [2]
2x no cartão:              [3]
3x ou mais no cartão:      [4]
Qual a opção de pagamento? """
    )
)

pix = compra - compra * 0.1
cartao = compra - compra * 0.05
cartao2 = compra / 2
cartaomais = compra + compra * 0.2

if pagamento == 1:
    print('\nGANHOU UM DESCONTE DE 10% e pagará apenas R${:.2f}.'.format(pix))
elif pagamento == 2:
    print(('\nGANHOU UM DESCONTE DE 5% e pagará apenas R${:.2f}'.format(cartao)))
elif pagamento == 3:
    print('\nO clente pagará R${:.2f} por mês em 2x.\nTotal: R${:.2f}'.format(cartao2, compra))
elif pagamento == 4:
    print('\nAtenção!\nPagamentos em mais de 2x no cartão possui correção de juros.')
    vezes = int(input('informe a quantidades de parcelas? '))
    if vezes == 2:
        print('\nO clente pagará R${:.2f} por mês em 2x.\nTotal: R${:.2f}'.format(cartao2, compra))
    else:
        print(
            '\nO cliente pagará R${:.2f} por mês em {} vezes.\nTotal: R${:.2f}'.format(
                cartaomais / vezes, vezes, cartaomais
            )
        )
else:
    print('OPÇÃO INVÁLIDA. Tente novamente.')
