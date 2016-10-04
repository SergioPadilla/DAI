# -*- coding: utf-8 -*-
"""
Created at 30/09/16
__author__ = 'Sergio Padilla'

Exercise: Implements 2 sort algorithms and calculate the time to sort a random vector

"""
from random import randint


def insertion_sort(vector):
    sort = []
    n = len(vector)
    if n == 0:
        return

    for i in vector:
        m = len(sort)
        insert = False
        j = 0

        while j < m and not insert:
            if sort[j] > i:
                sort.insert(j, i)
                insert = True
            j += 1

        if not insert:
            sort.append(i)

    return sort


randon_vector = []
n = int(input('Tamaño del vector: '))
for i in range(0,n):
    randon_vector.append(randint(0, 99))

print('vector desordenado:', end=' ')
print(randon_vector)
print('vector ordenador:', end=' ')
print(insertion_sort(randon_vector))
