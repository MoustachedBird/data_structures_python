
"""
Given an integer array, output all the ** unique ** pairs that sum up to a specific value k.

So the input:

pair_sum([1,3,2,2],4)
would return 2 pairs:

 (1,3)
 (2,2)
NOTE: FOR TESTING PURPOSES CHANGE YOUR FUNCTION SO IT OUTPUTS THE NUMBER OF PAIRS
"""

def pair_sum(arr,k):
    """
    Find all unique pairs in the array that sum up to k.
    Args:
        arr (list): List of integers.
        k (int): Target sum. 
    Returns:
        int: Number of unique pairs that sum up to k.
    """
    if len(arr) < 2:
        return 0
    
    #sets to store unique pairs
    seen = set()
    output = set()

    for num in arr:
        target = k - num
        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num, target), max(num, target)))

    print('\n'.join(map(str, list(output))))

    return len(output)

if __name__ == "__main__":
    pass