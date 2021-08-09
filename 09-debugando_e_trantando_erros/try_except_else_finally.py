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
"""

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
