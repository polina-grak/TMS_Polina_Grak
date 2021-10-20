#Ex.3.02
#x = int(input('Enter the first integer: '))
#y = int(input('Enter the secobd integer: '))
#z = f'{x} plus {y} is equal {x+y}'
#print (z)


'''Ex. 3.03
x = input('Enter: ')
y= x.split(' ')
y.reverse() #меняем местами
#y.append('!')
#y.insert(0, '!')
result = ' '.join(y)
print ('!' + result + '!')'''

''' Ex.3.04
x = input('Enter: ')
if len(x) % 3 == 0:
    print(x + '!')
else:
    print ('(((')'''

'''Ex. 3.05 
Ввести предложение. Если в предложении есть слово 
code - вывести на экран Yes, иначе вывести на экран No

x= input('Enter: ')
if 'code' in x:
    print ('Yes')
else:
    print(('No'))'''

'''Ex.3.06 
Запросить у пользователя возраст. Если возраст меньше 
0 - вывести Wrong input, если меньше 18 - вывести 
CocaCola, иначе - вывести Beer 

x = int(input ('Age: '))
if x < 0:
    print ('Wrong input')
elif x <18:
    print ('CocaCola')
else:
    print ('Beer')'''


x, y = input().split(' ')
x=int(x)
y = int(y)
if x == 1:
    print (str(x) +'рубль')
elif x <= 0:
    print (None)
elif x> 1 and x < 5:
    print (str(x) + 'рубля')
else:
    print (str(x) + 'рублей')

if y == 1:
    print(str(y) + 'копейка')
elif y <= 0:
    print(None)
elif y > 1 and y < 5:
    print(str(y) + 'копейки')
else:
    print(str(y) + 'копеек')









