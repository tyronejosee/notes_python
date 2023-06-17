### Exceptions ###

NUM1 = 2
NUM2 = "2"

try:
    print(NUM1 + NUM2)
except Exception as error: # Se ejecuta al haber un error en try
    print(f"La Suma tiene un error {error}.")
else:
    print("Prueba de else")
finally:
    print("Prueba de finally")