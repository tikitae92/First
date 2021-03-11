#write a program that requests users to enter their email address
#and create a username and password
    #criteria
        #username length >=8
        #password length >=8

        #email address must contain @ and .edu
username_length=8
password_length=8
check1="@"
check2=".edu"
username=input("Enter username(at least %d chr): " %username_length)
password=input("Enter password(at least %d chr): " %password_length)
email_address=input("Enter email address: ")
#username is <min
#password is <min
#username and password <min


decision_check2=email_address.endswith(".edu")



if len(username)>=username_length and len(password)>=password_length and check1 in email_address and decision_check2==True:
    print("Account created")
else:
    if len(username)<username_length:
        print("username need to be at least %d chr in length" %username_length)
    if len(password)<password_length:
        print("password need to be at least %d chr in length" %password_length)
    if check1 not in email_address:
        print("Email must contain %s" %check1)
    if decision_check2==False:
        print("Email address must end with %s" %check2)










    




































