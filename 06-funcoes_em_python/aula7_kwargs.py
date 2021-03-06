"""
 Uso do **kwargs

Poderíamos chamar este parâmetro de **x ou ** qualquer_coisa. Mas por convenção usamos **kwargs.
O **kwargs é só mais um parâmetro, porém, diferente do *args que coloca os valores extras em uma tupla,
o **kwargs exige que seja utilizado parâmetros nomeados, e transforma-os em um dicionário.

# Exemplo


def cores(**kwargs):
    print(kwargs)


cores( Maria='verde', Luiz='laranja', Julia='amarelo', Eduardo='azul')


# Saida
# >>> {'Maria': 'verde', 'Luiz': 'laranja', 'Julia': 'amarelo', 'Eduardo': 'azul'}


def cores_favoritas(**kwargs):
    ''' Mais um teste com o **kwargs com uma iteração no dicionario do feito no kwargs
    :param: kwargs
    :return:
    '''
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')


cores_favoritas(maria='verde', luiz='laranja', julia='amarelo', eduardo='azul')


#OBS: Nem os parâmetros *args e **kwargs são obrigatórios

cores_favoritas()

cores_favoritas(Juliana='roxo')

# Exemplo 3

def saudacao(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Saudações Pythonicas, Geek!!!'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek"
    return 'Não tenho certeza quem você é...'


print(saudacao())
print(saudacao(geek='Python'))
print(saudacao(geek='oi!'))
print(saudacao(geek='especial!'))


# As funções podem conter:
# 1) Parâmetros obrigatórios,
# 2) *args,
# 3) Parâmetros default (não obrigatórios)
# 4) **kwargs
# SEMPRE NESSA ORDEM !!!!!


def outra_funcao(idade, nome, *args, estado_civil=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if estado_civil:
        print('Solteiro(a)')
    else:
        print('Casado(a)')
    print(kwargs)


outra_funcao(18, 'Maria')
outra_funcao(32, 'Carlene', 1, 2, 3, estado_civil=True)
outra_funcao(28, 'Julia', eu='não', voce='vai')
outra_funcao(42, 'Henrique', 9, 8, 7, estado_civil=True, java=False, python=True)

# Saída

# Maria tem 18 anos
# ()
# Casado(a)
# {}
# Carlene tem 32 anos
# (1, 2, 3)
# Solteiro(a)
# {}
# Julia tem 28 anos
# ()
# Casado(a)
# {'eu': 'não', 'voce': 'vai'}
# Henrique tem 42 anos
# (9, 8, 7)
# Solteiro(a)
# {'java': False, 'python': True}


# Função com a ordem correta de parâmetros


def mostra_resultados(a, b, *args, instrutor='Geek', **kwargs):
    return [a, b, args, instrutor, kwargs]


# A saida que esperamos para a execução
# a = 1
# b = 2
# args = (3)
# instruto = 'Geek'
# kwargs = {
#          'sobrenome': 'University',
#          'cargo': 'instrutor'
#          }


print(mostra_resultados(1, 2, 3, sobrenome='University', cargo='instrutor'))
# Saida:
# >>> [1, 2, (3,), 'Geek', {'sobrenome': 'University', 'cargo': 'instrutor'}]

# Função com a ordem incorreta de parâmetros


def mostra_resultados2(a, b, instrutor='Geek',  *args, **kwargs):
    return [a, b, args, instrutor, kwargs]


# A saida que esperamos para a execução
# a = 1
# b = 2
# args = (3)   #Tupla
# instruto = 'Geek'
# kwargs = {
#          'sobrenome': 'University',
#          'cargo': 'instrutor'
#          }


print(mostra_resultados2(1, 2, 3, sobrenome='University', cargo='instrutor'))
# Saida:
# >>> [1, 2, (), 3, {'sobrenome': 'University', 'cargo': 'instrutor'}]



# Desempacotando o **kwargs

def mostra_nome(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nomes = {
    'nome': 'Julia',
    'sobrenome': 'language'
    }
# Note o uso do duplo asterisco
print(mostra_nome(**nomes))
"""

from collections import defaultdict


def soma_num(a, b, c):
    print(a+b+c)


# em forma de *args
lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}

soma_num(*lista)
soma_num(*tupla)
soma_num(*conjunto)

# em forma de *kwargs

dic = defaultdict(list)
dicionario = dict(a=1, b=2, c=3)
soma_num(**dicionario)


# ATENÇÃO: OS nomes das chaves em um dicionario devem ser os mesmo dos parâmetros da função
