string="Woodchuck How much wood would a woodchuck chuck if a woodchuck could chuck wood ?"
# converting the string into lowercase
string=string.lower()
# Whenever we encounter a space, break the string
string=string.split(" ")
# Initializing a dictionary to store the frequency of words
word_frequency={}
for i in string:
     # If the word is already in the keys, increment its frequency
        if i in word_frequency:
            word_frequency[i]+=1
             
    # It means that this is the first occurence of the word
        else:
            word_frequency[i]=1
print(word_frequency)
