"""
Debugando com PDB

PDB --> Python debugger

Bug --> inseto = problema


# A maneira mais tradicional usada até mesmo por programadores experientes é o print() de dados
# No entanto, essa é uma prática ruim
# ------ Exemplo com o print() ------

def divisao(a, b):
    print(f'a={a}, b={b}')
    try:
        return f'A divisão do número é {int(a)/int(b)}'
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'


print(divisao(4, 7))


# Existem formas mais profissionais de se fazer esse debug utilizando o debugger
# Em Python, podemos fazer isso em diferentes IDE's, como o PyCharm, ou utilizando o PDB - Python debugger
# ------ Exemplo com PyCharm ------

def divisao(a, b): # coloca um breakpoint
    try:
        return int(a)/int(b) # coloca outro breakpoint
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'


print(divisao(4, 0))


# Para utilizar o Python debugger, precisamos* importar a biblioteca pdb
# e então utilizar a função set_trace()

# comando básico do PDB para usar no terminal
# l - para listar onde estamos no código
# n - próxima linha
# p - imprime variável
# c - continua a execução, ou seja, finaliza o debug

# ------ Exemplo 1 com PDB ------
import pdb

nome = "John"
sobrenome = "Doe"
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = "Programação em python Essencial"
final = nome_completo + ' faz o curso ' + curso
print(final)
"""

# ------ Exemplo 2 com PDB ------


nome = "John"
sobrenome = "Doe"
import pdb; pdb.set_trace()  # quando queremos executar dois comando por linha separamos por ;
nome_completo = nome + ' ' + sobrenome
curso = "Programação em python Essencial"
final = nome_completo + ' faz o curso ' + curso
print(final)

# Por que utilizar este formato?
# O debug é utilizado durante o desenvolvimento. Costumamos, realizar todos os imports de bibliotecas no
# início do código. Como o PDB só será usado onde queremos detectar problema, podemos fazer o import somente
# onde vamos debuggar. Ao finalizar o debug, removemos imediatamente o pdb!!!
