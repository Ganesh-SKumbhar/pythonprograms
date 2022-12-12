# find second-largest number in the list

list1 = input('Enter the numbers separated by "," : \n').split(',')
temp = []
for i in list1:
    temp.append(int(i))

# using comprehension
temp = [int(n) for n in list1]

temp.sort(reverse=True)
print('Sorted List is: \n', temp)
print('Second Largest number is : ', temp[1])       # index 1 will give 2nd element of the list
