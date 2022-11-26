
# 1.The following is a list of 10 students ages:

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

#Sort the list and find the min and max age
ages.sort()
print('Min:= ', ages[0], 'Max:- ', ages[-1])

# Add the min age and the max age again to the list
ages.append(ages[-1])
ages.append(ages[0])
print(ages)

# Find the median age (one middle item or two middle items divided by two)
print(ages)
ages.sort()
ln = len(ages)
if ln % 2 == 0:
    print('Median Age is: ', (ages[(ln//2)-1]+ages[ln//2])//2)
else:
    print('Median Age is: ', (ages[ln//2]) // 2)

# Find the average age (sum of all items divided by their number )
print(ages)
average_age = sum(ages)/len(ages)
print('Average age : ', average_age)

# Find the range of the ages (max minus min)
range_of_ages = max(ages) - min(ages)
print('Range of ages : ', range_of_ages)

# Compare the value of (min - average) and (max - average), use abs() method
print('Min-Average : ', abs(min(ages)-average_age), '\nMax - Average', abs(max(ages) - average_age))

# 2.Find the middle country(ies) in the countries list
countries = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina',
  'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus',
  'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei',
  'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Central African Republic',
  'Chad', 'Chile', 'China', 'Colombi', 'Comoros', 'Congo (Brazzaville)', 'Congo', 'Costa Rica', "Cote d'Ivoire",
  'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic',
  'East Timor (Timor Timur)', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia',
  'Fiji', 'Finland', 'France', 'Gabon', 'Gambia, The', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala',
  'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq',
  'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Korea, North',
  'Korea, South', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein',
  'Lithuania', 'Luxembourg', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta',
  'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia',  'Morocco',
  'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria',
  'Norway', 'Oman', 'Pakistan', 'Palau', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland',
  'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent', 'Samoa',
  'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia and Montenegro', 'Seychelles', 'Sierra Leone',
  'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'Spain', 'Sri Lanka', 'Sudan',
  'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand',  'Togo',
  'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates',
  'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam', 'Yemen',
  'Zambia']

print(countries)
ln = len(countries)
mid = ln // 2

if ln % 2 == 0:
    print('Middle Country is: ', countries[mid-1:mid+1])
else:
    print('Middle Countries are: ', countries[mid])

print([countries[mid-1:mid+1] if ln % 2 == 0 else countries[mid]])         # list comprehension

# 3.Divide the countries list into two equal lists if it is even if not one more country for the first half.
ln = len(countries)
mid = ln // 2
print(mid)
if ln % 2 == 0:
    print('Countries list is even:\n')
    list1 = countries[:mid]
    list2 = countries[mid:]
    print('List1 is: ', list1, '\nlength is', len(list1))
    print('List2 is: ', list2, '\nlength is', len(list2))
else:
    print('Countries list is not even:\n')
    list1 = countries[:mid+1]
    list2 = countries[mid+1:]
    print('List1 is: ', list1, '\nlength is', len(list1))
    print('List2 is: ', list2, '\nlength is', len(list2))

# 4.['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
countries_list = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first, second, third, *scandic = countries_list
print('First country: ', first)
print('Second country: ', second)
print('Third country: ', third)
print('Scandic Countries: ', scandic)