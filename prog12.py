# Write a Python program to find the single number in a list that doesn't occur twice

num_list = (input('Enter list of items seperated by , : ')).split(',')
print(num_list)

for i in num_list:
    if (num_list.count(i)) > 1:
        pass
    else:
        print(i)

