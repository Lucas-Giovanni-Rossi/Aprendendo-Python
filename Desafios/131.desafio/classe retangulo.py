from rich import print


class Retangulo:
    def __init__(self, base=1, altura=1):
        self._base = None
        self._altura = None
        self._area = None

        self.base = base
        self.altura = altura

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, valor):
        if not isinstance(valor, (int, float)):
            raise TypeError('O valor da base deve ser um número.')
        elif valor <= 0:
            raise ValueError('O valor da base deve ser maior que 0')
        else:
            self._base = valor

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, valor):
        if not isinstance(valor, (int, float)):
            raise TypeError('O valor da altura deve ser um número.')
        elif valor < 0:
            raise ValueError('O valor da altura deve ser maior que 0')
        else:
            self._altura = valor

    @property
    def area(self):
        self._area = self._base * self._altura
        return self._area

    @area.setter
    def area(self):
        raise PermissionError('Área não podes ser cálcula desse jeito.')

    @property
    def medidas(self):
        return f'Base = {self.base} \nAltura = {self.altura} \nÁrea = {self.area}'

    @medidas.setter
    def medidas(self, valores: tuple):
        if not isinstance(valores, tuple):
            raise TypeError('As medidas devem ser informadas em uma tupla.')
        if len(valores) != 2:
            raise SyntaxError('Informe uma tupla com apenas 2 números.')

        if isinstance(valores[0], (float, int)):
            self.base = valores[0]
        else:
            raise TypeError('A medida da base deve ser um número.')
        if isinstance(valores[1], (float, int)):
            self.altura = valores[1]
        else:
            raise TypeError('A medida da altura deve ser um número.')


r = Retangulo(7, 2)
try:
    r.base = 12
    r.altura = 1
    r.medidas = (3, 40)
except Exception as e:
    print(f'[red]Ocorreu um erro do tipo {type(e).__name__}: {e}[/]')

print(r.medidas)
