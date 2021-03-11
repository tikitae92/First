
#ask user to enter the inputs

studentName=input("Enter student name: ")
GPA=float(input("Enter student GPA: "))

SEMESTER="Fall"
YEAR=2020

emailTemplate="""Dear %s,

Your current GPA for the %s %d is %.2f.

CSULB Admission

"""

print(emailTemplate %(studentName,SEMESTER,YEAR,GPA))
