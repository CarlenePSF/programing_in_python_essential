"""
Preservando metadados com warps

Metadados -> São dados intrínsecos em arquivos

Wraps -> São funções que envolvem elementos com diversas finalidades

# Problema 1 -


def ver_log(funcao):
    def logar(*args, **kwargs):
        '''Eu sou uma função logar dentro de outra'''
        print(f'Você está chamando {funcao.__name__}')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


# Função que será decorada
@ver_log
def soma(a, b):
    '''Soma dois numeros'''
    return a+b


# teste
print(soma(1, 2))

# Problema
# Esperamos que as saidas abaixo fosse iguais as mostradas ao lado de cada comando.
# Porém não é isso que a saída retorna.
print(soma.__name__)  # soma
print(soma.__doc__)  # Soma dois numeros

# Os metadados retornados estão sendo alterados pela nossa
# função decoradora. Isso pode ser um problema quando estamos criando módulos para bibliotecas, pois quando um
# usuário solicitar as informações de uma dado método, pode ser que essas informações não estarão de acordo com aquilo
# que o método executa.

"""


# Corrigindo com um decorador próprio da linguagem Python

from functools import wraps


def ver_log(funcao):
    @wraps(funcao)   # adicionamos o wrapper
    def logar(*args, **kwargs):
        """Eu sou uma função logar dentro de outra"""
        print(f'Você está chamando {funcao.__name__}')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


# Função que será decorada
@ver_log
def soma(a, b):
    """Soma dois numeros"""
    return a+b


# teste
print(soma(1, 2))

# Repare que agora a saída é como esperado
print(soma.__name__)  # soma
print(soma.__doc__)  # Soma dois numeros
