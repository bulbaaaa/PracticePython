num = int(input('Check if this number is odd or even: '))

if num % 2 == 0:
    if num % 4 == 0:
        print('Num is even and divided by 4')
    else:
        print('Num is even')

else:
    print('Num is odd')

num = int(input('Put one number: '))
check = int(input('Put second number: '))

if num % check == 0:
    equal = int(num / check)
    print('You can divide first number by second and this is equal to: ' + (str(equal)))
else:
    print('You can\'t divide first number by second')
