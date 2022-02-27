"""
POO- Polimorfismo
Poli -> muitas
Mofis -> formas

Quando reimplementamos um método presente na classe pai em classes filhas estamos sobreescrevendo um método (overriding).
Overriding é a representação do polimorfismos.


"""


class Animal(object):

    def __init__(self, nome):
        self.__nome = nome

    def falar(self):
        raise NotImplementedError('A classe filha precisa implementar esse método')

    def comer(self):
        print(f'{self.__nome} está comendo')


# Extensões da classe Animal
class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala auau')


class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala miau')


# Note o warning na classe Rato
class Rato(Animal):

    def __init__(self, nome):
        super().__init__(nome)


gato = Gato('Mimi')
dog = Cachorro('Flush')
rato = Rato('Mickey')

gato.comer()
gato.falar()  # falar terá um comportamento

dog.comer()
dog.falar()  # falar terá outro comportamente

rato.falar()
rato.comer()  # falar terá outro comportamento


