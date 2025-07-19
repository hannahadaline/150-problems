#* 46 (5.1)
''' Given a string, return whether the string is a palindrome
    (reads the same forwards and backwards) ''' 

def is_palindrome(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False 
        i += 1
        j -= 1

    return True 
