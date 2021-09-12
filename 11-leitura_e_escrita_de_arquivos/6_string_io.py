"""
StringIO
Atenção: Para ler ou escrever dados em arquivos do sistema operacional o software precisa ter
permissão:
   * Permissão de leitura -> para ler o arquivos
   * Permissão de escrita -> para escrever o arquivo

StringIO -> utilizado para ler e criar arquivos em memória.
"""

# primeiro importamos o módulo
from io import StringIO

mensagem = 'Esta é apenas uma string normal.'

# Podemos criar uma arquivo em memória já com uma string inserida
# ou podemos inserir a string posteriormente

arquivo = StringIO(mensagem)  # equivalente a arquivo = open('nome_arquivo.txt', 'w')

# Agora com o arquivo criado, podemos utilizar o que já vimos sobre manipulação de arquivos
print(arquivo.read())

arquivo.write('Outro texto')

# movimentando o cursor
arquivo.seek(0)
print(arquivo.read())
