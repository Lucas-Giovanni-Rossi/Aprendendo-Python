# Dicionários

pessoas = {'nome': 'Lucas', 'idade': '21', 'sexo': 'M'}

# TESTES
print(pessoas)
print()
print(pessoas['nome'])
print()
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos e é do sexo {pessoas["sexo"]}.')
print()

# Acessar dicionarios
print(pessoas.keys())
print()
print(pessoas.values())
print()
print(pessoas.items())

del pessoas['idade']  # deleta uma variavel
pessoas['peso'] = 76.5  # adicionando a um dicionario
lista = pessoas.copy()  # cria uma copia de dicionario a outra variavel com .copy e não com [:]

# Para dicionarios não tem enumerate
for k in pessoas.keys():
    print(k)
print()
for k in pessoas.values():
    print(k)
print()
for k, v in pessoas.items():
    print(f'{k} = {v}')
