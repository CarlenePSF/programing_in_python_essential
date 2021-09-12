"""
Filtros em Python
Uso mais comum de expressões lambdas

filter() -> Serve para filtrar dados de uma determinada coleção

# Exemplo 1

from statistics import mean

# Dados coletados
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
valores = 1, 2, 3, 4, 5, 6


media_dados = mean(dados)
media_valores = mean(valores)
print(media_dados)
print(media_valores)

# Queremos filtrar os valores acima da média
# Assim como a função map(), a função filter() recebe dois parâmetros
# sendo uma função e um iterável.
# como função vamos passar uma função lambda

res_dados = filter(lambda x: x > media_dados, dados)
print(type(res_dados))
print(list(res_dados))

res_valores = filter(lambda y: y > media_valores, valores)
print(type(res_valores))
print(list(res_valores))

# Novamente, os dados com o filter só ficam na memoria para a primeira utilização
# Como podemos ver pela saída abaixo
print(f'Novamente: {list(res_dados)}')
# >>> Novamente: []


# Exemplo 2 - filtro para dados faltantes

America_latina = ['', 'Brasil', 'Venezuela', 'Mexico', '', 'Colombia', 'Chile']
print(America_latina)

# Forma simples e elegante
novo_amarica_latina = filter(None, America_latina)
print(list(novo_amarica_latina))

# Outra forma de resolver com um lambda
novo_latina = filter(lambda pais: len(pais) > 0, America_latina)
print(list(novo_latina))

# Terceira forma
novo2 = filter(lambda pais: pais != '', America_latina)
print(list(novo2))


# Exemplo mais complexo onde a filtragem pode ser empregada

users = [
    {'username': "Sara", 'tweets': ["Python é legal!", "Mais mulheres no tech"]},
    {'username': "Samantha", 'tweets': []},
    {'username': "Nick", 'tweets': []},
    {'username': "Samuel", 'tweets': ["Fui selecionado para o BBB22! :O", "#Vamosjuntos#BBB22!"]},
    {'username': "Luna", 'tweets': ["#ForaBolsonaro", "#ForaBolsonaro"]},
    {'username': "Luana", 'tweets': ["#Salescaiu!", "#ForaBolsonaro"]},
    {'username': "John", 'tweets': []},
    ]

print(users)

# Tarefa: filtrar os usuários que estão inativos no tweeter ( os que não tuitaram nenhuma vez)

# Forma 1
inativo = list(filter(lambda user: len(user['tweets']) == 0, users))
print(inativo)

# forma 2
inativo2 = list(filter(lambda user: not user['tweets'], users))
print(inativo2)


# Combinando filter() e map()

nomes = ['Vanessa', 'Ana', 'Maria']

# Tarefa: criar uma lista contendo a seguinte string  'Sua instrutora é' + nome, desde que cada nome tenha menos de
# cinco caracteres

instrutores = list(filter(lambda nome: len(nome) < 5, nomes))
# print(instrutores)

frase = list(map(lambda nome: 'Sua instrutora é ' + nome, instrutores))
print(frase)
"""

#  ******************** Vamos Praticar! ***********************

"""
4 - Faça um programa que solicite cinco números ao usuário, depois disso, exiba apenas os números maiores do que 10.
    Utilize a função filter para fazer isso.


# pode usar um loop ou list comprehension (como no próximo exemplo)
data = []
for i in range(5)
    dado = float(input("Digite um numero: "))
    data.append(dado)

# Ou

data = [float(input("Digite um numero: ")) for i in range(5)]

print(list(filter(lambda num: num > 10, data)))
"""

"""
5 - Faça um programa que solicite dez números ao usuário, depois disso, exiba todos números pares e só então exiba 
    todos os números ímpares. Utilize a função filter para fazer isso.

data2 = [float(input("Digite um numero: ")) for i in range(10)]
print(list(filter(lambda num: num % 2 == 0, data2)))
print(list(filter(lambda num: num % 2 != 0, data2)))
"""


dados = [1, 1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 7, 7, 7, 7, 7, 8, 8, 9]

dados_dup = {i for i in dados if dados.count(i) == 2}
print(dados_dup)

print(set(filter(lambda num: dados.count(num) >= 2, dados)))
