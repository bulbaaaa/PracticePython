user_num = int(input('Check if number is prime or not: '))


def check_primality(num):
    if num > 1:
        for i in range(2, num): 
            if( num % i) == 0:
                print('This is not a prime number')
                break;
            else:
                print('This is a prime number')
                break
    else:
        print('This is not a prime number')
        

check_primality(user_num)
