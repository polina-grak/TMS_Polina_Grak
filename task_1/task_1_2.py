# Даны действительные числа x и y. Получить (|x| − |y|)/(1+ |xy|) / (|x| − |y|)

flag1 = False
while flag1 == False:
    try:
        x = int(input('Enter the x: '))
        flag1 = True
    except:
        print('Invalid number.')
mx= abs(x)

flag2 = False
while flag2 == False:
    try:
        y = input('Enter the y: ')
        y = int(y)
        flag2 = True
    except:
        print('Invalid number.')

my= abs(y)

print ((mx-my)/(1+(my*mx)))

