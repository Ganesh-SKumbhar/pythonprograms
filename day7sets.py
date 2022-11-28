"""
# sets

---------------------------------------------------------------------

# Exercises: Level 1
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

# 1. Find the length of the set it_companies
print('Length :', len(it_companies))

# 2. Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

# 3. Insert multiple IT companies at once to the set it_companies
it_companies.update({'Bluestock', 'Infosys', 'Tech Mahindra'})
print('list after multiple update : ', it_companies)

# 4. Remove one of the companies from the set it_companies
print('Removed : ', it_companies.pop())

# 5. What is the difference between remove and discard
# - remove throws error if element is not present
# - discard does not raise any error if element is not present


------------------------------------------------------------------
Exercises: Level 2

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print('A:----> ', A)
print('B:----> ', B)

# 1. Join A and B
print('Joining A and B :- ', A.union(B))

# 2. Find A intersection B
print('Intersection of A and B :- ', A.intersection(B))

# 3. Is A subset of B
print('A is Subset of B :- ', A.issubset(B))

# 4. Are A and B disjoint sets
print('A is disjoint to B :- ', A.isdisjoint(B))

# 5. Join A with B and B with A

# A.update(B)
# print('Join A with B :- ', A)
# B.update(A)
# print('Join B with A :- ', B)

# 6. What is the symmetric difference between A and B

print('Symmetric Difference between A and B :- ', A.symmetric_difference(B))

# 7. Delete the sets completely
del A
del B

# print('A', A,'B',  B)      # NameError as del will delete the sets from memory

-----------------------------------------------------------------
Exercises: Level 3

age = [22, 19, 24, 25, 26, 24, 25, 24]
print('List of ages :- ', age)
print('Set of ages :- ', set(age))
# 1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
print('length of list of ages :- ', len(age), 'Length of set of ages :- ', len(set(age)))

# 2. Explain the difference between the following data types: string, list, tuple and set
* list -
- represented by []
- List allows duplicate elements
- mutable
- ordered
- empty list: l = []
- created by - l = list()

* tuple -
- represented by ()
- Tuple allows duplicate elements
- immutable
- ordered
- empty tuple: t = ()
- created by - t = tuple()

* set -
- represented by {}
- Set do not allow duplicate elements
- mutable
- unordered
- empty set: s = {()}
- created by - s = set()

* dictionary -
- represented by {}
- Dictionary do not allow duplicate keys
- mutable
- ordered
- empty dictionary: d = {}
- created by - d = dict()

"""

# 3. I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence?
# Use the split methods and set to get the unique words.

str1 = 'I am a teacher and I love to inspire and teach people'
set1 = set(str1.split())

print('set of unique words :- ', set1, f'\n with {len(set1)} unique words')

