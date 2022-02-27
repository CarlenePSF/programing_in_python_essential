"""
Tipo string - vetores de characters
Em python, um dado e considerado do tipo string sempre que:

- Estiver entre aspas simples ->  'uma string' / '1234' / 'true'/
- Sempre que estiver entre aspas duplas -> "uma string"/ "1234" / "true"
- Estiver entre aspas simples triplas -> '''uma string'''/ '''1234''' / '''true'''
"""
# - Estiver entre aspas duas triplas -> """uma string"""/ """1234""" / """true"""

"""
nome = 'John Doe'
nome1 = "John's computer"
print(nome1)
print(type(nome1))
print(dir(nome1))
"""

nome = 'Geek University'
# ['G','e','e','k',' ','U','n','i','v','e','r','s','i','t','y']
# ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14']
'''
print(dir(nome))
print(nome.upper())
print(nome.lower())
print(nome.split())  # transforma em uma lista de strings
print(nome[0:4])    # slice de string
print(nome[5:15])    # slice de string

print(nome.split()[0])
print(nome.split()[1])

'''
# [::-1] -> comece do primeiro elemento e va ate o ultimo elemento invertendo a ordem
print(nome[::-1])
print(nome.replace('G', 'P'))
print(type(nome))
