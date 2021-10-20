'''Incorrect:
t = input('Enter:')
r = t.split(' ')
r = int(r)
correct:'''

'''r = [34, 45, 3, 6]
index= 0
sum = 0

while index < len(r):
    if r[index] > 10:
        sum += r[index]
    index += 1

print (sum)'''

'''Просуммировать неопределенное количество чисел, 
вводимых пользователем, суммировать до тех пор, пока 
пользователь не введёт слово «стоп»


sum = 0
while True:
    r= input ('Enter:')
    if r == 'stop':
        break 
    
    sum += int(r)

print ( sum )'''


'''Просуммировать неопределенное количество чисел, 
вводимых пользователем, суммировать до тех пор, пока 
пользователь не введёт слово «стоп». Не учитывать 
числа кратные 
sum = 0
while True:
    r = input('Enter:')
    if r == 'stop':
        break
    elif int(r) % 5 == 0:
        continue
    sum += int(r)

print(sum)'''


'''4.05 Написать программу, которая будет выводить 
на экран случайные числа от 1 до 10 до тех 
пор, пока не выпадет 7'''

'''
import random

while True:
    tm=random.randint(0,10)
    print (tm)
    if tm == 7:
        break 
'''

'''Получить сумму кубов натуральных чисел от n
до m используя цикл for
'''

'''
m = int(input('enter:'))
n = int(input('enter:'))
sum = 0
for i in range (n,m,1):
    sum += i**3
print (sum)'''


'''Ввести два целых числа A и B ( A < B ). Вывести в порядке 
возрастания все целые числа, расположенные между A и 
B (включая сами числа A и B ), а также количество N этих 
чисел. [01-08-For2]'''

'''
a = int(input('enter:'))
b = int(input('enter:'))
if a<b:
    c= list(range(a,b +1,1))
print (c )
print (len(c)) '''


#Вложенные циклы:
#TEST

ls = [[1,3,5],[4,5,'5'],[2,7,8]]
for i in ls:
    for j in i:
        if type(j) == int:
            print (j)
        else:
            print ('not a number')
