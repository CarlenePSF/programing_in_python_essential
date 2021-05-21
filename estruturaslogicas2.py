""":cvar
Estruturas logicas: and (e), or (ou), not (não), is(é)

operadores unários:
    - not,

operadores binários:
    - and, or, is


Para o end ser verdadeiro ambos as declaracoes precisam ser verdadeiras. Caso contrario sera falso.
Para o or ser verdadeiro, ou uma ou outra declaracao deve ser verdadeira. Caso contrario sera falso.
Para o not, o boleano e invertido
"""

ativo = False
logado = True
'''
if ativo and logado:
    print('Bem-vindo usuarios!')
else:
    print('Voce precisa ativar a sua conta. Por favor, verifique o seu email ')

if not ativo:
    print('Voce precisa ativar a sua conta. Por favor, verifique o seu email ')
else:
    print('Bem-vindo usuario')
'''
if ativo is True and logado is True:
    print('Bem-vindo!')

elif ativo is False and logado is False:
    print('Voce precisa ativar a sua conta. Por favor, verifique o seu email ')

elif ativo is True or logado is False:
    print('Bem-vindo!')

elif ativo is False or logado is True:
    print('Bem-vindo!')



