"""
Lista de exercícios sobre funções
from math import sqrt, pi
"""
# from math import pi, sqrt
# from random import randint, seed
#----------------------------------------------------
# Exercício 1 - função dobro
#----------------------------------------------------
'''
def dobro(num):
    return 2.*num

print(dobro(2))
'''

#----------------------------------------------------
# Exercício 2 - imprime data
#----------------------------------------------------

'''
def imprime_data(dia, mes, ano):
    meses = {
        1: 'janeiro',
        2: 'fevereiro',
        3: 'março',
        4: 'abril',
        5: 'maio',
        6: 'junho',
        7: 'julho',
        8: 'agosto',
        9: 'setembro',
        10: 'outubro',
        11: 'novembro',
        12: 'dezembro'
    }
    return f'{dia} de {meses[mes]} de {ano}'


print(imprime_data(15, 5, 2021))
print(imprime_data(9, 1, 1999))
'''

# ---------------------------------------------------------------
# Exercício 3 - verificando se um numero é positivo ou negativo
# ---------------------------------------------------------------

'''
def verifica_numero(num):
    if num > 0:
        return 1
    elif num < 0:
        return -1
    else:
        return 0


print(verifica_numero(5))
print(verifica_numero(-5))
print(verifica_numero(0))
'''
# ---------------------------------------------------------------
# Exercício 4 - verificando se um numero é um quadrado perfeito
# ---------------------------------------------------------------

'''
def quadrado_perfeito():
    """
    Verificando se um numero é um quadrado perfeito
    """
    num = int(input('Digite um número: '))
    i = 0
    while i <= num:
        i = i+1
        if num == i**2:
            print(f'O {num} é um quadrado perfeito')
            break
        elif num != i**2:
            continue


quadrado_perfeito()
'''
# --------------------------------------------------------------
# Exercício 5 - Cálculo do volume de uma esfera
# -------------------------------------------------------------

'''
def volume_esfera(r):
    volume = (4./3.)*pi*r**3
    return f'O volume da esfera de raio {r} é {volume} m^3'


raio = float(input('Qual o raio da esfera? '))
print(volume_esfera(raio))
'''

# --------------------------------------------------------------
# Exercício 6 - convertendo as horas em segundos
# -------------------------------------------------------------
'''

def convert_segundos(hora, minuto, segundo):
    return hora*3600 + minuto*60 + segundo


h = int(input('digite a hora: '))
m = int(input('digite os minutos: '))
s = int(input('digite os segundo: '))

print('A conversão para segundos é', convert_segundos(h, m, s))

'''
# --------------------------------------------------
# Exercício 7 - convertendo escalas de temperatura
# --------------------------------------------------
'''
def convert_Fahrenheit(fahrenheit):
    return fahrenheit * (9 / 5) + 32.0


T_c = float(input('Type the temperature in Celsius: '))
print(f'The result of the conversion {convert_Fahrenheit(T_c)} Fº')
'''

# --------------------------------------------------
# Exercício 8 - triangulo retangulo 
# --------------------------------------------------

'''
def hipotenusa(a, b):
    return round(sqrt(a**2 + b**2), 2)


a1 = float(input('Digite o valor do primeiro cateto em cm: '))
a2 = float(input('Digite o valor do segundo cateto em cm: '))

print(f'A hipotenusa do triangulo mede {hipotenusa(a1, a2)} cm')
'''
# --------------------------------------------------
# Exercício 9 - volume do cilindro
# --------------------------------------------------
'''
def volume_cilindro(h, r):
    return pi * r ** 2 * h


altura = float(input('Digite a altura do cilindro em cm: '))
raio = float(input('Digite o valor do raio da base em cm: '))
print(f'O volume desse cilindro é {volume_cilindro(altura, raio)} cm3')
'''

# --------------------------------------------------
# Exercício 10 - o maior de dois números
# --------------------------------------------------

'''
def MaiorDeDois(num1, num2):
    if num1 > num2:
        return f'{num1} é maior.'
    else:
        return f'{num2} é maior.'


a = float(input('Digite um número: '))
b = float(input('Digite outro número: '))
print(MaiorDeDois(a, b))
'''
# --------------------------------------------------
# Exercício 11 - Notas de alunos
# --------------------------------------------------

'''
def Media_Notas(notas, op='P'):
    if op == 'A':
        return f'A média aritmética das notas é {round(sum(notas)/len(notas), 2)}'
    elif op == 'P':
        return f'A média ponderada das notas é {round((notas[0]*5+notas[1]*3+notas[2]*2)/10, 2)}'


Notas = [float(input(f'Digite a nota {i+1}: ')) for i in range(3)]
media = input('Média: aritmética (A) ou ponderada (P): ')
print(Media_Notas(Notas, media))
'''
# --------------------------------------------------
# Exercício 12 -
# --------------------------------------------------

'''
def soma_algarismos(num):
    try:
        if num >= 0:
            v = str(num)
            lista = [float(i) for i in v]
            print(f'A soma dos algarismo de {num} é {sum(lista)}')
        elif num < 0:
            return 'Número inválido'
    except ValueError or SyntaxError or TypeError:
        return 'algo deu errado'


print(soma_algarismos(0))
'''
# --------------------------------------------------
# Exercício 13 - calculadora simples
# --------------------------------------------------

'''
def calculadora(x1, x2, op):
    if op == '+':
        return x1+x2
    elif op == '-':
        return x1-x2
    elif op == '*':
        return x1*x2
    elif op == '/':
        try:
            return x1/x2
        except ZeroDivisionError as err1:
            print(f'Algo deu errado: {err1}')


print(calculadora(2, 0, '*'))
'''
# --------------------------------------------------
# Exercício 14 - economia de um carro
# --------------------------------------------------

'''
def consumo(distancia, litros):
    try:
        res = distancia/litros
        if res < 8:
            print(f'O consumo é de {res}. Venda o carro!')
        elif 8 <= res <= 14:
            print(f'O consumo é de {res}. Econômico!')
        elif res >= 12:
            print(f'O consumo é de {res}. Super econômico!')
    except (NameError, ZeroDivisionError, TypeError, SyntaxError) as err1:
        print(f'Algo deu errado: {err1}')


consumo(15, 1.5)

'''
# --------------------------------------------------
# Exercício 15 - classificação de triângulos
# --------------------------------------------------

'''
def triangulo(a=1.0, b=1.0, c=1.0):
    """
    Determina se os valores formam um triângulo e qual tipo de triangulo
    :var a, b, c lados do triangulo
    """
    try:
        if [a, b, c] < [b+c, a+b, a+b]:
            print('Forma um triângulo.')
            if a == b == c:
                print('Triângulo equilátero.')
            elif a == b != c or a != b == c or a == c != b:
                print('Triângulo isósceles.')
            else:
                print('Triângulo escaleno.')
        else:
            print('Não podem ser lados do um triangulo.')
    except (ValueError, SyntaxError):
        print('Algo deu errado.')


triangulo(4, 1, 2)
'''

# --------------------------------------------------
# Exercício 16 - desenha linhas
# --------------------------------------------------
'''
def desenha_linha(n):
    print('=' * n)


desenha_linha(100)
'''
# ----------------------------------------------------------
# Exercício 17 - soma dos N números inteiros em um intervalo
# ----------------------------------------------------------
'''
def soma_inteiros(a, b):
    """
    retorna a soma dos números inteiros num intervalo [a, b]
    parameters:
        a: ponto inicial
        b: ponto final
    """
    if a <= 0 and b <= 0:
        raise ValueError('Valores negativos. Digite números inteiros positivos e maiores que zero.')
    else:
        soma = 0
        for i in range(a, b):
            soma += i
            #print(soma)
        return soma


print(soma_inteiros(0, 9))
'''

# --------------------------------------------------
# Exercício 18 - desenha linhas
# --------------------------------------------------

'''
def potencia(x, z=2):
    return x**z


print(potencia(2, 3))
'''

# --------------------------------------------------
# Exercício 19 - Maior fator primo de um número
# --------------------------------------------------


def maximo_fator_primo(num):
    fator = 2
    while fator < num:
        print(num/fator)
        fator += 1
    print(fator)


maximo_fator_primo(3)
# --------------------------------------------------
# Exercício extra -  probabilidades
# --------------------------------------------------
'''
seed(2)

lista = [randint(0, 1) for i in range(40)]
print(lista)


def reduz_elementos(lista_original):
    lista_copy = lista_original.copy()
    for i in lista_copy:
        if lista_copy.count(i) > 1:
            lista_copy.remove(i)
    return list(set(lista_copy))


def probabilidade(lista_original, lista_reduzida):
    return [(lista_original.count(i)/len(lista_original)) for i in lista_reduzida]


reduzida = reduz_elementos(lista)
print(reduzida)
print(probabilidade(lista, reduzida))
print('Soma das probabilidades:', sum(probabilidade(lista, reduzida)))
'''