'''Ввести строку. Вывести на экран букву, которая находится в середине этой
строки.
Также, если эта центральная буква равна первой букве в строке, то создать и
вывести часть строки между первым и последним символами исходной строки.
(подсказка: для получения центральной буквы, найдите длину строки и разделите
ее пополам. Для создания результирующий строки используйте срез'''


t = str(input('enter the word:'))
e = t[round((len(t)-1)/ 2 )]
print (e)
if t[0] == e:
    print (t[slice(1,(len(t)-1),1)])


