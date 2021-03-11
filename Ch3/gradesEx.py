#user enters a grade 0-100
#a>=90,b>=80,c>=70,d>=60,f<60, or incorrect (<0 or >100)

grade=float(input("Enter a grade between 0-100: "))

#create variables for letter grades min
min_A=90
min_B=80
min_C=70
min_D=60
min_Grade=0
max_Grade=100


#
if grade<min_Grade or grade>max_Grade:
    print("Invalid grade")
elif grade>=min_A:
    print("Grade is A")
elif grade>=min_B:
    print("Grade is B")
elif grade>=min_C:
    print("Grade is C")
elif grade>=min_D:
    print("Grade is D")
else:
    print("Grade is F")
    
    
    

    
