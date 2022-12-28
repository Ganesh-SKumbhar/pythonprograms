# getting sum of items in a dictionary
from functools import reduce

dct = {'a': 100, 'b': 200, 'c': 300}

# using for loop
summ = 0
for i in dct:
    summ += dct[i]

print('sum of all items is :- ', summ)


# using reduce function
print('sum of all items is using reduce() and lambda function :- ', reduce(lambda a, b: a+b, [dct[i] for i in dct]))

print('maximum element is :', reduce(lambda a, b: a if a > b else b, [dct.get(i) for i in dct]))

# used get method as it returns value for the key provided
