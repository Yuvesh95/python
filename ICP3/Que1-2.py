#icp-3

""" Que-1 Part-2"""


vowels = {'a', 'e', 'i', 'o', 'u'}# list which says the vowels

# Getting Input from the User
sentence = input('Please enter your sentence to get vowels count: ')
sentence.lower()
# it makes the sentence sutiable for vowels list as it is in lower case
Count = 0

dictionary = {}

for word in sentence:
#for all words in sentences
    if word in vowels:


        if word not in dictionary:
            dictionary[word] = 1
            Count = Count + 1
#if the word is already in vowels list then it will count as word

print("Vowels count  --> ", Count)
