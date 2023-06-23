### Functions ###

def Sum_two_values (value_1, value_2):
    result_sum: int = value_1 + value_2
    return result_sum


result: int = Sum_two_values (2, 4)
print(result)

### Ejemplo 2 ###

def Calcule_calories (Carbohidratos: int, Grasas: int, Proteinas: int):
    calorias = Carbohidratos + Grasas + Proteinas
    return calorias

VAR_CAL = Calcule_calories (200, 50, 80)
print(VAR_CAL)
