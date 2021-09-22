"""
POO - Métodos

- Métodos (funções) -> representam os comportamentos do objeto, isto é, as ações que este objeto pode realizar no
seu sistema.

Em Python, dividimos os métodos em dois grupos: métodos de instâncias e métodos de classe.

# *********** Métodos de instâncias ****************

O método __init__ é um método especial chamado de construtor e sua função é
construir o objeto a partir da classe.

OBS: Todos os elementos em Python que iniciam e finalizam-se com o duplo underline são chamados de dander
(double underline)

OBS: Os métodos/funções dander em Python são chamados de métodos mágicos.

ATENÇÃO: Não é indicado criar métodos próprios com o double underscore tais como __meumetodo__, porque isso pode
gerar conflitos com os métodos internos da própria linguagem python.

Método são escritos em letras minúsculas, assim como funções, se o nome for composto, deverá ser escrito com as
palavras separadas por underline.


# ----------------  Exemplos de classes


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False


class ContaCorrente:

    contador = 1234

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


# ----------------- Classe produto


class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        '''Retorna o valor do produto com o desconto'''
        return (self.__valor * (100 - porcentagem))/100


# Testando a classe produto

p1 = Produto('PlayStation 4', 'Video Game', 2300)

# Duas maneiras de invocar o método
print(p1.desconto(20))  # somente o desconto
print(Produto.desconto(p1, 20))  # self, desconto


# ---------------- Classe usuário


class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha

    # def __nome_completo__(self):   # forma errada
    #     return f'{self.__nome} {self.__sobrenome}'

    def nome_completo(self):   # forma correta
        return f'{self.__nome} {self.__sobrenome}'


# Testando a classe Usuário

user1 = Usuario('Mario', 'Bros', 'mariobros@gmail.com', '123456')
user2 = Usuario('Lara', 'Croft', 'laraarqueologia@gmail.com', '123@#lara')

print(user1.nome_completo())
print(user2.nome_completo())
# print(f'Senha User 1: {user1._Usuario__senha}')  # Acesso de forma errada de um atributo de classe
# print(f'Senha User 2: {user2._Usuario__senha}')  # Acesso de forma errada de um atributo de classe

***** Awesome tips I found on https://www.freecodecamp.org/news/python-property-decorator/
'''Specifically, you can define three methods for a property which is private:

* A getter - to access the value of the attribute.
* A setter - to set the value of the attribute.
* A deleter - to delete the instance attribute.

Some final Tips:
 - You don't necessarily have to define all three methods for every property.
 - You can define read-only properties by only including a getter method.
 - You could also choose to define a getter and setter without a deleter.
 - If you think that an attribute should only be set when the instance is created or that
 it should only be modified internally within the class, you can omit the setter.

You can choose which methods to include depending on the context that you are working with.'''
"""
# Exemplo
# ************* Criando senhas criptografadas *************

from passlib.hash import pbkdf2_sha256 as cryp


class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)

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

    def nome_completo(self):  # forma correta
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False


# Testando a criação de usuário com senha criptografada

user1 = 0
user_nome = input('Informe seu nome: ')
user_sobrenome = input('Informe o seu sobrenome: ')
user_email = input('Informe o email: ')
user_senha = input('Informe a senha: ')
confirma_senha = input('Confirme a senha: ')

if user_senha == confirma_senha:
    user1 = Usuario(user_nome, user_sobrenome, user_email, user_senha)
    print('Usuário criado com sucesso.')
else:
    print('Senha não confere...')
    exit(1)

user_senha = input('Informe a senha para acesso: ')

if user1.checa_senha(user_senha):
    print('Acesso Permitido')
else:
    print('Acesso negado.')

print(f'Senha user1: {user1.senha}')
