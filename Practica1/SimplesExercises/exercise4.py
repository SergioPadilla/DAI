"""
Created at 4/10/16
__author__ = 'Sergio Padilla'

Exercise: Read a integer of a text file and write in another text file the n-term of its fibonacci sequence

"""


def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


filepath = input('Introduce la ruta base hasta el directorio donde se encuentra el archivo: ')
if filepath[len(filepath)-1] != '/':
    filepath += '/'
readfilename = input('Introduce el nombre del archivo de lectura: ')
writefilename = input('Introduce el nombre del archivo de salida: ')
readfilepath = filepath+readfilename
writefilepath = filepath+writefilename

read_file = open(readfilepath, mode='r')
n = int(read_file.readline().replace('\n', ''))

write_file = open(writefilepath, mode='w')
write_file.write(str(fibonacci(n)))
