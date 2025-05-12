

"""
Given an array of integers (positive and negative) find the largest continuous sum. 

Example: Given array: [1,2,-1,3,4,10,10,-10,-1]      Expected value is: 29
"""


def large_cont_sum(arr:list) ->int: 
    """
    Find the largest continuous sum.
    Args: 
        arr: the array to check
    Returns:
        int: the result of the sum
    """
    if len(arr) == 0:
        return 0
 
     # Start the max and current sum at the first element
    max_sum=current_sum=arr[0] 

    # For every element in array
    for num in arr[1:]: 
        
        # Set current sum as the higher of the two
        current_sum=max(current_sum+num, num)
        
        # Set max as the higher between the currentSum and the current max
        max_sum=max(current_sum, max_sum) 
        
    return max_sum 