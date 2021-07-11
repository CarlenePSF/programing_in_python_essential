"""
Lista de exercícios : estruturas lógicas
-> Uso de if, else, elif
-> uso de and, or, not, is

"""
#from math import log
#from math import sqrt
#from random import seed
#from random import randint

"""
#------------------------------------------------------
# Exercício 1 - verificando o maior entre dois números
#------------------------------------------------------
num1 = float(input('Digite um número:'))
num2 = float(input('Digite outro numero:'))

if num1 > num2:
    print(f'{num1} é maior do que {num2}.')
else:
    print(f'{num2} é maior do que {num1}.')

#-----------------------------------------------------
# Exercício 2  - Raiz quadrada de um número positivo 
#-----------------------------------------------------

num = float(input('Digite um numero:'))

if num >= 0:
    raiz = num**1/2
    print(f'A raiz quadrada de {num} é {raiz}.')
elif num < 0:
    print('Número inválido.')

#----------------------------------------------------------------------------------------
# Exercício 3 - Raiz quadrada de um número positivo e o quadrado de um número negativo
#----------------------------------------------------------------------------------------

num = float(input('Digite um numero:'))

if num >= 0:
    raiz = num**1/2
    print(f'A raiz quadrada de {num} é {raiz}.')
elif num < 0:
    print(f'O quadrado de {num}  é {num*num} ')

#---------------------------------------------------------------------------
# Exercício 4 - Raiz quadrada e o quadrado de número estritamente positivo
#---------------------------------------------------------------------------

num = float(input('Digite um numero:'))

if num >= 0:
    raiz = num**1/2
    print(f'A raiz quadrada de {num} é {raiz}.')
    print(f'O quadrado de {num}  é {num * num} ')
else:
    print('Número inválido.')

#------------------------------------------------------
# Exercício 5 - verificando se um número é par ou ímpar
#-----------------------------------------------------

num = float(input('Digite um numero:'))
if num % 2 == 0:
    print(f'{num} é par.')
else:
    print(f'{num} é ímpar.')


#----------------------------------------------------------------------
# Exercício 6 - O maior entre dois números e a diferença entre eles
#----------------------------------------------------------------------

a = int(input('Digite um número:'))
b = int(input('Digite outro número:'))
if a > b:
    print(f'{a} é maior do que {b}.')
    print(f'A diferença ente eles é {a-b}')
else:
    print(f'{b} é maior do que {a}.')
    print(f'A diferença ente eles é {b-a}')


#--------------------------------------------
# Exercício 7 - O maior entre dois números
#--------------------------------------------

a = int(input('Digite um número:'))
b = int(input('Digite outro número:'))
if a > b:
    print(f'{a} é maior do que {b}.')
elif b == a:
    print('Numeros iguais')
else:
    print(f'{b} é maior do que {a}.')

#------------------------------------------------------
# Exercício 8 -  Calculando medias para os estudantes
#------------------------------------------------------

nota1 = float(input('Digite a primeira nota:'))
nota2 = float(input('Digite a segunda nota:'))

if 0.0 < nota1 < 10.0 and 0.0 < nota1 < 10.0:
    media = (nota1+nota2)/2
    print(f'A média o aluno é {media}')
else:
    print('Nota invalida! Fim da execução.')

#----------------------------------------
# Exercício 9 - Concedendo um empréstimo
#----------------------------------------

salario = float(input('Qual o salário mensal?'))
emprestimo = float(input('Qual o valor do empréstimo?'))
n = float(input('Em quantas parcelas será dividido?'))
parcela = emprestimo/n
if parcela > 0.2*salario:
    print('Empréstimo não concedido.')
elif parcela < 0.2*salario:
    print('Empréstimo concedido.')
    print('É assim que a pessoa se endivida!!')

#------------------------------------------------------
# Exercício 10 - Calculando o peso ideal de uma pessoa
#------------------------------------------------------

h = float(input('Qual a altura?'))
s = input('Qual o sexo (m/f)?')

if s == 'm':
    peso = 72.7 * h - 58
    print(f'O peso ideal é de {peso}')
elif s == 'f':
    peso = 62.1*h - 44.7
    print(f'O peso ideal é de {peso} kg.')


#-------------------------------------------------------------
# Exercício 11 - Somando os algarismos de um inteiro positivo
#-------------------------------------------------------------

num1 = input('Digite um número inteiro com 3 algarismos:')
num2 = int(num1)
if int(num2) > 0:
    soma = int(num1[0]) + int(num1[1]) + int(num1[2])
    print(f'A soma dos algarismos de {num1} e {soma}')
else:
    print('Número inválido.')


# -------------------------------------------------------------------
# Exercício 12 - Calculando o logaritmo natural de um número positivo
# -------------------------------------------------------------------

num = int(input('Digite um número inteiro:'))

if num <= 0:
    print('Número inválido.')
elif num > 0:
    res = log(num)
    print(f'O logaritmo natural de {num} é {res}')


# -------------------------------------------------------------------
# Exercício 13 - Calculando media ponderada
# -------------------------------------------------------------------
nota1 = float(input('Digite a primeira nota:'))
nota2 = float(input('Digite a segunda nota:'))
nota3 = float(input('Digite a terceira nota:'))
w1 = 1
w2 = 1
w3 = 2
media = (w1*nota1 + w2*nota2 + w3*nota3)/(w1+w2+w3)

if media >= 60:
    print(f'A média final é de {media}')
    print('Aprovado!')

elif media < 60:
    print(f'A média final é de {media}')
    print('Reprovado!')


# -------------------------------------------------------------------
# Exercício 14 - Calculando media de alunos
# -------------------------------------------------------------------
nota1 = float(input('Digite a nota do trabalho de laboratório:'))
nota2 = float(input('Digite a nota da avaliação semestral:'))
nota3 = float(input('Digite a nota do exame final:'))

if 0.0 < nota1 < 10.0 and 0.0 < nota2 < 10.0 and 0.0 < nota3 < 10.0:
    w1 = 2
    w2 = 3
    w3 = 5
    media = (w1*nota1 + w2*nota2 + w3*nota3)/(w1+w2+w3)
    if 0.0 <= media <= 2.9:
        print(f'Média final {media}.')
        print('Reprovado.')
    if 3.0 <= media <= 4.9:
        print(f'Média final {media}.')
        print('Recuperação.')
    if media >= 5.0:
        print(f'Média final {media}.')
        print('Aprovado.')
else:
    print('Alguma notas é invalida.')


#----------------------------------------------------------------------
# Exercício 15 - Usando o switch
# Diferente de outras linguagens de programação como C/C++/Java/PHP
# onde existe in-built switch statement, o switch não existe em python. 
# Nesse caso utiliza-se casos condicionais if/else/elif.
#----------------------------------------------------------------------

num = int(input('Digite um número inteiro de 1 a 7 correspondente ao dia da semana:'))

if num == 1:
    print('domingo')
elif num == 2:
    print('segunda-feira')
elif num == 3:
    print('terça-feira')
elif num == 4:
    print('quarta-feira')
elif num == 5:
    print('quinta-feira')
elif num == 6:
    print('sexta-feira')
elif num == 7:
    print('sábado')

# Uma outra maneira de escrever esse programa seria usando um dicionário como abaixo

def switch_demo(argumento):
    switcher = {
        1: "domingo",
        2: "segunda-feira",
        3: "terça-feira",
        4: "quarta-feira",
        5: "quinta-feira",
        6: "sexta-feira",
        7: "sábado"
    }
    print(switcher.get(int(argumento), "Invalid day"))

switch_demo(num)

#--------------------------------------------------------------------
# Exercício 16 - Usando novamente o switch para imprimir os meses do ano
#--------------------------------------------------------------------

num = int(input('Digite um número inteiro de 1 a 12 correspondente ao mes do ano:'))


def switch_demo(argument):
    switcher = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    print(switcher.get(int(argument), "Invalid month"))

switch_demo(num)


#----------------------------------------------------------------
# Exercício 17 - Calculando a área de um trapézio
#-----------------------------------------------------------------

B = float(input('Tamanho da base maior:'))
b = float(input('Tamanho da base menor:'))
h = float(input('Altura do trapézio:'))

if B > 0 and b > 0:
    Area = (B+b)*h/2
    print(f'A área do trapézio é {Area}.')
else:
    print('Valores incorretos')


#----------------------------------------------------------------
# Exercício 18 - Operações matemáticas básicas
#-----------------------------------------------------------------
op = input('Escolha uma operação matemática dentre as opções soma (+), subtração (-), multiplicação (*) e divisão (/):')
if op == '+':
    a = float(input('Digite um número:'))
    b = float(input('Digite outro número:'))
    print(f'A soma entre {a} e {b} é {a+b}')
elif op == '-':
    a = float(input('Digite um número:'))
    b = float(input('Digite outro número:'))
    if a > b:
        print(f'A diferença entre {a} e {b} é {a-b}')
    if b > a:
        print(f'A diferença entre {a} e {b} é {b - a}')
elif op == '*':
    a = float(input('Digite um número:'))
    b = float(input('Digite outro número:'))
    print(f'O produto entre {a} e {b} é {a*b}')
elif op == '/':
    a = float(input('Digite um número:'))
    b = float(input('Digite outro número:'))
    if b == 0:
        print('divisão por 0 inválida.')
    if b != 0:
        print(f'A divisão de {a} por {b} é {a/b}')

#----------------------------------------------------------------
# Exercício 19 - multiplos de 3 e 5
#-----------------------------------------------------------------

num = int(input('Entre com um número:'))

if num % 3 == 0 or num % 5 == 0:
    if num % 3 != 0:
        print(f' {num} e multiplo de 5.')
    if num % 5 != 0:
        print(f' {num} e multiplo de 3.')
if num % 3 == 0 and num % 5 == 0:
    print(f'{num} multiplo de 3 e 5.')
    print('numero inválido.')

#-----------------------------------------------------------------
# Exercício 20 - triângulos
#-----------------------------------------------------------------

A = float(input('Entre com um número:'))
B = float(input('Entre com um número:'))
C = float(input('Entre com um número:'))

if A > 0.0 and B > 0.0 and C > 0.0:
    print('todos valores positivos.')

    if A < B+C and B < A+C and C < A+B:
        print('podem ser valores de lados de um triângulo.')

        if A == B and A == C and B == C:
            print('Triangulo equilátero.')

        if A != B and A == C or B == C:
            print('Triangulo isósceles.')
        if A != C and A == B or C == B:
            print('triangulo isósceles')
        if B != C and B == A or C == A:
            print('Triângulo isósceles')

        if A != B and A != C and B != C:
            print('Triangulo escaleno.')

    if A > B + C or B > A + C or C > A + B:
        print('Nao podem ser valores de lados de um triângulo.')

if A < 0.0 or B < 0.0 or C < 0.0:
    print('Algum valor é negativo.')

#-----------------------------------------------------------------
# Exercício 21 - trabalhando com um menu para selecionar operacoes
#-----------------------------------------------------------------

num1 = float(input('Entre com um número:'))
num2 = float(input('Entre com outro número:'))

print('Escolha a opção dentre as disponiveis abaixo:')
print('1- Soma de números.')
print('2- Diferença entre dois número - maior pelo menor.')
print('3- Produto entre dois números.')
print('4- Divisão entre dois números - o denominador não pode ser zero.')

op = int(input('Digite sua escolha aqui:'))

if op == 1:
    print(f'A soma dos numeros {num1} e {num2} e {num1+num2}')
elif op == 2:
    if num1 > num2:
        print(f'A diferenca dos numeros {num1} e {num2} e {num1 - num2}')
    if num1 < num2:
        print(f'A diferenca dos numeros {num1} e {num2} e {num2 - num1}')
elif op == 3:
    print(f'O produto entre {num1} e {num2} e {num1*num2}')
elif op == 4:
    if num2 != 0:
        print(f'A divisao de {num1} por {num2} e {num1/num2}')
    else:
        print('Divisao por zero!!')

#-----------------------------------------------------------------
# Exercício 22 - Tempo de servico e aposentadoria
#-----------------------------------------------------------------

idade = int(input('Qual a idade?'))

if idade >= 65:
    tempo = int(input('Quanto tempo de servico?'))
    if tempo >=30:
        print('Pode se aposentar.')
    else:
        print('Nao pode se aposentar.')
elif idade >=60:
    tempo = int(input('Quanto tempo de servico?'))
    if tempo >= 25:
        print('Pode se aposentar')
    else:
        print('Nao pode se aposentar.')
elif idade < 60:
    print('Nao pode se aposentar.')

#-----------------------------------------------------------------
# Exercício 23 - Identificando se o ano e bissexto ou nao
#-----------------------------------------------------------------
ano = int(input('Digite um ano:'))
print(ano % 400)
print(ano % 4)
print(ano % 100)
if ano % 400 == 0 or ano % 4 == 0 and (ano % 100) != 0:
    print('Ano bissexto.')
else:
    print('Ano não bissexto.')


# -----------------------------------------------------------------
# Exercício 24 - Calculando impostos sobre produtos
# -----------------------------------------------------------------
'''
print('Destinos:')
print('1 - Minas Gerais.')
print('2 - São Paulo.')
print('3 - Rio de Janeiro.')
print('4 - Mato Grosso do Sul.')

Estado = int(input('Dentre as opções acima, escolha o número referente ao estado para onde o produto será enviado:'))

def switch_state(estado):
    switcher = {
        1: "Minas Gerais",
        2: "São Paulo",
        3: "Rio de Janeiro",
        4: "Mato Grosso do Sul"
    }
    print(switcher.get(int(estado), "Estado invalido"))
'''

valor = float(input('Entre com o valor do produto:'))

ImpMG = 0.07
ImpSP = 0.12
ImpRJ = 0.15
ImpMS = 0.08


Estado = input('Qual o estado para onde o produto será enviado:')

if Estado == "Minas Gerais":
    total = valor + ImpMG * valor
    print('O produto sera encaminhado para Minas Gerais.')
    print(f'O valor total do produto com o imposto e de {total} ')
elif Estado == "São Paulo" or Estado == "Sao Paulo":
    total = valor + ImpSP * valor
    print('O produto sera encaminhado para São Paulo.')
    print(f'O valor total do produto com o imposto e de {total} ')
elif Estado == "Rio de Janeiro":
    total = valor + ImpRJ * valor
    print('O produto sera encaminhado para Rio de Janeiro.')
    print(f'O valor total do produto com o imposto e de {total} ')
elif Estado == "Mato Grosso do Sul":
    total = valor + ImpMS * valor
    print('O produto sera encaminhado para  Mato Grosso do Sul.')
    print(f'O valor total do produto com o imposto e de {total} ')
else:
    print('Estado não coberto.')
    print('Destinos possiveis sao:')
    print('Minas Gerais.')
    print('São Paulo.')
    print('Rio de Janeiro.')
    print('Mato Grosso do Sul.')


#------------------------------------------------------------------
# Exercício 25 - Formula de Bhaskara
#------------------------------------------------------------------

print('A seguir, digite os coeficientes da equacao do tipo a*x^2 + b*x + c.')
a = float(input('Coeficiente angular a: '))

if a != 0:
    b = float(input('Coeficiente linear b: '))
    c = float(input('termo constante c: '))
    Delta = b**2 - 4*a*c
    if Delta < 0:
        print('Nao existe raiz real.')
    elif Delta == 0:
        x = -b/(2*a)
        print(f'Raiz unica e igual a {x} ')
    elif Delta > 0:
        x1 = (-b + sqrt(Delta))/2*a
        x2 = (-b - sqrt(Delta))/2*a
        print(f'Duas raizes reais, sendo x+ = {x1} e x- = {x2}')
else:
    print('Nao e uma equação de segundo grau!')


#---------------------------------------------------------------
# Exercicio 26 - Consumo de gasolina de um carro
#---------------------------------------------------------------

km = float(input('Qual a distancia total do percurso?'))
litro = float(input('Quanto litros de gasolina foram consumidos nesse percursos?'))

consumo = km/litro

if consumo <= 8:
    print('Venda o carro!')
elif 8 < consumo <= 14:
    print('Economico!')
elif consumo >= 12:
    print('Super economico!')
    

#---------------------------------------------------------------
# Exercicio 27 - Categorias de natacao
#---------------------------------------------------------------

idade = int(input('Qual a idade do atleta?'))

if 5 <= idade <= 7:
    print('categoria infantil A.')
elif 8 <= idade <= 10:
    print('categoria infantil B.')
elif 11 <= idade <= 13:
    print('categoria juvenil A.')
elif 14 <= idade <= 17:
    print('categoria juvenil B.')
elif idade > 18:
    print('categoria senior.')


# ---------------------------------------------------------------
# Exercicio 28 - Calculando diferentes medias
# ---------------------------------------------------------------

x = int(input('Digite um valor para x:'))
y = int(input('Digite um valor para y:'))
z = int(input('Digite um valor para z:'))

print('Escolha um letra para cada uma das opcoes de media a ser calculada:')
print('a - Geometrica')
print('b - Ponderada')
print('c - Harmonica')
print('d - Aritmetica')

letra = input('Qual media sera calculada:')

if letra == "a":
    media = (x*y*z)**1/3
    print(f'A media geometrica de {x}, {y}, e {z} e {media}')
elif letra == "b":
    media = (x+2*y+3*z)/6
    print(f'A media ponderada de {x}, {y}, e {z} e {media}')
elif letra == "c":
    media = x*y*z/(x*y+y*z+z*x)
    print(f'A media harmonica de {x}, {y}, e {z} e {media}')
elif letra == "d":
    media = (x+y+z)/3
    print(f'A media aritmetica de {x}, {y}, e {z} e {media}')


# ---------------------------------------------------------------
# Exercicio 29 - prova de matematica
# ---------------------------------------------------------------

print('Prova de matematica.')
print('Assunto: adicao de numeros naturais')
print('Responda as 5 perguntas abaixo. Cada item vale 1 ponto.')

Q1 = True
Q2 = True
Q3 = True
Q4 = True
Q5 = True

nota = 0.0
q = 0.0

if Q1 is True:
    # seed random number generator
    seed()
    # generate random integer values
    a = randint(0, 100)
    b = randint(0, 100)
    print(f'Seja os numero {a}, {b}.')
    resposta1 = int(input('Qual a soma entre eles?'))
    if resposta1 == a + b:
        print('Voce acertou.')
        nota = nota + 1
        q = q+1
    else:
        print('Voce errou.')
        print(f'Resposta correta e {a + b}')
if Q2 is True:
    # seed random number generator
    seed()
    # generate some integers
    a = randint(0, 100)
    b = randint(0, 100)
    print(f'Seja os numero {a}, {b}.')
    resposta = int(input('Qual a soma entre eles?'))
    if resposta == a + b:
        print('Voce acertou.')
        nota = nota + 1
        q = q+1
    else:
        print('Voce errou.')
        print(f'Resposta correta e {a+b}')
if Q3 is True:
    # seed random number generator
    seed()
    # generate some integers
    a = randint(0, 100)
    b = randint(0, 100)
    print(f'Seja os numero {a}, {b}.')
    resposta = int(input('Qual a soma entre eles?'))
    if resposta == a + b:
        print('Voce acertou')
        nota = nota + 1
        q = q+1
    else:
        print('Voce errou')
        print(f'Resposta correta e {a+b}')
if Q4 is True:
    # seed random number generator
    seed()
    # generate some integers
    a = randint(0, 100)
    b = randint(0, 100)
    print(f'Seja os numero {a}, {b}.')
    resposta = int(input('Qual a soma entre eles?'))
    if resposta == a + b:
        print('Voce acertou')
        nota = nota + 1
        q = q+1
    else:
        print('Voce errou')
        print(f'Resposta correta e {a+b}')
if Q5 is True:
    # seed random number generator
    seed()
    # generate some integers
    a = randint(0, 100)
    b = randint(0, 100)
    print(f'Seja os numero {a}, {b}.')
    resposta = int(input('Qual a soma entre eles?'))
    if resposta == a + b:
        print('Voce acertou')
        nota = nota + 1
        q = q+1
    else:
        print('Voce errou')
        print(f'Resposta correta e {a+b}')

print(f'Voce acertou {int(q)} questoes e sua nota foi {nota}.')


# ---------------------------------------------------------------
# Exercicio 30 - ordem crescente de 3 numeros
# ---------------------------------------------------------------

a = float(input('Digite um numero:'))
b = float(input('Digite outro numero:'))
c = float(input('Digite mais um numero:'))

if a > b and a > c:
    if b > c:
        print(f'Ordem crescente {c}< {b} < {a}')
    else:
        print(f'Ordem crescente {b}< {c} < {a}')
elif b > a and b > c:
    if a > c:
        print(f'Ordem crescente {c}< {a} < {b}')
    else:
        print(f'Ordem crescente {a}< {c} < {b}')
elif c > a and c > b:
    if a > b:
        print(f'Ordem crescente {b} < {a} < {c}')
    else:
        print(f'Ordem crescente {a} < {b} < {c}')

#---------------------------------------------------------------------
# Exercicio 31 - Categorias de atletas
#---------------------------------------------------------------------

altura = float(input('Qual a altura em cm?'))
peso = float(input('Qual o peso em kg ?'))

if altura < 120:
    if peso < 60:
        print('Classificacao A')
    elif 60 <= peso <=90:
        print('Classificacao D')
    elif peso > 90:
        print('Classificacao G')
elif 120<= altura <= 170:
    if peso < 60:
        print('Classificacao B')
    elif 60 <= peso <=90:
        print('Classificacao E')
    elif peso > 90:
        print('Classificacao H')
elif altura > 170:
    if peso < 60:
        print('Classificacao C')
    elif 60 <= peso <=90:
        print('Classificacao F')
    elif peso > 90:
        print('Classificacao I')

# ---------------------------------------------------------------------
# Exercicio 32 - Lendo codigos de um pedido
# ---------------------------------------------------------------------

codigo = int(input('Digite o codigo do pedido:'))
qtd = int(input('Quantidade do pedido:'))

if codigo == 100:
    print('Preco do cachorro quente R$ 1.20')
    valor = 1.20*qtd
    print(f' Valor de {qtd} cachorro quente sera {valor}')
elif codigo == 101:
    print('Preco do Bauru simples R$ 1.30')
    valor = 1.30*qtd
    print(f' Valor de {qtd} Bauru simples sera {valor}')
elif codigo == 102:
    print('Preco do Bauru com ovo R$ 1.50')
    valor = 1.50*qtd
    print(f' Valor de {qtd} Bauru com ovo sera {valor}')
elif codigo == 103:
    print('Preco do hamburguer R$ 1.20')
    valor = 1.20*qtd
    print(f' Valor de {qtd} hamburguer sera {valor}')
elif codigo == 104:
    print('Preco do cheeseburguer R$ 1.70')
    valor = 1.70*qtd
    print(f' Valor de {qtd} cheeseburguer sera {valor}')
elif codigo == 105:
    print('Preco do suco R$ 2.20')
    valor = 2.20*qtd
    print(f' Valor de {qtd} sucos sera {valor}')
elif codigo == 106:
    print('Preco do refrigerante R$ 1.00')
    valor = 1.00*qtd
    print(f' Valor de {qtd} refrigerante sera {valor}')

# ---------------------------------------------------------------------
# Exercicio 33 - ajuste de preco
# ---------------------------------------------------------------------

antigo = float(input('Qual o preco antes do reajuste: '))
novo = 0.0
#calcular e escrever o novo preco

if antigo <= 50.00:
    novo = 0.05*antigo + antigo
    print(f'O valor apos o reajuste sera de {novo}')
elif 50.00 < antigo <= 100:
    novo = 0.10*antigo + antigo
    print(f'O valor novo apos o reajuste sera de {novo}')
elif antigo > 100.00:
    novo = 0.15*antigo + antigo
    print(f'O valor novo apos o reajuste sera de {novo}')

if novo <= 80.00:
    print('Barato')
elif 80.00 < novo <= 120.00:
    print('Normal')
elif 120.00 < novo <= 200.00:
    print('Caro')
elif novo > 200.00:
    print('Muito caro')


#------------------------------------------------------------------
# Exercicio 34 - Calculando conceito para uma disciplina
#-------------------------------------------------------------------

nota = float(input('Qual a nota do aluno? '))
faltas = int(input('Quantas faltas o aluno teve? '))
conceito = ''

if faltas <= 20:
    if 0.0 <= nota <= 3.9:
        conceito = 'E'
    elif 4.0 <= nota <= 4.9:
        conceito = 'D'
    elif 5.0 <= nota <= 7.4:
        conceito = 'C'
    elif 7.5 <= nota <= 8.9:
        conceito = 'B'
    elif 9.0 <= nota <= 10.0:
        conceito = 'A'
elif faltas > 20:
    if 0.0 <= nota <= 3.9:
        conceito = 'E'
    elif 4.0 <= nota <= 4.9:
        conceito = 'E'
    elif 5.0 <= nota <= 7.4:
        conceito = 'D'
    elif 7.5 <= nota <= 8.9:
        conceito = 'C'
    elif 9.0 <= nota <= 10.0:
        conceito = 'B'

print(f'O conceito do aluno na disciplina e {conceito}')

#-----------------------------------------------------------------------------
# Exercicio 35 - Validando uma data inserida pelo usuario
# obs: pensar melhor como distinguir os meses com 30 e 31 dias
# obs: Se quiser alterar para datas a posteriores ou anteriores da data atual,
# basta colocar uma outra condicao mais abrangente
#------------------------------------------------------------------------------

data = input('Entre com uma data no formato (dd/mm/aaaa): ')
dia = int(data[0:2])
mes = int(data[3:5])
ano = int(data[6:10])

#print(dia, mes, ano)

#meses do ano
teste = list(range(1, 13, 1))

#lista com meses de 31 dias mais fevereiro
lista1 = [1, 2, 3, 5, 7, 8, 10, 12]
#lista com meses de 30 dias mais fevereiro
lista2 = [2, 4, 6, 9, 11]


#print(teste)

if mes in teste:
    if ano % 400 == 0 or ano % 4 == 0 and (ano % 100) != 0:
        #print('Ano bissexto.')
        if mes == 2:
            if 1 <= dia <= 29:
                print('Data valida')
            else:
                print('Data invalida')
        elif mes in lista1:
            if 1 <= dia <= 31:
                print('Data valida')
            else:
                print('data invalida')
        elif mes in lista2:
            if 1 <= dia <= 30:
                print('Data valida')
            else:
                print('data invalida')

    else:
        #print('Ano não bissexto.')
        if mes == 2:
            if 1 < dia <= 28:
                print('Data valida')
            else:
                print('data invalida')
        elif mes in lista1:
            if 1 < dia <= 31:
                print('Data valida')
            else:
                print('data invalida')
        elif mes in lista2:
            if 1 < dia <= 30:
                print('Data valida')
            else:
                print('data invalida')
else:
    print('Data invalida')

#-------------------------------------------------------
# Exercicio 36 - Calculando comissao de vendas
#------------------------------------------------------
valor = float(input("Qual foi o  valor da venda:"))

if valor >= 100000:
    print("Venda acima de R$100.000,00. Parabens!!")
    print(f'A comissão será de {700+0.16*valor}.')
elif 80000 <= valor < 100000:
    print("Venda entre R$80.000,00 R$100.000,00. Parabens!!")
    print(f'A comissão será de {650+0.14*valor}')
elif 60000 <= valor < 80000:
    print("Venda entre R$60.000,00 R$80.000,00.")
    print(f'A comissão será de {600 + 0.14*valor}')
elif 40000 <= valor < 60000:
    print("Venda entre R$40.000,00 R$60.000,00.")
    print(f'A comissão será de {550 + 0.14*valor}')
elif 20000 <= valor < 40000:
    print("Venda entre R$20.000,00 R$40.000,00.")
    print(f'A comissão será de {500 + 0.14*valor}')
elif valor < 20000:
    print("Venda abaixo de R$20.000,00.")
    print(f'A comissão será de {400 + 0.14*valor}')
"""

# -------------------------------------------------------
# Exercicio 37 - preço cobrado pelo estacionamento
# -------------------------------------------------------


# --------------------------------------------------------------------------------------------------------
# Exercício 38 - similar ao exercicio 36 mas considerando datas de nascimento ate o dia mes ano atual.
# ---------------------------------------------------------------------------------------------------------


# -------------------------------------------------------
# Exercício 39 - calculando aumentos de salario
# -------------------------------------------------------


# -------------------------------------------------------
# Exercício 40 - Validando data
# -------------------------------------------------------


# -------------------------------------------------------
# Exercício 41 - Validando data
# -------------------------------------------------------
