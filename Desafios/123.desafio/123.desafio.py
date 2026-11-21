from abc import ABC, abstractmethod
from math import pi


class FormaGeometrica(ABC):  # Super classe Abstrata
    def __init__(self, qtd_lados=0):
        self.qtd_lados = qtd_lados

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Quadrado(FormaGeometrica):
    def __init__(self, lado):
        super().__init__(qtd_lados=4)
        self.lado = lado

    def perimetro(self):
        return f'{self.qtd_lados * self.lado:.2f}'

    def area(self):
        return f'{self.lado**2:.2f}'


class Circulo(FormaGeometrica):
    def __init__(self, raio):
        super().__init__(qtd_lados=0)
        self.raio = raio

    def perimetro(self):
        return f'{pi * (2 * self.raio):.2f}'  # C = 2 * pi * raio (ou pi * diametro):.2f

    def area(self):
        return f'{pi * self.raio**2:.2f}'


# ----- PROGRAMA PRINCIPAL ------ #

p1 = Quadrado(5)
c1 = Circulo(20)

print(f'Perimetro = {p1.perimetro()}')
print(f'Area = {p1.area()}')
print()
print(f'Perimetro = {c1.perimetro()}')
print(f'Area = {c1.area()}')
