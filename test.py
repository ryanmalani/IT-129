def digits(fname):
    digi_list = list()
    with open(fname, 'r') as fhand:
        for line in fhand:
            line = line.strip()
            digi_list.append(line)
            separator = ""
            digi_string = separator.join(digi_list)
        desired_num = input("Please enter a 7 digit number: ")
        found = digi_string.find(desired_num)
        if found == -1:
            print("That number is not in the larger number!")
        else:
            print("That number is in the larger number!")

digits("digits.txt")

#with open('t.txt') as f:
# s = " ".join([l.rstrip() for l in f])

def tickets(num):
    total = 0.0
    tickets_purchased = num
    while num > 0:
        age = input("Please enter the age of ticket holder: ")
        age = int(age)
        if age <= 5:
            total += .50
        elif age <= 13 and age > 5:
            total += 1.00
        elif age < 18 and age > 13:
            total += 1.50
        elif age >= 18:
            total += 2.75
        num -= 1

    total = "${:,.2f}".format(total)

    print("You purchased", tickets_purchased, "tickets for a total of",total)

tickets(5)
