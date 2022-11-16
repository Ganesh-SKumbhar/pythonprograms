# find character with maximum frequency in string

str1 = input('Enter the string: ')
str2 = str1.replace(' ', '')

char_count_dct = {}

for i in str2:
    if i in char_count_dct:
        char_count_dct[i] += 1
    else:
        char_count_dct[i] = 1

res = max(char_count_dct, key=char_count_dct.get)

print(f'maximum frequency character in {str1} is ==> {res}')
