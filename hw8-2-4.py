# Author: ATN 12/9/21

def letter_counter(word, letter):

    instances = 0 
    for position in list(word):
        if(position == letter):
            instances += 1
        else:
            continue
    return instances


print(letter_counter("cat", "t") == 1)
print(letter_counter("apple", "p") == 2)
print(letter_counter("supercalifragilisticexpialidocious", "i") == 7)
