"""
Funções com retorno

# **** Exemplo de função builtin com retorno e sem retorno ***
numeros = [1, 2, 3]

#removendo o ultimo elemento da lista com .pop()
ret_pop = numeros.pop()
#imprimindo a nova lista modificada
print(f'Retorno de pop: {ret_pop}')


# A saída sera None, pois a função print não retorna nenhum valor
ret_prt = print(numeros)
print(f'Retorno de print: {ret_prt}')


OBS:
#>>> Em Python, quando uma função não retorna nenhum valor o resultado
retornada sera none
#>>> Funções em Python que retornam valores devem retornar estes valores
com a palavra reservada return
# >>> Não precisamos necessariamente criar uma variavel para receber o
retorno de uma função. Podemos passar a execução da função para outras
funções, como o print(), por exemplo.


# Exemplo de função simples mas que não retorna nada

def quadrado_de_7():
    print(7*7)


quadrado_de_7()
#>>> 49


print(f'Retorno de da função ret_quadrado_de_7: {quadrado_de_7()}')
# >>> Retorno de da função ret_quadrado_de_7: None


# Podemos corrigir o exemplo acima com a seguinte definição
# Esse processo, na programação, chama-se REFATORAR

def quadrado_de_7_corr():
    return 7*7


print(f'Retorno de da função ret_quadrado_de_7: {quadrado_de_7_corr()}')
#>>> Retorno de da função ret_quadrado_de_7: 49

# Refatorando o def diz_oi()


def diz_oi():
    return "Oi!"


diz_oi()
# >>> Não retorna nada, porque ninguem esta recebendo o dado para imprimir

print(diz_oi())
# >>> retorna o Oi!, pois o print recebe o valor de retorno


alguem = 'Maria'
print(diz_oi() + alguem)


OBS: Sobre a palavra reservada return
1 - Ela finaliza a função, ou seja, ela sai da execução da função;
2 - Em uma função, podemos ter diferentes returns;
3 - Em uma função, podemos retornar qualquer tipo de dado e até mesmo
multiplos valores;


# Exemplo 1 - Ela finaliza a função, ou seja, ela sai da execução da função;


def diz_oi():
    print("Print executado antes do return...")
    return 'Oi!'
    #A linha abaixo nunca será executada!!!
    print("Print executado após do return...")


print(diz_oi())


# Exemplo 2 - Em uma função, podemos ter diferentes returns;

def nova_funcao():
    variavel = False
    if variavel:
        return 5
    elif variavel is None:
        return 3.5
    return 'ultimo retorno'


print(nova_funcao())

# Exemplo 3 -  Em uma função, podemos retornar qualquer tipo de dado e até mesmo
# multiplos valores;

def outra_func():
    return 2, 3, 4, 5

#desenpacotando
num1, num2, num3, num4 = outra_func()

print(num1, num2, num3, num4)
#>>> 2 3 4 5

#imprime uma tupla
print(outra_func())
#>>> (2, 3, 4, 5)


# Vamos criar uma função para jogar moeda

from random import random, seed

seed()


def joga_moeda():
    #gera um numero pseudo aleatorio no intervalo entre [0,1]
    if random() > 0.5:
        return 'cara'
    return 'coroa'


print(joga_moeda())


# Para importar funções
# >>>  from function_with_returned_values import joga_moeda

# Erros comuns na utilização de um retorno de uma função
# que na verdade não são erros, mas codificação desnecessária

def eh_impar(numero):
    if numero % 2 != 0:
        return True
    return False


print(eh_impar(5))


"""



