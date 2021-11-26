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


# In[ ]:


def get_frequency_dict(sequence):
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


# In[ ]:


def display_hand(hand):
    for letter in hand.keys():
        for j in range(hand[letter]):
            print(letter, end=' ') # print all on the same line
    print() 


# In[ ]:


def deal_hand(n):
    hand={}
    num_vowels = int(math.ceil(n / 3))
    hand['*'] = 1
    for i in range(num_vowels - 1):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    for i in range(num_vowels, n):
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    return hand


# In[ ]:


def update_hand(hand, word):
    hand_new = hand
    for key in word:
        if key in hand:
            if hand_new.get(key) > 0:
                hand_new[key] =  hand_new[key] - 1
            else:
                pass
        else:
            continue
    return hand_new


# In[ ]:


def is_valid_word(word, hand, word_list):
    wildcard_values = ['a', 'e', 'i', 'o', 'u']
    wildcard_attempts = []
    if '*' in hand:
        for i in wildcard_values:
            letter_replace = word.replace('*', i)
            wildcard_attempts.append(letter_replace)
        for i in wildcard_attempts:
            if i in word_list:
                word = i
                return True
            else:
                pass
        
    else:
        if word in word_list:
            counter = 0
            handCopy = hand.copy()
            for i in word:
                if (i in handCopy) and (handCopy[i] > 0):
                    handCopy[i] = handCopy.get(i, 0) - 1
                    counter += 1
                elif (i in VOWELS and "*" in handCopy) and (handCopy['*'] > 0):
                    handCopy['*'] = handCopy.get('*', 0) - 1
                    counter += 1
            if len(word) == counter and word in word_list:
                return True

            else:
                return False
        else:
            return False


# In[ ]:


def get_word_score(word,n):
    """Assumes the word is correct and calculates the score, will need to handle strings with mixed cases"""
    sum1 = 0
    word_low = word.lower()
    length = len(word_low)
    for i in word_low:
        if (i != '*'):
            sum1 += SCRABBLE_LETTER_VALUES[i]
        else:
            sum1 += 0
    sum2 = max(1,(7*length-3*(n-length)))
    return sum1 * sum2


# In[ ]:


def calculate_handlen(hand):
    hand_length = sum(hand.values())
    return hand_length


# In[ ]:


def play_hand(hand, wordlist):
    score = 0
    new_hand = hand.copy()
    while calculate_handlen(new_hand) > 0:
        display_hand(new_hand)
        word_input = input("Please enter word. If you would like to quit, enter !!: ")
        if word_input == "!!":
            print("Game over, man. Hand score:", score)
            break
        else:
            if is_valid_word(word_input, new_hand, wordlist) == True:
                update_hand(new_hand, word_input)
                score += get_word_score(word_input, calculate_handlen(new_hand))
                print("Points earned:", score)
            else:
                new_hand = update_hand(new_hand, word_input)
                print("Word is not valid, try again.")
    else:
        print("Game over, man. Hand score:", score)
    return score


# In[ ]:


def substitute_hand(hand, letter):
    import random
    tot_letters = VOWELS + CONSONANTS
    rand_letter = random.choice(tot_letters)
    while rand_letter in hand:
        rand_letter = random.choice(tot_letters) 
    else:
        if letter in hand:
            hand[rand_letter] = hand.pop(letter)
        else:
            pass
    return(hand)


# In[ ]:


def play_game(word_list):
    score = 0
    total_score = 0
    sub_count = 1
    replay_count = 1
    input_hands_count = eval(input("Please enter how many hands you would like to play as an integer: "))
    hand_length = eval(input("Please enter how many letters you would like in a hand as an integer: "))
    while input_hands_count > 0:
        hand = deal_hand(hand_length)
        dummy_hand = hand.copy()
        display_hand(dummy_hand)
        if sub_count == 1 and replay_count == 1:
            input_sub = input("Would you like to substitute a letter in the current hand? This can only be done once per game. If so, input 'y'/'n': ")
            if input_sub == 'y':
                display_hand(dummy_hand)
                sub_pref = input("Please choose letter in hand to be replaced: ")
                sub_hand = substitute_hand(dummy_hand, sub_pref)
                dummy_sub_hand = sub_hand.copy()
                sub_count = sub_count - 1
                hand_value = play_hand(dummy_sub_hand, wordlist)
                replay_input = input("Would you like to replay this hand? Enter either y/n: ")
                if replay_input == 'y':
                    score += max(hand_value, play_hand(sub_hand, wordlist))
                    total_score += score
                    replay_count -= 1
                    print("Total score:", score)
                elif replay_input == 'n':
                    score += hand_value
                    total_score += score
                    print("Total score:", score)
            elif input_sub == 'n':
                hand_value = play_hand(dummy_hand, wordlist)
                replay_input = input("Would you like to replay this hand? Enter either y/n: ")
                if replay_input == 'y':
                    score += max(hand_value, play_hand(hand, wordlist))
                    total_score += score
                    replay_count -= 1
                    print("Total score:", score)
                elif replay_input == 'n':
                    score += hand_value
                    total_score += score
                    print("Total score:", score)                
        elif sub_count == 0 and replay_count == 1:
            print("All substitutions have been used up this game.")
            hand_value = play_hand(dummy_hand, wordlist)
            replay_input = input("Would you like to replay this hand? Enter either y/n: ")
            if replay_input == 'y':
                score += max(hand_value, play_hand(hand, wordlist))
                total_score += score
                replay_count -= 1
                print("Total score:", score)
            elif replay_input == 'n':
                score += hand_value
                total_score += score
                print("Total score:", score)
        elif sub_count == 1 and replay_count == 0:
            print("All replays have been used up this game")
            input_sub = input("Would you like to substitute a letter in the current hand? This can only be done once per game. If so, input 'y'/'n': ")
            if input_sub == 'y':
                display_hand(dummy_hand)
                sub_pref = input("Please choose letter in hand to be replaced: ")
                substitute_hand(dummy_hand, sub_pref)
                sub_count = sub_count - 1
                hand_value = play_hand(dummy_hand, wordlist)
                score += hand_value
                total_score += score
                print("Total score:", score)
            elif input_sub == 'n':
                hand_value = play_hand(dummy_hand, wordlist)
                score += hand_value
                total_score += score
                print("Total score:", score)
        elif sub_count == 0 and replay_count == 0:
            print("All substitutions and replays have been used up this game.")
            hand_value = play_hand(dummy_hand, wordlist)
            score += hand_value
            total_score += score
            print("Total score:", score)
        input_hands_count = input_hands_count - 1
    else:
        print("Series complete! Total score: ", score)

