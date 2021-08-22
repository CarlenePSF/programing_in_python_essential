"""
Seek and Cursors
Vamos entender mais sobre o cursor para leitura de arquivos e como usar a função seek() para manipular o cursor

-- seek() -> Usada para movimentar o cursor pelo arquivo.
          Ela recebe um parâmetro que indica onde queremos colocar o cursor

# ----- Exemplo 1 - uso do cursor

arquivo = open('teste.txt')
print(arquivo.read())

# alinha abaixo não imprime o arquivo
print(arquivo.read())

# movimentando o cursor pelo arquivo com a função seek()
arquivo.seek(0)  # movemos o cursor para a posição zero

# alinha abaixo vai ler novamente o arquivo
print(arquivo.read())

arquivo.seek(29)  # retornando o cursor para a posição 29
print(arquivo.read())

-- readline() -> função que lê o arquivo linha a linha
"""
# ----- Exemplo 2 - lendo linha a linha


arquivo = open('teste.txt')
print(type(arquivo))

print(arquivo.readline())
print(arquivo.readline())


# texto = arquivo.read().split('\n')
# print(len(texto))
# 
# for ele in texto:
#     print(ele)
