"""
Manipulando data e hora

O Python tem um módulo built-in (integrado) para se trabalhar com data e hora chamado de datetime


# Exemplo 1 - Conhecendo o módulo datetime

import datetime

# print(dir(datetime))
# ['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__',
# '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time',
# 'timedelta', 'timezone', 'tzinfo']

print(datetime.MAXYEAR)  # imprime 9999 (maior ano)
print(datetime.MINYEAR)  # imprime 1 (ano mínimo)

# Imprimindo a data e hora atual

print(datetime.datetime.now())  # formato %Y-%m-%d %h%min%seg%millisecond

# qual a representação do método now
print(repr(datetime.datetime.now()))  # datetime.datetime(year, month, day, hour, minute, second, millisecond)

# replace() para fazer ajustes na data/hora
inicio = datetime.datetime.now()

print(inicio)

# alterando o horário para 10hs:0min:0s:0miles
inicio = inicio.replace(year=2022, hour=10, minute=0, second=0, microsecond=0)
print(inicio)

# # Criando uma data - formato datetime vs. string

evento = datetime.datetime(2019, 1, 1, 0)
print(type(evento))  # <class 'datetime.datetime'>
print(evento)

data = '31/12/2020'
print(type(data))  # <class 'str'>
print(data)

# Quando é útil transformar a data?
# Quando existir input do usuário ou quando for necessário.
nascimento = input('Informe sua data de nascimento no formato (dd/mm/aaaa): ')
# print(nascimento)
# print(type(nascimento))

nascimento = nascimento.split('/')
nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))
print(nascimento)
print(type(nascimento))

# Acessando informações

evento = datetime.datetime.now()

# acesso individual dos elementos data-hora
print('O ano:', evento.year)  # ano
print('O mês:', evento.month)  # mês
print('O dia:', evento.day)  # dia

"""

# Convertendo uma coluna do dataframe em objeto datetime

# import datetime
import pandas as pd

df = pd.DataFrame(dict(datas=['06/04/2021', '07/04/2021'], compra=[3, 6]))
print(df)
print(df.dtypes)


df['datas'] = pd.to_datetime(df['datas'], format="%d/%m/%Y")
print(df.datas[0].year)
print(df.datas[0].month)
print(df.datas[0].day)


def converte_datetime(dataframe, coluna_tempo, formato):
    """
    Retorna um Dataframe com as datas de no formato object (string) convertidas para datetime do python
    :parametros:
    ------------------
        dataframe: pandas dataframe
            o dataframe onde vamos converter as datas.
        coluna_tempo: str
            o nome da coluna que contém os data temporais.
        formato: str
            o formato em que está a data.
    :retorna:
        novo_df: pandas dataframe
            um novo dataframe com a coluna de tempo transformada para o formato datetime do python.
    ------------------
    """
    novo_df = dataframe.copy()
    novo_df[coluna_tempo] = pd.to_datetime(novo_df[coluna_tempo], format=formato)
    return novo_df
