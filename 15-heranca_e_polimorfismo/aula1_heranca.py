"""
POO — Herança (Inheritance)

A ideia por trás do conceito de herança é a possibilidade de reaproveitar códigos e extender as nossas classes.
A partir de uma classe existente, nós podemos extender outra classe que passa a herdar atributos e métodos da classe
herdade.

Exemplo:

class Cliente
   - nome
   - sobrenome
   - cpf
   - renda

Funcionario:
   - nome
   - sobrenome
   - cpf
   - matricula

# Exemplo 1-


class Cliente:

    def __init__(self, nome, sobrenome, cpf, renda):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__renda = renda

    @property
    def nome(self):
        return self.__nome

    @property
    def sobrenome(self):
        return self.__sobrenome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def renda(self):
        return self.__renda

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Funcionario:

    def __init__(self, nome, sobrenome, cpf, matricula):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__matricula = matricula

    @property
    def nome(self):
        return self.__nome

    @property
    def sobrenome(self):
        return self.__sobrenome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def matricula(self):
        return self.__matricula

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


cliente1 = Cliente('Maria', 'Joaquina', '123.456.789-09', 5550.00)
funcionario1 = Funcionario('John', 'Doe', '987.654.321- 01', 1234)

print(f'O cliente {cliente1.nome} recebe {cliente1.renda}')
print(cliente1.nome_completo())

print(f'O funcionário {funcionario1.nome} possui número de matrícula igual a {funcionario1.matricula}')
print(funcionario1.nome_completo())


# Note que nas classes acima pelo menos 3 atributos estão repetidos
# e tem o método nome completo. A pergunta que devemos dizer é:
# -  Existe um entidade genérica o suficiente para encapsular os atributos e métodos comuns a outras
#    entidades??

Podemos refatorar as classes acima criando uma terceira classe que encapsula as características semelhantes de
cada uma das classes, digamos uma classe chama Pessoa.

Nesse ponto , algumas observações são necessárias.

# OBS 1: Quando uma classe herda de outra classe, a classe herdeira possui todos
# os atributos e métodos da classe herdada.

# OBS 2: Quando uma classe herda de outra classe, a classe a ser herdade é conhecida como
#   [Pessoa]
#   - Super classe;
#   - Classe Mãe;
#   - Classe Pai;
#   - classe Base;

# OBS #: Quando uma classe herda de outra classe, ela é chamada de:
#   [Cliente, Funcionario]
#   - Subclasse
#   - Classe filha
#   - Classe específica



# Exemplo 2 - refatorando as classes e criando a super-classe Pessoa


class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    @property
    def nome(self):
        return self.__nome

    @property
    def sobrenome(self):
        return self.__sobrenome

    @property
    def cpf(self):
        return self.__cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    '''Cliente herda de Pessoa'''

    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)  # acessar qualquer atributo ou método da super classe (recomendada)
        # Pessoa.__init__(self, nome, sobrenome, cpf)  # outra maneira de acessar o construtor da super classe
        self.__renda = renda

    @property
    def renda(self):
        return self.__renda


class Funcionario(Pessoa):
    '''Funcionario herda de Pessoa'''

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

    @property
    def matricula(self):
        return self.__matricula


cliente1 = Cliente('Maria', 'Joaquina', '123.456.789-09', 5550.00)
funcionario1 = Funcionario('John', 'Doe', '987.654.321- 01', 1234)

print(f'O cliente {cliente1.nome} tem renda de {cliente1.renda}.')
print(cliente1.nome_completo())
print(cliente1.__dict__)

print(f'O funcionário {funcionario1.nome} possui número de matrícula igual a {funcionario1.matricula}.')
print(funcionario1.nome_completo())
print(funcionario1.__dict__)
"""


# Sobrescrita de método, ocorre quando reescrevemos/reimplementamos um método presente na super-classe
# em subclasses. Vejamos um exemplo com a superclasse pessoa e a subclasse funcionário

# Exemplo3 -


class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    @property
    def nome(self):
        return self.__nome

    @property
    def sobrenome(self):
        return self.__sobrenome

    @property
    def cpf(self):
        return self.__cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    """Cliente herda de Pessoa"""

    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)  # acessar qualquer atributo ou método da super classe (recomendada)
        # Pessoa.__init__(self, nome, sobrenome, cpf)  # outra maneira de acessar o construtor da super classe
        self.__renda = renda

    @property
    def renda(self):
        return self.__renda


class Funcionario(Pessoa):
    """Funcionario herda de Pessoa"""

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

    @property
    def matricula(self):
        return self.__matricula

    def nome_completo(self):
        print(super().nome_completo())  # acessando o método da super classe com o super()
        print(super(Funcionario, self).nome_completo())
        return f'Funcionário: {self.__matricula} Nome: {self._Pessoa__nome}'


cliente1 = Cliente('Maria', 'Joaquina', '123.456.789-09', 5550.00)
print(cliente1.nome_completo())  # vai executar o método da superclasse Pessoa

funcionario1 = Funcionario('John', 'Doe', '987.654.321- 01', 1234)
print(funcionario1.nome_completo())  # vai executar o método da subclasse Funcionario
