

# PROGRAM TO GET SINGLE STRING FROM TWO GIVEN STRINGS, SEPERATED
# BY A SPACE AND SWAP THE FIRST TWO CHARACTERS OF EACH STRING

#str1 = input("Enter string 1 :")
#str2 = input("Enter string 2 :")
#str11=str2[:2]+str1[2:]
#str22=str1[:2]+str2[2:]
#print(str11+' '+str22)

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
