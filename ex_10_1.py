#Ryan Malani

import string

fname = input("Enter a file name: ")

try:
    fhand = open(fname)
except:
    print("invalid input for file name: ", fname)
    exit()

countsent = dict() #creating empty dictionary to count # of times an email address shows up in log
desired_word = "From" #setting desired word to search for in text file
for line in fhand: #traversing through opened file
    if not line.startswith(desired_word) or line.startswith(desired_word + ":"): continue #ignoring any words not matching desired word
    if line.startswith(desired_word):
        words = line.split() #creating a list of words in the text file
        sent_from = words[1] #picking day of week from list of words
        if sent_from not in countsent:
            countsent[sent_from] = 1 #adding new keys to the dictionary
        else:
            countsent[sent_from] += 1 #adding 1 to value if the key repeats

most_emails = list()
for key, val in list(countsent.items()):
    most_emails.append((val, key))

most_emails.sort(reverse=True)

print(most_emails[0])
