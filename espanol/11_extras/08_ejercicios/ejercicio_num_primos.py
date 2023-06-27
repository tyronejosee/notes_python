# def primos():
#     for index in range(1, 100):
#         if index / index == index:
#             print("Numero Primo", index)
#         elif index / 1 == index:
#             print("Numero Primo", index)
        
# primos()


def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            print("No es primo", n, "es divisor")
            return False
    print("Es primo")
    return True

es_primo(5)
