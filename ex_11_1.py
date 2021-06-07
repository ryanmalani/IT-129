#Ryan Malani

import re

fname = input("Enter file name: ")

try:
    fhand = open(fname)
except:
    print("Invalid input for file name:", fname)
    exit()

numlist = list()

for line in fhand:
    line = line.rstrip()
    lst = re.findall(' Revision: ([0-9.]+)', line)
    if len(lst) != 1 :  continue
    num = float(lst[0])
    numlist.append(num)

avg = sum(numlist)/len(numlist)
print(avg)
