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


# Para utilizar o Python debugger, precisamos * importar a biblioteca pdb
# e então utilizar a função set_trace()

A partir do Python 3.7, não é mais necessário importar a biblioteca pdb pois o comando de debug foi incorporado como
função built-in (função integrada) chamada breakpoint()

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


# ------ Exemplo 2 com PDB ------


nome = "John"
sobrenome = "Doe"
# import pdb; pdb.set_trace()  # quando queremos executar dois comando por linha separamos por ;
nome_completo = nome + ' ' + sobrenome
curso = "Programação em python Essencial"
final = nome_completo + ' faz o curso ' + curso
print(final)

# Por que utilizar este formato para debug?

# O debug é utilizado durante o desenvolvimento. Costumamos, realizar todos os imports de bibliotecas no
# início do código. Como o PDB só será usado onde queremos detectar problema, podemos fazer o import somente
# onde vamos debuggar. Ao finalizar o debug, removemos imediatamente o pdb!!!

# ------ Exemplo 3 com breakpoint ------

nome = "John"
sobrenome = "Snow"
breakpoint()
nome_completo = nome + ' ' + sobrenome
curso = "Programação em python Essencial"
final = nome_completo + ' faz o curso ' + curso
print(final)
"""


# OBS: Cuidado com conflitos entre nomes de variáveis e os comandos do pdb
# Veja exemplo abaixo.
# ------ Exemplo 4 ------
def soma(l, n, p, c):
    breakpoint()
    print(l + n + p + c)


soma(1, 3, 5, 7)


# Como o nome das variáveis são os mesmo do pdb debugger, podemos usar o comando p antes do nome
# da variável para imprimir o valor que ela armazena, p <nome_da_var>

# O ideal é usar nome significativos e representativos para cada variável ;) !!!!
# Como o exemplo abaixo
def soma_2(num1, num2, num3, num4):
    breakpoint()
    print(num1+num2+num3+num4)
