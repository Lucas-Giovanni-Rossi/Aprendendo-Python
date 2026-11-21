# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

itens_escolares = (
    ('Caderno', 15.90),
    ('Lápis', 1.50),
    ('Caneta', 2.00),
    ('Borracha', 1.20),
    ('Apontador', 2.50),
    ('Mochila', 120.00),
    ('Estojo', 35.00),
    ('Régua', 3.00),
    ('Marca-texto', 4.50),
    ('Calculadora', 45.00),
)

print('-' * 40)
print('LISTAGEM DE PREÇOS'.center(40))
print('-' * 40)
for nome, preco in itens_escolares:
    print(f'{nome:.<30}R${preco:>7.2f}')

print('-' * 40)
