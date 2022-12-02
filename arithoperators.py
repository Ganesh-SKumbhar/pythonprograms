# Simple Basic Calculators with all arithmetic operators on python

a=float(input("Enter First Number: "))
b=float(input("Enter Second Number: "))

add = a + b
sub = a - b
pro = a * b
div = a / b
floor_div = a // b
power = a ** b
mod = a % b

print(f"Addition of {a} + {b} =  {add}")
print(f"Subtraction of {a} - {b} = {sub}")
print(f"Product of {a} * {b} = {pro}")
print(f"Division of {a} / {b} = {div}")
print(f"Floor Division of {a} // {b} = {floor_div}")
print(f"Power of {a} to {b} = {power}")
print(f"Modulus of {a} % {b} = {mod}")

