# A palindrome is a number/string that is same 
# forwards and backwards. 
# For example 545, 151, 34543, 343, 171, 48984 are palindrome. 
# A string like LOL, MADAM are also palindromes. 
# Write a function that takes an variable and returns 
# True or False if the variable is a palindrome.

def is_palindrome(var):
    str_var = str(var) 
    new_var = str_var[::-1] 
    if (str_var == new_var):
        return True
    else:
        return False

    # pass

def test_challenge_04_palindrome_number1():
    assert is_palindrome(545) == True

def test_challenge_04_palindrome_number2():
    assert is_palindrome(34543) == True

def test_challenge_04_palindrome_number3():
    assert is_palindrome(345432) == False

def test_challenge_04_palindrome_string1():
    assert is_palindrome('MADAM') == True    
    
def test_challenge_04_palindrome_string2():
    assert is_palindrome('LOL') == True    

def test_challenge_04_palindrome_string3():
    assert is_palindrome('Ayumi') == False  