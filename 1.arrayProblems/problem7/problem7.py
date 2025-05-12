"""
Given a string,determine if it is compreised 
of all unique characters. 
For example, the string 'abcde' has all unique characters and should return True. 
The string 'aabcde' contains duplicate characters and should return false.
"""


def uni_char(s:str) -> bool:

    if s == '':
        return True

    d = dict()

    for eachChar in s:
        if eachChar not in d:
            d[eachChar] = 1
        else:
            return False

    return True