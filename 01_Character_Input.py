name = input("Give me your name: ")
age = int(input("Give me your age: "))
print_msg = int(input('How many times you want print this message?: '))
age_after = str((2021 - age) + 100)

for num in range(0, print_msg):
    print('You reach 100 years old in ' + age_after)
