"""
Lista de exercícios sobre funções


#----------------------------------------------------
# Exercício 1 - função dobro
#----------------------------------------------------

def dobro(num):
    return 2.*num

print(dobro(2))


#----------------------------------------------------
# Exercício 2 - imprime data
#----------------------------------------------------

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


# ----------------------------------------------------
# Exercício 3 - verificando se um numero é positivo ou negativo
# ----------------------------------------------------


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



def quadrado_perfeito():
    '''Verificando se um numero é um quadrado perfeito'''
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


# --------------------------------------------------------------
# Exercício 5 - Cálculo do volume de uma esfera
# -------------------------------------------------------------


from math import pi


def volume_esfera(r):
    volume = (4./3.)*pi*r**3
    return f'O volume da esfera de raio {r} é {volume} m^3'


raio = float(input('Qual o raio da esfera? '))
print(volume_esfera(raio))


# --------------------------------------------------------------
# Exercício 6 - convertendo as horas em segundos
# -------------------------------------------------------------


def convert_segundos(hora, minuto, segundo):
    return hora*3600 + minuto*60 + segundo


h = int(input('digite a hora: '))
m = int(input('digite os minutos: '))
s = int(input('digite os segundo: '))

print('A conversão para segundos é', convert_segundos(h, m, s))
"""

# --------------------------------------------------
# Exercício 7 - convertendo escalas de temperatura
# --------------------------------------------------



