#write a simple calculator program
#define 4 functions: add2num, sub2num, multiply2num, div2num
#ask user to input 2 numbers
#ask user to choose arthmetic operation
#call the appropriate function
#display the result

def add2num(n1,n2):
    result=n1+n2
    return result

def sub2num(n1,n2):
    result=n1-n2
    return result

def mult2num(n1,n2):
    result=n1*n2
    return result

def div2num(n1,n2):
    result=n1/n2
    return result

def main():
    n1=float(input("Enter first number: "))
    n2=float(input("Enter second number: "))
    arthmetic_op=input("Choose operation(+, -, *, or /) :")
    #check for invalid operation
    while arthmetic_op!="+" and arthmetic_op!="-" and arthmetic_op!="*" and arthmetic_op!="/":
        print("Invalid operation, please try again")
        arthmetic_op=input("Choose operation(+, -, *, or /) :")

    if arthmetic_op=="+":
        result=add2num(n1,n2)
    elif arthmetic_op=="-":
        result=sub2num(n1,n2)
    elif arthmetic_op=="*":
        result=mult2num(n1,n2)
    elif arthmetic_op=="/":
        result=div2num(n1,n2)
    #5+5=10
    #5*5=25

    print ("%.2f %s %.2f = %.2f " %(n1,arthmetic_op,n2,result))

main()








