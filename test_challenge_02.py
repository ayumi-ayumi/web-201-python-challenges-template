# Create a Python function that accepts a string. 
# The function should return a string, with each 
# character in the original string doubled. 
# If you send the function "now" as a parameter, 
# it should return "nnooww," and if you send "123a!", 
# it should return "112233aa!!".

from ast import Str


def duplicate_characters(string):
     if type(string) != str:
          return False
     double = [] 
     for i in string:
          double.append(i * 2)
     return "".join(double)

def test_challenge_02_case_1(): 
     assert duplicate_characters('now') == 'nnooww'

def test_challenge_02_case_2(): 
     assert duplicate_characters('123a!') == '112233aa!!'

def test_challenge_02_upper_case(): 
     assert duplicate_characters('ABCDEF') == 'AABBCCDDEEFF'

def test_challenge_02_non_str_case(): 
     assert duplicate_characters('$#%') == '$$##%%'

def test_challenge_02_sad_case(): 
     assert duplicate_characters(1234) == False

     #  def duplicate_characters (s):
     #      return ''.join(a * 2 for a in s)