#Дана длина ребра куба. Найти объем куба и площадь его боковой поверхности.

flag1 = False
while flag1 == False:
    try:
        x = int(input('Enter the rib length: '))
        flag1 = True
    except:
        print('Invalid number.')
mx= abs(x)


print ('cube area:')
print (mx**3)

print ('surface area:')
print(4*mx**2)