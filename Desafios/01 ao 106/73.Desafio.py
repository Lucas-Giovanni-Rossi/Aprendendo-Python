#  Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
"""a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense."""

tabela = (
    'Palmeiras',
    'Flamengo',
    'Atlético-MG',
    'Grêmio',
    'Botafogo',
    'RB Bragantino',
    'Fluminense',
    'Athletico-PR',
    'Internacional',
    'Chapecoense',
    'São Paulo',
    'Cuiabá',
    'Corinthians',
    'Cruzeiro',
    'Santos',
    'Vasco',
    'Bahia',
    'Goiás',
    'Coritiba',
    'América-MG',
)

print(f'Ordem de colocação times: {tabela}')
print('~=' * 50)
print(f'Os primeiros time são: {tabela[:5]}')
print('~=' * 50)
print(f'Os ultimos 4 colocados são: {tabela[-4:]}')
print('~=' * 50)
print(f'Ordem alfabetica: {sorted(tabela)}')
print('~=' * 50)
print(f'O time de Chapecoense esta na {tabela.index("Chapecoense") + 1}º posição ')
