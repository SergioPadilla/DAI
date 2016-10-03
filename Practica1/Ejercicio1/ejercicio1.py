# -*- coding: utf-8 -*-
"""
Created at 30/09/16
__author__ = 'Sergio Padilla'

"""
from random import randint

mesagges = {
    '0': u'El número buscado es mayor',
    '1': u'El número buscado es menor',
    '2': u'Número máximo de intentos alcanzado, no has conseguido adivinar el número',
    '3': u'Enhorabuena! Has acertado el número'
}

number = randint(1, 100)

print('Se ha generado un número aleatorio, ¿serás capaz de adivinarlo?')

for i in range(0, 10):
    n = int(input('Indica un número: '))

    if n == number:
        print(mesagges['3'])
        break
    elif n < number:
        print(mesagges['0'] if i < 9 else mesagges['2'])
    else:
        print(mesagges['1'] if i < 9 else mesagges['2'])
