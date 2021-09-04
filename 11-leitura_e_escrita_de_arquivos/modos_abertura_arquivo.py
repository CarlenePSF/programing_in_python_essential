"""
Modos de abertura de arquivos

'r' -> Abre para leitura - padrão
'w' -> Abre para escrita - sobrescreve caso o arquivo já exista
'x' -> abre para escrita somente se o arquivo não existir
       Caso o arquivo já exista retorna um FileExistsError.
'a' -> Abre para a escrita adicionando o conteudo ao final do arquivo
     OBS: Abrindo no modo 'a' (append), se o arquivo não existe ele é criado. Caso o arquivo exista,
     o novo conteúdo será adicionado ao final do conteúdo existente.
'+' -> Abre para o modo de atualização: leitura e escrita


Mais modos em: http://docs.python.org/3/library/functions.html#open


# ---- Exemplo de uso com  modo 'x'
try:
    with open('arquivos_saida/university.txt', 'x') as file:
        file.write('Teste de conteúdo 2.\n')
except FileExistsError:
    print('Arquivo já existe!')


# ---- Exemplo de uso com  modo 'a'
with open('arquivos_saida/frutas.txt', 'a') as file:
    while True:
        fruta = input('Digite uma fruta ou sair, para sair: ')
        if fruta != 'sair':
            file.write(fruta)
            file.write('\n')
        else:
            break

# OBS: No modo 'a' não controlamos o cursor com o a função .seek()

with open('arquivos_saida/outro.txt', 'a') as file:
    file.seek(0)
    file.write('Cursor no topo 2. \n')
    file.write('Nova linha.\n')
    file.write('Mais uma linha.\n')
"""

with open('arquivos_saida/outro3.txt', 'w+') as file:
    file.write('Cursor no topo. \n')
    file.write('Nova linha.\n')
    file.write('Mais uma linha.\n')
    file.seek(10)
    file.write(' alguma coisa\n')
