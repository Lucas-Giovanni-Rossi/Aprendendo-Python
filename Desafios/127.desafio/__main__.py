from desafio import Guerreiro, Mago
from rich import inspect


def main():
    p1 = Guerreiro('Leonidas', 7000)
    p2 = Mago('Merlin', 3000)

    p1.attack(p2, 500)
    p2.heal()
    p2.attack(p1, 1500)
    p1.heal()
    p1.attack(p2, 500)

    inspect(p1, methods=True)  # testes de inspeção


if __name__ == '__main__':
    main()
