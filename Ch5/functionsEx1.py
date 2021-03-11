#examples of built-in functions we have used

#print
#grade=input()
#grade=round(54.3333,2)
#grade=float("54.3333")
#nstdt=int("3")

#add 2 numbers
#define my own function for adding two numbers
#goal: add 2 numbers
#return: the total of the 2 numbers
#name it: add2num
#arguments: 2 arguments (the 2 numbers)
def add2num(n1,n2):
    result=n1+n2
    return result

#define a function to get difference (n1-n2)
def sub2num(n1,n2):
    result=n1-n2
    return result

num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))
total=add2num(num1,num2)
diff_result=sub2num(num1,num2)
print("%.2f + %.2f = %.2f" %(num1,num2,total))
print("%.2f - %.2f = %.2f" %(num1,num2,diff_result))

















 



