"""
Escrevendo em arquivos CSV

reader() — leitor
writer() — escritor
writerow() — escrever numa linha

from csv import writer

# Usando o writer

with open('filmes.cvs', 'w') as arquivo:
    escritor_csv = writer(arquivo)
    filme = None
    escritor_csv.writerow(['titulo', 'genero', 'duracao'])  # recebe uma lista com o título das colunas
    while filme != 'sair':
        filme = input('Nome do filme: ')
        if filme != 'sair':
            genero = input('Gênero: ')
            duracao = input('Duração: ')
            escritor_csv.writerow([filme, genero, duracao])
"""

from csv import DictWriter

# Usando o Dictwriter

with open('filmes.cvs', 'w') as arquivo:
    cabecalho = ['titulo', 'genero', 'duracao']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme = None
    while filme != 'sair':
        filme = input('Nome do filme: ')
        if filme != 'sair':
            genero = input('Gênero: ')
            duracao = input('Duração: ')
            escritor_csv.writerow(
                {
                    'titulo': filme,
                    'genero': genero,
                    'duracao': duracao
                }
            )



