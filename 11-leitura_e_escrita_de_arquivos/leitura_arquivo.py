"""
Leitura de Arquivos

Para ler um conteúdo de um arquivo em Python, utilizamos a função integrada open, que literalmente significa abrir.
Por ser uma função integrada não requer import de módulos ou instalação de pacotes externos

open() -> Na forma mais simples de usar a função open, passamos apenas um parâmetro de entrada, que nesse caso é o
          nome do arquivo a ser lido. Essa função retorna um arquivo com extensão _io.TextIOWrapper e é com esse
          objeto (arquivo) retornado que trabalhamos.

          Para visualizar a documentação acesse: https://docs.python.org/3/library/functions.html#open

# OBS: Por padrão, a função open() abre o arquivo para leitura. Esse arquivo deve existir, ou então teremos um erro
FileNotFounderError

O objeto <_io.TextIOWrapper name='teste.txt' mode='r' encoding='cp1252'>

'_io.TextIOWrapper' -> classe
mode='r' -> modo de leitura=read
encoding='cp1252'> -> a codificação em que o arquivo foi escrito



# ------ Exemplo 1
arquivo = open('teste.txt')
print(arquivo)
print(type(arquivo))

# Para ler o conteúdo após a abertura utilizamos a função read()
print(arquivo.read())

# OBS: O Python usa um recurso para se trabalhar com arquivos chamado de cursor.
# Esse cursor, funciona como o cursos padrão do computador quando estamos escrevendo.
# Isso significa que após a primeira leitura do arquivo, o cursor ficará posicionado no final do arquivo e ao
# solicitar novamente a impressão so arquivo, ele não será mais exibido, como no print abaixo.

# A linha abaixo não imprimirá o arquivo novamente.
print(arquivo.read())
# Concluímos que a função read() lê o conteúdo do arquivo por inteiro


# ---- Exemplo 2 --- tipo de retorno da função read()
arquivo = open('teste.txt')
retorno = arquivo.read()

print(type(retorno))  # retorna um tipo string
print(retorno)
# print(dir(retorno))
print(retorno.split('\n'))
"""


# OBS: A função read() aceita como parâmetro um número que define a quantidade de caracteres na string que queremos ler.
arquivo = open('arquivos_saida/teste.txt')
print(arquivo.read(100))
