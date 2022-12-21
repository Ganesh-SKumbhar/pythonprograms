# Write a Python program to find the single element in a list where every element appears three times except for one.Go to the editor
#Input : [5, 3, 4, 3, 5, 5, 3]
#Output : 4

list1 = (input('Enter list of items separated by , : ')).split(',')

for i in list1:
    if (list1.count(i)) == 1:
        print(i)
