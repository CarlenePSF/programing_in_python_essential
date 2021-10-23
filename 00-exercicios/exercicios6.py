"""
Exercícios de programação orientada a objetos

 lista da python Brasil  - https://wiki.python.org.br/ExerciciosClasses
"""


# --------------------------------------------------------
# Exercicio 1 - Classe bola
# --------------------------------------------------------


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


# --------------------------------------------------------
# Exercicio 1 - Classe Quadrado
# --------------------------------------------------------

class Quadrado:

    def __init__(self, lado):
        self.__lado = lado

    @property
    def lado(self):
        return self.__lado

