# This program calculates the GPA for a student.

# Define variables.
n=1
totalPoints=0
totalUnits=0

# Obtain a number of courses that the student has taken.
numCourse=int(input("Enter number of courses: "))

# If a user inputs zero or negative numbers,
# print an error message and ask the user for the valid input. 
while numCourse<=0:
        print("Invalid Entry, number of courses must be positive number")
        numCourse=int(input("Enter number of courses: "))

# Obtain the letter grade and the number of credits for each course.
while n<=numCourse:
    print("For course number %s" %n)
    letterGrade=input("Enter letter grade(A,B,C,D, or F): ").upper()

    # When valid letter grade and number of credit are entered,
    # calculate and/or update subTotal, totalPoints and totalUnits
    # until the data for all courses are obtained.
    if letterGrade=="A":
        numCredit=float(input("Enter number of credits: "))
        while numCredit<1 or numCredit>3:
            print("Invalid Entry, a course can have between 1 and 3 credits.")
            numCredit=float(input("Enter number of credits: "))
        subTotal=numCredit*4
        totalPoints=totalPoints+subTotal
        totalUnits=totalUnits+numCredit
        n=n+1
    elif letterGrade=="B":
        numCredit=float(input("Enter number of credits: "))
        while numCredit<1 or numCredit>3:
            print("Invalid Entry, a course can have between 1 and 3 credits.")
            numCredit=float(input("Enter number of credits: "))
        subTotal=numCredit*3
        totalPoints=totalPoints+subTotal
        totalUnits=totalUnits+numCredit
        n=n+1
    elif letterGrade=="C":
        numCredit=float(input("Enter number of credits: "))
        while numCredit<1 or numCredit>3:
            print("Invalid Entry, a course can have between 1 and 3 credits.")
            numCredit=float(input("Enter number of credits: "))
        subTotal=numCredit*2
        totalPoints=totalPoints+subTotal
        totalUnits=totalUnits+numCredit
        n=n+1
    elif letterGrade=="D":
        numCredit=float(input("Enter number of credits: "))
        while numCredit<1 or numCredit>3:
            print("Invalid Entry, a course can have between 1 and 3 credits.")
            numCredit=float(input("Enter number of credits: "))
        subTotal=numCredit*1
        totalPoints=totalPoints+subTotal
        totalUnits=totalUnits+numCredit
        n=n+1
    elif letterGrade=="F":
        numCredit=float(input("Enter number of credits: "))
        while numCredit<1 or numCredit>3:
             print("Invalid Entry, a course can have between 1 and 3 credits.")
             numCredit=float(input("Enter number of credits: "))
        totalUnits=totalUnits+numCredit
        n=n+1

    # If the user inputs invalid entry,
    # print an error message and ask for the valid input.   
    else :
        print("Invalid Entry")

# Compute and print GPA. 
GPA=totalPoints/totalUnits
print("Your GPA is: %.2f" %GPA)
