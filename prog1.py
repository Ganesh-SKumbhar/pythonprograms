# largest number in list

list1 = input('Enter the numbers separated by "," : \n').split(',')

n1 = int(list1[0])
c = len(list1)

for i in range(1, c):
    if int(list1[i]) > n1:
        n1 = int(list1[i])
    else:
        continue
print('Largest number is : ', n1)
