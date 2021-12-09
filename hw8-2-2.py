# Author: ATN 12/9/21

def sum_odds(odds):
    numbers = 0
    for number in odds:
        if((number % 2) == 0):
            continue
        else:
            numbers += number
    return(numbers)

sum_odds([1, 2, 3, 4, 5, 6]) == 9
sum_odds([1, 3, 5, 7, 9]) == 25
sum_odds([2, 4, 6, 8, 10]) == 0
