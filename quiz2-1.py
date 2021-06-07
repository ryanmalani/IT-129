fhand = open("therepublic.txt")
count = 0

def find_a_word(fname, key_word):
    for line in fhand:
        if line.lower().startswith(key_word):
            count = count + 1
    return count

find_a_word("therepublic.txt", "plato")

print(key_word + " showed up " + str(count) + " times in " + fname)
