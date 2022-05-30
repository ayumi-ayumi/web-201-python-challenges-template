# Write a function that tests if a number, n, is a prime number 

# sample input: 1
# sample output: false

# sample input: 13
# sample output: true

def prime(num):
  if type(num) != int or num < 0:
    return 'invalid'
  p = 0
  for i in range (1,10):
    if num % i == 0:
      p += 1
  if p > 1 or num == 1:
    # return print("Not a prime number")
    return False
  else:
    # return print('A prime number')
    return True
  
# prime(int(input('number?:')))

def test_challenge_19_happy_case1(): 
     assert prime(1) == False

def test_challenge_19_happy_case2(): 
     assert prime(13) == True

def test_challenge_19_sad_case1(): 
     assert prime("13") == 'invalid'

def test_challenge_19_sad_case2(): 
     assert prime([1]) == 'invalid'

def test_challenge_19_sad_case3(): 
     assert prime(-1) == 'invalid'