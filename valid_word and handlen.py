#!/usr/bin/env python
# coding: utf-8

# In[8]:


VOWELS = 'aeiou'

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


def calculate_handlen(hand):
    return len(hand)


# In[ ]:





# In[ ]:




