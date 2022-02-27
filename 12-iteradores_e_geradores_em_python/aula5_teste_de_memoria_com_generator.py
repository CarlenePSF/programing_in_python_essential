"""
Teste de memória com generators

# Exemplo com a sequencia de Fibonacci
# 1, 1, 2, 3, 5, 8, 13, 21, ...

# 1 ---- Função usando lista


def fib_lista(tam):
    num = []
    a, b = 0, 1
    while len(num) < tam:
        num.append(b)
        a, b = b, a + b
    return num


print(fib_lista(100000))  # gasta aproximadamente ~ 1Gb
"""
# 2 ---- Função usando generators


def fibonacci(tam):
    a, b, contador = 0, 1, 0
    while contador < tam:
        a, b = b, a + b
        yield a
        contador = contador + 1


# testando o generator usar aproximadamente ~ 3,2 Mb
for i in fibonacci(100000):
    print(i)

