#!/usr/bin/env python
# coding: utf-8

# In[1]:


outfile = open("testfile.txt", "w")
print(outfile)

outfile.write("Mary had a little lamb, \n")
outfile.write("whose fleece was white was snow, \n")
outfile.write("and everywhere that Mary  went, \n")
outfile.write("she was sure to cap some hoes, \n")

outfile.close()


# In[2]:


import numpy as np
X = np.random.rand(5)

mydatafile = open("datafile.txt", "w")

for i in range(5):
    mydatafile.write(str(X[i]) + "\n")
    
mydatafile.close()


# In[3]:


infile = open("testfile.txt", "r")

linetxt = infile.readlines()

print(linetxt)

infile.close()


# In[4]:


infile = open("testfile.txt", "r")

linetxt = infile.readlines()

infile.close()

Nline = len(linetxt)
print("There are", Nline, "lines of text in the file")

for i in range(Nline):
    print(linetxt[i])


# In[6]:


mystring = "Jack and Jill went up a hill"
wordlist = mystring.split(" ")
print(wordlist)

nwords = len(wordlist)
print ("Number of words = ", nwords)

for i in range(nwords):
    print("word", i , "=", wordlist[i])


# In[10]:


mystring = "Mary had  a   little    lamb"
wordstring = mystring.split(' ')
print(wordstring)


# In[13]:


infile = open("datafile.txt", "r")

linetxt = infile.readlines()

infile.close()

Nline = len(linetxt)

for i in range(Nline):
    strlist = linetxt[i].split(",")
    a = int(strlist[0])
    b = float(strlist[1])
    print(a, b)


# In[ ]:




