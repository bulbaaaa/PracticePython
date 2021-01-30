user_input = int(input('How many Fibonacci numbers u want to generate?: '))

def fibonacci(num):
    a = 0
    b = 1
    if num < 2:
        return 1
    else:
        for i in range(0, num):
            c = a + b
            a = b
            b = c
            print(b)



fibonacci(user_input)
