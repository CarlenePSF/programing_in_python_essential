"""
# Funções em Python

- Funções são pequenas partes de códigos que realizam tarefas específicas;
- Podem, ou não, receber entradas de dados e retornar, ou não, uma saída de dados;
- São muito úteis para executar procedimentos similares por repetidas vezes

OBS: Se escrevermos uma função que realiza várias tarefas dentro dela, o ideal
é fazer uma verificação para que a função seja simplificada

Já utilizamos muitas funções implicitamente, tais como
->>> print()
->>>len()
->>> max()
->>>min()
->>>count()
... muitas outras

# **** Exemplo de função built-in do Python 'print()'

cores = ['verde', 'vermelho', 'azul', 'branco']
print(cores)

curso = 'Programação em Python'

print(curso)
# A função .append() é local para uso com listas
cores.append('amarelo')
print(cores)
# A função .clear() não recebe parâmetros
cores.clear()
print(cores)


# Alinha abaixo retorna um erro do tipo AttributeError,
# pois a função .append() só é usada com determinado tipo de dado
# como listas, coleções, tuplas, etc...
#>>> AttributeError: 'str' object has no attribute 'append'
#>>> curso.append('Calculo I')
#>>> print(curso)


print(help(print()))

#DRY - Don't repeat yourself - Não repita você mesmo /
# Não repita seu código. Principio da programação

#***  Definindo funções ***
Em python a forma geral para sintaxe de funções é como abaixo

def nome_da_função(parâmetros_de_entrada):
    bloco_da_função

onde:

nome_da_função ->> SEMPRE com letras minúsculas, e se for nome composto,
                   separado por underline;
parâmetros_de_entrada->> Os parâmetros são opcionais, se tiver
                         mais de um parâmetro, eles devem ser
                         separados por vírgula;
bloco_da_função ->> Também chamado de corpo da função ou implementação.
                    É onde o processamento da função acontece. Neste bloco
                    pode ter, ou não, retorno da função;

OBS: Para definir uma função, utilizamos uma palavra reservada da linguagem
Python 'def'. Isso informará ao Python que estamos definindo uma função.
O bloco de código que será executado é aberto com o sinal de dois pontos - :

"""

# *** Exemplo 1
# Definição da função


def diz_oi():
    print("Oi!")

# OBS do exemplo acima:
# ->> Veja que dentro da nossa função executamos outras funções. No caso do exemplo acima a função built-in print();
# ->> A função só executar 1 tarefa, ou seja, imprimir a palavra "Oi!";
# ->> Essa função não recebe parâmetros de entrada
# ->> A Função não retorna nenhum valor

#Chamando a função
diz_oi()
# ATENÇÃO : Sempre utilizar o parêntese!!
# ERRADO: >>> diz_oi
# CORRETO: >>> diz_oi()


# *** Exemplo 2 -


def canta_parabens():
    print("Parabéns para você!")
    print("Nesta data querida,")
    print("Muitas felicidades,")
    print("Muitos anos de vida!")
    print("Viva o aniversariante")

# Podemos executar loops na funções
#for i in range(5):
#    canta_parabens()


# Em python, podemos, inclusive, criar variáveis do tipo de uma função e executar esta função através da variável
# Note a seguinte passagem de parâmetros
# No entanto essa forma pode confundir! o indicado é usar o nome de definição da funcção.
canta = canta_parabens
canta()
