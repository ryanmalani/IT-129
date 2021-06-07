#Ryan Malani

fname = input("Enter a file name: ")

try:
    fhand = open(fname)
except:
    print("invalid input for file name: ", fname)
    exit()

counthours = dict() #creating empty dictionary to count # of times an email address shows up in log
desired_word = "From" #setting desired word to search for in text file
for line in fhand: #traversing through opened file
    if not line.startswith(desired_word) or line.startswith(desired_word + ":"): continue #ignoring any words not matching desired word
    if line.startswith(desired_word):
        words = line.replace(" ", ":").split(":") #creating a list of words in the text file
        hour = words[6] #picking hour from list of words
        if hour not in counthours:
            counthours[hour] = 1 #adding new keys to the dictionary
        else:
            counthours[hour] += 1 #adding 1 to value if the key repeats

hourslist = list()

for val, key in list(counthours.items()):
    hourslist.append((val, key))

hourslist.sort()

for key, val in hourslist[:]:
    print(key, val)
