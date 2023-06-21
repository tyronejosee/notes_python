"""
num2words is a Python function that converts a number into its textual representation.
It takes an integer number as input and returns a string that represents the number in words.
"""
# Instala modulo num3words e importalo.
from num2words import num2words

numero = 23454354
palabras = num2words(numero, lang="es")

print(f"{palabras}")
