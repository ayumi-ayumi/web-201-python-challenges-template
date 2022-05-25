# Create a function in Python that accepts a single word and 
# returns the number of vowels in that word. 
# In this function, only a, e, i, o, and u 
# should be counted as vowels — not y.

def count_vowels(word):
    lower_word = word.lower()
    count = 0
    for each_character in lower_word:
        if each_character == 'a' or each_character == 'e' or each_character=='i' or each_character == 'o' or each_character == ' u':
            count += 1
    print(count)
    return count

def test_challenge_01_happy_case1(): 
     assert count_vowels('Kaleidoscope') == 6   

def test_challenge_01_upper_case(): 
    assert count_vowels('MISSISSIPPI') == 4

def test_challenge_01_withNum_case(): 
    assert count_vowels('python123') == 1

def test_challenge_01_mixed_upper_lower_case(): 
    assert count_vowels('FLOWERooo') == 5


 
#   Add test case