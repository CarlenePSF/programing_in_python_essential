"""
Lista de exercicios sobre tipos de dados
"""

# -------------------------------------------------
# Exercicio numero 1 - imprime um número inteiro
# -------------------------------------------------

"""
numero_inteiro: int = int(input('Digite um número inteiro: '))
print(f'O número inserido foi {numero_inteiro}.')
"""

# -------------------------------------------------
# Exercicio numero 2 - imprime um número real
# -------------------------------------------------

"""
numero_real: float = float(input('digite um número real: '))
print(f'O número inserido foi {numero_real}')
"""

# -------------------------------------------------
# Exercicio numero 3 - soma três valores inteiros
# -------------------------------------------------

"""
a: int = int(input('digite um valor para a: '))
b: int = int(input('digite um valor para b: '))
c: int = int(input('digite um valor para c: '))
soma = a+b+c
print(f'A soma de {a} + {b} + {c} e igual a {soma}')
"""

# ----------------------------------------------
# Exercicio 4 - quadrado de um número real
# -----------------------------------------------

"""
numero_real = float(input('Digite um numero real: '))
print(f'O quadrado de {numero_real} é %f' % (numero_real*numero_real))  # precisando casas decimais
print(f'O quadrado de {numero_real} é {numero_real*numero_real}')  # arredonda as casas decimais
"""
# ------------------------------------------------
# Exercicio 5 - a quinta parte de um número
# -----------------------------------------------

"""
numero = input('Digite um número real: ')
quinta_parte = float(numero) / 5
print(quinta_parte)
"""

# ----------------------------------------------
# Exercicio 6 - Converte Celsius em Fahrenheit
# -----------------------------------------------
"""
temperatura_celsius = float(input('Digite a temperatura em Celsius: '))
temperatura_fahrenheit = temperatura_celsius * (9.0 / 5.0) + 32.0  # formula para converter
print(f'A temperatura em Fahrenheit e {temperatura_fahrenheit}.')
"""

# ----------------------------------------------
# Exercicio 7 - Converte Fahrenheit em Celsius
# -----------------------------------------------
"""
temperatura_fahrenheit = float(input('Digite a temperatura em Fahrenheit: '))
temperatura_celsius= 5.0 * (temperatura_fahrenheit - 32) / 9.0  # formula para converter
print(f'A temperatura em Celsius e {temperatura_celsius}.')
"""

# ----------------------------------------------
# Exercicio 8 - Converte Kelvin an Celsius
# -----------------------------------------------
"""
temperatura_kelvin = float(input('Digite a temperatura em Kelvin: '))
temperatura_celsius= temperatura_kelvin - 273.15  # formula para converter
print(f'A temperatura em Celsius e {temperatura_celsius}.')
"""

# ----------------------------------------------
# Exercicio 9 - converte Celsius em Kelvin
# ----------------------------------------------

"""
temperatura_celsius = float(input('Digite a temperatura em Celsius: '))
temperatura_kelvin= temperatura_celsius + 273.15  # formula para converter
print(f'A temperatura em Kelvin e {temperatura_kelvin}.')
"""

# ----------------------------------------------------
# Exercicio 10 - convertendo velocidade de km/h -> m/s
# ----------------------------------------------------

"""
velocidade_km_por_hora = float(input('Digite uma velocidade em k/h: '))
velocidade_metro_por_segundo = velocidade_km_por_hora/3.6  # formula para converter
print(f'A velocidade em m/s e {velocidade_metro_por_segundo}.')
"""

# ----------------------------------------------------
# Exercicio 11 - convertendo velocidade de m/s -> km/h
# ----------------------------------------------------

"""
velocidade_metro_por_segundo = float(input('Digite uma velocidade em m/s: '))
velocidade_km_por_hora =  velocidade_metro_por_segundo*3.6  # formula para converter
print(f'A velocidade em km/h e {velocidade_km_por_hora}.')
"""

# ---------------------------------------------------
# Exercicio 12 - convertendo distâncias  milhas -> km
# ---------------------------------------------------

"""
milhas = float(input('Digite a distancia em milhas: '))
quilometros = 1.609 * milhas  # formula para converter
print(f'A distancia em quilômetros é {quilometros}.')
"""

# --------------------------------------------------
# Exercicio 13 - convertendo distâncias km -> milhas
# --------------------------------------------------

"""
quilometro = float(input('Digite a distancia em quilômetro: '))
milhas = quilometro/1.609  # formula para converter
print(f'A distancia em milhas é {milhas}.')
"""

# ---------------------------------------------------
# Exercicio 14 - convertendo de graus para radianos
# ---------------------------------------------------

"""
graus = float(input('Digite o ângulo em graus: '))
pi = 3.14
radianos = graus*pi/180  # formula para converter
print(f'O ângulo {graus} em graus equivale à {radianos} em radianos.')
"""

# ---------------------------------------------------
# Exercicio 15 - convertendo de radianos para graus
# ---------------------------------------------------

"""
radianos = float(input('Digite o angulo em radianos: '))
pi = 3.141592
graus = radianos * 180 / pi  # formula para converter
print(f'O ângulo {radianos} em radianos equivale à {graus} em graus.')
"""

# -------------------------------------------------------
# Exercicio 16 - convertendo de polegada para centímetro
# -------------------------------------------------------

"""
polegadas = float(input('Digite o comprimento em polegadas: '))
centimetros = polegadas * 2.54  # formula para converter
print(f'{polegadas} polegadas equivale à {centimetros} em centímetros.')
"""

# ------------------------------------------------------
# Exercicio 17 - convertendo de centímetro para polegada
# ------------------------------------------------------

"""
centimetro = float(input('Digite o comprimento em centimetros: '))
polegada = centimetro/2.54 # formula para converter
print(f'{centimetro} centímetros equivale à {round(polegada, 2)} em polegadas.')
"""

# -----------------------------------------------------
# Exercicio 18 - conversão de volume
# -----------------------------------------------------

"""
volume_metros_cubicos = float(input('Digite o valor do volume em metros cúbicos que deve ser convertido: '))
volume_litros = volume_metros_cubicos * 10.0**3
print(f'O volume {volume_metros_cubicos} em metros cubicos equivale à {volume_litros} em litros.')
"""

# -----------------------------------------------------
# Exercicio 28 - soma do quadrado de três números
# -----------------------------------------------------

"""
a = float(input('Digite o primeiro valor: '))
b = float(input('Digite o segundo valor: '))
c = float(input('Digite o terceiro valor: '))
print(f'A soma dos quadrados dos três valores digitados é {a*a + b*b + c*c}.')
"""

# -----------------------------------------------------
# Exercicio 29 - calculando média aritmética
# -----------------------------------------------------
"""
primeira_nota = float(input('Nota da primeira avaliação: '))
segunda_nota = float(input('Nota da segunda avaliação: '))
terceira_nota = float(input('Nota da terceira avaliação: '))
quarta_nota = float(input('Nota da quarta avaliação: '))
media = (primeira_nota+segunda_nota+terceira_nota+quarta_nota)/4.0

print(f'A media aritmetica do aluno foi {media}')
"""

# ---------------------------------------------------
# Exercicio 30 - convertendo moedas
# ---------------------------------------------------

"""
dollar = float(input('Qual a cotação do dollar hoje? '))
real = float(input('Quanto quer converter?'))
real = real / dollar
print('O valor convertido total sera de %f dolares' % real)
"""

# ---------------------------------------------------
# Exercicio 31 - antecessor e sucessor de um número
# ---------------------------------------------------

"""
numero = int(input('Digite um valor numerico? '))
print(f'O antecessor e o sucessor de {numero} sao {numero - 1} e {numero + 1}, respectivamente.')
"""

# ---------------------------------------------------------------------------
# Exercicio 32 - antecessor e sucessor do dobro e do triplo, respectivamente.
# ---------------------------------------------------------------------------

"""
numero = int(input('Digite um valor numérico? '))
print(f'O sucessor do triplo de {numero}  e {numero ** 3 + 1}.')
print(f'O antecessor do dobro de {numero}  e {numero ** 2 - 1}.')
print(f' A soma de {numero ** 3 + 1} com {numero ** 2 - 1} e igual a {(numero ** 3 + 1) + (numero ** 2 - 1)}')
"""

# ---------------------------------------------------
# Exercicio 33 - área de um quadrado
# ---------------------------------------------------

"""
lado = float(input('Qual o lado do quadrado? '))
print(f'A area do quadrado e {lado **2}')
"""

# ------------------------------------
# Exercicio 34 - área de um círculo
# -----------------------------------
"""
raio = float(input('Qual o raio do circulo?'))
pi = 3.242592
area = pi * raio**2
print(f'A area do circulo e {area}.')
"""

# -------------------------------------
#  Exercicio 35 - teorema de Pitágoras
# -------------------------------------
"""
cateto_1 = float(input('Valor do primeiro cateto: '))
cateto_2 = float(input('Valor do segundo cateto: '))
hipotenusa = (cateto_1 ** 2 + cateto_2 ** 2) ** (1 / 2)
print('O valor da hipotenusa e %f' % hipotenusa)
"""

# --------------------------------------
#  Exercicio 36 - volume de um cilindro
# --------------------------------------

"""
raio = float(input('Qual o raio da base do cilindro? '))
altura = float(input('Qual a altura do cilindro? '))
pi = 3.242592
volume = pi * raio**2 * altura
print(f'O volume do cilindro e {volume}')
"""

# -------------------------------------
# Exercicio 37 - desconto numa compra
# ------------------------------------

"""
preco_produto = float(input('Quanto custa o produto? '))
desconto = (12/100)*preco_produto
print(f'O valor a ser pago com desconto sera {preco_produto - desconto}.')
"""

# --------------------------------------------
# Exercicio 38 - calculando aumentos na folha
# -------------------------------------------

"""
salario = float(input('Qual o valor do salario? '))
aumento = (25/100)*salario
print(f'O valor d salario apos o aumento sera {salario + aumento}.')
"""

# ------------------------------------
# Exercicio 39 - Dividindo um prêmio
# ------------------------------------

"""
premio = 780000.00
primeiro_lugar = (46/100)*premio
segundo_lugar = (32/100)*premio
terceiro_lugar = (premio - primeiro_lugar - segundo_lugar)

print(f'O prêmio total foi de {premio}')
print('O prêmio para cada ganhador será:')
print(f'Primeiro ganhador {primeiro_lugar}')
print(f'Segundo ganhador {segundo_lugar}')
print(f'Terceiro ganhador {terceiro_lugar}')
"""

# ------------------------------------------------
# Exercicio 40 - desconto do imposto de renda
# -----------------------------------------------

"""
numero_de_dias = int(input('Quantos dias foram trabalhados? '))
salario_base_por_dia = 30.00
total = numero_de_dias*salario_base_por_dia
imposto = (8/100)*total
print(f'O valor que deve ser pago é {total - imposto}')
"""

# ----------------------------------------------------------------------
# Exercicio 41 - salário com gratificação e desconto do imposto de renda
# ----------------------------------------------------------------------

"""
salario_base = float(input('Qual o valor pago por hora, em reais? '))
horas_trabalhadas = float(input('Quantas horas foram trabalhadas no mes? '))
gratificacao = (10/100)*(horas_trabalhadas*salario_base)
print(f'O valor total a ser pago ao funcionario é {horas_trabalhadas*salario_base + gratificacao}')
"""

# ----------------------------------------------------------------------
# Exercicio 42 - salário com gratificação e desconto do imposto de renda
# ----------------------------------------------------------------------

"""
salario_base = float(input('Qual o valor do salario base?'))
gratificacao = (5/100)*salario_base
imposto = (7/100)*salario_base
print(f'O salário a receber é {salario_base+gratificacao-imposto}')
"""

# ------------------------------------------------
# Exercicio 43
# -----------------------------------------------

"""
valor_produto = float(input('Qual o valor do produto? '))
desconto = (10/100)*valor_produto
numero_de_parcelas = int(input('Quantas parcelas? '))
valor_das_parcelas = (valor_produto - desconto)/numero_de_parcelas
comissao_venda_a_vista = (5/100)*(valor_produto - desconto)
comissao_venda_parcelada = (5/100)*valor_produto

print(f'À vista: total a pagar com desconto de 10% {valor_produto-desconto}')
print(f'O valor de cada uma das {numero_de_parcelas} sera {valor_das_parcelas}')
print(f'Comissão do vendedor da venda à vista: {comissao_venda_a_vista}')
print(f'Comissão do vendedor na venda parcelada: {comissao_venda_parcelada}')
"""

# --------------------------------------
# Exercicio 44 - construindo uma escada
# --------------------------------------
"""
altura_degrau = float(input('Qual a altura do degrau (cm)? '))
altura_nivel = float(input('Qual a altura do nível? '))
altura_nivel = altura_nivel*100

numero_de_degraus = int(altura_nivel/altura_degrau)
print(f'Serão necessário {numero_de_degraus} degraus de {altura_degrau} cm de altura para atingir o nível à '
      f'{altura_nivel/100} metros')
"""

# -----------------------------------------
# Exercicio 45 - retorna a letra minúscula
# -----------------------------------------

"""
letra_maiuscula = input('Digite uma letra maiuscula: ')
print(letra_maiuscula.lower())
"""

# ----------------------------------------------------
# Exercicio 46 - invertendo os algarismos de um número
# ----------------------------------------------------

"""
numero_inteiro = input('Digite um numero inteiro de três digitos:')
print(f'o número invertido é {numero_inteiro[::-1]}')
"""

# -----------------------------------------------------------------------
# Exercicio 47 - imprimindo digitos de um número inteiro com 4 algarismos
# -----------------------------------------------------------------------

"""
inteiro_quatro_digitos = input('Digite um número inteiro com quatro digitos:')
#print(dir(num))
print(f'{inteiro_quatro_digitos[0]}')
print(f'{inteiro_quatro_digitos[1]}')
print(f'{inteiro_quatro_digitos[2]}')
print(f'{inteiro_quatro_digitos[3]}')
"""

# ----------------------------------------
# Exercicio 49 - hora/ minutos / segundos
# ----------------------------------------

"""
inicio = input('Qual o horario inicial (hh:mm:ss)? ')
hora = int(inicio[0:2])
minutos = int(inicio[3:5])
segundos = int(inicio[6:8])

print(f'{hora} h')
print(f'{minutos} min')
print(f'{segundos} s')

inicio_em_segundos = int(hora * 3600 + minutos * 60 + segundos)
print(f'A tempo inicial total em segundos é de {inicio_em_segundos} s ')
"""
# --------------------------------------------
# Exercicio 50 - calculando data de nascimento
# --------------------------------------------

"""
nome = input('Qual seu nome? ')
print(f'Seja bem-vindo(a) {nome}!')
idade = input('Qual a sua idade? ')
ano_atual = input('qual é o ano atual? ')
print(f'{nome} nasceu em {int(ano_atual) - int(idade)} e tem {idade} anos de idade.')
print("%s tem %s de idade" % (nome, idade))
"""

# ------------------------------------------------
# Exercício 51 - distância euclidiana
# -----------------------------------------------

"""
coordenada_x = float(input('Qual a coordenada x? '))
coordenada_y = float(input('Qual a coordenada y? '))
distancia = (coordenada_x**2 + coordenada_y**2)**(1/2)
print(f'A distância do ponto ({coordenada_x}, {coordenada_y}) da origem em (0,0) é %f' % distancia)
"""

# --------------------------------------------------------------------
# Exercício 52 - dividindo um prêmio em partes proporcionais a aposta
# --------------------------------------------------------------------

aposta_jogador_1 = float(input('Aposta do primeiro jogador:'))
aposta_jogador_2 = float(input('Aposta do segundo jogador:'))
aposta_jogador_3 = float(input('Aposta do terceiro jogador:'))

premio_total = float(input('Qual o valor do premio?'))

total_de_apostas = aposta_jogador_1 + aposta_jogador_2 + aposta_jogador_3

porcentagem_aposta_1 = (aposta_jogador_1*100)/total_de_apostas
porcentagem_aposta_2 = (aposta_jogador_2*100)/total_de_apostas
porcentagem_aposta_3 = (aposta_jogador_3*100)/total_de_apostas

print(f'O premio do primeiro colocado: {0.01*porcentagem_aposta_1*premio_total}')
print(f'O premio do segundo colocado:  {0.01*porcentagem_aposta_2*premio_total}')
print(f'O premio do terceiro colocado: {0.01*porcentagem_aposta_3*premio_total}')
