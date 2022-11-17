# program to find the simple interest and compound interest and give the difference between them for same amount.

principle_amount = float(input('Enter principal Amount : '))
duration = int(input('Enter duration : '))
rate_of_interest = float(input('Enter rate of interest : '))

# Simple Interest
simple_interest = (principle_amount * rate_of_interest * duration)/100
print('Simple interest is: ', simple_interest)

# Compound Interest
compound_interest = round(((principle_amount * ((1+rate_of_interest/100) ** duration)) - principle_amount), 2)
print('Compound interest is: ', compound_interest)


# difference between compound interest and simple interest
difference_ci_si = compound_interest - simple_interest
print('Difference between Compound Interest and Simple Interest is :', difference_ci_si)
