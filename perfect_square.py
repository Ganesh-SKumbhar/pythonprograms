# program to check if an number is a perfect square
"""
num = int(input("Enter number :  "))

x = num // 2

while x * x != num:
    x = (x + (num // x)) // 2
if x*x == num:
    print(True)
else:
    print('False')

#----------------------------------------------------


def is_perfect_square(n):
    x = n // 2
    y = set([x])
    while x * x != n:
        x = (x + (n // x)) // 2
        if x in y: return False
        y.add(x)
    return True

print(is_perfect_square(8))
print(is_perfect_square(9))
print(is_perfect_square(100))

"""


def is_perfect_square(n):
    x = n // 2
    y = {x}
    while x * x != n:
        x = (x + (n // x)) // 2
        if x in y:
            return False
        y.add(x)
    return True

# print(is_perfect_square(8))
# print(is_perfect_square(9))
print(is_perfect_square(123))
