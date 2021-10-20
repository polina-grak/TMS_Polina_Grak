'''Введите число. Если это число делиться на 1000 без остатка, то выведите на
экран "millennium"
'''

t= False
while t == False:
    r= int(input('Enter the integer:'))
    if r % 1000 == 0:
        print ('millennium')
        t= True
    else:
        print ('Try again')
