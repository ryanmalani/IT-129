#Ryan Malani
try:
    fname = input('Enter file name: ')
    fhand = open(fname)
    readfile = fhand.read()
    words = readfile.split()
    for word in words:
        if words.count(word) == 1:
            uniqueWords = []
            uniqueWords.append(word)
            print(uniqueWords)
except:
    print('Invalid Input for file: ', fname)
