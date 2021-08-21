""" Arquivo segundo.py """

# imports
import primeiro


def funcao_dois():
    primeiro.funcao_um()


if __name__ == '__main__':
    funcao_dois()
    print(f'{__name__}.py está sendo executado diretamente.')
else:
    print(f'{__name__}.py foi importado.')
