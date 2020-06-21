#task1
a=int(input('Enter a= '))
b=int(input('Enter b= '))
print(id(a))
print(id(b))
dictionary1=dict((('a',b),('b',a)))
print(dictionary1)
#task2
a=int(input('Enter amount of information in bytes= '))
print('You have entered ', a, 'B')
kilo=a*0.001
mega=a*0.000001
print('Information in kilobytes=', kilo, 'KB')
print('Information in megabytes=', mega, 'MB')
#task3
w=float(input('Enter width= '))
h=float(input('Enter heigh= '))
p=(w+h)*2
a=w*h
print('Perimeter=', p)
print('Area=', a)
#task4
r=float(input('Enter radius= '))
pi=3.14
a=pi*r**2
p=2*pi*r
print('Area=', a)
print('Primeter=', p)
#task5
import math
k1=float(input('Enter catheus='))
k2=float(input('Enter another catheus='))
h=math.sqrt(k1**2+k2**2)
print('Hypothenus=', h)
#task6.1
#description of collection should look like
collections={'cats':'collection contains southern Europe cats', \
             'cars':'collection contains Porshe and BMW cars', \
             'elephans':'collection contains African elephants'}
#description of marks of collection should look like
cats={'Sphinks':'stamp dated 1900 year, estimated cost=1000$', \
      'Bengal':'stamp dated 1976, estimated cost=250$'}
#if you want to exchange 'cats' to 'airplanes' collection
del collections['cats']
airplanes={'airplanes':'collection contains airplanes'}
collections.update(airplanes)
