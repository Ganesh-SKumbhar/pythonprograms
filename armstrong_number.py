# program to find whether the number is armstrong or not
# sum of cube of digits of number is exactly equal to that number

def is_armstrong(num):
    add = 0

    while num > 0:
        digit = num % 10
        add = add + digit ** 3
        num = num // 10
    return add


numb = int(input('Enter a number to find whether it is armstrong or not : '))

if numb == is_armstrong(numb):
    print('number is armstrong')
else:
    print('number is not armstrong')
