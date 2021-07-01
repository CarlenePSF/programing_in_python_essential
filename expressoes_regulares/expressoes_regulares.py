"""
Expressões regulares (regular expression)

definição: é uma forma de identificar cadeia de caracteres que contém determinado padão dentro de uma string

Exemplos de utilização:
1 - Num texto que contenha email de várias pessoas, é possível usar expressões regulares para extrair todos
os emails como um  objeto na forma de lista.

2 - Validar campos quando os dados vem do usuário. como criação de CPF ou Ids de identificação

3 - Substituir expressões dentro de uma texto, por exemplo quando utilizamos muitas vezes uma palavra e
queremos substituí-la por outra  (olá -> oi)

Para utilizar expressões regulares, devemos importar o módulo re. Nessa aula vamos usar a funções:

 - findall --> encontra todas as ocorrências da expressão padrão dentro do texto.
 - search --> vai encontrar a primeira ocorrência da expressão e retornar o índice em que a expressão foi encontrada.
 - sub --> substituir alguma coisa dentro do texto.
 - compile --> usada para compilar expressões regulares. Seu uso é interessante quando precisar reutilizar a expressão
              de regular em alguns casos.

# importar o modulo re
# import re

string = "Este é um teste de expressões teste regulares."

# Exemplo 1 - re.search()

# Buscando a palavra 'teste' na string acima e retornando a primeira ocorrência
print(re.search(r'teste', string))

# A saída do programa retorna um objeto Match, onde o span=(init, end) indica a posição onde começa e a posição onde
# termina a expressão, e por ultimo o match= expressão encontrada
# >>> <re.Match object; span=(10, 15), match='teste'>

# Obs: Se a expressão não existir é retornado um valor None
print(re.search(r'teste2', string))
# >>> None


# Exemplo 2 - re.findall()


# Buscando a palavra 'teste' na string acima e retornando uma lista com TODAS as ocorrências da palavra especificada
print(re.findall(r'teste', string))
# Saída
# >>> ['teste', 'teste']


# Obs: Se a expressão não existir é retornado uma lista vazia
print(re.findall(r'teste2', string))
# >>> []

# Exemplo 3 - re.sub()


# Buscando a palavra 'teste' na string acima e substituindo por outra expressão
print(re.sub(r'teste', 'ABC', string))
# Saída
# >>> Este é um ABCD de expressões ABCD regulares.

# OBS: Se quisermos fazer a substituição somente em 1 ocorrência passamos o parâmetro count após a passagem da string
# que queremos modificar, como abaixo
print(re.sub(r'teste', 'ABC', string, count=1))
# Saída
# >>> Este é um ABC de expressões teste regulares.


# Obs: Lembre-se que Python é case sensitive, isto quer dizer que a string 'Teste' é diferente de 'teste'
# Portanto devemos ficar atento quanto forma da escrita da expressão que estamos passando.
# Para isso existe o uso de flags. que será visto posteriormente.

"""

import re


string = "Este é um teste de expressões teste regulares."

# Exemplo 4 - re.compile()

# Nos exemplos acima, repetimos o teste da expressão regular trê vezes fazendo com que o interpretador Python
# compilasse a expressão a cada vez que fosse pedido no códio. Nessa situação, é mais interessante compilar a expressão
# regular uma única vez e utilizar as funções de dentro da expressão regular com o uso do compile

# criamos uma variável que receberá a expressão teste que deve ser compilada pelo menos uma vez
reg_exp = re.compile(r'teste')

# depois reutilizamos a variável para executar as funções search, find all e sub diretamente, como abaixo.
print(reg_exp.search(string))
print(reg_exp.findall(string))
print(reg_exp.sub('DEF', string))


