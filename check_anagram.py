"""
 Write a Python program to check if a given string is an anagram of another given string. Go to the editor
Input : 'anagram','nagaram'
Output : True
"""

def anagram(str1, str2):
    lst_str1 = list(str1)
    lst_str1.sort()
    lst_str2 = list(str2)
    lst_str2.sort()
    return lst_str1.sort() == lst_str2.sort()


print(anagram('anagram', 'margana'))
