# It takes 21 seconds to wash your hands 
# and help prevent the spread of COVID-19.
#
# Create a function that takes the number of times 
# a person washes their hands per day (n) 
# and the number of months (m) they follow this routine, 
# and calculates the duration in minutes and seconds 
# that person spends washing their hands.
#
# Examples:
# wash_hands(8, 7) ➞ "588 minutes and 0 seconds"
# wash_hands(0, 0) ➞ "0 minutes and 0 seconds"
# wash_hands(7, 9) ➞ "661 minutes and 30 seconds"
# 
# Notes: Consider a month has 30 days.

def wash_hands(n, m):
    if type(n) != int or type(m) != int:
        return 'False'

    elif n < 0 or m < 0:
        return 'False'
        
    else:
        # times_perday = n
        # months = m
        onceSeconds = 21
        totalSecondas = n * onceSeconds * m * 30
        mins = totalSecondas // 60
        seconds = totalSecondas % 60
        return (str(mins) + ' minutes and ' + str(seconds) + ' seconds')

def test_challenge_03_case_1(): 
    assert wash_hands(8, 7) == '588 minutes and 0 seconds'
    
def test_challenge_03_case_2(): 
    assert wash_hands(0, 0) == '0 minutes and 0 seconds'

def test_challenge_03_case_3(): 
    assert wash_hands(7, 9) == '661 minutes and 30 seconds'

def test_challenge_03_case_4(): 
    assert wash_hands(7, -9) == 'False'

def test_challenge_03_case_5(): 
    assert wash_hands(7, 'you') == 'False'

def test_challenge_03_case_6(): 
    assert wash_hands('you', 7) == 'False'