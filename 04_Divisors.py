user_num = int(input('Put random number: '))

b = [i for i in range(1,user_num + 1) if user_num % i == 0]

print(b)
