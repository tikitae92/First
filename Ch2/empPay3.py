#get all required input
#first name, last name, hourly wage, hours worked

firstName = input("Enter employee first name: ") #adam
lastName = input("Enter employee last name: ") 


firstName=firstName.upper()
lastName=lastName.upper()
#hold() #example of a function from life
#car.drive() #example if method

fnLength=len(firstName)
lnLength=len(lastName)
totalLength=fnLength+lnLength
#totalLength=len(firstName)+len(lastName)


#extract initials
firstInitial=firstName[0]
lastInitial=lastName[0]

#find a function that counts chr name, what arguments it need, what does it return

initials=firstInitial+lastInitial
#initials=firstName[0]+lastName[0]

#hourlyWage= input("Enter hourly wage: ")
#hourlyWage=float(hourlyWage)

hourlyWage=float(input("Enter hourly wage: "))

#hoursWorked= input("Enter hours worked in a week: ")
#hoursWorked=float(hoursWorked)

hoursWorked=float(input("Enter hours worked in a week: "))

#blackbox concept

#calcuate weekly pay
weeklyPay=hourlyWage*hoursWorked
weeklyPay=round(weeklyPay,2)


#dispaly results
print("-"*30)
print("Employee Name: %s %s" %(firstName,lastName))
#       MA
#       19
print("Employee Initials: %9s" %initials)
print("Full name length: %10d" %totalLength)
# string=s, float=f, integer=d
print("Weekly pay: $%.2f" %weeklyPay)
















