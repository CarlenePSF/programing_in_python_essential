"""
Recebendo dados do usuário
input() -> Todo dado recebido via input e uma string

Em python, uma string e tudo que estiver entre
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duas triplas;


EXEMPLO

- Aspas simples -> 'String'
- Aspas duplas -> "string"
- Aspas simples triplas -> '''string'''
"""
# - Aspas duplas triplas -> """string"""


"""
# Entrada de dados

#print('Qual o seu nome? ')
#nome = input()


#Exemplo de print antigo com python 2.X
#print('Seja bem-vindo(a) %s !', nome)

#exemplo de print moderno criado a partir das versoes 3.X
print{'Seja bem-vindo(a) {0}'.format(nome)}

#exemplo de print mais atual versoes 3.7 em diante
print(f'Seja bem-vindo(a) {nome}!')


#print('Qual a sua idade')
idade = input()

# Processamento

# Saida de dados
#exemplo de print antigo 2.X
print( "%s tem %s de idade" % (nome, idade))

#exemplo de print moderno
print{'A {0} tem {1} anos'.format(nome,idade)}

''':cvar
int(idade) => cast 
Cast e a conversao de um tipo de dado para outro
'''

print(f'A {nome} nasceu em {2021- int(idade)}')

"""

""":cvar
#De forma resumida, o programa para receber dados poderia ser escrito como abaixo
"""



nome = input('Qual seu nome?')
print(f'Seja bem-vindo(a) {nome}!')
idade = input('Qual a sua idade?')
print(f'A {nome} nasceu em {2021- int(idade)} e tem {idade} anos ')
print("%s tem %s de idade" % (nome, idade))

