"""
Exercícios de programação orientada a objetos

 lista da python Brasil  - https://wiki.python.org.br/ExerciciosClasses
"""


# --------------------------------------------------------
# Exercicio 1 - Classe bola
# --------------------------------------------------------

"""
class Bola:

    def __init__(self, cor, circunferencia, material):
        self.__cor = cor
        self.__circunferencia = circunferencia
        self.__material = material

    @property
    def cor(self):
        return self.__cor

    @property
    def circunferencia(self):
        return self.__circunferencia

    @property
    def material(self):
        return self.__material

    def troca_cor(self, nova_cor) -> object:
        self.__cor = nova_cor
        return self.__cor

    def mostra_cor(self):
        return f'a cor da bola é {self.__cor}'


bola = Bola('azul', '10 cm', 'couro')
print(bola.__dict__)
print(bola.mostra_cor())
bola.troca_cor('amarela')
print(bola.mostra_cor())
"""

# --------------------------------------------------------
# Exercicio 2 - Classe Quadrado
# --------------------------------------------------------

"""
class Quadrado:

    def __init__(self, lado):
        self.__lado = lado

    @property
    def lado(self):
        return self.__lado

    def muda_lado(self, lado) -> object:
        self.__lado = lado
        return self.__lado

    def calcula_area(self):
        return self.__lado**2


quadrado = Quadrado(2)
print('O lado do quadrado é', quadrado.lado)
quadrado.muda_lado(3)
print('Novo valor para o lado:', quadrado.lado)
print(f'A área do quadrado de lado {quadrado.lado} é {quadrado.calcula_area()}')
"""

# --------------------------------------------------------
# Exercicio 2 - Classe Quadrado
# --------------------------------------------------------


class Retangulo:

    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura

    @property
    def base(self):
        return self.__base

    @property
    def altura(self):
        return self.__altura

    def muda_lados(self, nova_base, nova_altura):
        self.__base = nova_base
        self.__altura = nova_altura
        return self.__base, self.__altura

    def area_retangulo(self):
        return self.__base * self.__altura

    def perimetro(self):
        return 2*self.__base + 2*self.__altura


# retangulo = Retangulo(3, 4)
# print('Base do retângulo:', retangulo.base)
# print('Altura do retângulo:', retangulo.altura)

width = float(input('Informe a largura: '))
height = float(input('Informe o comprimento: '))
retangulo = Retangulo(width, height)
print(f'O cômodo tem uma área de {retangulo.area_retangulo()}')
