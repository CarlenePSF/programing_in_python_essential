"""
Erros mais comuns em Python

Atenção: É importante prestar atenção e a prender a ler as saídas de erros geradas pela execução do nosso código.

# A linha abaixo fornece um NameError
# printf('geek Univerity')
# Algumas IDEs, como o PyCharm, oferecem a alternativa de refatorar o código ou cria uma funçãochamada 'printf'

     Os erros mais comuns:
# -----------------------------------
1 - SyntaxError --> Ocorre quando o Python encontra um erro de sintaxe. Ou seja, você escreveu algo que o python
não reconhece como parte da linguagem.

 Exemplo de SyntaxError

# (a)
def funcao:
    print('Geek University')

# def funcao:
#          ^
# SyntaxError: invalid syntax

# (b)
None = 1

# None = 1
#     ^
# SyntaxError: cannot assign to None

# (c)
   return


# -----------------------------------
2 - NameError --> Ocorre quando uma variável ou função não foi definida.

# Exemplos de NameError

(a)
# >>> print(geek)
NameError: name 'geek' is not defined

(b)
# >>> geek()
NameError: name 'geek' is not defined

(c)
No exemplo abaixo o código nunca entra no condicional porque o valor da variável global não é menor que 10
consequentemente, a variável local msg não é criada retornando o NameError
# >>> a = 18
# >>> if a < 10:
# >>>     msg = 'É maior que 10'
# >>> print(msg)
NameError: name 'msg' is not defined


# -----------------------------------
3 - TypeError --> Ocorre quando uma função, operação ou ação é aplicada a um tipo errado

# Exemplos de TypeError

(a)
# A função len só pode ser usada com tipos de dados específicos como listas, tuplas, conjuntos
# No exemplo abaixo fornecemos um número inteiro como argumento da função. Logo a saída gera um TypeError
print(len(5))
# TypeError: object of type 'int' has no len()

(b)
# O comando abaixo pede para concatenar dois tipos de dados que são incompatíveis, isto é, uma string e uma lista.
print('Geek' + [1, 2, 3])
#TypeError: can only concatenate str (not "list") to str

# -----------------------------------
4 - IndexError --> Comum quando tentamos acessar um elemento em uma lista ou outro tipo de dado indexado utilizando
                   um índice inválido.
# Exemplos de IndexError

(a)
# A lista abaixo só possui um único elemento indexado na posição 0
lista = ['Geek']
print(lista[1])
# IndexError: list index out of range

# A linha abaixo funciona corretamente
print(lista[0][1])

# A linha abaixo retorna um IndexError
print(lista[0][10])

# -----------------------------------
5 - ValueError --> Ocorre quando uma função/operação built-in (integrada) recebe um argumento com tipo correto, mas
                   valor inapropriado.

# Exemplos de ValueError

(a)
# A linha abaixo funciona corretamente.
print(int('45'))
# A linha abaixo não funciona. porque o valor da string é inapropriado.
print(int('Geek'))


# -----------------------------------
6 - KeyError --> Ocorre quando tentamos acessar um calor num dicionário cuja chave não existe!


# Exemplos de KeyError

(a)
dicio = {'Geek': 'University'}
# A linha abaixo funciona corretamente
print(dicio['Geek'])

# A linha abaixo retorna um KeyError
print(dicio['geek'])

# -----------------------------------
7 - AttributeError --> O corre quando uma variável não tem um atributo/função

# Exemplos de AttributeError

# A linha abaixo retorna um AttributeError, porque o método .sort() não pode ser aplicado à dados em uma tupla
tupla = (11, 2, 31, 4)

# A linha abaixo retorna um AttributeError, porque o método .sort() não pode ser aplicado à dados em uma tupla
print(tupla.sort())
# AttributeError: 'tuple' object has no attribute 'sort'

# -----------------------------------
7 - IndentationError --> Ocorre quando não respeitamos a indentação no python- 4 espaços para um novo bloco.

# Exemplos de IndentationError
(a)
# A declaração da função abaixo retorna um IndentationError
def soma(a, b):
return a+b
^
# IndentationError: expected an indented block

(b)
for i in range(10):
print(i+10)
#     print(i+10)
#     ^
# IndentationError: expected an indented block

"""
