# program to find the sum of squares of n numbers
num = int(input('Enter number to get the sum of squares of number up to given number : '))


def sum_of_sqrs(n):
    addition = 0
    for i in range(1,n+1):
        addition += (i*i)
    return addition


print(f'sum of squares of numbers till {num} is : {sum_of_sqrs(num)}')
