check = input('Check this string if it is a palindrome: ')

if check.lower() == check[::-1].lower():
    #list[<start>:<stop>:<step>]
    print('this is a palindrome')
else:
    print('this is not a palindrome')
