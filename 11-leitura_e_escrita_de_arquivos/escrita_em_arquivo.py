"""
Escrevendo em um arquivo

Ao abrir um arquivo para leitura, a escrita nesse arquivo é desabilitada.
Da mesma forma, se um arquivo for aberto para escrita, não poderá ser lido.

Para escrevermos dados em um arquivo, após abrir o arquivo usamos a função write, que recebe uma string como parâmetro.
Se for passado como argumento outro tipo que não seja a string um TypeError é retornado.

Ao abrir um arquivo para escrita com o modo 'w', se o arquivo não existe ele é criado. Caso o arquivo já exista
o conteúdo anterior do arquivo será apagado e um novo conteúdo será criado.
ATENÇÃO: Isso significa que o conteúdo do arquivo anterior será perdido!

# ---- Exemplo 1 -- Escrita de arquivo
with open('novo.txt', 'w') as arquivo:
    arquivo.write('Nova primeira linha.\n')
    arquivo.write('Essa linha foi gerada com a função write.\n')
    arquivo.write('Escrever dados em arquivo é muito fácil.\n')
    arquivo.write('Podemos escrever quantas linhas quisermos.\n')
    arquivo.write('Essa é a última linha.\n')

# lendo o que escrevemos no arquivo
with open('novo.txt', 'r') as arquivo:
    print(arquivo.read())

# ---- Exemplo 2 -
# Forma não Pythonica de abrir um arquivo - forma tradicional
arquivo = open('novo2.txt', 'w')
arquivo.write('Este é um outro arquivo criado de maneira não pythonica.')
arquivo.close()
print(arquivo.closed)
"""
with open('arquivos_saida/novo2.txt', 'w') as arquivo:
    arquivo.write('Geek\n'*10)


# ----  Exemplo 3 -- Recebendo dados do usuário e escrevendo num arquivo
with open('arquivos_saida/frutas.txt', 'w') as arquivo:
    while True:
        fruta = input('Digite uma fruta: ')
        if fruta != 'sair':
            arquivo.write(fruta+'\n')
        else:
            arquivo.close()
            break
