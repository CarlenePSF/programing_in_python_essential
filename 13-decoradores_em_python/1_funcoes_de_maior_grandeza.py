"""
*** Funções de maior grandeza - higher order function (HOF)

O que isso significa?

Quando uma linguagem de programação suporta HOF, indica que podemos ter funções que retornam outras
funções como resultado. Ou mesmo que podemos passar funções como argumento para outras funções, e até mesmo
criar variáveis do tipo de funções nos nossos programas.

# OBS: Isso já foi utilizado e discutido inicialmente na seção de funções


Em Python, as funções são cidadãos de primeira classe (first class citizens).
Isso significa que elas suportam operações como sendo passadas como um argumento que é
retornado de uma função, modificado e atribuído à uma variável.


# Exemplo - Definimos as funções


def somar(a, b):
    return a+b


def diminuir(a, b):
    return a-b


def multiplicar(a, b):
    return a*b


def dividir(a, b):
    return a/b


def calcular(num1, num2, func):
    return func(num1, num2)


# Testando as funções
print(calcular(4, 3, somar))
print(calcular(4, 3, diminuir))
print(calcular(4, 3, multiplicar))
print(calcular(4, 3, dividir))

*** Nested functions - ou funções aninhadas

Em Python, também podemos ter funções dentro de funções, que são conhecidas por nested functions
ou inner functions (funções internas)


# Exemplo de nested functions

from random import choice


def cumprimento(pessoa):
    def humor():
        return choice(('E ai?', 'Suma daqui!', 'Gosto muito de você!'))
    return humor() + pessoa


print(cumprimento('Felicity'))

print(cumprimento('Felicity'))


# Outro exemplo  - Retornando funções de outras funções
from random import choice



def faz_me_rir():
    def rir():
        return choice(('hahahahahaha', 'kkkkkkkkkkkk', 'yayayayayaya'))
    return rir()


rindo = faz_me_rir()
print(rindo)

Inner functions (funções internas/nested functions) podem acessar o escopo de funções mais externas
"""

from random import choice


def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(('hahahahahaha', 'kkkkkkkkkkkk', 'yayayayayaya'))
        return f'{risada} {pessoa}'
    return dando_risada


# teste
rindo = faz_me_rir_novamente('Fernanda')

print(rindo())
print(rindo())
print(rindo())
