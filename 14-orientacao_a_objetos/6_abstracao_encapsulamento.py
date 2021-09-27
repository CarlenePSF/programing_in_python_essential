"""
POO - Abstração e encapsulamento

O grande objetivo da POO é encapsular nosso código dentro de um grupo lógico e
hierárquico que utiliza classes.

Encapsular -> colocar dentro de uma cápsula

            classe
____________________________________
|      atributos e métodos         |
------------------------------------

# Relembrando Atributos/ métodos privados em Python
Imagine que temos uma classe chamada Pessoa, que contém um atributo privado
chamado __nome e um método privado chamado __falar(). Esses elementos privados só devem/deveriam
ser acessados dentro da classe. Porém, o Python não bloqueia o acesso mesmo fora da classe a esses atributos ou aos
métodos. O que o Python faz é atribuir um Name Mangling que altera a forma de se acessar os elementos privados,
da seguinte forma:

_Classe__elemento

Exemplo- acessando elementos privados fora da classe (maneira ruim de acessar os elementos):

instancia._Pessoa__nome

instância._Pessoa__falar()

Abstração, em POO, é o ato de expor apenas os dados relevantes de uma classe, escondendo os
atributos e métodos privados do usuário.


# Exemplo 1 - Criando uma classe sem que os elementos estejam encapsulados


class Conta:

    contador = 123

    def __init__(self, titular, saldo, limite):
        self.numero = Conta.contador
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.saldo} do titular {self.titular} com limite de {self.limite}')

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor


conta01 = Conta('John Doe', 200, 1000)
print(conta01)

print(conta01.titular)
print(conta01.saldo)
print(conta01.limite)
print(conta01.numero)

# Não assegura a integridade dos dados. Pois eles podem mudar, já que não estão encapsulados.

conta01.numero = 45
conta01.titular = 'John Snow'
print(conta01.__dict__)

conta01.extrato()

"""

# Exemplo 2 - Refatorando a classe colocando os atributos privados e respeitando o encapsulamento


class Conta:

    contador = 123

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')

    def depositar(self, valor):
        if valor >= 0:
            self.__saldo += valor
        else:
            print(f'O valor precisa ser Positivo.')

    def sacar(self, valor):
        if valor > 0:
            if valor <= self.__saldo:
                self.__saldo -= valor
            else:
                print(f'Você não tem saldo suficiente para essa transação')
        else:
            print(f'O valor precisa ser Positivo.')

    def tranferencia(self, valor, conta_destino):
        if valor >= 0:
            if valor <= self.__saldo:
                # 1- Remove o valor da conta de origem
                self.__saldo -= valor
                # 2- Adiciona o valor à conta destino
                conta_destino.__saldo += valor
            else:
                print('Você não tem saldo suficiente.')
        else:
            print('Valor precisa ser positivo.')


conta01 = Conta('John Doe', 200, 1000)
conta02 = Conta('John Snow', 2000, 5000)

# print(conta01)
# print(conta01.titular)
# print(conta01.saldo)
# print(conta01.limite)
# print(conta01.numero)

conta01.extrato()  # imprime o saldo inicial da conta de john doe
conta01.depositar(-100)  # Deposita e incrementa o saldo mas faz o teste para saber se o valor é aceito
conta01.extrato()  # imprime o novo saldo após o deposito
conta01.sacar(2000)  # vai realizar um saque e o valor é testado para saber se a transação pode ser feita
conta01.extrato()  # imprime o novo saldo após o saque

conta01.tranferencia(300, conta02)  # John Doe transfere $100.00 para John Snow

# imprimindo informações das duas contas
print(conta01.__dict__)
print(conta02.__dict__)
