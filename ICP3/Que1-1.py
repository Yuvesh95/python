#icp-3

""" Que-1 Part-1"""

def wordListToFreqDict(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    return dict(zip(wordlist,wordfreq))
"""
zip() means can be built-in iterables (like: list, string, dict), or user-defined iterables
where dict defines the dictionary output files
"""
# here we take the input from the user
sen=input("enter your sentence")
#used for spliting the sentence into words
words2 = sen.split()
words2.sort() # here we are sorting the sentence into alphabical order and the counting the frequency
print(wordListToFreqDict(words2))