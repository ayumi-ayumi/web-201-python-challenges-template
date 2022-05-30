# Write a function that will find the nth number (n is input parameter) in the Fibonacci Sequence. The fibonacci sequence is :
# 0, 1, 1, 2, 3, 5, 8, 13 ... 
# The pattern is: it starts with 0 and 1 and then generates the consequtive number as the sum of previous two numbers. 

# sample input: 3 (index: input - 1)
# sample output: 1

# sample input: 5
# sample output: 3

def fibo(num):
  if type(num) != int or num <= 0:
    return 'invalid'
  else:
    fibo_list = [0, 1]
    a = 0
    b = 1 
    for i in range(num-1):
      c = a + b
      a = b
      b = c
      fibo_list.append(c)
    return fibo_list[num-1]

# fibo(int(input('nth number?')))

def test_challenge_09_happy_case1(): 
     assert fibo(3) == 1

def test_challenge_09_happy_case2(): 
     assert fibo(5) == 3
     
def test_challenge_09_sad_case1(): 
     assert fibo(-2) == 'invalid'

def test_challenge_09_sad_case2(): 
     assert fibo("-2") == 'invalid'

def test_challenge_09_sad_case3(): 
     assert fibo([1]) == 'invalid'