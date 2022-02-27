"""
Módulos Customizados
Como módulos Python nada mais são do que scripts em python, então todos os programas
ou todos os arquivos que são criados na estrutura de uma projeto, são módulos Python prontos para serem utilizados
como os arquivos desse projeto programacao_em_python_ess

# Exemplo 1  - importando uma função específica do nosso módulo


from meu_modulo import soma_impares
print(soma_impares([1, 3, 5, 8, 6]))

"""

# Exemplo 2 - importando o módulo inteiro (acesso a todos os elementos do módulo)


import meu_modulo as mm
print(mm.soma([1, 3, 5, 8, 6]))

print(mm.diz_oi('Geek'))
