#create a function that transforms all items in a list to upper case
def upperList(myList):
    #get every item, change it to upper case and replace old value
    #return the new list with all upper case items
    for i in range (0,len(myList)):
        
        myList[i]=myList[i].upper()
        #print(myList[i])
    return myList
