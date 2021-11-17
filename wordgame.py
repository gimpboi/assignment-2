#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import random
import string
VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7
SCRABBLE_LETTER_VALUES = {
'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j':
8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't'
: 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

WORDLIST_FILENAME = "words.txt"
def load_words():
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print(" ", len(wordlist), "words loaded.")
    return wordlist


# In[2]:


load_words()

def get_word_score(word,n):
    """Assumes the word is correct and calculates the score, will need to handle strings with mixed cases"""
    sum1 = 0
    word_low = word.lower()
    length = len(word_low)
    for i in word_low:
        sum1 += SCRABBLE_LETTER_VALUES[i]
    sum2 = max(1,(7*length-3*(n-length)))
    return sum1 * sum2

def get_frequency_dict(sequence):
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


# In[3]:


def display_hand(hand):
    for letter in hand.keys():
        for j in range(hand[letter]):
            print(letter, end=' ') # print all on the same line
    print() 

def deal_hand(n):
    hand={}
    num_vowels = int(math.ceil(n / 3))
    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    for i in range(num_vowels, n):
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    return hand


def update_hand(hand, word):
    hand_new = hand
    for key in word:
        if key in hand:
            if hand_new.get(key) > 0:
                hand_new[key] =  hand_new[key] - 1
            else:
                hand_new[key] = 0
        else:
            continue
    return hand_new

def is_valid_word(word, hand, word_list):
    if word in word_list:
        counter = 0
        for i in word:
            if (i in hand) and (hand[i] > 0):
                hand[i] = hand.get(i, 0) - 1
                counter += 1
            elif (i in VOWELS and "*" in hand) and (hand['*'] > 0):
                hand['*'] = hand.get('*', 0) - 1
                counter += 1
        if len(word) == counter:
            return True

        else:
            return False
    else:
        return False

def play_hand(hand, wordlist):
    score = 0
    letter_total = sum(hand.values())
    while letter_total > 0:
        display_hand(hand)
        word_input = input("Would you like to quit? If so, input two !!, otherwise enter word: ")
        if word_input == "!!":
            print("Game over, man. Total score:", score)
            break
        else:
            if is_valid_word(word_input, hand, wordlist) == True:
                hand = update_hand(hand, word_input)
                score += get_word_score(word_input, letter_total)
                print("Points earned:", score)
            else:
                print("Word is not valid, try again.")
    else:
        print("Game over. Total score:", score)

