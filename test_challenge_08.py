# Write a program that prints the numbers from 1 to 100. But for multiples of three, print Fizz instead of the number, and multiples of five, print Buzz. For numbers that are multiples of both three and five, print FizzBuzz

# sample output:
# 1, 2, Fizz, 3, 4, Buzz, 5, 6, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz ... and so on ..

def FizzBuzz (n):
  if type(n) != int or n < 0:
    return "invalid"

  list100 = range(1, n)
  new_list = []

  for i in list100:
    if i % 3 == 0 and i % 5 == 0:
      new_list.append('FizzBuzz')
    elif i % 3 == 0:
      new_list.append('Fizz')
    elif i % 5 == 0:
      new_list.append('Buzz')
    else:
      new_list.append(str(i))

  str_list = " ".join(new_list)
  return str_list

def test_challenge_08_happy_case1(): 
     assert FizzBuzz(20) == "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19"

def test_challenge_08_sad_case1(): 
     assert FizzBuzz('20') == "invalid"

def test_challenge_08_sad_case2(): 
     assert FizzBuzz(-2) == "invalid"