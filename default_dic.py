"""
Modulo collection - Default Dict

# Recapitulando dicionários
dicionario = {'curso': 'Programação em Python: essencial'}

print(dicionario)
print(dicionario['curso'])

# A entrada de uma chave que nao consta no dicionario retorna um KeyError
# como na linha abaixo
#>>>print(dicionario['instrutor'])

Default Dict -> Ao criar um dicionario utilizando o default dict, informamos
                um valor default, podendo utilizar um lambda para este fim.
                Esse valor sera sempre usado quando nao houver um valor definido
                Caso tentemos acessar uma chave que nao existe, essa chave sera criada
                e o valor default sera atribuído
OBS: Lambdas sao funções sem nome que podem ou nao receber parâmetros de entrada e retornar
     valores

"""


# Importando módulos


from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario['curso'] = "Programação em Python: Essencial"
# print(dicionario)

# Entrando com uma chave que nao existe no dicionario o KeyError nao sera
# impresso
print(dicionario['outro'])
print(dicionario)
