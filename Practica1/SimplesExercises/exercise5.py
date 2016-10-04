"""
Created at 4/10/16
__author__ = 'Sergio Padilla'

Exercise: Generate random vector of '[' and ']' and check if the vector is balanced

"""
from random import randint


def random_string(n):
    v = ''
    n = randint(2, n)
    n = n if n % 2 == 0 else n+1
    for i in range(0, n):
        v += ']' if randint(0, 2) == 0 else '['
    return v


def isbalanced(vector):
    open, close = 0, 0
    ok = True
    for elem in vector:
        if elem == '[':
            open += 1
        else:
            close += 1
        if close > open:
            ok = False
            break

    return ok if open == close else False


n = int(input('Indica el número de cadenas aleatorias que quieres que se generen: '))
m = int(input('Indica la longitud máxima de esas cadenas: '))
for i in range(0, n):
    v = random_string(m)
    print(v)
    print(isbalanced(v))
