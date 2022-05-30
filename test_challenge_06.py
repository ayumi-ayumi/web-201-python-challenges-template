# Write a function in python that 
# takes an array of numbers and returns a
# sum of the square of all the numbers in the array.

def sum_of_squares(array_of_numbers):
     if type(array_of_numbers) != list:
          return 'Not a list'

     sum_square = 0
     for i in array_of_numbers:
          if type(i) != int or type(i) != float: 
               return 'invalid'
          sum_square += i * i
     return sum_square

    # pass

def test_challenge_06_happy_case(): 
     assert sum_of_squares([1,2,3,4]) == 30

def test_challenge_06_happy_case2(): 
     assert sum_of_squares([0,2,3,4]) == 29

def test_challenge_06_happy_case3(): 
     assert sum_of_squares([3,-4]) == 25
     
def test_challenge_06_happy_case4(): 
     assert sum_of_squares([10,20.0]) == 500.0

def test_challenge_06_happy_case5(): 
     assert sum_of_squares({-1,2}) == "Not a list"

def test_challenge_06_sad_case(): 
     assert sum_of_squares(1) == "Not a list"

def test_challenge_06_sad_case2(): 
     assert sum_of_squares(['banana', 'apple']) == "invalid"