"""
Levantando os próprios erros com o raise

raise -> lança exceções
O raise não é uma função, mas sim uma palavra reservada, assim como o def ou qualquer outra em python.
Para simplificar, pense no raise como sendo útil para que possamos criar nossas próprias exceções e mensagens de erros

Sintaxe para utilização do raise:
raise TipoDoErro('mensagem de erro')

# ------------- Exemplo ---------------

def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string.')
    elif type(cor) is not str:
        raise TypeError('Cor precisa ser uma string.')
    print(f'O texto {texto} será impresso na cor {cor}')


# Forma correta dos parâmetros
colore('Geek', 'azul')

# Forma erra dos parâmetros
colore('Geek', 4)

OBS: O raise, assim como o return finaliza a função. Ou seja, nada após o raise é executado.

"""

# Exemplo refatorado


def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string.')
    elif type(cor) is not str:
        raise TypeError('Cor precisa ser uma string.')
    elif cor not in cores:
        raise ValueError('A cor precisa ser uma entre verde, amarelo, azul e branco.')
    print(f'O texto {texto} será impresso na cor {cor}')


# executa corretamente
colore('Geek', 'amarelo')

# levando o ValueError
colore('Geek', 'vermelho')


