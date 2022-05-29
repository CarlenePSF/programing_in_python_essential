"""
Por que testar nosso código?

Testes automatizados --


Aplicação web
-------------------------------------
/                                   /
/       frontend e backend          /
-------------------------------------
/      Testes automatizados
/ Verificar cada etapa da aplicação /
/ para ver se está funcionando ok   /
=====================================

Por que testar nosso código??
  - Para reduzir bugs (problemas) no código;
  - Garantem que novos recursos da aplicação não quebrem (alterem) recursos antigos;
  - Garantem que bugs (problemas) que foram corrigidos anteriormente continuam corrigidos;
  - Garantem que a refatoração contínua para melhorias não tragam novos bugs (problemas)

TDD Test Driven Development (Desenvolvimento guiado por testes)
  - Primeiro escreve o teste depois escrevemos o código
  -Utiliza estágios de desenvolvimento:
    -> Escreve o teste;
    -> Escreve o código mínimo para fazer o teste passar (executar com sucesso);
    -> Refatora o código para incluir as funcionalidades;
    -> Uma vez que o teste execute com sucesso, o recurso é considerado completo;

Os estágios de desenvolvimento com TDD são quase como um mantra seguido pelos desenvolvedores
  - Red;
  - Green;
  - Refactor;

# Exemplo de classe
"""


class Gato:

    def __init__(self, nome):
        self.__nome = nome

    # getters
    @property
    def nome(self):
        return self.__nome

    def miar(self):
        print(f'{self.__nome} está miando...')


# Declarando instancia (objeto) do tipo Usuario
nome1 = 'mimi'
gato = Gato(nome1)
print(gato.nome)
gato.miar()

