"""
Try and Except
Utilizamos o bloco try/except para tratar erros que podem ocorrer no nosso código.
Prevenindo assim que o programa pare de funcionar e o usuário receba mensagens de erro inesperadas.

A forma geral mais simples é:

try:
    //execução problemática
except:
    //o que deve ser feito em caso de problema

# ------------- Exemplo 1 -----------


# A passagens abaixo retorna o NameError: name 'geek' is not defined

# >>>geek()

# As linhas abaixo: Tente executar a função geek(). Caso encontre erros, imprime a mensagem de erro.
try:
    geek()
except:
    print('Deu algum problema')

# ------------ Exemplo 2 -------------

try:
    len(5)
except:
    print('Deu algum problema')


# OBS: Tratar erro genérico (bare except) não é a melhor forma de tratamento de erro. O ideal é SEMPRE tratar
de forma específica, Como exemplificado abaixo.

# ------------ Exemplo 3 -------------

try:
    geek()
except NameError:
    print('Você está usando uma função inexistente!')

# As linhas abaixo não tratam o erro!! porque o len(5) retorna um TypeError, não um NameError.
try:
    len()
except NameError:
    print('Você está usando uma função inexistente!')

# Refatorando com um alias...
try:
    len(5)
except TypeError as err:
    print(f'A aplicação gerou o seguinte erro: {err}')

# podemos efetuar diversos tratamentos de erros de uma vez

try:
    print('Geek'[5])
except NameError as err1:
    print(f'NameError {err1}')
except TypeError as err2:
    print(f'TypeError {err2}')
except IndexError as err3:
    print(f'Deu um erro diferente: {err3}!')
"""

# --------- Exemplo 4 Try/except com função --------


def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None


dic = {'nome': 'Geek'}
# A linha abaixo executa o try
print(pega_valor(dic, 'nome'))

# As linhas abaixo executam o except
print(pega_valor(dic, 'game'))

print(pega_valor(7, 'game'))

print(pega_valor(dic, 5))
