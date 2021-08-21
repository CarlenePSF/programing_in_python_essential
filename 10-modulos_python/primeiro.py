""" Arquivo primeiro.py """


def funcao_um():
    print('Geek University - primeiro.py')


if __name__ == '__main__':
    funcao_um()
    print(f'{__name__}.py está sendo executado diretamente.')
else:
    print(f'{__name__}.py foi importado. ')
