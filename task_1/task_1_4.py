#Даны два действительных числа. Найти среднее арифметическое и среднее геометрическое этих чисел


flag1 = False
while flag1 == False:
    try:
        first_integer = int(input('Enter the first integer: '))
        flag1 = True
    except:
        print('Invalid number.')

flag2 = False
while flag2 == False:
    try:
        second_integer = input('Enter the second integer: ')
        second_integer = int(second_integer)
        flag2 = True
    except:
        print('Invalid number.')

x = 2/(second_integer + first_integer)

import math

y= math.sqrt(second_integer * first_integer)

print('arithmetical mean:'+ str(x))
print('geometric mean:' + str(y))