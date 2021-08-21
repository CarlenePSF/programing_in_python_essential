"""
Módulo Random e o que são módulos

- Em Python, módulos nada mais são do que outros arquivos Python, arquivo.py

- Módulos servem para deixar a estrutura dos programas mais simples e para que possamos reutilizar partes de códigos

- Módulos podem ser escritos por qualquer programador e compartilhados com a comunidade.

- Se não estiver instalado, precisa ser feita a instalação primeiramente, em seguida fazemos a importação.

Nessa aula trabalhamos com o módulo Random, que possui várias funções para geração de números reais pseudo-aleatórios.


# ------ Forma 1 (Não recomendada!!!!)
# O uso do import faz com que importemos o módulo por completo e, portanto, todas as funções, atributos,
# classes e propriedades que estiverem dentro do módulo ficarão disponíveis em memória.
# Essa não é a forma ideal de utilização, pois ocupa espaço de memória!!!

# Sintaxe: import nome_do_módulo
import random

print(dir(random))
# print(help(random)

# random.random() gera o num aleatório entre 0 e 1
print(round(random.random(), 3))
# OBS: não confunda a função random() com o pacote random, pois random() é apenas uma das funções dentre do módulo.
"""

# ------ Forma 2 (Recomendada)
# Recomendada quando já sabemos quais funções importar
# Caso você já saiba quais funções precisa utilizar do módulo específico, basta utilizar a forma 2 mostrada abaixo.

# Sintaxe: do módulo random importe a função desejada
from random import random, seed, uniform, randint, choice, shuffle
# acessando a semente de números aleatórios
seed()

for i in range(3):
    print(round(random(), 3), end=', ')


# ---- Gerando valores reais pseudo-aleatório entre os valores estabelecidos co o uniform.
for i in range(0, 5):
    print(round(uniform(3, 10), 2))  # o 7 não é incluído


# ---- Gerando valores inteiros
# O randint() gera valores inteiros pseudo-aleatórios entre os valores pré-estabelecidos

for i in range(6):
    print(randint(1, 61), end=', ')  # começa em 1  indo até 60


# choice() -> mostra um valor aleatório entre um iterável (lista, tupla, dicionário, conjunto)
jogadas = ['pedra', 'papel', 'tesoura']
print(choice(jogadas))

print(choice('Geek University'))

# shuffle() -> embaralha dados
cartas = ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10']
print(cartas)
shuffle(cartas)
print(cartas)
# dando uma carta para o usuário
print(cartas[5])
