#Ryan Malani

def chop(t):
    del t[0]
    del t[-1]

def middle(t):
    return t[1:len(t)-1]

numlist = [1, 3, 4, 5, 6, 7]

chop(numlist)
newlist = middle(numlist)

print(numlist)
print(newlist)
