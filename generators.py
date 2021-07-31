"""
Generators
Em aulas anteriores estudamos:
 - list comprehension
 - dictionary comprehension
 - set comprehension

Não vimos:
- tuple comprehension... porque elas se chamam Generators


# Exemplo - Usando generators
nomes = ('Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa')
print(any(nome[0] == 'C' for nome in nomes))

# list comprehension
res = [nome[0] == 'C' for nome in nomes]
print(type(res))
print(res)

# Generator mais eficiente em termos de memória
res = (nome[0] == 'C' for nome in nomes)
print(type(res))
print(res)
print(any(res))


# Qual é a utilidade de getsizeof? Retorna a quantidade de bytes em
# memória do elemento passado em parâmetros.

from sys import getsizeof
# Mostra quantos bytes a string 'Geek' está ocupando em memória
print(getsizeof('Geek'))
print(getsizeof('University'))
print(getsizeof(9))
print(getsizeof(91))
print(getsizeof(4595484546848488789456151658469851465168746875213654698465165494561))
print(getsizeof(True))

# Comparando a capacidade de memória que é usada

from sys import getsizeof

# Gerando uma lista de números com uma list comprehension
list_comp = getsizeof([x*10 for x in range(1000)])

# Gerando uma set de números com uma set comprehension
set_comp = getsizeof({x*10 for x in range(1000)})

# Gerando uma dict de números com uma dict comprehension
dict_comp = getsizeof({x: x*10 for x in range(1000)})

# Gerando uma lista de números com generator
# Gera somente o objeto sem retornar o valor
gen = getsizeof(x*10 for x in range(1000))

print(f'Para executar a mesma tarefa, utilizamos em termos de meória:\n'
      f'list comprehension: {list_comp} bytes,\n'
      f'set comprehension: {set_comp} bytes,\n'
      f'dict comprehension: {dict_comp} bytes,\n'
      f'Generator: {gen} bytes!!')

"""
# Visualizando os numeros gerados pelo generator
gen = (x*10 for x in range(5))
print(gen)

for num in gen:
    print(num)
