"""
Forçando tipos de dados com decoradores

Em Python, não precisamos definimos o tipo de dado que uma variável irá armazenar.
Isso já está implicito na sua declaração.
Ex.:
    numero_int = 1
    numero_float = 3.1415
    string = 'isso é uma string'
    booleana = True


Em outras linguagens é comum definir o tipo de dado que a variável poderá armazenar antes de
atribuir um calor para a mesma.
Ex. em C:
    int num = 1                             # tipo inteira
    float pi = 3.1415                       # tipo float - ponto flutuante
    char letra = 'c'                        # tipo caractere
    char frase[100] = 'Isso é uma string'   # tipo string

Porém em alguns casos, é interessante forçar o tipo de dado para uma variável. No python, fazemos isso com o auxílio
de um decorator.

# -------- Lembrando a função zip -----------
# >>> a = (1, 3, 5)
# >>> b = (2, 4, 6)
# >>> print(list(zip(a, b)))
[(1, 2), (3, 4), (5, 6)]


"""


def forca_tipo(*tipos):
    def decorador(funcao):
        def converte(*args, **kwargs):
            novo_args = []
            for (valor, tipo) in zip(args, tipos):
                novo_args.append(tipo(valor))   # str('oi'), int('3')
            return funcao(*novo_args, **kwargs)
        return converte
    return decorador


@forca_tipo(str, int)
def repete_mensagem(msg, vezes):
    for vez in range(vezes):
        print(msg)


repete_mensagem('oi', '5')


@forca_tipo(float, int)
def divide(a, b):
    print(a/b)


divide('2', 4.7)
