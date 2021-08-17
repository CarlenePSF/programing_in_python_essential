"""
Try/ Except/ Else/ Finally

Dica para quando e onde tratar código:
Toda entrada deve ser tratada!!

OBS: A função do usuário é DESTRUIR seu sistema

------------ Exemplo 1 -----------
try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto')

print(f'Você digitou {num}.')
# Se o usuário digitar um valor incorreto o ValueError é impresso.
# Porém, outro erro é gerado, NameError, pois a variável num não é criada por ser uma variável local

# Refatorando com o else para que o NameError não aparece na saída
# Adicionamos o else que só será executado se não ocorrer o erro
try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto')
else:
    print(f'Você digitou {num}.')


#  Uso do Finally
# Após receber um valor do usuário. Se o valor informado estiver incorreto
# entra no except, se não executa o else. Se não der erro tanto executa o else quanto o finally.


try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto')
else:
    print(f'Você digitou o número {num}')
finally:
    print(f'Executando o finally')

# OBS: O bloco finally é sempre executado, independente de haver erro ou não.

# O finally é geralmente utilizado para fechar ou desalocar recursos.

# ----------------- Exemplo mais complicado ---------
# tratando dados do usuário


def dividir(a, b):
    return a/b

try:
    num1 = int(input('Informe o primeiro número: '))
except ValueError:
    print(f'O valor precisa ser numérico')


try:
    num2 = int(input('informe o segundo número: '))
except ValueError:
    print(f'O valor precisa ser numérico!')

try:
    print(f'{dividir(num1, num2)}')
except NameError:
    num1 = int(input('Informe o primeiro número: '))
    print(f'{dividir(num1, num2)}')

# No exemplo acima, o código fica carregado porque tem muitos try/excepts para cada bloco de instrução.
# A maneira mais limpa de fazer isso é tratar os possíveis erros dentro da propria função
# O desenvolvedor é o responsável pelas entradas das funções


def divisao_refatorada(a, b):
    try:
        return f'A divisão do número é {int(a)/int(b)}'
    except ZeroDivisionError:
        print('Divisão por zero!')
    except ValueError:
        print('Algum valor está incorreto')


num1 = input('Informe o primeiro número: ')
num2 = input('informe o segundo número: ')
print(divisao_refatorada(num1, num2))

# O exemplo acima poderia ser feito um tratamento d forma genérica, como mostrado a baixo

def divisao_refatorada2(a, b):
    try:
        return f'A divisão do número é {int(a)/int(b)}'
    except:
        return 'Ocorreu um problema'
print(divisao_refatorada2(num1, num2))
"""


# Tratando erro de uma forma semi-genérica
def divisao_refatorada3(a, b):
    try:
        return f'A divisão do número é {int(a)/int(b)}'
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'


num1 = input('Informe o primeiro número: ')
num2 = input('informe o segundo número: ')
print(divisao_refatorada3(num1, num2))
