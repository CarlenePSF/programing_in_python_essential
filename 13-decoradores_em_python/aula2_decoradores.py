"""
Decoradores (decorators)

O que são decorators?

- São funções que envolvem outras funções e aprimoram seus comportamentos;
- Também são exemplos de high order functions;
- Tem uma sintaxe própria, usando "@" (Syntactic Sugar / açúcar sintático)


# Representação

|------------------------------------------------------|
|          Function Decorator                          |
|------------------------------------------------------|

|------------------------------------------------------|
|  ******   @@@@@   Function normal  @@@@ ******       |
|------------------------------------------------------|



# Exemplo 1 - Decorators como funções (Sintaxe não recomendada / Sem 'Açúcar Sintático ')

def seja_educado(funcao):  # uma função decorator recebe como parâmetro uma outra função
    def sendo_educado():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um ótimo dia!')
    return sendo_educado()


# Teste 1
def saudacao():  # função que será decorada
    print('Seja bem-vindo(a) à Geek University!')


saudacao()  # comportamento normal da função

teste = seja_educado(saudacao)  # função decorada - alteramos o comportamento


# Teste 2
def raiva():
    print('EU TE ODEIO!')


raiva_educada = seja_educado(raiva)


# Onde podemos usar decoradores?
Em websites temos abas para acessar vários servições, algumas dessas abas podem solicitar autenticação com
login e senha. Para permitir que somente pessoas com acesso (login + senha ) tenham acesso a esses espaços, podemos
usar decorators. como no exemplo abaixo de pseudo-código.

|------------------------------------|
| home | serviços | produtos | admin |
|------------------------------------|

http://www.suaempresa.com.br/home

http://www.suaempresa.com.br/servicos

http://www.suaempresa.com.br/produtos

http://www.suaempresa.com.br/admin


# OBS:Não é código funcional, serve somente para exemplificar como poderíamos usar os decorators

def checa_login():
    if not request.usuario:
        redirect('http://www.suaempresa.com.br')


def home(request):
    return 'pode acessar home'


def servicos(request):
    return 'pode acessar servicos'


def produtos(request):
    return 'pode acessar produtos'

@checa_login
def admin(request):
    return 'pode acessar admin'

# OBS: Não confundir decorator com decoration function

"""


# Exemplo 2 -  Decorators com a sintaxe recomendada
def seja_educado_mesmo(funcao):   # decorator function
    def sendo_mesmo_educado():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um excelente dia!')
    return sendo_mesmo_educado()


# teste 1
# função que vamos decorar
@seja_educado_mesmo  # decorator
def apresentando():
    print('Meu nome é Pedro')


apresentando


# teste 2
@seja_educado_mesmo
def dormir():
    print('Quero dormir ...')


dormir
