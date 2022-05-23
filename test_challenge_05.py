# Write a function in Python that accepts a list of 
# any length that contains a mix of non-negative 
# integers and strings. The function should return 
# a list with only the integers in the original 
# list in the same order.

def extract_integers(mixed_list):
    int_list =[]
    for i in mixed_list:
        if type(i) == int:
            int_list.append(i)
    return int_list

    # pass  

def test_challenge_05_happy_case(): 
     assert extract_integers([1, 'apple', 2, 'banana',3, 4]) == [1,2,3,4]   

def test_challenge_05_happy_case2(): 
     assert extract_integers(['pen', 'book', '123', '1', 1, 50, 1234]) == [1, 50, 1234]   