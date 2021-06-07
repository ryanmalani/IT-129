#Ryan Malani

score = input("Enter Score: ")

def computegrade(score):
    try:
        if float(score) < 1.0 and float(score) >= 0.9:
            grade = "A"
        elif float(score) < 0.9 and float(score) >= 0.8:
            grade = "B"
        elif float(score) < 0.8 and float(score) >= 0.7:
            grade = "C"
        elif float(score) < 0.7 and float(score) >= 0.6:
            grade = "D"
        elif float(score) < 0.6 and float(score) >= 0:
            grade = "F"
        return grade
    except:
        print("Bad score")

print(computegrade(score))
