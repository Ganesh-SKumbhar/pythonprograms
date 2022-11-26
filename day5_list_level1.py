# 1.declare an empty list
lst = []            # direct method using square brackets
lst1 = list()       # using inbuilt list function

print('Empty list : ', lst, lst1)    # [] []
# ----------------------------------------------------------
# 2. Declare a list with more than 5 items

lst = [12, 23, 34, 45, 56]
print('List :- ', lst)          # [12, 23, 34, 45, 56]
# ----------------------------------------------------------
# 3. Find length of your list

print('Length of list : ', len(lst))     # 5

# 4.Get the first item, the middle item and the last item of the list

first_item = lst[0]
middle_item = lst[len(lst)//2]
last_item = lst[len(lst)-1]

print('First item : ', first_item, '\nMiddle item : ', middle_item, '\nLast item : ', last_item)        # 12 34 56

# 5.Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mix_list = ['ganesh', 32, 5.5, 'married', 'Kolhapur']

# 6.Declare a list variable named it_companies and assign initial values
#   Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7.Print the list using print()
print('List of companies :- ', it_companies)

# 8.Print the number of companies in the list
print('Number of companies :- ', len(it_companies))

# 9.Print the first, middle and last company
print('First :- ', it_companies[0], '\nMiddle :- ', it_companies[len(it_companies)//2], '\nLast :-',  it_companies[-1])

# 10. Print the list after modifying one of the companies
it_companies[3] = 'Harbinger'
print('After modification :- ', it_companies)

# 11.Add an IT company to it_companies
it_companies.append('Accenture')
print('list after addition of company :\n', it_companies)

# 12.Insert an IT company in the middle of the companies list
it_companies.insert(len(it_companies)//2, 'Infosys')
print('adding company in middle of list: \n', it_companies)

# 13.Change one of the it_companies names to uppercase (IBM excluded!)
print('upper case : -\n', [it_companies[i].upper() for i in range(len(it_companies))])

# 14.Join the it_companies with a string '#;  '
print('joining companies with "#; "\n', "#; ".join(it_companies))

# 15.Check if a certain company exists in the it_companies list.
print('Check Google is within list :-  ', 'Google' in it_companies)
print('Check Suma-soft is within list :- ', 'Suma-soft' in it_companies)

# 16.Sort the list using sort() method
it_companies.sort()
print('Sorting company list :- ', it_companies)

# 17.Reverse the list in descending order using reverse() method
it_companies.sort(reverse=True)
print('Sorting company list :- ', it_companies)

# 18.Slice out the first 3 companies from the list
print('First 3 companies :- ', it_companies[:3])

# 19.Slice out the last 3 companies from the list
print('Last 3 companies :- ', it_companies[-4:-1])

# 20.Slice out the middle IT company or companies from the list
middle_list = it_companies[(len(it_companies)//2)-1:(len(it_companies)//2)+2]
print(middle_list)

# 21.Remove the first IT company from the list
del it_companies[0]
print(it_companies)

# 22.Remove the middle IT company or companies from the list
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
del it_companies[len(it_companies)//2]
print('List after removing middle company :- ', it_companies)

# 23.Remove the last IT company from the list
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print('Removing last company :- ', it_companies.pop())

# 24.Remove all IT companies from the list
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.clear()
print('After removing all companies from list', it_companies)

# 25.Destroy the IT companies list
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
del it_companies

# 26.Join the following lists
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

print('Joining two lists :- ', front_end + back_end)    # concatenate
front_end.extend(back_end)                              # extend() method
print('Joining two lists :- ', front_end)

# 27.After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack.
# Then insert Python and SQL after Redux.
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

full_stack = front_end+back_end
print(full_stack)

full_stack.insert(full_stack.index('Redux')+1, 'Python')
full_stack.insert(full_stack.index('Python'), 'SQL')
print(full_stack)







