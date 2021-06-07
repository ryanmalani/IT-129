#getting file name from user and error checking

fname = input("Enter a file name: ")
key_word = input("Enter the word you would like to search for: ") #getting input for keyword search

try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    exit()
#creating the function

def find_a_word(fname, key_word):
    count = 0 #initializing variable for counting number of times keyword shows up
    for line in fhand:
        found = line.lower().find(key_word)
        if found != -1 and found != 0:
            count = count + 1
    print(key_word, "was found in", fname, count, "times")

find_a_word(fname, key_word)
