# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# – Quantidade de notas
# – A maior nota
# – A menor nota
# – A média da turma
# – A situação (opcional)


def notas(*numeros, sit=False):
    """
    Calcula estatísticas de um conjunto de notas.

    Parâmetros:
    *numeros : float
        Uma ou mais notas a serem analisadas.
    sit : bool, opcional
        Indica se deve ou não incluir a situação da média (default é False).

    Retorno:
    dict
        Um dicionário contendo:
        - total: quantidade de notas
        - Maior: maior nota
        - Menor: menor nota
        - Media: média das notas
        - Situação (opcional): classificação da média

    """

    dados = {}
    dados['total'] = len(numeros)
    dados['Maior'] = max(numeros)
    dados['Menor'] = min(numeros)
    media = sum(numeros) / len(numeros)
    dados['Media'] = media

    if sit:
        if media >= 7:
            dados['Situação'] = 'Boa'
        elif media >= 5:
            dados['Situação'] = 'Razoável'
        else:
            dados['Situação'] = 'Ruim'

    return dados


# Programa principal
resp = notas(5.5, 9.2, 3.4, 10, 10, 5, sit=True)
print(resp)
