"""
POO - O método super()

O método super() se refere à superclasse

"""


class Animal:

    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie

    def emite_som(self, som):
        print(f'O {self.__nome} emite o som {som}')


class Gato(Animal):
    def __init__(self, nome, especie, raca):

        # Animal.__init__(self, nome, especie)  # possibilidade 1, mas não aconselhado
        super().__init__(nome, especie)  # método mais aconselhado
        self.__raca = raca


mimi = Gato('Mimi', 'felino', 'tigrado')
mimi.emite_som('miau')
print(mimi.__dict__)
