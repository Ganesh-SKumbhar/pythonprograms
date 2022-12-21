# Write a Python program to find two elements once in a list where every element appears exactly twice in the list. Go to the editor
# Input : [1, 2, 1, 3, 2, 5]
# Output :[5, 3]

list1 = (input('Enter list of items separated by , : ')).split(',')
set1 = set()
for i in list1:
    if (list1.count(i)) == 2:
        set1.update(i)
#print(set1)

for i in set1:
    print(i, end=' ')
