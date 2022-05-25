# This is a sample of a challenge that is already solved.
# See how there are multiple tests defined, to verify the solution
# function is working for multiple cases / inputs
# 
# The Problem:
# Create a Python function that accepts a string. 
# This function should count the number of Xs and the number of Os 
# in the string. It should then return a boolean value of 
# either True or False.
# If the count of Xs and Os are equal, then the function 
# should return True. If the count isn't the same, it should 
# return False. If there are no Xs or Os in the string, 
# it should also return True because 0 equals 0. 
# The string can contain any type and number of characters.

def contains_equal_x_and_o_letters(word):
    count_X = 0
    count_O = 0
    for letter in word:
        if letter == 'X': 
            count_X = count_X + 1
        if letter == 'O': 
            count_O = count_O + 1
    return count_X == count_O

# It is common to call 'happy case'
# or 'happy path' to that where the function under
# test returns a positive result for expected or 'good'
# input.
def test_challenge_00_happy_case():
    assert contains_equal_x_and_o_letters('AXAOA') == True

# This is a test for an edge case, if we pass an empty
# string, or a null / None, we verify the function 
# still returns the expected result 
def test_challenge_00_empty_string():
    assert contains_equal_x_and_o_letters('') == True

# Another edge case: non empty string containing
# other characters, and none of the 'expected' ones (X or O)
def test_challenge_00_all_other_characters():
    assert contains_equal_x_and_o_letters('ABCCCD') == True 

# Verify that passing more Xs than Os will return False
def test_challenge_00_uneven():
    assert contains_equal_x_and_o_letters('AXXXCO') == False  

# Verify that passing a string with only Xs will return False
def test_challenge_00_only_x():
    assert contains_equal_x_and_o_letters('AXBC') == False 

# Verify that passing a string with only Os will return False
def test_challenge_00_only_o():
    assert contains_equal_x_and_o_letters('AOBO') == False 

def test_challenge_00_only_num():
    assert contains_equal_x_and_o_letters('12345') == True 
