#Ryan Malani

import string

fname = input("Enter file name: ")

try:
    fhand = open(fname)
except:
    print("Invalid input for file name:", fname)
    exit()

ltrs = dict()

for line in fhand:
    line = line.lower()
    line = line.replace(" ", "")
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.digits))
    line = line.translate(line.maketrans('', '', string.punctuation))
    for keys in line:
        ltrs[keys] = ltrs.get(keys, 0) + 1

indltrs = list()
for key, val in list(ltrs.items()):
    indltrs.append((key, val))

indltrs.sort()

for key, val in indltrs:
    print(key, val)

ten = 10

twenty = '20'

print(ten + twenty)
