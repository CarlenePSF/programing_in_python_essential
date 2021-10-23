"""
 - Sistema de Arquivos - Manipulando arquivos

# Exemplo 1 - Descobrindo se uma arquivo ou diretório existe

# *** caminhos relativos
# arquivos
print(os.path.exists('README.md'))  # False
print(os.path.exists('1_leitura_arquivo.py'))  # True

# diretório
print(os.path.exists('00-exercicios'))  # False

os.chdir('..')
print(os.getcwd())
print(os.path.exists('00-exercicios'))  # True, pois voltou um diretório na hierarquia
print(os.path.exists('README.md'))  # True,  pois voltou um diretório na hierarquia


print(os.path.exists('10-modulos_python/geek'))  # True

# *** caminhos absolutos -
# desde a raiz até onde o caminho se encontra
print(os.path.exists('/home/usuario/Imagens'))  # True


# criando arquivos e verificando se existe

# Forma - 1
open('arquivo-teste.txt', 'w').close()  # cria o arquivo caso ele não exista

# Forma - 2
open('arquivo-teste2.txt', 'a').close()

# Forma - 3
with open('arquivo-teste3.txt', 'w') as arquivo:
    pass


# Forma mais indicada de criar arquivos

if os.path.exists(os.path.join('..', '11-leitura_e_escrita_de_arquivos/arquivo-teste6.txt')):
    print('Arquivo já existe!')
else:
    os.mknod(os.path.join('..', '11-leitura_e_escrita_de_arquivos/arquivo-teste6.txt'))
    print('arquivo criado com sucesso')

# OBS 1: Caso esteja usando o sistema operacional mac OS, o os.mknod() pode retorna o erro PermissionError
# OBS 2: Se estiver usando o os.mknod() para criar um arquivo e os arquivo já existir,
# o erro FileExistsError é retornado


# Forma mais indicada de criar diretórios - os.mkdir()

os.mkdir('templates2')  # o diretório templates é criado

# OBS 3: Caso o diretório já exista o seguinte erro FileExistsError é retornado
# OBS 4: Se não tivermos permissão para criar o diretório, teremos um PermissionError

os.mkdir('templates2/geek')  # o diretório geek é criado dentro de templates
os.mkdir('templates2/geek/university')  # o diretório university é criado dentro de geek

# Note que sempre que quisermos criar uma árvore de diretórios, precisaremos passar o novo diretório a frente do
# diretório anterior. Porém, em Python existe uma maneira mais eficiente de fazer isso usando o os.makedirs()

# os.makedirs('templates3/geek/university')

# Se não quisermos observar a mensagem de erro quando os diretórios criado já existirem basta passar o abaixo
# os.makedirs('templates3/geek/university', exist_ok=True)

# Renomeando arquivos e diretórios
# os.rename('templates3', 'geek4')

# OBS 1: Se o diretório não existir, teremos um FileNotFoundError
# OBS 2: Se o diretório que queremos renomear não estiver vazio, teremos um OSError

# Renomeando arquivos
os.rename('geek3/arquivo-teste3.txt', 'geek3/geek.txt')
os.rename('geek3/arquivo-teste4.txt', 'geek3/geek1.txt')
os.rename('geek3/arquivo-teste5.txt', 'geek3/geek2.txt')
os.rename('geek3/arquivo-teste6.txt', 'geek3/arquivo-teste.txt')

# ***  Deletando arquivos

# ATENÇÃO: Tome cuidado com os comandos de deleção, pois ao deletarmos um arquivo ou diretório eles não
# vão para lixeira, eles somem do sistema. Se estiver usando windows e o arquivo que você estiver tentando apagar
# estiver em uso, um erro será retornado.

# apagando arquivo
os.remove(os.path.join(os.getcwd(), 'geek3/arquivo-teste.txt'))
# Executando a linha acima mais de uma vez teremos o FileNotFoundError:

# OBS: Se informar-mos um diretório ao invés de um arquivo, teremos um IsADirectoryError, como na linha abaixo
os.remove(os.path.join(os.getcwd(), 'geek3'))


# *** Removendo diretórios - os.rmdir()
os.rmdir(os.path.join(os.getcwd(), 'geek1/geek/university'))
os.rmdir(os.path.join(os.getcwd(), 'geek2/geek/university'))
os.rmdir(os.path.join(os.getcwd(), 'geek4/geek/university'))

# Note que quando existe uma arvore de diretórios, o comando não é muito direto,
# pois termos que remover um diretório de cada vez. Cado o diretório que estamos
# tentando remover não esteja vazio o erro OSError,
# e se o diretório não existe temos um FileNotFoundError.

# Removendo o conteúdo e o diretório ao mesmo tempo ou um árvore inteira de diretórios.

# limpando os arquivos geek.txt, geek1.txt, geek2.txt dentro do diretório geek3
for arquivo in os.scandir(os.path.join(os.getcwd(), 'geek3/')):
    print(arquivo.name)
    if arquivo.is_file():
        os.remove(arquivo.path)
    if arquivo.is_dir():
        os.rmdir(arquivo.path)

"""

import os

# apagando as sub-pastas dentro do diretório atual

# for arquivo in os.scandir(os.getcwd()):
#     print(arquivo.name())
#     if arquivo.is_dir():
#         os.rmdir(arquivo.path())


if os.path.exists(os.path.join('..', '11-leitura_e_escrita_de_arquivos/geek')):
    print('diretorio já existe!')
else:
    os.makedirs(os.path.join('..', '11-leitura_e_escrita_de_arquivos/geek'))
    print('diretório criado com sucesso')
