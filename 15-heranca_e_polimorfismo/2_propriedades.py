"""
POO — Propriedades (Properties)

Em linguagens de programação como o Java, ao declarar atributos privados nas classes costuma-se
criar métodos públicos para manipulação desses atributos. Esses métodos

# Exemplo 1 — Forma incorreta de acessar atributos


class Conta:
    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor


conta1 = Conta('Allan', 3000, 5000)
conta2 = Conta('Felicity', 5000, 7000)

print(conta1.extrato())
print(conta2.extrato())

# Acessando um elemento privado de uma classe — forma incorreta

soma = conta1._Conta__saldo + conta2._Conta__saldo
print(f'A soma do saldo é de {soma}')

# É incorreto, pois se o elemento foi declarado como provado ele só deve ser acessado na classe.


# Exemplo 2 — acesso de forma correta - parecido com o Java
# A forma mais indicada de acessar elementos declarados como provados é usando métodos definidos
# como getters e ‘setters’. Vamos refatorar a classe criando os métodos getter e ‘setter’


class Conta:
    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    # getters para acessar atributos

    def get_numero(self):
        return self.__numero

    def get_titular(self):
        return self.__titular

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite

    def set_titular(self, titular):
        self.__titular = titular

    def set_limite(self, limite):
        self.__limite = limite

    # métodos da classe

    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor


conta1 = Conta('Allan', 3000, 5000)
conta2 = Conta('Felicity', 5000, 7000)

print(conta1.extrato())
print(conta2.extrato())

# Acessando elementos privados de uma classe — forma correta

soma = conta1.get_saldo() + conta2.get_saldo()
print(f'A soma do saldo é de {soma}')

print(f'O titular da conta {conta1.get_numero()} é o sr. (sra.) {conta1.get_titular()}')
print(f'O titular da conta {conta2.get_numero()} é o sr. (sra.) {conta2.get_titular()}')

print(conta1.__dict__)
print(conta2.__dict__)

# definindo novo limite para a conta 2
conta2.set_limite(10 000)
print(f'O novo saldo da conta de {conta2.get_titular()} é {conta2.get_limite()}')
"""


# Exemplo 3 — Refatorando a classe Conta
# acessando com o @property — pythonic way

class Conta:
    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    # getters para acessar atributos

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

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    @property
    def valor_total(self):
        return self.__saldo + self.__limite

    # métodos da classe

    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor


conta1 = Conta('Allan', 3000, 5000)
conta2 = Conta('Felicity', 5000, 7000)

print(conta1.extrato())
print(conta2.extrato())

print(f'O titular da {conta1.numero} é {conta1.titular}')
print(f'O titular da {conta2.numero} é {conta2.titular}')

# definindo novo limite para a conta 2
conta2.limite = 10000
print(f'O novo saldo da conta de {conta2.titular} é {conta2.limite}')

print(conta1.valor_total)
print(conta2.valor_total)
