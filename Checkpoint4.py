#Exercise 1
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_float = 9.84
my_integer = 37
from decimal import Decimal
my_decimal = Decimal(53.27)
my_dictionary = {
    'día': 'lunes',
    'mes': 'enero',
    'año': 2025,
}

#Exercise 2
import math
print(math.ceil(my_float))

#Exercise 3
import math

print(math.sqrt(my_float))

#Exercise 4
print(my_dictionary['día'])

#Exercise 5
print(my_tuple[1])

#Exercise 6
my_list.extend([7])

#Exercise 7
my_list[0] = 8

#Exercise 8
my_list.sort()

#Exercise 9
my_tuple += (6,)
