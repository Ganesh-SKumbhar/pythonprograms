# 1.Create an empty tuple
tup1 = ()
# OR
tup2 = tuple()
print('Empty tuples: ', tup1, tup2)

# 2.Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ('Suresh', 'Mahesh', 'Avdhut', 'Digambar')
sisters = ('Manisha', 'Vijaya', 'Jayashri', 'Lata')

print('Brothers list: ', brothers)
print('Sisters list: ', sisters)

# 3.Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters
print('Siblings list : ', siblings)

# 4.How many siblings do you have?
siblings_count = len(siblings)
print('Number of siblings : ', siblings_count)

# 5.Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = siblings + ('Nanda', 'Shankar')
print('Family members : ', family_members)

# ================================  LEVEL 2  ============================================
# 1.Unpack siblings and parents from family_members
*siblings, parent1, parent2 = family_members
parents = [parent1, parent2]
print('unpacked Siblings: ', siblings)
print('Parents : ', parents)

# 2.Create fruits, vegetables and animal products tuples.
# Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('Apple', 'Banana', 'Grapes', 'Kiwi')
print('Fruits :- ', fruits)
vegetables = ('Tomato', 'Spinach', 'BitterGourd', 'Potato')
print('Vegetables :- ', vegetables)
animal_products = ('Milk', 'Fish', 'Meat', 'Ribs')
print('Animal Products :- ', animal_products)

food_stuff_tp = fruits + vegetables + animal_products
print('Food stuff tuple :- ', food_stuff_tp)

# 3.Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print('Food Stuff List :- ', food_stuff_lt)

# 4.Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
len_fs = len(food_stuff_tp)
mid = len_fs // 2

if len_fs % 2 == 0:
    print('Middle items are: ', food_stuff_tp[mid-1:mid+1])
else:
    print('Middle item is: ', food_stuff_tp[mid])

# 5.Slice out the first three items and the last three items from food_staff_lt list
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]

print('First three :- ', first_three, '\nLast three :- ', last_three)

# 6.Delete the food_staff_tp tuple completely
del food_stuff_tp

# 7.Check if an item exists in tuple:
print(food_stuff_tp)

# 8.Check if 'Estonia' is a nordic country
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

print('\'Estonia\' is a nordic country :- ', 'Estonia' in nordic_countries)

# 9.Check if 'Iceland' is a nordic country
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print('\'Iceland\' is a nordic country :- ', 'Iceland' in nordic_countries)
