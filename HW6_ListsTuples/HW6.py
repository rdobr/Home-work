#task1
list_default = [4, 55, 15, 666, 33]

number1 = int(input('Enter any number1 - '))
number2 = int(input('Enter any number2 - '))
number3 = int(input('Enter any number3 - '))
number4 = int(input('Enter any number4 - '))
number5 = int(input('Enter any number5 - '))
list_entered = [number1, number2, number3, number4, number5]
list_sum = [sum(list_default), sum(list_entered)]
print(list_sum)

#task2
import random
list_positive = []
list_negative = []
list_null = []
list_random = []

for x in range(10):
    list_random.append(random.randint(-5,5))
print('Your random numbers are ', list_random)
for y in list_random:
    if y > 0:
        list_positive.append(y)
    elif y < 0:
        list_negative.append(y)
    elif y == 0:
        list_null.append(y)
number_null = len(list_null)
print('List of values more than 0 is', list_positive)
print('List of values less than 0 is', list_negative)
if number_null > 0 and number_null == 1:
    print('There is', number_null, 'value that equal 0')
elif number_null > 1:
    print('There are', number_null, 'values that equal 0')
else: print('There are no values that equal 0')
