from Diario import Diario
from rich import inspect, print


def main():
    d = Diario()
    d.escrever('Teste de escrita do diario')
    d.escrever('estou aprendendo python')
    try:
        d.ler(input('Digite a senha:' ))
    except Exception as e:
        print(f'[red]ERRO: {e}[/]')

    inspect(d, private=True)


if __name__ == '__main__':
    main()
