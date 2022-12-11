"""
Exercises: Level 1

1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive.
If below 18 give feedback to wait for the missing amount of years.
---------------------------------------------------
age = int(input("Enter your age: "))

if age >= 18:
    print('You are old enough to drive.')
else:
    print(f'You need {18 - age} more years to learn to drive.')

 ---------------------------------------------------
Output:
Enter your age: 30
You are old enough to learn to drive.
Output:
Enter your age: 15
You need 3 more years to learn to drive.

#=======================================================================
2. Compare the values of my_age and your_age using if … else. Who is older (me or you)?
Use input(“Enter your age: ”) to get the age as input.
You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences,
and a custom text if my_age = your_age.
-------------------------------------------------
my_age = 32
age = int(input("Enter your age: "))

if age >= my_age:    # OLDER
    if age - my_age == 1:
        print('Age difference is 1 year.')
    elif age == my_age:
        print('We are same age.')
    else:
        print(f'You are {age - my_age} years older than me.')
else:               # younger
    print('I am older than You.')
-----------------------------------------------
Output:
Enter your age: 30
You are 5 years older than me.
#=======================================================================
    3. Get two numbers from the user using input prompt. If a is greater than b return a is greater than b,
    if a is less b return a is smaller than b, else a is equal to b.
-------------------------------------------------

num1 = int(input('Enter number one: '))
num2 = int(input('Enter number two: '))
if num1 > num2:
    print(f'{num1} is greater than {num2}')
else:
    print(f'{num2} is greater than {num1}')

--------------------------------------------------
Output:
Enter number one: 4
Enter number two: 3
4 is greater than 3
#=============================================================================
### Exercises: Level 2

1. Write a code which gives grade to students according to theirs scores:

80-100, A
70-89, B
60-69, C
50-59, D
0-49, F
-------------------------------------------------------------
percentage = int(input('Enter your percentage : '))
if percentage > 90:
    print('A')
elif percentage > 70:
    print('B')
elif percentage > 60:
    print('C')
elif percentage > 50:
    print('D')
else:
    print('F')

#=======================================================================
2. Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November,
the season is Autumn. December, January or February, the season is Winter. March, April or May,
the season is Spring June, July or August, the season is Summer
---------------------------------------------------------
autumn = ['September', 'October', 'November']
winter = ['December', 'January', 'February']
spring = ['March', 'April', 'May']
summer = ['June', 'July', 'August']

month = input('Enter month of year to know which season it falls in :').capitalize()

if month in autumn:
    print('It is Autumn')
elif month in winter:
    print('It is Winter')
elif month in spring:
    print('It is Spring')
elif month in summer:
    print('It is Summer')
else:
    print('Invalid month')

#=======================================================================
3. The following list contains some fruits:

fruits = ['banana', 'orange', 'mango', 'lemon']

If a fruit doesn't exist in the list add the fruit to the list and print the modified list.
If the fruit exists print('That fruit already exist in the list')
-------------------------------------------------------------
fruits = ['banana', 'orange', 'mango', 'lemon']

fruit = input('Enter fruit:  ')

if fruit in fruits:
    print('fruit already exists')
else:
    fruits.append(fruit)
    print(fruits)

#=======================================================================
Exercises: Level 3
4. Here we have a person dictionary. Feel free to modify it!

person={
'first_name': 'Asabeneh',
'last_name': 'Yetayeh',
'age': 250,
'country': 'Finland',
'is_marred': True,
'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
'address': {
    'street': 'Space street',
    'zipcode': '02210'
}
}

* Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in person:
    middle_skill = len(person['skills'])//2
    print(person['skills'][middle_skill])

# * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result
if 'skills' in person:
    if 'Python' in person['skills']:
        print('has  Python skill.')

# * If a person skills has only JavaScript and React, print('He is a front end developer'),
    #if the person skills has Node, Python, MongoDB, print('He is a backend developer'),
    #if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'),
    #else print('unknown title') - for more accurate results more conditions can be nested!

skills = person['skills']
print(skills)
if skills == ['JavaScript', 'React']:
    print('He is a front end developer')
elif skills == ['NodeJS', 'MongoDB', 'Python']:
    print('He is a backend developer')
elif skills == ['React', 'NodeJS', 'MongoDB']:
    print('He is a fullstack developer')
else:
    print('unknown title')

# * If the person is married and if he lives in India, print the information in the following format:

if person['is_marred'] == True and person['country'] == 'India':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")


"""
