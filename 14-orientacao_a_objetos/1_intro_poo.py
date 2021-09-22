"""
Programação Orientada à Objetos - POO

- POO é um paradigma de programação que utiliza um mapeamento de objetos do mundo real para modelos computacionais.
- Paradigma de programação é a forma/metodologia utilizada  para pensar/desenvolver sistemas.

Principais elementos da orientação a objetos:
- Classe -> modelo do objeto do mundo real sendo representado computacionalmente
- Atributo -> caracteristica do objeto
- Método -> comportamento do objeto (funções).
- Construtor -> método especial utilizado para criar os objetos
- Objetos -> instâncias da classe.


"""
# Exemplo - ciando novo tipos de dados com poo

numero = 10
print(numero, type(numero))

nome = "Geek"
print(nome, type(nome))


class Produto:
    pass


prod = Produto()

print(prod, type(prod))
