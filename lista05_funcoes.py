"""
Lista de exercicios sobre funções


#----------------------------------------------------
# Exercicio 1 - função dobro
#----------------------------------------------------

def dobro(num):
    return 2.*num

print(dobro(2))


#----------------------------------------------------
# Exercicio 2 - imprime data
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
"""



#----------------------------------------------------
# Exercicio 3 - imprime data
#----------------------------------------------------