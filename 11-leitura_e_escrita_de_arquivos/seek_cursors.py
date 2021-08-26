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

# ----- Exemplo 2 - lendo linha a linha

arquivo = open('teste.txt')
print(type(arquivo))

# Como o arquivo contém 7 linhas pedimos para a imprimir 7 vezes
print(arquivo.readline())
print(arquivo.readline())
print(arquivo.readline())
print(arquivo.readline())
print(arquivo.readline())
print(arquivo.readline())
print(arquivo.readline())

# Podemos também separar em um listas as palavras contidas em um linha
ret = arquivo.readline()
print(type(ret))
print(ret.split(' '))


# --- Exemplo 3 ----

# Transformando cada linha em itens de uma lista
# .readlines()
arquivo = open('teste.txt')
linhas = arquivo.readlines()
print(linhas)
print(len(linhas))


OBS: Quando abrimos um arquivo com a função open() é criada uma conexão entre o arquivo no disco do
computador e o nosso programa. Essa conexão é chamada de streaming. Ao finalizar as tarefas com o arquivo,
essa conexão deve ser fechada com o a função close()

Resumindo: para trabalhar com arquivos seguimos os passos seguintes

1 - Abrir o arquivo
2 - Trabalhando com o arquivo
3 - Fechando o arquivo

# 1 - Abrir o arquivo
arquivo = open('teste.txt')

# 2 - Trabalhando com o arquivo
print(arquivo.read())

print(arquivo.closed)  # Verifica se o arquivo está aberto ou fechado -  retorna True or False

# 3 - Fechando o arquivo
arquivo.close()
print(arquivo.closed)  # Verifica se o arquivo está aberto ou fechado -  retorna True or False

# É importante verificar se o arquivo foi fechado!
# Se tentarmos acessar o arquivo aós o fechamento veja que ocorre um ValueError: I/O operation on closed file.
print(arquivo.read())
"""

