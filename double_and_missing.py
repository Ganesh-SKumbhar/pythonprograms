"""
Problem

You are given a read-only array of n integers from 1 to n.
Each integer appears exactly once except A which appears twice and B which is missing.
Print A and B.

###Input:
    First-line will contain TT, the number of test cases. Then the test cases follow.
    Second-line will contain NN, the number of elements in the array.
    The third line will contain the elements of the array.

###Output: For each test case, the single line output will contain A followed by B.

###Sample Input: 2

5

3 1 2 5 3

8

5 7 2 3 1 8 7 4

###Sample Output:
3 4
7 6
--------------------------------------------------------------

t = int(input('Enter the test cases: '))
missing = 0
double = 0
for i in range(t):
    num = int(input('Enter number of elements in array:'))
    num_list = eval(input('enter number with comma between them'))
    for nums in range(1, num+1):
        if num_list.count(nums) > 1:
            double = nums
        if nums not in num_list:
            missing = nums
    print(double, missing)
----------------------------------------------------------------------
"""

t = int(input('Test cases:- '))
missing = 0
double = 0
for tc in range(t):
    num = int(input('Numbers in array: '))

    # using different ways for multiple inputs

    # lst1 = list(map(int, input().split(' ')))         # using map

    lst1 = [int(i) for i in input().split()]            # list comprehension

    for nums in range(1, len(lst1) + 1):
        if lst1.count(nums) > 1:
            double = nums
        if nums not in lst1:
            missing = nums
    print('Double:- ', double, 'Missing:- ', missing)
