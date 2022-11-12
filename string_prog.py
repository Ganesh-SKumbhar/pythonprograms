

# PROGRAM TO GET SINGLE STRING FROM TWO GIVEN STRINGS, SEPERATED BY A SPACE AND SWAP THE FIRST TWO CHARACTERS OF EACH STRING

str1 = input("Enter string 1 :")
str2 = input("Enter string 2 :")
str11=str2[:2]+str1[2:]
str22=str1[:2]+str2[2:]
print(str11+' '+str22)

