# Write a Python program to check if a given positive integer is a power of four

num = int(input())
while num % 4 == 0:
    num //= 4
if num == 1:
    print("yes")
else:
    print('No')





