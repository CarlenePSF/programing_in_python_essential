"""
Funções com parâmetro (de entrada)

- Funções que recebem dados para serem processados dentro do seu corpo de instrucoes

Num programa qualquer, a lógica de execução de tarefas segue o padrão:
#>>> entrada -> processamento de dados -> saída

Sobre funções me Python, já sabemos que existem tipos que:
1 - Não possuem entrada;
2 - Não possuem saída;
3 - Possuem entrada, mas não saída;
4 - Não possuem entrada, mas possuem saída;
5 - Possuem entrada e saída


# Exemplo 1
#Refatorando uma função
#>>>def quadrado_de_numero():
#>>>    return 7**2


def quadrado(numero):
    return numero**2


print(quadrado(2))
print(quadrado(8))
print(quadrado(4))


# Se tentarmos executar a função sem passar o parâmetro obrigatório
# um erro do tipo TypeError será retornado

#print(quadrado())
#>>>TypeError: quadrado() missing 1 required positional argument: 'numero'

# Exemplo 2
#Refatorando a função canta parabéns
#passando uma string com o nome do aniversariante


def canta_parabens(nome):
    print("Parabéns para você!")
    print("Nesta data querida,")
    print("Muitas felicidades,")
    print("Muitos anos de vida!")
    print(f'Viva  {nome}!!!')


canta_parabens('Maria')


# Funções podem ter n parâmetros de entrada.
# Ou seja, podemos receber como entrada de uma função tantos parâmetros
# quanto forem necessários


def soma(a, b):
    return a+b


def multiplica(num1, num2):
    return num1*num2


def outra(num1, b, mensagem):
    return (num1+b)*mensagem


print(soma(5, 3))
print(multiplica(5, 3))

print(outra(5, 3, 2))
print(outra(5, 3, 'Geek '))


# OBS.: Se informamos um numero errado de parâmetros ou argumentos,
# receberemos um TypeError
# soma(2, 3, 5)
#>>> TypeError: soma() takes 2 positional arguments but 3 were given


#                  Como nomear parâmetros?
# O ideal é nomear os parâmetros com nomes que tenham sentido

#       A diferença entre parâmetro x argumento
# parametros são variáveis declaradas na definição de uma função
# Argumentos são dados passados durante a execução de uma função

#nome, sobrenome são parâmetros
# Note que é importante a ordem de passagem dos parametros!!!!
def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'


#As strings 'John' e 'Doe' são argumentos que serão passados
# para a função nome_completo
print(nome_completo('John', 'Doe'))

# Argumentos nomeados: mais conhecidos na programação como Keyword Arguments

# Caso utilizemos nomes dos parâmetros nos argumentos para informá-los,
# podemos utilizar qualquer ordem

print(nome_completo(nome='John', sobrenome='Doe'))
#>>> A ordem com os argumentos nomeados pode ser invertida!
print(nome_completo(sobrenome='Doe', nome='John'))

"""

# Erro comum na utilização do return


def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total+num
    return total


lista = [1, 2, 3, 4, 5, 6, 7]

print(soma_impares(lista))


