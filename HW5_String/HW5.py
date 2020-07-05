#task3
number = input('Enter your number = ')
product_number = 1
for x in range(0, len(number)):
    product_number = product_number * int(number[x])
print('Your number is', number)
print('Product of digits of your number is', product_number)
reverse = number[::-1]
product_reverse = 1
for y in range(0, len(reverse)):
    product_reverse = product_reverse * int(number[y])
print('Reverse number is', reverse)
print('Product of digits of reverse number is', product_reverse)

#task4
text = input('Enter any text here - ')
number_spaces = text.count(' ')
print('Text contains', number_spaces, 'spaces')

#task5
text = input('Enter any text here - ')
swap_text = text.replace(' ', '_')
print(swap_text)

#task6
lower = 0
upper = 0
text = input('Enter any text here - ')
for x in range(0, len(text)):
    if text[x].islower() is True:
        lower = lower + 1
    if text[x].isupper() is True:
        upper = upper + 1
if lower > 0:
    print('Your text has at least one lowercase character')
else:
    print('Your text does not have lowercase characters')
if upper > 0:
    print('Your text has at least one uppercase character')
else:
    print('Your text does not have uppercase characters')




