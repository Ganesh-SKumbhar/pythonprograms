# program to find whether entered string is anagram or not
# anagram is case where,if given strings have same letters

str1 = input('Enter string 1 : ')
str2 = input('Enter string 2 : ')

if sorted(str1.lower()) == sorted(str2.lower()):
    print(f'{str1} and {str2} are anagram.')
else:
    print('strings are not anagram.')
