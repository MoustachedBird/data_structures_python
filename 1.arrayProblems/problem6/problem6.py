"""
Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'. 
For this problem, you can falsely "compress" strings of single or double letters. 
For instance, it is okay for 'AAB' to return 'A2B1' even though this technically takes more space. 

The function should also be case sensitive, so that a string 'AAAaaa' returns 'A3a3'.
"""

def compress(s:str) -> str:
    """
    This function will compress any given string
    Args: 
        s: the given string
    Returns:
        The compressed string. Example, string 'AAAaaa' returns 'A3a3'
    """
    r = ''
    l = len(s)

    if l == 0:
        return ""
    
    if l==1:
        return s + "1"
    
    last = s[0]
    cnt = 1
    i = 1

    while i<l:
        if s[i] == s[i-1]:
            cnt += 1
        else:
            r = r + last + str(cnt)
            cnt = 1
            last = s[i]
        i +=1
    r = r + last + str(cnt)

    return r