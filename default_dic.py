"""
Modulo collection - Default Dict

# Recapitulando dicionarios
dicionario = {'curso': 'Programacao em Python: essencial'}

print(dicionario)
print(dicionario['curso'])

# A entrada de uma chave que nao consta no dicionario retorna um KeyError
# como na linha abaixo
#>>>print(dicionario['instrutor'])

Default Dict -> Ao criar um dicionario utilizando o default dict, informamos
                um valor default, podendo utilizar um lambda para este fim.
                Esse valor sera sempre usado quando nao houver um valor definido
                Caso tentemos acessar uma chave que nao existe, essa chave sera criada
                e o valor default sera atribuido
OBS: Lambdas sao funcoes sem nome que podem ou nao receber parametros de entrada e retornar
     valores

"""

#Importando modulos

from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario['curso'] = "Programacao em Python: Essencial"
#print(dicionario)

# Entrando com uma chave que nao existe no dicionario o KeyError nao sera
# impresso
print(dicionario['outro'])
print(dicionario)
