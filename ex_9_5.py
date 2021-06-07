#Ryan Malani

from operator import itemgetter

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
        words = line.replace(" ", "@").split("@") #creating a list of words in the text file
        # words = line.split("@")
        sent_from = words[2] #picking day of week from list of words
        if sent_from not in countsent:
            countsent[sent_from] = 1 #adding new keys to the dictionary
        else:
            countsent[sent_from] += 1 #adding 1 to value if the key repeats

print(countsent)
