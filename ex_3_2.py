#Ryan Malani

hours = input("Enter Hours: ")
rate = input("Enter Rate: ")
try:
    if float(hours) > 40:
        otrate = float(rate) * 1.5
        pay = (40 * float(rate)) + ((float(hours) - 40) * otrate)
    else:
        pay = float(hours) * float(rate)
    print("Pay:", pay)
except:
    print("Error, please enter numeric input")
