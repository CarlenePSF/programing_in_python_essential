"""

Já vimos os meta-caracteres | (ou), . (qualquer coisa) e [] (conjunto)
Vamos ver agora os  meta-caracteres quantificadores, que são representados pelos símbolos:
 - *   - representa 0 ou n (pode ser ilimitada) repetições
 - +   - representa 1 ou n (pode ser ilimitada) repetições
         pode ser usado num grupo como [a-zA-Z0-9]+
 - ?   - representa 0 ou 1 repetição
 - {}  - especificando as vezes e pode ser equivalente ao quantificadores acima
 - ()

Esses caracteres quantificadores vão quantificar padrões na nossa expressão alvo.
"""

import re

texto = '''Pyyyyyyyyython is an interpreted high-level general-purpose programming language. PYYYYYYYYYYthon's design 
philosophy emphasizes code readability with its notable se of significant indentation. Its language constructs 
as well as its object-oriented approach aim to help programmers write clear, logical code for small and large-scale 
projects. Guido van Rossum began working on pytttttthon in the late 1980s, as a successor to the ABBBBBBC 
programming language, and first released it in 1991 as Pythhhhhhhon 0.9.0. Pythooooooooon consistently ranks 
as one of the most popular programming languages.

João, joão, Maria, maria, joooooooooooooooooooãooooooooooo...'''

# --------------------------------Exemplo 1 - uso do *

# Vamos solicitar que seja verificado no texto acima a presença de todos as formas em que o nome João está escrito.
# passamos a flag para que o python reconheça tanto as letras maiúsculas quanto minúsculas.
print(re.findall(r'jo*ãO', texto, flags=re.I))


# -------------------------------- Exemplo 2 - uso do +


# No texto acima vamos buscar as strings alvo Python e a João. Note que escrevemos propositalmente essas palavras
# algumas vezes com letras repetidas. Como passamos essa instrução para a nossa expressão regular???
# Com o uso de quantificadores!!! Nesse caso passamos o quantificados +, que pode representar 1
# ou ilimitadas repetições de um caractere.

print(re.findall(r'jo+ãO|Py+thon', texto, flags=re.I))


# ------------------------- Exemplo 2.1 - quantificador aplicado a um grupo +

outra_string = '''Várias formas de escrever python: Pythhhhooooonnnnn, python, PPPPpppppython '''

print(re.findall(r'p[a-z]+thon', outra_string, flags=re.I))


homofonos = '''Açooooo e asSSSSSso
               ou Accccennnnto e assssssennnnto
               ou Alllllto e auuuuto
               ou Apressar e apreçar
               ou Brocha e broxa '''

print(re.findall(r'A[a-z]+o', homofonos, flags=re.I))


# ---------------------------- Exemplo 3

# Usando um quantificados podemos aplicar qualquer uma das instruções de expressões regulares
# A linha abaixo encontra todas as ocorrências da palavra python onde o y aparece repetido ais de uma vez
print(re.findall(r'Py+thon', texto, flags=re.I))


# A linha abaixo substitui todas as instancias de python por pelo caractere C
print(re.sub(r'Py+t+h+o+n', 'C', texto, flags=re.I))


# -------------------------- Exemplo 4 - colchetes

# O quantificado { } produz o mesmo resultado que o +, como demonstrado abaixo
print(re.findall(r'Py+t+h+o+n', texto, flags=re.I))


# Podemos especificar um limite inferior para o mínimo de repetições {n, }
print(re.findall(r'Py{1,}t{1,}h{1,}o{1,}n', texto, flags=re.I))


# Podemos ainda especificar uma quantidade fixa de ocorrências com  {n} onde  n vezes
print(re.findall(r'Pytho{9}n', texto))


# Podemos especificar um intervalo {min, max}
print(re.findall(r'Pytho{1,9}n', texto))


# Podemos especificar um limite superior para o máximo de repetições {, n}
print(re.findall(r'pyt{,6}hon', texto))


# OBS: Um quantificador só é aplicado ao objeto que está à sua esquerda
