#python is case sensitive
#math define x=3, y=3, z=x+y
#define my variables and ask user to enter values
studentName=input("Enter student name: ")
GPA=input("Enter GPA:")
yearOfBirth=input("Enter year of birth: ")
#convert year of birth to an integer (because input command always saves data as string)
#int is an integer (1,2,3)
#float is a decimal such as 3.5
yearOfBirth=int(yearOfBirth)

CURRENT_YEAR=2020

#calculate age
Age=CURRENT_YEAR-yearOfBirth

#print output
print("Name:",studentName)
print("GPA:",GPA)
print("Age:",Age)
