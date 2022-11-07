# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random

guesses_left = 9

words = ['santa','gifts','sugar', 'angel','snowflake','star','reigndeer','cookie','tree', 'candle']

secret_word = random.choice(words)

clue = list('?' * len(secret_word))

symbol = "🎄"

guessed_word_correctly = False

def update_clue(guessed_letter, secret_word):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
        index = index + 1
    
def listToString(mylist):
    cluestring = ' '
    return cluestring.join(mylist)

print("Guess the word associated with winter holidays! ")

while guesses_left > 0:
    print(listToString(clue))
    print("Guesses left: " + symbol * guesses_left)
    guess = input("Guess a letter or the whole word: ")
    if guess == secret_word:
        guessed_word_correctly = True
        break
    
    if guess in secret_word:
        update_clue(guess, secret_word)
        
    else:
        print('Incorrect. You lose a life!')
        guesses_left = guesses_left - 1

if guessed_word_correctly:
    print("You win!  The secret word was " + secret_word)
else:
    print("You lose! Womp, womp.  The secret word was " + secret_word)



