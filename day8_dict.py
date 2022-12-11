"""

"""

# 1. Create an empty dictionary called dog
# dog = {}
#dog = dict()

# 2. Add name, color, breed, legs, age to the dog dictionary
dog = {'name': 'Tommy', 'color': 'White', 'breed': 'Debar Man', 'legs': 4, 'age': 3}
print('Description of dog :- ', dog)

# 3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city
# and address as keys for the dictionary

student = { 'first_name': 'Ganesh', 'last_name': 'Kumbhar',
            'gender': 'Male', 'age': 32,
            'marital status': True, 'skills': ['Python', 'Machine Learning', 'SQL', 'HTML', 'Data Science'],
            'country': 'India', 'city': 'Kolhapur', 'address': {'Area': 'Pachgaon', 'Pincode': 416013}
            }

# 4. Get the length of the student dictionary
print(student)
print('Length of student dictionary is: ', len(student))

# 5. Get the value of skills and check the data type, it should be a list
skills = student['skills']
print('Student skills list : ', student.get('skills'), '\nDatatype of skills is: ', type(skills))

# 6. Modify the skills values by adding one or two skills
student['skills'].extend(['C', 'C++'])
print(student.get('skills'))

# 7. Get the dictionary keys as a list
print('Students keys list : ', student.keys())

# 8. Get the dictionary values as a list
print('Students values list : ', student.values())

# 9. Change the dictionary to a list of tuples using items() method
print('List  of tuples:- ', student.items())

# 10.Delete one of the items in the dictionary
print('Deleted item is  :- ', student.popitem())

# 11.Delete one of the dictionaries
del student
