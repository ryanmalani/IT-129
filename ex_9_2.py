#Ryan Malani

fname = input("Enter a file name: ")

try:
    fhand = open(fname)
except:
    print("invalid input for file name: ", fname)
    exit()

countdays = dict() #creating empty dictionary to count # of times an email comes in a day
desired_word = "From" #setting desired word to search for in text file
for line in fhand: #traversing through opened file
    if not line.startswith(desired_word) or line.startswith(desired_word + ":"): continue #ignoring any words not matching desired word
    if line.startswith(desired_word):
        words = line.split() #creating a list of words in the text file
        day_sent = words[2] #picking day of week from list of words
        if day_sent not in countdays:
            countdays[day_sent] = 1
        else:
            countdays[day_sent] += 1

print(countdays)
