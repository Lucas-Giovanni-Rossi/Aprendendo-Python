from rich import print
from rich.traceback import install

install()


class Livro:
    def __init__(self, livro, total):
        self.livro = livro
        self.total = total
        self.atual = 1

    def avançar_paginas(self, qtd=0):
        while self.atual <= qtd:
            if self.atual == 1:
                print(f'📖 Você acabou de abrir o livro [green]{self.livro}[/] que tem {self.total} páginas.\n')

            print(f'Pág_{self.atual}', end=' → ')

            if self.atual == self.total:
                break

            self.atual += 1

        if self.atual == self.total:
            print('[yellow]Acabou.[/]\n\n📕 [green]Fim do livro! Parabéns![/] 📕')
        elif qtd == 0:
            print(f'Vocês está na capa do Livro: [red]{self.livro}[/]')
        else:
            print(f'[yellow]Página atual: {self.atual - 1}[/]')

        print()


l1 = Livro('Chamado do Python', 20)
l1.avançar_paginas()
l1.avançar_paginas(5)
l1.avançar_paginas(10)
l1.avançar_paginas(50)
