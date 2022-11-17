# program to find whether given number is prime or not
num = int(input('Enter any number to check whether it is prime: '))
if num < 0:
    print('Number is negative.')
elif num == 1:
    print('1 is not a prime number')
else:
    for i in range(2, num):
        if num % i == 0:
            print(f'{num} is not a prime number')
            break
    else:
        print(num, ' is a prime number')