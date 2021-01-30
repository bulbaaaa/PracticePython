import random

number = random.randint(0,9)
count_guesses = 0

while True:
    user = input('Guess the number from 1 to 9. If u want stop type exit: ')
    if user == 'exit':
        print('Thanks for the game')
        break
    elif int(user) > number:
        print('Number is too high')
        count_guesses += 1
    elif int(user) < number:
        print('Number is too low')
        count_guesses += 1
    else:
        count_guesses += 1
        print('You guess the number in ' + str(count_guesses) + ' tries')
