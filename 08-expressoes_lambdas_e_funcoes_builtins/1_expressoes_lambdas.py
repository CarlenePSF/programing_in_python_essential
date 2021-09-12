"""
Utilizando lambdas

Conhecidas por Expressões lambdas, ou simplesmente lambdas, são funções sem nome, ou seja, funções anonimas.

# uma função em Python é definida como abaixo

def soma(a, b):
    return a+b


def funcao(x):
    return 3 * x + 1


print(funcao(5))
print(funcao(7))

# Escrevendo a mesma função como uma expressão lambda
# lambda x: 3 * x + 1


# E como utilizar uma expressão lambda? Veja o exemplo abaixo
from typing import Any, Callable


soma_lambda = lambda numero1, numero2: numero1 + numero2


print(soma_lambda(5, 3))
print(soma_lambda(7, 5))

# No entanto, o exemplo acima não é a forma mais adequada de se empregar uma expressão lambda.
# Nesse caso o preferível seria criar uma função (procedimento). Existem formas mais dignas de se usar
# uma expressão lambda


# Podemos ter expressões lambdas com múltiplas entradas. Veja o exemplo abaixo
# .strip() remove espaços em branco de uma string que estão no inicio e no final da string
# .title() coloca em maiúscula a primeira letra da string


nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo(' carlene', 'PAULA'))
print(nome_completo(' Julius', '  cesar'))

# Em funções Python podemos escrever funções que tenham nenhuma ou várias entradas. Em lambdas também

ama_python = lambda: 'Como não amar o Python?'

uma = lambda x: 3*x+1

duas = lambda x, y: (x**2 + y**2)**1/2

tres = lambda x, y, z: 1/x + 1/y + 1/z

# Generalizando
# n = lambda x1, x1, ... xn: <expressão>

print(ama_python())
print(uma(2))
print(duas(1, 1))
print(tres(1, 1, 1))


Ok, entendi o conceito, mas para o que isso serve?
Agora vem a parte mais complicada desta lição. Existem funções que podem receber outras funções por parâmetro!

Sim, você não leu errado, uma função recebe como parâmetro outra função. Estes são os exemplos
onde as expressões lambda são mais utilizadas.


# Outro exemplo: uso mais adequado para expressões lambdas

autores = ['J. R. R. Tolkien', 'H. G. Wheels', 'Isaac Asimov', 'Jane Austen', 'Dan Brown',
           'Edgar Alan Poe', 'Itamar Vieira Jr']
print(autores)

# Vamos criar uma expressão lambda para extrair o sobrenome e ordená-los numa nova lista organizada alfabeticamente
autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(autores)

# Usando uma expressão lambda para criar uma função quadrática
# Usada em jogos, para lançamento de projéteis ...

# Funções quadráticas são funções do tipo:
# f(x) = a*x**2 + b*x + c


def quadrado(a, b, c):
    # Retorna a função f(x) = a*x** + b*x + c
    return lambda x: a*x**2 + b*x + c


teste = quadrado(2, 3, 1)
# Executando passando os valores de x
print(teste(0))
print(teste(2))
print(teste(4))

# outra forma
print(quadrado(2, 3, 1)(0))
print(quadrado(2, 3, 1)(2))
print(quadrado(2, 3, 1)(4))
"""

"""
******************** Vamos Praticar! ***********************

1 - Faça um programa que escreva “Minha primeira função”, esta escrita deve ser realizada a partir da chamada de uma 
    função que foi declarada como uma expressão lambda.
"""


escreve_string = lambda: 'Minha primeira função.'

print(escreve_string())

"""
2 - Faça um programa que solicite o nome do usuário e a idade do usuário, depois disso exiba a mensagem: 
   "{nome} possui {idade} anos.". Esta mensagem deve ser escrita em uma função lambda.
"""
nome = input("Qual o seu nome? ")
idade = input("Qual a sua idade? ")


escreve_string_2 = lambda: f'{nome} possui {idade} anos.'
print(escreve_string_2())

"""
3 - Faça um programa que solicite dois números ao usuário e exiba a multiplicação deles. 
    A multiplicação deve ser calculada em uma função lambda.
"""

num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro numero "))

multiplicacao = lambda a, b: a * b

print(multiplicacao(num1, num2))
