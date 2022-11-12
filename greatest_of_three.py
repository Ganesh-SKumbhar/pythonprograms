
num1=int(input("number 1: "))
num2=int(input("number 2: "))
num3=int(input("number 3: "))

if num1>num2:
    if num1>num3:
        print("largest number is: ",num1)
if num2>num1:
    if num2>num3:
        print("largest number is: ",num2)
if num3>num2:
    if num3>num1:
        print("largest number is: ",num3)
