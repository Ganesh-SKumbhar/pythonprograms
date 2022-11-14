"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order,
and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
"""


l1 = [9, 9, 9, 9, 9, 9, 9]
l2 = [9, 9, 9, 9, ]


def ret_num(lst):
    num = ''
    for i in range(len(lst)):
        num = num + str(lst[i])
    return int(num)


n1 = ret_num(l1)
n2 = ret_num(l2)

add = n1 + n2


# approach 1
sum_lst = []                            # empty list
for i in range(len(str(add))):
    sum_lst.insert(0, str(add)[i])
print(sum_lst)


# approach 2
print(list(str(add))[::-1])     # here converting add to str, and then converting to list, and use slicing to reverse it
