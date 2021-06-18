"""
Loop while
Serve tambem para iterar sobre sequencias

Foma geral

while express_booleana:
    //execusao do loop


OBS: Em um loop while e importante tomar cuidado com o criterio de parada


O loop sera repetido enquanto a expressao booleana for verdadeira .
Uma expressao booleana e uma expressao onde todo o resultado e verdadeiro ou falso.
Eemplo:
num = 5
num <5 -> Falso
num == 5 True


# Em C ou Java:
while (expresso){
     //instrucoes do loop
}

do {
  // bloco de instrucoes
}while(expressao);
"""


#----------------------------
# Exemplo: Forma 1
#----------------------------
num = 1
while num < 10:
    print(num)
    num = num + 1   # toma conta do incremento para o loop nao ser infinito


#----------------------------
# Exemplo: Forma 2
#----------------------------
resposta = ''

while resposta != 'sim':
    resposta = input('Ja acabou??')
