"""
O bloco with -- Forma Pythonica de se trabalhar com arquivos ;)

Já vimos os passos para manipular um arquivo
1 - Abrir o arquivo
2 - Trabalhando com o arquivo
3 - Fechando o arquivo

O bloco with é utilizado para criar um contexto de trabalho onde os recursos utilizados são fechados após o bloco with;
"""

#  -- Exemplo 1

with open('arquivos_saida/teste.txt') as arquivo:
    print(arquivo.read())
    print(arquivo.closed)  # retorna True

# Verificando se o arquivo foi fechado
print(arquivo.closed)  # retorna False

# Se tentarmos manipular o arquivo fora do bloco with recebemos um ValueError: I/O operation on closed file.
# print(arquivo.read())
