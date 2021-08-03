"""
- Precisamos entender o loop for para usar a função range
- precisamos conhecer a função range para trabalhar melhor o loop for
Ranges são utilizados para gerar sequências numéricas,
 não de forma aleatória, mas de maneira especificada

Formas gerais:
1- range(valo_de_parada)

OBS: o valor_de_parada non inclusive
(inicio padrao em 0, e passo de 1 em 1.)


2- range(valor_de_inicio, valor_de_parada)

OBS: valor de parada is non inclusive
(inicio especificado pelo usuario e passo de 1 em 1)


3- range(valor_de_inicio, valor_de_parada, passo)

OBS: valor de parada is non inclusive
(inicio especificado pelo usuario, e passo especificado pelo usuario)


4- inversa
range(valor_de_inicio, valor_de_parada, passo)

OBS: valor de parada is non inclusive
(valor inicial especificado pelo usuario, e passo especificado pelo usuario)


"""


"""
#----------------------------
# Exemplo: Forma 1
#  range(valo_de_parada)
#----------------------------
for num in range(11):
    print(num)
"""

"""
#----------------------------
# Exemplo: Forma 2
#   range(valor_de_inicio, valor_de_parada)
#----------------------------
for num in range(1, 11):
    print(num)
"""
"""
#----------------------------
# Exemplo: Forma 3
#   range(valor_de_inicio, valor_de_parada, passo)
#----------------------------

for num in range(0, 55, 5):
    print(num)
"""

#----------------------------
# Exemplo: Forma 4
#   range(valor_de_inicio, valor_de_parada, passo)
#----------------------------

for num in range(10, 0, -1):
    print(num)

for num in range(10, -1, -1):
    print(num)
