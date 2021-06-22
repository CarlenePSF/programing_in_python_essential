"""
Entendendo o uso do *args

1 - O *args é um parâmetro como outro qualquer. Isso significa que você poderá chamar de qualquer coisa, desde que
   comece com

exemplo:
*qualquer_coisa
*X

Por convenção, a comunidade python define o uso *args
Ao utilizarmos esse parâmetro na função os valores extras informados como entrada são armazenados numa tupla
Lembre-se, tuplas são IMUTÁVEIS!!!!


# Exemplo

def soma_tres_num(num1, num2, num3):
    '''
    #Calcula a soma de 3 números num1, num2 e num3 e retorna o resultado
    #:param num1:
    #:param num2:
    #:param num3:
    #:return: num1+num2+num3
    '''
    return num1+num2+num3


print(soma_tres_num(4, 6, 9))


# Se passarmos menos parâmetros do que os exigidos na declaração da função, temos um TypeError
# como na execução abaixo


# print(soma_tres_num(2, 5))
# >>> TypeError: soma_tres_num() missing 1 required positional argument: 'num3'

# refatorando a função com uso do *args

def soma_num(*args):
    '''
    Calcula a soma de números fornecidos pelo usuário e retorna o resultado
    :param: args
    :return:
    '''
    print(args)


print(soma_num())
print(soma_num(1))
print(soma_num(1, 2))
print(soma_num(1, 2, 3))
print(soma_num(1, 2, 3, 4))

# Saida
# ()
# (1,)
# (1, 2)
# (1, 2, 3)
# (1, 2, 3, 4)


def soma_num(*args):
    '''
    Calcula a soma de números fornecidos pelo usuário e retorna o resultado
    :param: args
    :return: total (local variable)
    '''
    total = 0
    for el in args:
        total = total + el
    return total


print(soma_num())
print(soma_num(1))
print(soma_num(1, 2))
print(soma_num(1, 2, 3))
print(soma_num(1, 2, 3, 4))

# Saida
# 0
# 1
# 3
# 6
# 10

# Refatorando com uma propriedade de tupla

def soma_num3(*args):
    '''
    Calcula a soma de números fornecidos pelo usuário e retorna o resultado
    :param: args
    :return: total (local variable)
    '''
     return sum(args)


print(soma_num3())
print(soma_num3(1))
print(soma_num3(1, 2))
print(soma_num3(1, 2, 3))
print(soma_num3(1, 2, 3, 4))

# Saida
# 0
# 1
# 3
# 6
# 10


# Adicionando outro parâmetros


def soma_num4(nome, email, *args):
    '''
     Calcula a soma de números fornecidos pelo usuário e retorna o resultado
    :param: nome
    :param: email
    :param: args
    :return:
    '''
    if nome and email:
        print(nome, email)
    return sum(args)


print(soma_num4('Carlene ', 'carlene@aqui.com'))
print(soma_num4('Carlene ', 'carlene@aqui.com', 1))
print(soma_num4('Carlene ', 'carlene@aqui.com', 1, 2))
print(soma_num4('Carlene ', 'carlene@aqui.com', 1, 2, 3))
print(soma_num4('Carlene ', 'carlene@aqui.com', 1, 2, 3, 4))


# Adicionando outro parâmetros


def verifica_info(*args):
    '''
     Verifica informações fornecidas peo usuário
    :param: args
    :return: a string
    '''
    if 'Geek' in args and 'University' in args:
        return 'Bem-vindo Geek!'
    else:
        return 'Eu naõ tenho certeza quem você é...'


print(verifica_info())
print(verifica_info(1, True, 'University', 'Geek'))
print(verifica_info(1, False, 'University', 4, 5, 6))


"""


# Passando uma lista


def soma3(*args):
    print(args)
    return sum(args)


print(soma3())
print(soma3(1, 2, 3, 4))

# Ao passarmos uma lista recebemos um "TypeError: unsupported operand type(s) for +: 'int' and 'list' "
# lista = [1, 2, 3, 4]
# print(soma3(lista))

# A solução é sar o desempacotamento de lista ou uma forma automática
# O asterisco serve para que informemos ao python que estamos passado como argumento uma coleção de dados
# Isso informa ao Python que antes de usar os dados ele precisa desempacotá-los
# vale tanto para listas [] como sets {}
lista = {1, 2, 3, 4}
print(soma3(*lista))


