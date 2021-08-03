"""
Escopo de variaveis
Dois casos de escopo:

1- Variaveis glocais
    - sao reconhecidas em todo o programa, ou seja, seu escopo compreende todo o programa
2 - Variaveis locais
    - variaveis locais sao reconhecidas apenas no bloco em que foram declaradas, ou seja,
      seu escopo esta limitado ao bloco onde foram decladas
      
Para declarar variaveis em Python utilizamos a seguinte nomenclatura:

nome_da_variavel = valor_da_variavel

Python e uma linguagem de tipagem dinamica.
Isso significa que ao declararmos uma variavel, nao colocamos o tipo de dado que ela armazena.
Este tipo e inferido ao atribuirmos o seu valor

exemplo:

Em C:
    int numero = 42;
Em Java:
    int numero = 42;
"""

numero = 42
print(numero)
print(type(numero))

numero = 'Geek'
print(numero)
print(type(numero))
