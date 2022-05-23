# Create a Python function that accepts a string. 
# The function should return a string, with each 
# character in the original string doubled. 
# If you send the function "now" as a parameter, 
# it should return "nnooww," and if you send "123a!", 
# it should return "112233aa!!".

def duplicate_characters(str):

     double = [] 
     for i in str:
          double.append(i * 2)
     # print(double)
     return "".join(double)

def test_challenge_02_case_1(): 
     assert duplicate_characters('now') == 'nnooww'

def test_challenge_02_case_2(): 
     assert duplicate_characters('123a!') == '112233aa!!'

def test_challenge_02_case_3(): 
     assert duplicate_characters('ABCDEF') == 'AABBCCDDEEFF'

def test_challenge_02_case_4(): 
     assert duplicate_characters('$#%') == '$$##%%'

     #  def duplicate_characters (s):
     #      return ''.join(a * 2 for a in s)