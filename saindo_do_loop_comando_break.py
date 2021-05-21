"""
Saindo de loop com o break
- Funciona da mesma forma que nas linguagens C e Java
- Utilizamos o break para sair de loops de maneira projetada.
"""

#----------------------------
# Exemplo 1
#----------------------------

for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero)
print('Loop interrompido')


#----------------------------
# Exemplo 1
#----------------------------

while True:
    comando = input('Digite (sair) para sair: ')
    if comando == 'sair':
        break