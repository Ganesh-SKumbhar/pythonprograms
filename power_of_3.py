# Write a Python program to check if a given positive integer is a power of three

for i in range(1,10):
    print(3**i)

num = int(input("Enter number to check whether it is power of 3 : "))
# ---------------------------------
while num != 1:
    if num%3 != 0:
        print('no')
        break
    else:
        num = num//3
        continue
if num == 1:
    print("yes")
# -----------------------------------
while num % 3 ==0:
    num //= 3
if num == 1:
    print("yes")
else:
    print('No')