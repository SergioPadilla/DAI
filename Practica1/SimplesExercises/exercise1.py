# -*- coding: utf-8 -*-
"""
Created at 30/09/16
__author__ = 'Sergio Padilla'

Exercise: Little game that generate random number and the user must be to guess it in less than 10 attempts

"""

from random import randint

messages = {
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
        print(messages['3'])
        break
    elif n < number:
        print(messages['0'] if i < 9 else messages['2'])
    else:
        print(messages['1'] if i < 9 else messages['2'])
