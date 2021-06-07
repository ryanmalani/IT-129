# Ryan Malani

count = 0
total = 0.0
average = 0.0
list = []
while True:
    inp = input("Enter a number: ")

    if inp.lower() == "done":
        break
    try:
        num = float(inp)
        list.append(num)
    except:
        print("Invalid input")
        continue

    count = count + 1
    total = total + num
    average = total / count

print("Count:", count)
print("Total:", total)
print("Average:", average)
print("Minimum:", min(list))
print("Maximum:", max(list))
