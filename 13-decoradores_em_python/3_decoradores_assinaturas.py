"""
Decorators com diferentes assinaturas

# Relembrando


def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá, eu sou o/a {nome}'


@gritar
def order_food(principal, acompanhamento):
    return f'Olá! Eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor!'


# Teste
# print(saudacao('Angelina'))

# Teste 2
# Retorna um erro TypeError: aumentar() takes 1 positional argument but 2 were given
print(order_food('lasanha', 'salada verde com tomates'))

# Para corrigir esse erro, utilizamos um padrão de projeto chamado Decorator Pattern, que nada mais são
# do que o *args e o *kwargs



# Refatorando com o decorator patter

def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá, eu sou o/a {nome}'


@gritar
def order_food(principal, acompanhamento):
    return f'Olá! Eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor!'


# Teste após refatorar - 1
print(saudacao('Angelina'))

# Teste após refatorar - 2
print(order_food('lasanha', 'salada verde com tomates'))


# A assinatura de uma função é representada pelo seu retorno, nome e parâmetros de entrada.
@gritar
def lol():
    return 'lol'


print(lol())

# OBS: Vale lembrar que podemos utilizar parâmetros nomeados, como no exemplo abaixo

print(order_food(acompanhamento='batata frita', principal='bife'))

"""

# Decorator com argumentos - com parâmetro de entrada


def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto. Primeiro argumento precisa ser {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna


@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    print(args)


@verifica_primeiro_argumento(10)
def soma_dez(num1, num2):
    return num1 + num2


print(soma_dez(10, 12))  # 22

print(soma_dez(1, 21))  # Valor incorreto. Primeiro argumento precisa ser 10

print(comida_favorita('pizza', 'lasanha'))

print(comida_favorita('Torta', 'lasanha'))
