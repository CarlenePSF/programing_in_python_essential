"""
Len, Abs, Sum  and Round


lista = [1, 3, 5, 7, 9]
lista_float = [3.1415, 2.44, 6.28]
string = '13579'
tupla = (1, 3, 5, 7, 9)
conjunto = {1, 3, 5, 7, 9}
dicio = {'a': 1,
         'b': 3,
         'c': 5,
         'd': 7,
         'e': 9
         }


# *** len() --> retorna o tamanho (ou seja, o numero de items) de um iteravel

# ------- Exemplos com len() -------

# exemplo com len()
print(len(lista))
print(len(string))
print(len(tupla))
print(len(conjunto))
print(len(dicio))
print(len(range(5)))

# por baixo dos panos, quando usamos a funcao len() o Python executa a seguinte tarefa
# dander len :  .__len__() tambem chamada de  metodo magico

print('Geek University'.__len__())

# from Stackoverflow:
# So the general rule should be to never call a magic method directly
# (but always indirectly through a built-in) unless you know exactly why you need to do that
# (e.g., when you're overriding such a method in a subclass, if the subclass needs to defer to
# the superclass that must be done through explicit call to the magic method).


# **** abs() --> Retorna o valor absoluto de um numero inteiro (tipo int) ou real (tipo float).
            Valor numerico sem o sinal
# ------- Exemplos com abs() -------
print(abs(-5))
print(abs(5))
print(abs(3.1415))
print(abs(-3.1415))

# *** sum() --> Recebe como parametro um iteravel, podendo receber um valor inicial, e retorna a soma total
                dos elementos, incluindo o valor inicial.

# OBS: O valor inicial default e sempre zero!

# ------- Exemplos --------
# com uma lista
print(sum(lista))
print(sum(lista, 5))
print(sum(lista, -5))

print(sum(lista_float))
print(sum(lista_float, 5))
print(sum(lista_float, -5))

# com uma tupla
print(sum(tupla))
print(sum(tupla, 5))
print(sum(tupla, -5))

# com um conjunto
print(sum(conjunto))
print(sum(conjunto, 5))
print(sum(conjunto, -5))

# com um dicionario
print(sum(dicio.values()))
print(sum(dicio.values(), 5))
print(sum(dicio.values(), -5))

# OBS: sum NAO funciona com strings!!!


# round() --> Retorna um numero arredondado para n digitos de precisao apos a casa decima.
              Se a precisao nao for informada retorna o inteiro mais proximo da entrada.

# ------- Exemplos -----

# ate 0.5 arrendonda para baixo
print(round(10.2))
print(round(10.5))

# acima de 0.5 arredonda para cima
print(round(10.6))

# arredonda para reais
print(round(1.2121212121, 2))
print(round(1.219999999999, 2))
print(round(3.14159265358979323846, 2))

"""

