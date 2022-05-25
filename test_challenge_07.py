# Supermarket billing: Write a function in python that 
# takes a shopping list (dictionary of items and price) and returns the total.
# extension: apply discount accordingly:
# if total is greater than 50 Euros 5% discount.
# if total is greater than 60 Euros 6% discount.
# if total is greater than 70 Euros 7% discount and so on.

def calculate_bill(shopping_list):
    prices = shopping_list.values()

    sum = 0
    for price in prices:
        sum += price 
    sum_str = str(sum)
    first_num = sum_str[0]
    first_second_num = sum_str[0] + sum_str[1]

    if sum > 50:

        if sum > 300:
          return sum * 0.7

        elif sum <= 100:
            if str(sum) == first_num + '0':
                discount = float('0.0' + str(int(first_num) - 1))
                return round(sum * (1 - discount), 2)
            else: 
                discount = float('0.0' + str(int(first_num)))
                return round(sum * (1 - discount), 2)


        else: 
            if str(sum) == first_second_num + '0':
                discount = float('0.' + str(int(first_second_num) - 1))
                return round(sum * (1 - discount), 2)
            else: 
                discount = float('0.' + str(int(first_second_num)))
                return round(sum * (1 - discount), 2)

    else:
        return round(sum, 2)


    # if sum > 70:
    #     return round(sum * 0.93, 2)
    # elif sum > 60:
    #     return round(sum * 0.94, 2)
    # elif sum > 50:
    #     return round(sum * 0.95, 2)
    # else:
    #     return round(sum, 2)

    # pass

def test_challenge_07_happy_case1(): # sum:43.4
    shopping_list = {'apples':11.20, 'bananas':2.2, 'eggs':30.00}
    assert calculate_bill(shopping_list) == 43.4

def test_challenge_07_happy_case2(): # sum:54.7
    shopping_list = {'apples':10.20, 'bananas':22, 'eggs':22.50}
    assert calculate_bill(shopping_list) == 51.97

def test_challenge_07_happy_case3(): # sum:101
    shopping_list = {'apples':30, 'bananas':50, 'eggs':21}
    assert calculate_bill(shopping_list) == 90.9

def test_challenge_07_happy_case4(): # sum:200
    shopping_list = {'apples':100, 'bananas':50, 'eggs':50}
    assert calculate_bill(shopping_list) == 162

def test_challenge_07_happy_case5(): # sum:301
    shopping_list = {'apples':100, 'bananas':200, 'eggs':1}
    assert calculate_bill(shopping_list) == 210.7

    #sad case >> price is negative or str