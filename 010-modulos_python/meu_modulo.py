"""
==============================================
           Exemplo de um módulo
Nome: Meu módulo
Author: C.S. de Farias
==============================================
"""


def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total+num
    return total


def soma(numeros):
    return sum(numeros)


def diz_oi(nome):
    return f'Oi, {nome}!'


def outra_funcao(idade, nome, *args, estado_civil=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if estado_civil:
        print('Solteiro(a)')
    else:
        print('Casado(a)')
    print(kwargs)


def soma_num(*args):
    """
    Calcula a soma de números fornecidos pelo usuário e retorna o resultado
    param:
        args
    return:
         total (local variable)
    """
    total = 0
    for el in args:
        total = total + el
    return total
