# Extract unique values from dictionary

dict1 = {'one': [5, 7, 6, 8],
         'two': [10, 11, 7, 5],
         'three': [6, 12, 10, 8],
         'four': [1, 5, 2]
         }

# using for loop
unique = set()
for i in dict1:
    for j in dict1.get(i):
        unique.add(j)

print('using for loop', unique)

# using list comprehension
unique1 = [j for i in dict1 for j in dict1.get(i)]
print('using list comprehension', set(unique1))

# using set comprehension

print('using set comprehension', {nums for i in dict1 for nums in dict1[i]})   # set comprehension
