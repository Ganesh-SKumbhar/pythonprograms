"""
# Write a Python program to check if a given positive integer is a power of two
# bitwise operator is used. all bits for multiple of 2 are 1,

num = int(input('Enter any number: '))

if num > 0 and num & (num-1) == 0:
    print("yes")
else:
    print("no")
    
# -----------------------------------------------------------------
# approach:-- divide number by 2 (n//2) iteratively
# if the n%2 != 0 then number is not multiple of 2
# lastly we need the remainder as 0 and quotient as 1, so next if loop checks for it

num = int(input("Enter number to check whether it is power of 2 : "))

while num != 1:
    if num % 2 != 0:
        print('no')
        break
    else:
        num = num // 2
        continue
if num == 1:
    print("yes")
# ----------------------------------------------
"""
num = int(input("Enter number to check whether it is power of 2 : "))

while num % 2 == 0:
    num //= 2
if num == 1:
    print('yes')
else:
    print('No')
