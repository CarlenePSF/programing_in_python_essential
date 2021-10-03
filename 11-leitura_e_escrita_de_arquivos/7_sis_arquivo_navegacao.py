"""
Sistema de Arquivos e Navegação

Para fazer uso de manipulação de arquivos do sistema operacional, precisamos importar e fazer uso do modulo
externo python os.

os -> Operating System - sistema operacional
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

"""

# import
import os


# Juntando paths

print(os.getcwd())  # verificando o diretório em que estamos
# mudando o diretório por duas pasta acima da hierarquia
os.chdir('..')
os.chdir('..')
path = os.path.join(os.getcwd(), 'programing_in_python_essential')
print(path)
