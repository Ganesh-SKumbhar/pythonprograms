# program to find armstrong numbers in given range

lst = []
def is_armstrong(num):
    add = 0
    temp = num

    while num > 0:
        digit = num % 10
        add = add + digit ** 3
        num = num // 10

    if add == temp:
        lst.append(temp)


start, end = eval(input('Enter the range in which you want to find armstrong numbers separated by "," : '))

for i in range(start, end):
    is_armstrong(i)

print(f'List of Armstrong numbers between {start} and {end} is : {lst}')
