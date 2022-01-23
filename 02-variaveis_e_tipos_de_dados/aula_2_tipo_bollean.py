"""
Tipo boolean

Vem da algebra booleana, criada por George Boole

2 constantes uma para verdadeiro e outra para falso

True -> Verdadeiro
False -> Falso

OBS: Sempre com a inicial maiuscula

Errado:

true, false

correto

True, False

Utilizado para realizar operacoes basicas

Muito a ver com logica
"""


ativo1 = False

ativo2 = False

print(ativo1)
print(ativo2)
print(dir(ativo1))
print(dir(ativo2))

"""
Operacoes basicas:
"""

# Negacao (not):
"""
Fazendo a negacao: Se o boolean for verdadeiro o resultado sera falso
Se for falso o resultado sera verdadeiro
"""

print(not ativo1)
print(not ativo2)

# ou (or)
"""
E uma operacao binaria, ou seja, depende de 2 valores. para ser verdadeiro, 
ou um ou outro tem que ser verdadeiro.
True or True -> True
True or False -> True 
False or True -> True 
False or False -> False
"""

logado = False
print(ativo1 or logado)


# condicional 'E' (and)

"""
Tambem e uma operacao binaria, ou seja, depende de 2 valores. 
Para ser verdadeira, ambos os valores devem ser verdadeiros.

True and True -> True
True and False -> False
False and True -> False
False and False -> False
"""

num1 = 5
num2 = 1

if num2 > num1:
    print(f'{num1} > {num2}: False')
if num2 < num1:
    print(f'{num1} > {num2}: True')
