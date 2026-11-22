class Termostato:
    def __init__(self):
        self.__temperatura = 24

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, valor):
        if valor < 16:
            self.__temperatura = 16
        elif valor > 30:
            self.__temperatura = 30

        elif valor % 0.5 != 0:
            raise ValueError(f'Temperatura de {valor} é inválida.')

        else:
            self.__temperatura = valor

    @property
    def ftemperatura(self):
        return f'{self.__temperatura}ºC'
