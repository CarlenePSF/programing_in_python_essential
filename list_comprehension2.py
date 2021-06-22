"""
Aula 2 de list comprehension

Nos podemos adicionar estruturas condicionais logicas as list comprehension

# Exemplo

numeros = [1, 2, 3, 4, 5, 6]

pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

impares = [numero for numero in numeros if numero % 2 != 0]
print(impares)

# Refatorando
# Qualquer numero par modulo de 2 e zero e zero em python e false.
# not false = true
pares2 = [numero for numero in numeros if not numero % 2]

# Qualquer numero impar modulo 2 e 1, 1 em python e true
impares2 = [numero for numero in numeros if numero % 2]

print(pares2, impares2)


# Exemplo 2

res = [numero * 2 if numero % 2 == 0 else numero/2 for numero in numeros]

print(res)
"""

lista = [item**2 for item in range(10)]

nomes = ['julia', 'python', 'java']
resultado = [str(item[0]).upper() + str(item[1:]) for item in nomes]
print(lista)
print(resultado)


