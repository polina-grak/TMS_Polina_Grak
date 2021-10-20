#Даны катеты прямоугольного треугольника. Найти его гипотенузу и площадь

import math

flag1 = False
while flag1 == False:
    try:
        x = int(input('Enter the first cathetus lenght : '))
        flag1 = True
    except:
        print('Invalid number.')

flag2 = False
while flag2 == False:
    try:
        y = input('Enter the second cathetus lenght: ')
        y = int(y)
        flag2 = True
    except:
        print('Invalid number.')

g=math.sqrt(x**2 + y**2)
s= 0.5 * (x*y)

print ('hypotenuse:' + str (g) )
print ('area:'+ str(s))
