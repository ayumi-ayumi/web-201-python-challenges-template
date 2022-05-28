# A palindrome is a number/string that is same 
# forwards and backwards. 
# For example 545, 151, 34543, 343, 171, 48984 are palindrome. 
# A string like LOL, MADAM are also palindromes. 
# Write a function that takes an variable and returns 
# True or False if the variable is a palindrome.

def is_palindrome(var): #for loop can be used

    str_var = str(var) 
    new_var = str_var[::-1] 
    
    if type(new_var) != str:
        return 'False'
    elif (str_var == new_var):
        return True
    else:
        return False


def test_challenge_04_palindrome_number1():
    assert is_palindrome(545) == True

def test_challenge_04_palindrome_number2():
    assert is_palindrome(34543) == True

def test_challenge_04_palindrome_number3():
    assert is_palindrome(-343) == False

def test_challenge_04_palindrome_string1():
    assert is_palindrome('MADAM') == True    
    
def test_challenge_04_palindrome_string2():
    assert is_palindrome('MaddaM') == True   

def test_challenge_04_palindrome_list():
    assert is_palindrome([34543]) == False    
