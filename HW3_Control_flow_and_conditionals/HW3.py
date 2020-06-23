#task1
import calendar
year=1998 
#or year=int(input('Enter year: '))
calculation=year/100
if calculation==year//100:
    century=int(year/100)
else:
    century=int(year/100)+1
print(century, 'century')
if calendar.isleap(year) is True:
    print(year, 'is a leap year')
else:
    print(year, 'is not a leap year')
#task2
option=input('Enter what type of figure you want to calculate - \n "triangle", "rectangle" or "circle": ')
print('You have decided to calculate:', option)
import math
if option=='circle':
    r=float(input('Enter radius: '))
    s=math.pi * r**2
    print('Square =', s)
elif option=='rectangle':
    a=float(input('Enter side a: '))
    b=float(input('Enter side b: '))
    s=(a+b) * 2
    print('Square =', s)
elif option=='triangle':
    a=float(input('Enter side a: '))
    b=float(input('Enter side b: '))
    c=float(input('Enter side c: '))
    p=(a+b+c)/2
    s=math.sqrt(p*(p-a)*(p-b)*(p-c))
    print('Square =', s)
else:
    print('You have made some mistake while entering value')
#task3
number=int(input('Enter your number='))
if number > 0:
    print('positive,', len(str(number)), '-digit')
elif number < 0:
    print('negative,', len(str(abs(number))), '-digit')
else:
    print('Value is 0')
#task4
import math
R=float(input('Enter radius of the stage= '))
S=float(input('Enter square of the hall= '))
K=float(input('Enter size of requested passage= '))
side= math.sqrt(S)
real_passage= side/2 - R
if real_passage>=K:
    print('Passage=', real_passage, 'There is enough space for passage')
else:
    print('Passage=', real_passage, 'There is not enough space for passage')
#task5
number=int(input('Enter amount of money= '))
if number<10:
    one_coins = number
    print('Money= ', number)
    print('Bills: ')
    print(one_coins, '- 1 UAH coins')
else:
    if number < 100:
        ten_bills = number // 10
        one_coins = number - ten_bills*10
        print('Money= ', number)
        print('Bills: ')
        print(ten_bills, '- 10 UAH bills')
        print(one_coins, '- 1 UAH coins')
    else:
        if number < 200:
            one_h_bills = 1
            ten_bills = (number - 100) // 10
            one_coins = number - 100 - ten_bills*10
            print('Money= ', number)
            print('Bills: ')
            print(one_h_bills, '- 100 UAH bills')
            print(ten_bills, '- 10 UAH bills')
            print(one_coins, '- 1 UAH coins')
        else:
            two_h_bills = number//200
            if number - two_h_bills*200 >= 100:
                one_h_bills = 1
                ten_bills = (number - two_h_bills*200 - 100) // 10
                one_coins = number - two_h_bills*200 - 100 - ten_bills*10
            else:
                one_h_bills = 0
                ten_bills = (number - two_h_bills*200) // 10
                one_coins = number - two_h_bills*200 - ten_bills*10
            print('Money= ', number)
            print('Bills: ')
            print(two_h_bills, '- 200 UAH bills')
            print(one_h_bills, '- 100 UAH bills')
            print(ten_bills, '- 10 UAH bills')
            print(one_coins, '- 1 UAH coins')
