"""
 — Sistema de Arquivos — Navegação

Para fazer uso de manipulação de arquivos do sistema operacional, precisamos importar e fazer uso do modulo
externo python os.

os --> Operating System - sistema operacional
import os


# getcwd() -> pega o current work directory - diretório atual de trabalho - retorna o path (caminho) absoluto
print(os.getcwd())


# Para mudar o diretório, podemos utilizar o os.chdir()
os.chdir('..')  # mudamos para o diretório anterior
print(os.getcwd())


# Podemos checar se um diretório é absoluto ou relativo
print(os.path.isabs('/home/user'))  # retorna True pois é absoluto, se não fosse retornaria False.

OBS- Para usuários Windows:
Se o usuário estiver utilizando um computador com windows, deverá ter cuidado ao verificar diretórios!
print(os.path.isabs('C:\\Users\\user_root'))


Com o módulo os, também podemos identificar o sistema operacional
print(os.name) # posix (Linux e MacOS) ou nt (Windows)

Podemos ainda ter mais detalhes sobre o sistema operacional com o comando
print(os.uname())  # Não funciona no Windows

# Outra maneira com o sys que também funciona com o Windows
import sys

print(sys.platform)



# *** Juntando paths ***

print(os.getcwd())  # verificando o diretório em que estamos
# mudando o diretório por duas pasta acima da hierarquia
os.chdir('..')
print(os.getcwd())  # verificando se voltou um diretório
os.chdir('..')
print(os.getcwd())  # verificando se volteou outro diretório

# juntando o diretório atual com um ramo
path = os.path.join(os.getcwd(), 'programing_in_python_essential/11-leitura_e_escrita_de_arquivos')
print(path)

# Note que, o os.path.join() recebe dois parâmetros sendo o primeiro o diretório atual
# e oj segundo o diretório que vai ser juntado ao atual.

# *** Listando Arquivos ***
Podemos listar os arquivos e diretórios com o .listdir()

# imprime uma listas com os nomes dos arquivos dentro do diretório
print(os.listdir())
# ['1_leitura_arquivo.py', '8_sis_arquivo_manipulacao.py', '4_escrita_em_arquivo.py',
# '5_modos_de_arquivo.py', '3_o_comando_with.py', '6_string_io.py', '7_sis_arquivo_navegacao.py', '2_seek_cursors.py']


# imprime quantos arquivos tem no diretório
print(len(os.listdir()))  # 8 arquivos


# Também podemos listar os arquivos e diretorios com mais detalhes com o .scandir()
print(os.scandir())  # gera um iterator
"""

# import module
import os


scanner = os.scandir()  # transforma o iterator em uma lista

arquivos = list(scanner)
# print(arquivos)
# print(dir(arquivos[0]))


print(arquivos[0].inode())
print(arquivos[0].is_dir())  # É um diretório? False
print(arquivos[0].is_file())  # É um arquivo? True
print(arquivos[0].is_symlink())  # É um link simbólico? False
print(arquivos[0].name)  # Nome do arquivo
print(arquivos[0].path)  # caminho onde está o arquivo
print(arquivos[0].stat())  # Estatísticas...

# OBS: Quando usamos a função scandir(), nós precisamos fechá-la,
# assim quando como abrimos um arquivo

scanner.close()
