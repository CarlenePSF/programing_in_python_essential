"""
Criando nossa própria versão de loop - Entendo em detalhes como funcionam o loop


# loops comuns
for num in [1, 2, 3, 4, 5]:
    print(num)
    
for letra in 'Geek University':
    print(letra)

# lembrando que listas e string são iteráveis os loop acima aplicam uma forma de iter() em cada tipo de iterável
iter([1, 2, 3, 4, 5])
iter('Geek University')

"""


def meu_for(iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break


meu_for([1, 2, 3, 4, 5])
