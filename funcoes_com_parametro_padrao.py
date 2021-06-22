"""
Funções com parâmetro padão (default parameters)

- São funções onde a passagem de parâmetro é opcional

#Exemplo de função onde a passagem de parâmetro seja opcional

#>>> print('Python é legal')
#>>> print()

# Exemplo de função onde a passagem de parâmetro seja obrigatória

def quadrado(numero):
    return numero**2


print(quadrado(3))


def exponential(num, power):
    return num ** power


print(exponential(2, 3))
print(exponential(3, 2))



Alinha abaixo fornece um erro do tipo TypeError, pois o segundo parâmetro é obrigatório
 print(exponential(3))
#TypeError: exponential() missing 1 required positional argument: 'power'


# refatorando a função exponencial podemos modifica-la para

def exponential2(num, power=2):
    return num ** power


print(exponential2(3))
print(exponential2(2, 3))

OBS1: se o usuário passar somente um parâmetro num, e será calculado o quadrado desse numero por default.
Se o usuário passar dois argumentos, o primeiro será atribuído ao parâmetro num e o segundo ao parâmetro power.

OBS2: Em funções no python, os valores com parâmetros default (padrão) DEVEM estar ao final da declaração

ERRO! SyntaxError: invalid syntax
non-default parameter follows default parameter

def function(num = 2, potencia):
    return num**potencia

# Outro exemplo
def mostra_informacao(curso='Python', instrutor='Carlene'):
    if curso == 'Python' and instrutor:
        return f'Bem-vindo, {instrutor}! Você será o instrutor de Python hoje.'
    elif curso != 'Python' and instrutor != 'Carlene':
        return 'Eu pensei que o curso fosse de Python'
    return f'Bem-vindo ao curso de {curso}'


print(mostra_informacao())
print(mostra_informacao(curso='SQL', instrutor='Marcelo'))
print(mostra_informacao(curso='SQL'))

Vantagens de definir valores default
 1- Evita erros com parâmetros incorretos
 2- Dá mais flexibilidade nas funções
 3- Os códigos ficam mais legíveis


# Quais tipos de dados podemos usar como parâmetro padão?
#>>> Qualquer tipo de dado pode ser usado!

Entre eles:
 números int
 strings
 floats
 Booleans
 listas
 tuplas
 dicionários
 funções ...

 # passando funções como parâmetro

def soma(num1, num2):
    return num1+num2


def mat(num1, num2, fun=soma):
    return fun(num1, num2)


def subtracao(num1, num2):
    return num1-num2


#O default é a soma, ja que nenhuma outra função foi passada
print(mat(2, 3))


#vai realizar a subtração
print(mat(2, 3, subtracao))


#Escopo - Evitar problemas e confusão

# Variável global - São reconhecidas em todo o programa
instrutor = 'Carlene'


def diz_oi():
    return f'Oi, {instrutor}!'


print(diz_oi())


# Variável local - Só é reconhecida dentro do bloco onde foi declarada

def diz_oi_novamente():
    instrutor2 = 'Marcelo'
    return f'Oi, {instrutor2}!'


print(diz_oi_novamente())


OBS: Observe que no exemplo acima, se tivermos uma variável local com o mesmo nome de uma variável global,
 a local terá preferencia

total = 0


# >>> UnboundLocalError: local variable 'total' referenced before assignment
def incremento():
    total= total+1
    return total

print(incremento())

## Uma  maneira de corrigir

total = 0


def incremento():
    #avisando que vamos utilizar a variável global
    global total
    total = total+1
    return total


for i in range(3):
    print(incremento())

# Podemos ter funções declaradas dentro de funções e também tem uma forma especial de escopo de variáveis

def fora():
    contador = 0

    def dentro():
        #indicando que a variável naõ é global mas esta dentro da função anterior
        nonlocal contador
        contador = contador+1
        return contador
    return dentro()


for i in range(3):
    print(fora())
"""



