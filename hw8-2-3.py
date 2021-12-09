# Author: ATN 12/9/21

def three_letter_words(words):
    counter = 0
    for word in words:
        if(len(word) == 3):
            counter += 1
        else:
            continue
    return counter

print(three_letter_words(["cat", "bat", "apple"]) == 2)
print(three_letter_words(["apple", "hippo", "mouse"]) == 0)
print(three_letter_words(["hop", "pop", "bop"]) == 3)