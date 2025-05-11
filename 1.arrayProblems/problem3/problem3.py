import collections

"""
Consider an array of non-negative integers. A second array is formed by shuffling the elements 
of the first array and deleting a random element. Given these two arrays, find which element is missing in the second array.

Here is an example input, the first array is shuffled and the number 5 is removed to construct the second array.

Input:

finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])
Output:

5 is the missing number
"""

def finder(arr1:list,arr2:list) -> int:
    
    """
    Find the missing number in the second array.
    Args:
        arr1 (list): First array.
        arr2 (list): Second array.         
    Returns:
        int: The missing number.
    """
    if len(arr1) == 0 or len(arr2) == 0:
        return None
    
    arr1.sort()
    arr2.sort()

    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            return num1
        
    return None


def finder2(arr1:list,arr2:list) -> int:
    
    """
    Find the missing number in the second array.
    Args:
        arr1 (list): First array.
        arr2 (list): Second array.         
    Returns:
        int: The missing number.
    """
    if len(arr1) == 0 or len(arr2) == 0:
        return None
    
    #to prevent errors if key is not created. Init with 0 if key is not created
    d = collections.defaultdict(int) 

    for num in arr2:
        d[num] +=1
    
    for num in arr1:
        if d[num] == 0:
            return num
        else:
            d[num] -=1
        
    return None