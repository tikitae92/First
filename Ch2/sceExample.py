#SCE example
#customers enter name, acct number, and bill amount
#use template and specifiers to print

custName=input("Enter customer name: ")
acctNumber=input("Enter %s account number: " %custName)
billAmount=float(input("Enter bill amount: $"))

emailTemplate="""Dear %s,

You current bill for SCE customer account number %s is

Available now for viewing. Total due: $%.2f

"""

print()

print(emailTemplate %(custName,acctNumber,billAmount))
