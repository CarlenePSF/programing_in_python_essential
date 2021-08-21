""":return
Dunder Name e Dunder Main

dunder -> double underscore

Dunder Name -> __name__

Dunder Main -> __main__

Em Python, são utilizados double underscore (__nome__) para cria funções, atributos, propriedades etc ...
para que  não gerem conflito com os possíveis nomes de outras variáveis ou funções criadas na programação.


# Na linguagem C, temos a função main, que marca o inicio do programa principal.
A sintaxe é a seguinte:

int main(){
   ... bloco de código
}

Sem a função main o programa não executa tarefa alguma

# Em Java, o equivalente ao main do C é escrito da seguinte forma:

public static void main(String[] args){
 ... bloco de código
}


# Em Python não existe esse tipo de estrutura. Se executarmos um módulo diretamente na linha de
comando do terminal, por exemplo, internamente o Python atribuirá à variável __name__ o valor __main__
indicando que este módulo é o módulo de execução principal


Main -> principal


# Exemplo de uso do __main__

# Ao realizarmos o import abaixo, além de executar a tarefa requerida, e por existir um  print dentro do módulo,
# mesmo que não utilizemos nada de dentro do módulo o print será executado.
# Isso não é um comportamento esperado


from geek.university.geek3 import funcao3
print(funcao3())

# Como corrigir? adicionando a seguinte linha de código dentro do módulo que contém a função chamada.
# if __name__ == '__main__':
#     print('Isso não deveria ser impresso!!!')

# Quando adicionamos a linha acima tudo que estiver no arquivo do código dentro do módulo que contém a função
# utilizada só será impresso se o próprio arquivo fonte for executado. Isso é muito útil quando queremos fazer teste
# dos métodos ou das funções do  nossos módulos.

"""

from primeiro import funcao_um
from segundo import funcao_dois
import numpy as np
funcao_um()
funcao_dois()
