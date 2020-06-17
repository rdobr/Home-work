#task1
a=int(input('Enter a= '))
b=int(input('Enter b= '))
print((a+b), (a-b), (a*b), (a/b))

#task2
name=input('What is your name? ')
age=input('How old are you? ')
address=input('Where do you live? ')
print('Hello ', name)
print('Your age is ', age)
print('You live in ', address)

#task3
from PIL import Image
image = Image.open('happyface.jpg')
image.show()
