### Convirtiendo tuplas a listas ###

MY_TUPLE = tuple()

MY_TUPLE = 1, 2, 3, 4, 5, 6, 7, 8, 9

print(MY_TUPLE)
print(type(MY_TUPLE))

# my_tuple[3] = 23 # TypeError: 'tuple' object does not support item assignment
print(MY_TUPLE)

my_list_new = list(MY_TUPLE)
print(type(my_list_new))
