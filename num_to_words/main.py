# Instala modulo num3words e importalo.
from num2words import num2words

numero = 23454354
palabras = num2words(numero, lang="es")

print(f"{palabras}")
