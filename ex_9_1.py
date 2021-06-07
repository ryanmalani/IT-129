#Ryan Malani

fname = open('words.txt')
output = dict()
for line in fname:
    for word in line.split():
           if word not in output.keys():
               output[word] = 0
           else:
               output[word] += 1

print(output)

ans = 'data' in output
print(ans)
