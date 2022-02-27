"""
 POO - Method Resolution Order (MRO)

Resolução de ordem de métodos (MRO) é a ordem de exeção dos métodos herdados por uma classe
filha das suas classes pai se essas possuem métodos com o mesmo nome.

Em python, podemos conferir a ordem de execução dos métodos (MRO) de 3 formas:
    — Via propriedade de classe __mro__
    — Via método mro()
    — via help

"""


class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f'Olá! Eu sou {self.__nome}.'


class AnimalAquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} está nadando.'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} do mar!'


class AnimalTerrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} está andando.'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} da terra!'


class Pinguim(AnimalAquatico, AnimalTerrestre):
    # A ordem de herança altera como será o comportamento do objeto

    def __init__(self, nome):
        super().__init__(nome)


pinguim = Pinguim('Mamboo')
print(pinguim.cumprimentar())

# como descobrir a hieharquia para execução dos métodos?
# usando .__mro__
print(Pinguim.__mro__)
# usando .mro()
print(Pinguim.mro())
# usando .mro()
print(help(Pinguim))