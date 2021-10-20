first_name= 'Ivan'
second_name= 'Ivanov'
age= '34'

result = ' Hi, my name is ' + first_name + ' '+ second_name + ', my age is ' + age

result = f'Hi, my name is {first_name} {second_name} , my age is {age}'  ##формат  ddd {1} {0} {2} .format (x,y,z)

print(result)


st= 'Hello World'
st.isdigit()

tm = ['e',3.3,3223.,'3ee' ]
tm1 = ['ed','ew',22,333,]
print (tm)
print (tm1)
tm.insert(0,3)
tm.append(4)
print (tm)
tm1.insert (len(tm1),342)
print(tm1)

lt = [111,3,33]
kr = (22,66)
tr = {kr: lt}

print(tr.get(kr))


a= [1,2,3,45]
b= [3,5,2,6]
print (id(a),id(b))
b=a
print (id(a))
print (id(b))
b.append(4)
print (a,b)


