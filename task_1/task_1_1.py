# Даны 2 действительных числа a и b. Получить их сумму, разность и произведение.
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

sum = first_integer+second_integer
sum = str(sum)

dif = first_integer-second_integer
dif = str(dif)

mult = first_integer*second_integer
mult = str(mult)

div = first_integer/second_integer
div = str(div)

print('The sum is:'+ ' ' + sum)
print('The difference is:'+ ' ' + dif)
print('The multiplication is:'+ ' ' + mult)
print('The division is:'+ ' ' + div)

