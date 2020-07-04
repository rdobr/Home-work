#task1
import random

value = random.randint(0, 100)
print('Random number in range from 0 to 100 is generated.')
#print('Psss..Psss..Do mot tell anybody, but random number is =', value)
for i in range(1, 11):
    user_value=int(input('Try to guess it! Your number = '))
    if value == user_value:
        print('You have guessed the number!')
        print('Number of the attemp is', i)
        break
    elif value > user_value:
        print('You have missed, random number is more than entered number')
    elif value < user_value:
        print('You have missed, random number is less than entered number')
    i += 1
if i > 10:
    print('You are looser, you couldn\'t guess simple number in 10 attemps')
    print('Random number is', value)

#task2
i = 0
for x in range(0, 10):
    number = int(input('Enter your number grater than 2 - '))
    if number/5 == number//5:
        i += 1
    else:
        continue
print('Amount of numbers that are multiples of 5 -', i)

#task3
n=9
m = list(list(range(1*i,(n+1)*i, i)) for i in range(1,n+1))
for i in m:
       i = [str(j).rjust(len(str(m[-1][-1]))+1) for j in i]
       print(''.join(i))

#task4
w = 'w'
o = 'o'
e = ' '
print('%-10s %-50s' %(e, 50*w))
print('%-10s %-1s %-46s %1s' %(e, w, 46*o, w))
print('%-10s %-1s %-46s %1s' %(e, w, 46*o, w))
print('%-10s %-1s %-46s %1s' %(e, w, 46*o, w))
print('%-10s %-1s %-46s %1s' %(e, w, 46*o, w))
print('%-10s %-1s %-46s %1s' %(e, w, 46*o, w))
print('%-10s %-1s %-46s %1s' %(e, w, 46*o, w))
print('%-10s %-1s %-46s %1s' %(e, w, 46*o, w))
print('%-10s %-1s %-46s %1s' %(e, w, 46*o, w))
print('%-10s %-1s %-46s %1s' %(e, w, 46*o, w))
print('%-10s %-1s %-46s %1s' %(e, w, 46*o, w))
print('%-10s %-1s %-46s %1s' %(e, w, 46*o, w))
print('%-10s %-1s %-46s %1s' %(e, w, 46*o, w))
print('%-10s %-1s %-46s %1s' %(e, w, 46*o, w))
print('%-10s %-1s %-46s %1s' %(e, w, 46*o, w))
print('%-10s %-50s' %(e, 50*w))

#task5
p = 10
h = 20
total_sum = 0
count = 0
product = 1

while True:
    number = int(input('Enter your number - '))
    if number < p:
        total_sum = total_sum + number
    elif number > h:
        product = product * number
    elif h > number > p:
        count = count + 1
    elif number == p or number == h:
        print('Total sum = ', total_sum)
        print('Amount of number between "p" and "h" = ', count)
        if product == 1:
            print('Numbers more than "h" were not entered')
        else:
            print('Total product = ', product)
        break

#task6
count_neg = 0
count_pos = 0

while True:
    number = int(input('Enter your number = '))
    if number < 0:
        count_neg = count_neg + 1
    elif number > 0:
        count_pos = count_pos + 1
    elif number == 0:
        sum_numbers = count_neg + count_pos
        percent_neg = count_neg * 100 / sum_numbers
        percent_pos = 100 - percent_neg
        print('Percentage of positive numbers = %-3.1f' %percent_pos, '%')
        print('Percentage of negative numbers = %-3.1f' %percent_neg, '%')
        break
