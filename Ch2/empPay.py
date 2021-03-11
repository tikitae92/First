#get all required input
#first name, last name, hourly wage, hours worked

firstName = input("Enter employee first name: ")
lastName = input("Enter employee last name: ")

#hourlyWage= input("Enter hourly wage: ")
#hourlyWage=float(hourlyWage)

hourlyWage=float(input("Enter hourly wage: "))

#hoursWorked= input("Enter hours worked in a week: ")
#hoursWorked=float(hoursWorked)

hoursWorked=float(input("Enter hours worked in a week: "))

#calcuate weekly pay
weeklyPay=hourlyWage*hoursWorked

#dispaly results
print("---------------------------------")
print("Employee Name:",firstName,lastName)
print("Weekly pay:",weeklyPay)
