from Termostato import *  # noqa: F403


def main():

    t = Termostato()  # noqa: F405
    try:
        t.temperatura = 20
    except Exception as e:
        return print(f'Houve um erro. \n{e}')

    print(f'\nA temperatura do termostato é de {t.ftemperatura}.\n')


if __name__ == '__main__':
    main()
