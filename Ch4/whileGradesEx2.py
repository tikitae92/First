#write a program that asks the instructor for the num of stds
#ask instructor to enter grade for each student
#calculate and print avg grade
#print the highest grade
#print the lowest grade

nstds=int(input("Enter number of students in class: "))

while nstds<=0:
    print("Invalid number of students")
    nstds=int(input("Enter number of students in class: "))

MAX_GRADE=100
MIN_GRADE=0
DECIMAL_PLACES=2

#for highest grade
#you only need to remember the highest
#compare current entry with highest
highest_grade=MIN_GRADE
lowest_grade=MAX_GRADE
n=1
totalGrades=0
while n<=nstds:
    grade=float(input("Enter grade (%d-%d) for student %d: " %(MIN_GRADE,MAX_GRADE,n)))
    while grade<MIN_GRADE or grade>MAX_GRADE:
        print("Invalid entry")
        grade=float(input("Enter grade (%d-%d) for student %d: " %(MIN_GRADE,MAX_GRADE,n)))
    totalGrades=totalGrades+grade
    #keep track of highest grade
    if grade>highest_grade:
        highest_grade=grade
    if grade<lowest_grade:
        lowest_grade=grade
    n=n+1
    
avg=totalGrades/nstds
#print avg, lowest, and highest grade
print("Average grade:", round(avg,DECIMAL_PLACES))
print("Highest grade:", highest_grade)
print("Lowest grade:", lowest_grade)














