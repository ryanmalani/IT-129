#Ryan Malani

count = 0
desired_word = "From"
for line in open("mailboxdata.txt"):
    if not line.startswith(desired_word) or line.startswith(desired_word + ":"): continue
    if line.startswith(desired_word):
        words = line.split()
        sent = words[1]
        fromcount = []
        fromcount.append(sent)
        print(fromcount)
        count += 1
print("There were", count, "lines in the file with", desired_word, "as the first word")
