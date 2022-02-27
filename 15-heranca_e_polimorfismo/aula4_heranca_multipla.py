"""
POO — Herança multipla

Na linguagem Python, a herança multipla é a possibilidade de uma classe herdar de multiplas classes,
fazendo com que a classe filha herde todos os atributos e métodos de todas as classes mães.

OBS: A herança multipla pode ser feita de duas maneiras:
    — Por multiderivação direta
    — Por multiderivas indireta


# Exemplo 1 — Multiderivação direta


class Base1:
    pass


class Base2:
    pass


class Multiderivada_direta(Base1, Base2):
    pass


# Exemplo 2 — multiderivação indireta

class Base1:
    pass


class Base2(Base1):
    pass


class Base3(Base2):
    pass


class Multiderivada_indireta(Base3):
    pass

# OBS: não importa se a derivação é direta ou indireta. A classe multiderivada herdeira herdará
todos os atributos e métodos da superclasses

"""


class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def cumprimento(self):
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
    # a ordem de herança altera como será o comportamento do objeto

    def __init__(self, nome):
        super().__init__(nome)


baleia = AnimalAquatico('Willy')
print(baleia.cumprimentar())
print(baleia.nadar())


gato = AnimalTerrestre('Mimi')
print(gato.cumprimentar())
print(gato.andar())


pinguim = Pinguim('Mamboo')
print(pinguim.cumprimentar())
print(pinguim.nadar())
print(pinguim.andar())
print(pinguim.cumprimento())


# Descobrindo se um objeto é instância de ...
print(f'pinguim é instância de Pinguin? {isinstance(pinguim, Pinguim)}')
print(f'pinguim é instância de Animal_terrestre? {isinstance(pinguim, AnimalTerrestre)}')
print(f'pinguim é instância de Animal_aquatico? {isinstance(pinguim, AnimalAquatico)}')
print(f'pinguim é instância de Animal? {isinstance(pinguim, Animal)}')
print(f'pinguim é instância de object? {isinstance(pinguim, object)}')
