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




#* 48 (5.3)
''' Given a string of lowercase letters like caatsss,
    return the compressed version where every block of consecutive characters 
    is replaced by the number of characters then the character 
    (or just the character if one occurrence) '''

def compress(s):
    i = 0
    j = 1
    result = []
    s += ' '

    while j < len(s):
        if s[j] == s[i]:
            j += 1
        else:
            count = j - i 
            char = s[i]
            if count > 1:
                result.append(str(count) + char)
            else:
                result.append(char)
            i = j 
            j += 1 

    return ''.join(result)




#* 49 (5.4)
''' Given an array of numbers,
    Move all 5s to the end of the array, in-place
    (the order of the other numbers does not matter) '''

def five_sort(nums):
    i = 0
    j = len(nums) - 1

    while i < j:
        # neither is 5
        if nums[i] != 5 and nums[j] != 5:
            i += 1 
        # just nums[i] is 5 
        elif nums[i] == 5 and nums[j] != 5:
            nums[i], nums[j] = nums[j], nums[i] 
            i += 1 
            j -= 1 
        # just nums[j] is 5 
        elif nums[j] == 5 and nums[i] != 5:
            j -= 1 
        # both are 5 
        else:
            j -= 1

    return nums
        
            
