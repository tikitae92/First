#if statements/conditions

#ask user to enter passcode and compare to passcode in the DB/file

usernameInput=input("Enter username: ")
passwordInput=input("Enter password: ")

username="user123"
password="abc123"

#condition: does the password match the one in the system?

if passwordInput==password and usernameInput==username:
    #for the condition to be true both username and password have to match
    print("login successful")
#elif userInput!=password:
else:
    print("combination of username and password is incorrect")


    
    
    


