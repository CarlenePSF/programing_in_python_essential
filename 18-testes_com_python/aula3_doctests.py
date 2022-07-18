"""
Doctestes

more in https://docs.python.org/3/library/doctest.html

No terminal execute o arquivo com as seguintes flags
    python -m doctest -v <filename>.py

    #  ----- Exemplo 1 -


def soma(a: float, b: float):
    '''
    Soma os números a e b
    :param a: float
    :param b: float
    :return: a+b
    ex.:
        # >>> soma(1, 2)
        3

        # >>> soma(4, 6)
        10
    '''

    return a+b
"""

#  ----- Exemplo 2  - Aplicando o TDD


def duplicar(valores):
    """
    Duplicar valores de uma lista

    >>> duplicar([1, 2, 3, 4])
    [2, 4, 6, 8]

    >>> duplicar([])
    []

    >>> duplicar(['a', 'b', 'c'])
    ['aa', 'bb', 'cc']

    >>> duplicar([True, None])  # nesse caso a mensagem tem que ser identica a do console python
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """
    return [2*elemento for elemento in valores]


print(duplicar([2, 3]))
