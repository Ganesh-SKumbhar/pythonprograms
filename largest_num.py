# largest number in list

list1 = input('Enter the numbers separated by "," : \n').split(',')

n1 = int(list1[0])          # taking first number of list as default largest
c = len(list1)              # length of list

for i in range(1, c):
    if int(list1[i]) > n1:      # here we check for largest number of two
        n1 = int(list1[i])      # replace the largest number
    else:
        continue
print('Largest number is : ', n1)
