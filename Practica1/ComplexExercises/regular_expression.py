"""
Created at 4/10/16
__author__ = 'Sergio Padilla'

Exercise: Create regular expression for:
            1) Detect a world with a uppercase letter after blank space (Antonio N)
            2) Check email address
            3) check credit card's numbers

"""
import re


def search_world_with_uppercase(text):
    return re.findall(r'[a-zA-Z_]+\s[A-Z_]', text)


def check_email(email):
    return re.match(r'([\w.-]+)@([\w.-]+)\.\w+', email)


def credit_card_number(text):
    return re.findall(r'\d{4}[\s|-]+\d{4}[\s|-]+\d{4}[\s|-]+\d{4}', text)


inp = input('Introduce una cadena: ')
match = search_world_with_uppercase(inp)
print('Palabras con un espacio y una letra mayúscula después: ')
print(match)

inp = input('introduce un email a validar: ')
valid = check_email(inp)
if valid:
    print('email válido')
else:
    print('error email')

inp = input('Introduce una cadena para buscar número de tarjetas de crédito: ')
match = credit_card_number(inp)
print(match)
