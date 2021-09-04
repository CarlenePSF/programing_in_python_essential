"""
Escrevendo um iterador customizado

O iterador padrão que utilizamos até agora foi o a função range() - lembrando que o range é não 
inclusivo para a esquerda

for n in range(0, 11):  # imprime de 0 até 10
    print(n)

"""


class Contador:
    def __init__(self, menor, maior):  # metodo construtor
        self.menor = menor
        self.maior = maior

    def __iter__(self):
        return self

    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor = self.menor + 1
            return numero
        raise StopIteration


con = Contador(1, 6)

it = iter(con)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it), '\n')


# outra maneira sem usar o next()

for _ in Contador(1, 6):
    print(_)
