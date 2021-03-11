#example of sale transaction in a store
#cashier doesnt know the # of items in a cart
#input price
#add to total and display in the while loop
#starts sale transaction and ends it when no items are left
#keep track of # of items in customer shopping cart
#print total # of items

price=0
total=0
i=1

#sentinel (in this example negative number will stop loop)
while price >=0:
    #display item number
    price=float(input("Enter price for item #%d (enter -1 to stop): " %i))
    #one method of ending the loop
    #if price<0:
    #    print("End of sale transaction")
    #    break
    if price >=0:
        i=i+1
        total=total+price
        print("Total is $%.2f" %total)
i=i-1
print("Number of items:", i)
print("Total is $%.2f" %total)




    







