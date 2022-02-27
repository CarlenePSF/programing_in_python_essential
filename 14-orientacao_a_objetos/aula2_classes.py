"""
POO - Classes

Em POO, Classes são modelos dos objetos do mundo real sendo representados computacionalmente.

Imagine que você queria fazer um sistema para automatizar o controle das lampadas da sua casa.

Classes podem conter:
    - Atributos -> Representam as características do objeto, ou seja, pelos atributos conseguimos
    representar computacionalmente os estados de um objeto. No caso da classe Lampada, possivelmente
    iríamos querer saber se a lâmpada é de 110 Volts ou 220 Volts, se ela é branca ou colorida, qual é a a potência
    5 Watts, etc.

    - Métodos (funções) → representam os comportamentos do objeto, ou seja, as ações que este objeto pode realizar
    no seu sistema. No caso da lâmpada, por exemplo, um comportamento comum que  muito provavelmente iríamos querer
    representar no nosso sistema é o de ligar e desligar a lâmpada.


Em Python, para definir uma classe utilizamos a palavra reservada class.

OBS-1: usamos a palavra pass em python quando temos um bloco de código que ainda não está implementado.
OBS-2: quando nomeamos as nossas classes utilizamos por convenção o nome com inicial em maiúscula.
      Se o nome for composto, utilizam-se as iniciais de ambas as palavras em maiúsculas todas juntas.

Dica Geek: Em computação, não utilizamos acentuação, caracteres especiais, espaços ou similares, para nomes de classes,
atributos, métodos, arquivos, diretórios, etc.

Em python, podemos ter mais de uma classe num mesmo script .py, ao contrário do que ocorre em java.


# Exemplo 1 - Criando um 'tipo de dado lampada'


class Lampada:
    pass


lamp = Lampada()
print(type(lamp))

# Exemplo 2 - definindo outras classes no nosso script


class Produto:
    pass


class Usuario:
    pass
"""

# Exemplo 3 - Já utilizamos exemplos de classe indiretamente
# Veja o exemplo

valor = int('44')  # cast de variável
print(type(valor))  # class int(object)

# Note que classes internas da linguagem são nomeadas com minúsculas!


class Int:
    pass


inteiro = Int()
print(type(inteiro))


# OBS: quando estamos planejando um ‘software’ e definindo quais classes teremos que ter no sistema,
# chamamos estes objetos  que serão mapeados para as classes de entidades.
