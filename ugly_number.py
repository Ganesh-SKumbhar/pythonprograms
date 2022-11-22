# Write a Python program to check whether a given number is an ugly number.
# Ugly numbers are positive numbers whose only prime factors are 2, 3 or 5.
# The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 shows the first 10 ugly numbers.
# Note: 1 is typically treated as an ugly number.

num = int(input('Enter number to check whether it is ugly or not : '))
if num == 0:
    print('not ugly')
for i in [2,3,5]:
    while num % i == 0:
        num /= i
if num == 1:
    print('Number is UgLy.')
else:
    print('Number is not ugly')

