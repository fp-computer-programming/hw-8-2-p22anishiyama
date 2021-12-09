# Author: ATN 12/9/21

def count_odds(odds):
    numbers = 0
    for number in odds:
        if((number % 2) == 0):
            continue
        else:
            numbers += 1
    return(numbers)

print(count_odds([1, 2, 3, 4, 5, 6]) == 3)
print(count_odds([1, 3, 5, 7, 9]) == 5)
print(count_odds([2, 4, 6, 8, 10]) == 0)
