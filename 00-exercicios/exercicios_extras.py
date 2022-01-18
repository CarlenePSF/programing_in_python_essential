"""
Ecercícios extras de programação orientada a objetos
"""

# --------------------------------------------------------
# Exercicio 1 - Banco de dados de agenda de endereços
# --------------------------------------------------------


class Agenda:
    def __init__(self, nome, endereco, telefone):
        self.__nome = nome
        self.__endereco = endereco
        self.__telefone = telefone

    @property
    def nome(self):
        return self.__nome

    @property
    def endereco(self):
        return self.__endereco

    @property
    def telefone(self):
        return self.__telefone


contato1 = Agenda('Ana', 'St. Saint Louis 55', '555 6965')

print(contato1.telefone)
