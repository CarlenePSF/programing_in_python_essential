"""
Trabalhando com deltas de data e hora

data_inicial = dd/mm/aaaa  00:00:00
data_final = dd/mm/aaaa    12:34:23.09876


delta = data_final - data_inicial    <- esse será o delta

# Exemplo 1 -


import datetime

data_hoje = datetime.datetime.now()
aniversario = datetime.datetime(2022, 3, 17, 0)
tempo_para_evento = aniversario - data_hoje

print(type(tempo_para_evento))  # <class 'datetime.timedelta'>
print(repr(tempo_para_evento))
print(tempo_para_evento)


"""
# Exemplo e-commerce

import datetime


data_da_compra = datetime.datetime.now()  # data que um usuário fez a compra
print(data_da_compra)

regra_boleto = datetime.timedelta(days=3)  # gera um boleto cujo o vencimento é 3 dias depois que o cliente fez a compra
print(regra_boleto)

vencimento_boleto = data_da_compra + regra_boleto  # imprime a data de vencimento para o cliente
print(vencimento_boleto)
