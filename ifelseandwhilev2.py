# Written by: Ellyn Hindle
# File name: ifelseandwhile.ipynb
# Program will accept student last name, first name, and GPA.
# Then, program will output whether the student made the honor roll or dean's list.
# Terminates upon entering "ZZZ". No input validation.
studLName = ""
while studLName != "ZZZ":
    studLName = input("What is the student's last name? Type ZZZ to quit.")
    if studLName == "ZZZ":
        print("Terminating input.")
        break
    else:
        studFName = input("What is the student's first name?")
        studGPA = float(input("What is the student's GPA? (written in this format: 0.00)"))
        if studGPA >= 3.5:
            print(studFName, studLName, "has made the Dean's List!" )
        elif studGPA >= 3.25:
            print(studFName, studLName, "has made the Honor Roll!" )
        else:
            print(studFName, studLName, "has a GPA of", studGPA)
    
    