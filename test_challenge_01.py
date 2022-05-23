# Create a function in Python that accepts a single word and 
# returns the number of vowels in that word. 
# In this function, only a, e, i, o, and u 
# should be counted as vowels — not y.

def count_vowels(word):
    count = 0
    for each_character in word:
        if each_character == 'a' or each_character == 'e' or each_character=='i' or each_character == 'o' or each_character == ' u':
            count += 1
    print(count)
    return count

def test_challenge_01_happy_case1(): 
     assert count_vowels('Kaleidoscope') == 6   

def test_challenge_01_happy_case2(): 
    assert count_vowels('Mississippi') == 4

def test_challenge_01_happy_case3(): 
    assert count_vowels('python') == 1

def test_challenge_01_uppercase_case(): 
    assert count_vowels('FLOWER') == 0

 
#   Add test case