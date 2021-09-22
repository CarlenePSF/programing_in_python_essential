"""
POO - Atributos

Atributos -> Representam as características dos objetos, ou seja, pelos atributos nós conseguimos representar
computacionalmente os estados de um objeto.


Em Python, dividimos os atributos em 3 grupos:
    - Atributos de instância;
    - Atributos de classe;
    - Atributos dinâmicos;


#  ************ 1 - Atributo de instância ******************

Atributos de instâncias são atributos declarados dentro do método construtor, que nada mais é do
que um método especial utilizado para a construção do objeto.

# Exemplo 1 -

Em java, uma classe 'lâmpada', incluindo seus atributos, poderia ser escrita da forma abaixo:

public class Lampada(){
    private int voltagem;
    private String cor;
    private Boolean ligada = false;

    public Lampada(int voltagem, String cor){
       this.voltagem = voltagem;
       this.cor = cor;
    }

    public int getVoltage(){
        return this.voltagem
        }
}

# Em Python, a construção da classe Lampada, com o seu atributo de instância
# sera da seguinte forma.

class Lampada:

    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


# Exemplo 2 - Criando atributos de instância com o método __init__


class ContaCorrente:
    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Produto:
    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor



class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


# O significado de criar atributos de instancias om o __init__ pode ser lido da seguinte forma
# - O atributo nome do objeto Usuario receberá nome
# - O atributo email do objeto Usuario receberá email
# - O atributo senha do objeto Usuario receberá a senha


#  ----  Atributos publicos e atributos privados

Quando declaramos um atributo como privado, ele só poderá ser acessado dentro da própria classe.
Em Java, existe algumas palavras reservadas para distinguir atributos publicos e privados ou
protegidos (visível somente dentro do pacote na qual a classe se encontra)
    * public
    * private
    * protected

Em Python, essas palavras reservadas não existem! Por convenção, ficou estabelecido que qualquer atributo
de uma classe é público. Isso quer dizer que pode ser acessado em qualquer parte do projeto.
Caso queiramos demonstrar que determinado atributo deve ser tratado como privado, isto é,
que deve ser acessado/utilizado somente dentro da própria classe onde está declarado, utiliza-se
duplo underscore (__) no inicio de seu nome, também conhecido como Name Mangling. Todos os exemplos
acima são de atributos públicos!!!!


# Exemplo 3 - Classe com atributos de instância privados


class Acesso:

    def __init__(self, email, senha):
        self.email = email    # atributo publico
        self.__senha = senha  # atributo privado

    def monstra_senha(self):  # acessando a senha
        print(self.__senha)

    def mostra_email(self):
        print(self.email)


# OBS: Lembre-se que essa maneira de declarar atributos privados é a apenas uma convenção. Isso significa que a
# linguagem Python não vai impedir-nos de acessar os atributos sinalizados como privados fora da classe em que foram
# declarados.


user = Acesso('user@gmail.com', '12345')

print(user.email)  # imprime o email
# print(user.senha)  # AttributeError: 'Acesso' object has no attribute 'senha'

# Uma maneira de corrigir - usando o Name Mangling
# print(dir(user))
# print(user._Acesso__senha)  # Temos acesso. Mas não devemos fazer esse acesso.

# forma mais indicada, criamos um método para acessar o atributo privado
user.monstra_senha()


# O que são atributos de instância?
# Significa que ao criarmos instâncias/objetos de uma classe, todas as instâncias terão estes atributos.

user1 = Acesso('user1@gmail.com', '12345@#')
user2 = Acesso('outro_user@gmail.com', '23456432$%')

user1.mostra_email()
user2.mostra_email()


#  **************  2 - Atributo de classe *******************

São atributos que são declarados diretamente na classe, ou  seja, fora do construtor. Geralmente já inicializamos um
valor e este valor é compartilhado entre todas as instâncias da classe. Isto que dizer que ao invés de cada
instância da classe ter seus próprios valores, como o caso dos atributos de instância, com os atributos de classe
todas as instâncias terão o mesmo valor para este atributo.

# Exemplo 1 - criando a classe Produto


class Produto:
    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


prod1 = Produto('PlayStation 4', 'Video Game', 2399.00)
prod2 = Produto('Xbox 5', 'Video Game', 4499.00)

# novo valor com o imposto
print(prod1.valor)
print(prod2.valor)


# Refatorando a classe Produto


class ProdutoRef:

    # Atributo de classe
    imposto = 0.05  # 0.05 de imposto sobre o produto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = ProdutoRef.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor + valor * ProdutoRef.imposto)
        ProdutoRef.contador = self.id


p1 = ProdutoRef('PlayStation 4', 'Video Game', 2300.00)
p2 = ProdutoRef('Xbox 5', 'Video Game', 4500.00)

print(p1.imposto)  # Acesso possível, porém incorreto de um atributo de classe
print(p2.imposto)  # Acesso possível, porém incorreto de um atributo de classe

# novo valor com o imposto
print(p1.valor)
print(p2.valor)


# OBS: Não precisamos criar uma instância de uma classe para fazer acesso a um atributo de classe
print(ProdutoRef.imposto)  # Acesso correto de um atributo de classe


print(p1.id)
print(p2.id)

# OBS: Em Java, os atributos de classe do Python são chamados de atributos estáticos


# ************************  3 - Atributos dinâmicos *********************
- Não são comuns mas existem em python.
- São atributos de instância que podem ser criados ao mesmo tempo em que é executado.
  Um atributo dinâmico será exclusivo da instância que o criou.






"""

# Exemplo 1 - com a nossa classe produto

# note que na classe Produto não existe o atributo peso


class ProdutoRef:

    # Atributo de classe
    imposto = 0.05  # 0.05 de imposto sobre o produto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = ProdutoRef.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor + valor * ProdutoRef.imposto)
        ProdutoRef.contador = self.id


p1 = ProdutoRef('PlayStation 4', 'Video Game', 2300.00)
p2 = ProdutoRef('Xbox 5', 'Video Game', 4500.00)


# Criando o atributo dinâmico - peso
p2.peso = '5kg'

print(f'Produto: {p2.nome}')
print(f'Descrição: {p2.descricao}')
print(f'Valor: {p2.valor}')
print(f'Peso: {p2.peso}')

# print(f'Peso: {p1.peso}')  # Essa linha gera AttributeError: 'ProdutoRef' object has no attribute 'peso'

# Deletando atributos com a palavra reservada del
print(p1.__dict__)  # devolve um dicionário com cada atributo da classe e o valor que eles possuem
print(p2.__dict__)

del p2.peso
del p2.valor
del p2.descricao
print(p2.__dict__)
