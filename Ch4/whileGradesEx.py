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

n=1
totalGrades=0
while n<=nstds:
    grade=float(input("Enter grade (%d-%d) for student %d: " %(MIN_GRADE,MAX_GRADE,n)))
    while grade<MIN_GRADE or grade>MAX_GRADE:
        print("Invalid entry")
        grade=float(input("Enter grade (%d-%d) for student %d: " %(MIN_GRADE,MAX_GRADE,n)))
    totalGrades=totalGrades+grade

    n=n+1
    
avg=totalGrades/nstds
#print avg, lowest, and highest grade
print("Average grade:", round(avg,DECIMAL_PLACES))















