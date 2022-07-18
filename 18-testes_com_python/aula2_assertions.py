"""
Assertions (Afirmações= declarações)

Boa forma de validar dados.

Em python, utilizamos a palavra reservada 'assert' para realizar simples
afirmações utilizadas nos testes.

Usamos o 'assert' em uma expressão que queremos checar se é válida ou não.
Se a expressão for verdadeira, o assert retorna none.
Caso a expressão seja falsa, levanta um erro do tipo AssertionError

# OBS.: 1  Nós podemos especificar, opcionalmente, um segundo argumento
ou mesmo uma mensagem de erro personalizada

# OBS. 2: A palavra 'assert' pode ser utilizada em qualquer função ou código,
não sendo de uso exclusivo em testes.


# ALERTA: Cuidado ao utilizar o assert!
Se um programa Python for executado com o parâmetro -O, nenhum assertion
será validado e todas as validações não serão testadas.

# >>> python -O <filename>.py

***** Melhor forma de fazer checagem é o try/ except

"""


def some_numeros_positivos(a, b):
    """
    Recebe dois números positivos e calcula a soma
    :param a:
    :param b:
    :return: a soma a+b
    """
    assert a > 0 and b > 0, 'Ambos numeros precisam ser positivos'
    return a+b


print(some_numeros_positivos(2, 9))
print(some_numeros_positivos(-2, 9))  # AssertionError: Ambos numeros precisam ser positivos


def comer_fastfood(comida):
    """

    :param comida:
    :return:
    """
    assert comida in ['pizza', 'batata frita', 'hamburger', 'sorvete'], 'A comida precisa ser fastfood!'
    return f'Eu estou comendo {comida}'


print(comer_fastfood('pizza'))
print(comer_fastfood('arroz'))  # AssertionError: A comida precisa ser fastfood!
