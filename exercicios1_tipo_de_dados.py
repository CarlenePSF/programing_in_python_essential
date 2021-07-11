""":cvar
Lista d exercicios sobre tipos de dados
"""


"""
#-------------------------------------------------
# Exercicio numero 1
#-------------------------------------------------
num = 1
print(f'{num}')

#-------------------------------------------------
# Exercicio numero 2
#-------------------------------------------------
num2=3.4
print(f'{num2}')

#-------------------------------------------------
# Exercicio numero 3
#-------------------------------------------------
a = input('difite um valor para a:')
b = input('digite um valor para b:')
c = input('digite um valor para c:')
soma = int(a) + int(b) + int(c)             # nao esquecer de fazer o casting dos valores digitados no input()
print(f'A soma de {a} + {b} + {c} e igual a {soma}')


#------------------------------------------------
# Exercicio 4
#-----------------------------------------------
num = input('digite um numero real:')
sqrt = float(num)
print(f'O quadrado de {num} e %f' % (sqrt*sqrt))
print(f'O quadrado de {num} e {sqrt*sqrt}')


#------------------------------------------------
# Exercicio 5
#-----------------------------------------------

num = input('digite um numero real:')
quinta = float(num)/5
print(quinta)


#------------------------------------------------
# Exercicio 6
#-----------------------------------------------
temC = input('digite a temperatura em Celsius:')
TC = float(temC)                  #casting para transformar o valor do input em real
TF = TC * (9.0/5.0) + 32.0        # formula para converter
print(f'A temperatura em Fahrenheit e {TF}.')


#------------------------------------------------
# Exercicio 7
#-----------------------------------------------
temF = input('digite a temperatura em Fahrenheit:')
TF = float(temF)                  #casting para transformar o valor do input em real
TC= 5.0 * (TF -32) / 9.0          # formula para converter
print(f'A temperatura em Celsius e {TC}.')


#------------------------------------------------
# Exercicio 8
#-----------------------------------------------
temK = input('digite a temperatura em Kelvin:')
TK = float(temK)                  #casting para transformar o valor do input em real
TC= TK - 273.15          # formula para converter
print(f'A temperatura em Celsius e {TC}.')


#------------------------------------------------
# Exercicio 9
#-----------------------------------------------
temC = input('digite a temperatura em Celsius:')
TC = float(temC)                  #casting para transformar o valor do input em real
TK= TC + 273.15          # formula para converter
print(f'A temperatura em Kelvin e {TK}.')

#------------------------------------------------
# Exercicio 10
#-----------------------------------------------
K = input('digite uma velocidade em k/h:')
K = float(K)                  #casting para transformar o valor do input em real
M =  K/3.6          # formula para converter
print(f'A velocidade em m/s e {M}.')

#------------------------------------------------
# Exercicio 11
#-----------------------------------------------
m = input('digite uma velocidade em m/s:')
m = float(m)                  #casting para transformar o valor do input em real
k =  m *3.6          # formula para converter
print(f'A velocidade em km/h e {k}.')

#------------------------------------------------
# Exercicio 12
#-----------------------------------------------
milhas = input('digite a distancia em milhas:')
milhas = float(milhas)                  #casting para transformar o valor do input em real
km = 1.609 * milhas                      # formula para converter
print(f'A distancia em km e {km}.')


#------------------------------------------------
# Exercicio 13
#-----------------------------------------------
km = input('digite a distancia em quilometro:')
km = float(km)                  #casting para transformar o valor do input em real
milhas = km/1.609                      # formula para converter
print(f'A distancia em km e {milhas}.')


#------------------------------------------------
# Exercicio 14
#-----------------------------------------------
graus = input('digite o angulo em graus:')
graus = float(graus)                  #casting para transformar o valor do input em real
pi = 3.14
radianos = graus*(pi)/180                      # formula para converter
print(f'O angulo {graus} em graus equivale a {radianos} em radianos.')

#------------------------------------------------
# Exercicio 15
#-----------------------------------------------
radianos = input('digite o angulo em radianos:')
radianos = float(radianos)                  #casting para transformar o valor do input em real
pi = 3.141592

graus = radianos * 180 / pi                      # formula para converter
print(f'O angulo {radianos} em radiano equivale a {graus} em graus.')

print(2*pi)


#------------------------------------------------
# Exercicio 16
#-----------------------------------------------
pol = input('digite o comprimento em polegadas:')
#casting para transformar o valor do input em real
pol = float(pol)
cm = pol * 2.54                      # formula para converter
print(f'O comprimento de {pol} polegadas equivale a {cm} em centimetros.')


#------------------------------------------------
# Exercicio 17
#-----------------------------------------------
cm = input('digite o comprimento em centimetros:')
#casting para transformar o valor do input em real
cm = float(cm)
pol = cm / 2.54                      # formula para converter
print(f'O comprimento de {cm} centrimetros equivale a {pol} em polegadas.')


#-----------------------------------------------------
# Exercicio 18
#-----------------------------------------------------

m3 = input('digite o valor de volume em metros cubicos que deve ser convertido:')
m3 = float(m3)

litro = 10.0**3 * m3
print(f'O volume {m3} em metros cubicos equivale a {litro} em litros.')


#-----------------------------------------------------
# Exercicio 28
#-----------------------------------------------------
a = float(input('digite o primeiro valor:'))
b = float(input('digite o segundo valor:'))
c = float(input('digite o terceiro valor:'))
res = a**2+b**2+c**2
print(f'O resultado da soma dos quadrados dos tres valores digitados e {res}.')


#-----------------------------------------------------
# Exercicio 29
#-----------------------------------------------------

nota1 = float(input('Nota da primeira avaliação:'))
nota2 = float(input('Nota da segunda avaliação:'))
nota3 = float(input('Nota da terceira avaliação:'))
nota4 = float(input('Nota da quarta avaliação:'))

media = (nota1+nota2+nota3+nota4)/4.0

print(f'A media aritmetica do aluno foi {media}')

#---------------------------------------------------
# Exercicio 30
#---------------------------------------------------
# Dolar dia 21/04/2021 : 5.57

dollar = float(input('Qual a cotação do dollar hoje?'))
real = float(input('Quanto quer converter?'))

real = real / dollar

print('O valor convertido total sera de %f dolares' % (real))

#---------------------------------------------------
# EXercicio 31
#---------------------------------------------------
num = int(input('Digite um valor numerico?'))
print(f'O antecessor e o sucessor de {num} sao {num-1} e {num+1}, respectivamente.')


#---------------------------------------------------
# EXercicio 32
#---------------------------------------------------
num = int(input('Digite um valor numerico?'))
print(f'O sucessor do triplo de {num}  e {num**3 + 1}.')
print(f'O antecessor do dobro de {num}  e {num**2 - 1}.')
print(f' A soma de {num**3 + 1} com {num**2 - 1} e igual a {(num **3 + 1) + (num**2 - 1)}')

#---------------------------------------------------
# EXercicio 33
#---------------------------------------------------

lado = float(input('qual o lado do quadrado?'))
print(f'A area do quadrado e {lado **2}')

#------------------------------------
# Exercicio 34
# -----------------------------------
r = float(input('Qual o raio do circulo?'))
pi = 3.242592
A = pi * r**2
print(f'A area do circulo e {A}.')

#-------------------------------------
#  Exercicio 35
# -----------------------------------

a = float(input('Valor do primeiro cateto:'))
b = float(input('Valor do segundo cateto:'))
c = (a**2+b**2)**0.5
print(f'O valor da hipotenusa e {c}')


#-------------------------------------
#  Exercicio 36
# -----------------------------------
r = float(input('Qual o raio da base do cilindro?'))
h = float(input('Qual a altura do cilindro?'))
pi = 3.242592
V = pi * r**2 * h
print(f'O volume do cilindro e {V}')


#--------------------------------
# Exercicio 37
# --------------------------------

valor = float(input('Qual o valor do produto?'))
desconto = (12/100)*valor
print(f'O valor a ser pago com desconto sera {valor - desconto}.')

#--------------------------------
# Exercicio 38
# --------------------------------

salario = float(input('Qual o valor do salario?'))
aumento = (25/100)*salario
print(f'O valor d salario apos o aumento sera {salario + aumento}.')

#------------------------------------
# Exercicio 39
#------------------------------------

total = 780000.00
premio1 = (46/100)*total
premio2 = (32/100)*total
premio3 = (total - premio1 - premio2)

print(f'O premio total foi de {premio1+premio2+premio3}')
print('O premio para cada ganhador sera:')
print(f'Primeiro ganhador {premio1}')
print(f'Segundo ganhador {premio2}')
print(f'Terceiro ganhador {premio3}')


#------------------------------------------------
# Exercicio 40
# -----------------------------------------------


dias = int(input('Quantos dias foram trabalhados?'))
valor = 30.00
total = dias*valor
imposto = (8/100)*total
print(f'O valor que deve ser pago é {total - imposto}')

#------------------------------------------------
# Exercicio 41
# -----------------------------------------------


valorhora = float(input('Qual o valor pago por hora, em reais?'))
horas = float(input('Quantas horas foram trabalhadas no mes?'))
gratificacao = (10/100)*(horas*valorhora)
print(f'O valor total a ser pago ao funcionario e {horas*valorhora + gratificacao}')

#------------------------------------------------
# Exercicio 42
# -----------------------------------------------


salariobase = float(input('Qual o valor do salario base?'))
gratificacao = (5/100)*salariobase
imposto = (7/100)*salariobase
print(f'O salario a receber e {salariobase+gratificacao-imposto}')


#------------------------------------------------
# Exercicio 43
# -----------------------------------------------


valortotal = float(input('Qual o valordo produto?'))
desconto = (10/100)*valortotal
parcelas = int(input('Quantas parcelas?'))
valorcomparcelamento = (valortotal - desconto)/parcelas
comisaoavista = (5/100)*(valortotal-desconto)
comissoparcelada = (5/100)*valortotal

print(f'A vista : total a pagar com desconto de 10% {valortotal-desconto}')
print(f'O valor de cada uma das {parcelas} sera {valorcomparcelamento}')
print(f'Comissao do vendedor da venda a vista: {comisaoavista}')
print(f'Comisso do vendedor na venda parcelada: {comissoparcelada}')

#------------------------------------------------
# Exercicio 45
# -----------------------------------------------

dado = input('Digite uma maiuscula:')
#print(dir(dado))
print(dado.lower())


#------------------------------------------------
# Exercicio 46
# -----------------------------------------------

num = input('Digite um numero inteiro de tres digitos:')
#print(dir(num))
print(num[::-1])

#------------------------------------------------
# Exercicio 47
# -----------------------------------------------

num = input('Digite um numero inteiro com quatro digitos:')
#print(dir(num))
print(f'{num[0]}')
print(f'{num[1]}')
print(f'{num[2]}')
print(f'{num[3]}')


#------------------------------------------------
# Exercicio 49
# -----------------------------------------------

inicio = input('Qual o horario inicial (hh/mim/ss)?')
hora = int(inicio[0:2])
mim = int(inicio[3:5])
seg = int(inicio[6:8])

print(f'{hora} h')
print(f'{mim} mim')
print(f'{seg} s')

inicioseg = int(hora*3600+mim*60+seg)
print(f'A tempo inicial total em segundos {inicioseg} ')

#------------------------------------------------
# Exercicio 50
# -----------------------------------------------
nome = input('Qual seu nome?')
print(f'Seja bem-vindo(a) {nome}!')
idade = input('Qual a sua idade?')
print(f'A {nome} nasceu em {2021- int(idade)} e tem {idade} anos ')
print("%s tem %s de idade" % (nome, idade))

#------------------------------------------------
# Exercício 51
# -----------------------------------------------

x = float(input('Qual a coordenada x?'))
y = float(input('Qual a coordenada y?'))
distancia = (x**2 + y**2)**(1/2)
print(f'A distncia do ponto ({x},{y}) da origem (0,0) e {distancia}')
"""

# ------------------------------------------------
# Exercício 52
# -----------------------------------------------

p1 = float(input('Aposta do primeiro jogador:'))
p2 = float(input('Aposta do segundo jogador:'))
p3 = float(input('Aposta do terceiro jogador:'))

premiototal = float(input('Qual o valor do premio?'))

totalapostas = p1+p2+p3

porcentagem1 = (p1*100)/totalapostas
porcentagem2 = (p2*100)/totalapostas
porcentagem3 = (p3*100)/totalapostas

print(f'O premio do primeiro colocado: {0.01*porcentagem1*premiototal}')
print(f'O premio do segundo colocado:  {0.01*porcentagem2*premiototal}')
print(f'O premio do terceiro colocado: {0.01*porcentagem3*premiototal}')

print(f'{0.01*porcentagem1*premiototal +0.01*porcentagem2*premiototal + 0.01*porcentagem3*premiototal}')
