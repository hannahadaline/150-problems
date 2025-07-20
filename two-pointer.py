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




#* 47 (5.2)
''' Given a string formatted in concatenated <number><char> format like 2a127b,
    return the uncompressed string '''

def uncompress(s):
    i = 0
    j = 0
    result = []
    digits = '0123456789'

    while j < len(s):
        if s[j] in digits:
            j += 1
        else:
            count = int(s[i:j])
            char = s[j]
            result.append(count * char)
            j += 1
            i = j

    return ''.join(result)
