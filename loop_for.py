"""
Loop for
loop -> Estrutura de repeticao
for -> uma das estruturas de repeticao

#Na linguagem C:
for(int i = 0; i<10; i++) {
//instrucao do loop
}

#Em Python
for item in range:
 //excussao

Utilizamos loops para iterar sobre sequencias ou sobre valores iteraveis.
exemplos de iteraveis:
- Strings:
    nome = 'Geek University'
- Listas (vetores em 1D):
   listas = [1, 2, 3, 4]
- Range:
    numeros = range(1, 10)
"""


"""
nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)    # vai ser transformado em uma lista


#Exemplo de for iterando em uma string
for letra in nome:
    print(letra)


# Exemplo de for iterando em uma lista
for numero in lista:
    print(numero)


# Exemplo de for iterando sobre um range
#range (valor_inicial, valor_final)
#OBS: valor_final nao incluido

for numero in numeros:
    print(numero)
"""
nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)    # vai ser transformado em uma lista
"""
O enumerate cria tuplas como 
((0, 'G'), (1, 'e'), (2, 'e'), ... (14, 'y'))

for _, letra in enumerate(nome):   # o underline descarta o valor
    #print(nome[i])
    print(letra)

for indice,_ in enumerate(nome):
    #print(nome[i])
    print(indice)

for value in enumerate(nome):
    print(value)
"""
"""
#Pedindo um valor para execucao do loop ao usuario 
qtd = int(input('Quantas vezes o loop deve ser executado?'))
soma = 0
for n in range(1, qtd+1):
    num = int(input(f'Informe {n}/{qtd} valor:'))
    soma = soma + num
print(f'A soma e {soma}')


for letra in nome:
    print(letra, end='')
"""
#Imprimeindo emoticons
# original U+1F60D
# modificado U0001F60D

for num in range(1, 11):
    #print("\U0001F60D" * num)
    print('\U0001F923')

