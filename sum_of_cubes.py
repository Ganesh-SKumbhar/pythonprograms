# program to find the sum of cubes of n numbers
num = int(input('Enter number to get the sum of squares of number up to given number : '))


def sum_of_cube(n):
    addition = 0
    for i in range(1,n+1):
        addition += (i*i*i)
    return addition


print(f'sum of cubes of numbers till {num} is : {sum_of_cube(num)}')
