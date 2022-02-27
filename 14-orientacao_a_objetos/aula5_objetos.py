"""
POO - Objetos

São instâncias da classe. Isso quer dizer que, após o mapeamento do objeto do mundo real para sua representação
computacional, podemos  criar quantos objetos forem necessários. Podemos pensar nos objetos/ instâncias de uma classe
como variáveis do tipo definido na classe.

"""

# Exemplo 1 - criando classes e declarando os objetos


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    # getters
    @property
    def cor(self):
        return self.__cor

    @property
    def voltagem(self):
        return self.__voltagem

    @property
    def luminosidade(self):
        return self.__luminosidade

    def checa_lampada(self):
        return self.__ligada

    def liga_desliga(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True


# Declarando instancia (objeto) do tipo lampada
lampada1 = Lampada('verde', 220, 60)

lampada1.liga_desliga()  # liga a lampada
print(f'A lampada está ligada? {lampada1.checa_lampada()}')

lampada1.liga_desliga()  # desliga a lampada
print(f'A lampada está ligada? {lampada1.checa_lampada()}')
# -----------------------------------------------------


class ContaCorrente:

    contador = 12345

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero

    # getters
    @property
    def numero(self):
        return self.__numero

    @property
    def limite(self):
        return self.__limite

    @property
    def saldo(self):
        return self.__saldo


# Declarando instancia (objeto) do tipo ContaCorrente
conta_corrente = ContaCorrente(20000, 1400)
print(conta_corrente.numero)
print(conta_corrente.limite)
print(conta_corrente.saldo)

# -------------------------------------------


class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha

    # getters
    @property
    def nome(self):
        return self.__nome

    @property
    def sobrenome(self):
        return self.__sobrenome

    @property
    def email(self):
        return self.__email

    @property
    def senha(self):
        return self.__senha


# Declarando instancia (objeto) do tipo Usuario
nome1 = 'John'
sobrenome1 = 'Doe'
email1 = 'johndoe@gmail.com'
senha1 = '1234'
user1 = Usuario(nome1, sobrenome1, email1, senha1)
print(user1.email)
