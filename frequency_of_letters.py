# find the frequency of letters in string

str1 = 'python is easy to learn but requires lots of hands-on'

str2 = str1.replace(' ', '')    # string without spaces

dct = {}

for i in str2:
    dct[i] = dct.get(i, 0) + 1

print('letter frequency : - \n', dct)

print('max frequent letter is :- ', max(dct, key=dct.get))
