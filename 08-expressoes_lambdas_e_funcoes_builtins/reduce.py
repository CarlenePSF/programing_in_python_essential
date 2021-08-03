"""
Reduce

OBS: A partir do python 3 a função reduce() não é mais uma função integrada (builtin)
     Agora temos que importar e utilizar esta função a partir do módulo 'functools'

Guido van Rossum: "Utilize a função reduce se você realmente precisa dela. Em todo caso,
                   99% das vezes um loop for é mais legível."


Para entender o reduce()

-> imagine que temos uma coleção de dados:
dados = [a1, a2, a3, ..., an]

e temos uma função que recebe dois parâmetros:
def funcao(x, y):
    return x+y


Assim como o map() e o filter(), o reduce() também recebe dois parâmetros: uma função e um iterável.

A função reduce funcionada da seguinte forma:
    passo 1: res_1 = f(a1, a2) # aplica a função nos dois primeiros elementos da coleção
            e guarda o resultado.
    passo 2: res_2 = f(res1, a3) # aplica a função passando o resultado do passo um mais o terceiro elemento.
            O resultado é novamente guardado
    passo 3: res_3 = f(res2, a4)
    .
    .
    .
    passo n: res_n = f(res_n-1, an)

Isso é repetido até o final da lista de dados.

Ou seja, em cada passo a função é aplicada, passando como primeiro argumento o resultado do passo anterior.
No final, reduce() irá retornar o resultado final.

De maneira alternativa, podemos ver a função reduce() como uma função composta
funcao( funcao(...(...funcao(funcao(a1, a2),a3), a4))..., an-1),  an)
"""
# exemplo na prática
# multiplicando todos os números de uma lista com o reduce()

from functools import reduce

dados = [2, 3, 4, 5]

# para usar o reduce, precisamos de uma função que recebe dois parâmetros

res = reduce(lambda x, y: x*y, dados)
print(res)

# usando um loop normal
res2 = 1
for n in dados:
    res2 = res2*n
print(res2)
