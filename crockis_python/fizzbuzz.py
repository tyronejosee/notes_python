### Reto FizzBuzz ###
def fizzbuzz():
    for index in range(1, 101):
        if index % 3 == 0 and index % 5 ==0:
            print("FizzBuzz")
        elif index % 3 == 0:
            print("Fizz")
        elif index % 5 == 0:
            print("Buzz")
        else:
            print(index)

fizzbuzz()
