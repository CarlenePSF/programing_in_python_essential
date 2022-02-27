"""
Lendo arquivos csv

csv — comma separated values — valores separados por víglas

Exemplos
1, 2, 3, 4, 5, ...
"Geek", "University", "python", "ciência", "dados"

# Separados por espaço

1 2 3 4 5 6 7...

"Geek" "university" "python" "ciência" "dados"

# bases de dados disponibilizadas pelo governo federal
https://dados.gov.br/dataset


# trabalahndo com csv usando somente as estruturas da linguagem
# não muito prático!

with open('lutadores.csv') as arquivo:
    dados = arquivo.read()
    # print(type(dados))
    dados = dados.split(',')[2:]
    print(dados)

O Python possui duas formas diferentes para ler dados em arquivos csv:
    — reader → permite que iteremos sobre as linhas do arquivo CSV como uma lista
    — DictReader → permite que iteremos sobre as linhas do arquivo CSV como OrderedDicts


# Exemplo — usando o reader

from csv import reader

with open('lutadores.csv') as arquivo:
    leitor_csv = reader(arquivo)
    #print(type(leitor_csv))
    next(leitor_csv)  # para não imprimir o nome das colunas
    for linha in leitor_csv:
    #for linha in list(leitor_csv)[1:]:
        # cada linha do arquivo é uma lista
        print(f'{linha[0]} nasceu em {linha[1]} e mede {linha[2]} centímetros')
"""

# Exemplo - usando o DictReader

from csv import DictReader

with open('lutadores.csv') as arquivo:
    leitor_csv = DictReader(arquivo, delimiter=',')  # o parâmetro delimtador pode ser especificado
    for linha in leitor_csv:
        # Cada linha é um OrderedDict acessamos os valores pelas chaves que são os cabeçalhos
        print(f"{linha['Nome']} nasceu em {linha['País']} e mede {linha['Altura (em cm)']} centímetros")


