"""
Meta-caracteres podem ser
 - um ponto . - representa qualquer caractere que por padão não seleciona uma quebra de linha
 - um acento circunflexo ^
 - um cifrão $
 - um asterisco *
 - o sinal de soma +
 - o sinal de interrogação ?
 - chaves { }
 - colchetes [ ] -  conjunto de caracteres
 - barra \
 - barra vertical | pipe ou
 - parênteses ( )

que em geral não podem ser passados diretamente como uma expressão regular. Eles precisam ser passados com um sinal
de uma barra antes para serem reconhecidos como no exemplo abaixo

string = "Este é um teste de expressões teste. regulares."
print(re.search(r'teste\.', string))

# ------------------------------ Exemplo 1 - Caractere | (ou).

# Vamos supor que queremos buscar mais de uma expressão regular. Para isso usamos o caractere pipe | que traduz-se como
# ou. No texto abaixo queremos encontrar  as duas formas em que a palavra Python está escrita, com letra maiúscula e
# minúscula.

texto = ''' Python is an interpreted high-level general-purpose programming language.
            Python's design philosophy emphasizes code readability with its notable
            use of significant indentation. Its language constructs as well as its
            object-oriented approach aim to help programmers write clear, logical code
            for small and large-scale projects. Guido van Rossum began working on python
            in the late 1980s, as a successor to the ABC programming language, and first released
            it in 1991 as Python 0.9.0.
            Python consistently ranks as one of the most popular programming languages.
            João, joão, Maria, maria...
            '''


print(re.findall(r'Python|python', texto))
print(re.findall(r'programming|code', texto))
# Saída
# >>> ['Python', 'Python', 'python', 'Python', 'Python']
# >>> ['programming', 'code', 'code', 'programming', 'programming']



# ------------------------------- Exemplo 2 - Caractere ponto .

# Quando usamos um ponto numa expressão regular estamos pedindo para buscar qualquer coisa que não seja espaço vazio

print(re.findall(r'P.thon', texto))
print(re.findall(r'prog.amming|c.de', texto))

# Mesma saída de antes pois as expressões são procuradas não importa o caractere que esteja no lugar do ponto
# >>>['Python', 'Python', 'Python', 'Python']
# >>>['programming', 'code', 'code', 'programming', 'programming']

# ------------------------------------- Exemplo 2.1
string = "Isso é uma string para teste com expressão regular. codificar. analisar "

# Encontrando qualquer coisa que tenha ar
print(re.findall(r'.ar|.ssã', string))
# saída
# >>>['par', 'essã', 'lar', 'car', 'sar']


# -------------------------------Exemplo 3 - usando colchetes []
# Queremos buscar agora um conjunto de caracteres. Por exemplo os vários Python ou python, ou João e joão
# ou Maria e maria. Poderíamos usar uma barra mas, podemos fazer melhor usando um colchete.

print(re.findall(r'[Jj]oão|[Pp]ython|[Mdfasrtfdm]aria', texto))
# >>>['Python', 'python', 'python', 'Python', 'Python', 'João', 'joão', 'Maria', 'maria']

# podemos usar um range [init-end] dentro da especificação do conjunto de caracteres. Veja abaixo.
# Busca qualquer letra entre a-z minúsculas
print(re.findall(r'[a-z]aria', texto))
# >>> ['maria']

# Busca qualquer letra de A-Z maiúscula
print(re.findall(r'[a-zA-Z]aria', texto))
# >>> ['Maria', 'maria']

# Também podemos enviar range numérico
print(re.findall(r'[Pp]ython[0-9]..', texto))
# >>>['Python0.9']

"""

import re

texto = """ Python is an interpreted high-level general-purpose programming language.
            python's design philosophy emphasizes code readability with its notable
            use of significant indentation. Its language constructs as well as its
            object-oriented approach aim to help programmers write clear, logical code
            for small and large-scale projects. Guido van Rossum began working on python
            in the late 1980s, as a successor to the ABC programming language, and first released
            it in 1991 as Python0.9.0.
            Python consistently ranks as one of the most popular programming languages.
            
            João, joão, Maria, maria...
            """


# --------------------------- Exemplo 4 - flags
# Se fizesse-mos uma busca do tipo abaixo, onde a ultima letra é maiúscula a
# saída retornaria uma lista vazia, pois o python é case sensitive!

print(re.findall(r'[Jj]oãO|[Pp]ythoN|[Mfasrtdm]ariA', texto))
# >>>[]


# Para que isso não aconteça, podemos mandar uma instrução para o python para que ele
# não diferencie letras maiúsculas de minúsculas com um argumento flag=re.I
print(re.findall(r'[Jj]oãO|[Pp]ythoN|[Mfasrtdm]ariA', texto, flags=re.I))

# >>>['Python', 'python', 'python', 'Python', 'Python', 'João', 'joão', 'Maria', 'maria']
