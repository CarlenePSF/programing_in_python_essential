"""
Estruturas condicionais
if, else, elif

Estrutura condicional if/else em C:

if( idade <18){
    printf('Menor de idade');
}else if (idade  == 18){
    printf('18 anos de idade');
}
else{
     printf('Maior de idade');
}

Estrutura condicional if/else em Java:

if( idade <18){
    System.out.println('Menor de idade');
}else{
     System.out.println('Maior de idade');
}


"""

idade = int(input('digite a idade: '))

if idade < 18:
    print('Menor de idade!')
    print(idade)
elif idade == 18:
    print('Tem 18 anos de idade')
else:
    print('Maior de idade!')
    print(idade)

"""
print('  *')
print(' ***')
print('******')
print(' /|\\')
print(' Feliz Natal')
"""