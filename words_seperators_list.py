# write a python program to split a string of words separated by commas and spaces into separate lists words and separators. 

# str1 = input("Enter string: ")

str1 = 'Python has simple, clean syntax, good library support, and optional named parameters'
sep_list = []       # empty list to store seperators

for i in str1:
    if (i == ' ') or (i == ','):
        sep_list.append(i)
        
words_list = str1.split(sep=' ')        # list containing words splitted using space ' '

for i in words_list:
    if ',' in i:
        temp = i.split(',')
        words_list.remove(i)
        words_list.append(temp[0])

print("Seperator list: ", sep_list)
print("Words list: ", words_list)


'''
o/p:- 
Seperator list:  [' ', ' ', ',', ' ', ' ', ',', ' ', ' ', ' ', ',', ' ', ' ', ' ', ' '] 
Words list:  ['Python', 'has', 'clean', 'good', 'library', 'and', 'optional', 'named', 'parameters', 'simple', 'syntax', 'support'] 
'''
