# Write a function in python that 
# takes an array of numbers and returns a
# sum of the square of all the numbers in the array.

def sum_of_squares(array_of_numbers):
     sum_square = 0
     for i in array_of_numbers:
          if not isinstance(i, int):
               return 'invalid'
          sum_square += i * i
     return sum_square

    # pass

def test_challenge_06_happy_case(): 
     assert sum_of_squares([1,2,3,4]) == 30

def test_challenge_06_happy_case2(): 
     assert sum_of_squares([0,2,3,4]) == 29

def test_challenge_06_happy_case3(): 
     assert sum_of_squares([3,4]) == 25
     
def test_challenge_06_happy_case4(): 
     assert sum_of_squares([10,20]) == 500

def test_challenge_06_happy_case5(): 
     assert sum_of_squares([-1,2]) == 5

def test_challenge_06_happy_case5(): 
     assert sum_of_squares(['apple',2]) == "invalid"