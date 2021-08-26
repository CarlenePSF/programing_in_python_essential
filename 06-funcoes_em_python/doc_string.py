"""
Documentando funções com docstring
Qualquer comentário que seja importante documentar sobre os procedimentos e
quais são as tarefas da executadas pela função.

OBS: Podemos ter acesso a documentação (docstring) em python utilizando a propriedade especial .__doc__
     podemos usar também uma função built in help()
#Exemplo

def diz_oi():
    '''Isso é um docstring: uma função simples que retorna a string oi'''
    return 'oi!'


print(diz_oi())
print(diz_oi.__doc__)

"""


def exponential(num, power=2):
    """
    Função que por padrão retorna a potencia de um numero num elevado à potência power, por padrão 2,
    ou informada pelo usuário
    param num:
    param power:
    return: num ** power
    """
    return num ** power


print(exponential(2))
print(exponential(2, 16))
print(exponential.__doc__)
