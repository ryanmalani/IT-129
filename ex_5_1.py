# Ryan Malani

count = 0
total = 0.0
average = 0.0
while True:
    inp = input("Enter a number: ")

    if inp.lower() == "done":
        break
    try:
        num = float(inp)
    except:
        print("Invalid input")
        continue

    count = count + 1
    total = total + num
    average = total / count

print("Count:", count)
print("Total:", total)
print("Average:", average)
