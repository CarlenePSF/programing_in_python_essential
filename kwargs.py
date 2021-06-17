"""
 Uso do **kwargs

Poderíamos chamar este parâmetro de **x ou ** qualquer_coisa. Mas por convenção usamos **kwargs.
O **kwargs é só mais um parâmetro, porém, diferente do *args que coloca os valores extras em uma tupla,
o **kwargs exige que seja utilizado parâmetros nomeados, e transforma-os em um dicionário.

"""


# Exemplo


def cores(**kwargs):
    print(kwargs)


cores(Maria='verde', Luiz='laranja', Julia='amarelo', Eduardo='azul')
