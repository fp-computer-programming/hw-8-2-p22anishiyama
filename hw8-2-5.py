# Author: ATN 12/9/21

def sum_odds_exclusive(numbers):
    sum = 0
    for number in numbers:
        if(number % 2 == 0):
            sum += number
            continue
        else:
            break
    return sum

print(sum_odds_exclusive([2, 4, 6, 8, 9]) == 20)
print(sum_odds_exclusive([13, 12, 10]) == 0)
print(sum_odds_exclusive([14, 16, 32]) == 62)
