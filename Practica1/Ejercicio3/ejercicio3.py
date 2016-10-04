"""
Created at 4/10/16
__author__ = 'Sergio Padilla'

Exercise: Criba de erastótenes

"""
from math import sqrt


def criba_de_erastotenes(n):
    v = list(range(2, n+1))

    i = 2
    while i < int(sqrt(n)):
        j = i
        while j <= int(n/i):
            if i*j in v:
                v.remove(i*j)
            j += 1
        i += 1
    return v


n = int(input("Indica un número natural: "))
print('Los números primos menores que ', n, ' son: ')
print(criba_de_erastotenes(n))
