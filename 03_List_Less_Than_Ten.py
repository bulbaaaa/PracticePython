a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

user_num = int(input('Put number: '))
b = [i for i in a if i < user_num]
print(b)
