# -*- coding: utf-8 -*-
"""
Created at 30/09/16
__author__ = 'Sergio Padilla'

Exercise: Implements 2 sort algorithms and calculate the time to sort a random vector

"""
from random import randint
import time


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


def quicksort(vector):
    n = len(vector)
    if n == 0 or n == 1:
        return vector
    elif n == 2:
        if vector[0] > vector[1]:
            vector[0], vector[1] = vector[1], vector[0]
        return vector
    else:
        pivot = vector[0]
        i, j = 0, n-1

        while i < j:
            while vector[i] <= pivot and i < j:
                i += 1
            while vector[j] >= pivot and i < j:
                j -= 1

            if i < j:
                vector[i], vector[j] = vector[j], vector[i]

        if i == n - 1 and vector[n - 1] < pivot:
            one, two = vector[1:n], []
        else:
            one, two = vector[1:i], vector[i:n]

        return quicksort(one)+[pivot]+quicksort(two)


def randvector(n):
    x = []
    for i in range(0, n):
        x.append(randint(0, 99))
    return x

random_vector = randvector(int(input('Tamaño del vector: ')))
start_insertion = time.time()
insertion_sort(random_vector)
end_insertion = time.time()
print('Tiempo de ordenación insercción: ', end='')
insertion_time = end_insertion-start_insertion
print(insertion_time)

start_quicksort = time.time()
quicksort(random_vector)
end_quicksort = time.time()
print('Tiempo de ordenación quicksort: ', end='')
quicksort_time = end_quicksort-start_quicksort
print(quicksort_time)

print('La diferencia entre insercción y quicksort es ', end='')
print(insertion_time-quicksort_time)
