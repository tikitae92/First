#example of sale transaction in a store
#cashier doesnt know the # of items in a cart
#input price
#add to total and display in the while loop
#starts sale transaction and ends it when no items are left
#keep track of # of items in customer shopping cart
#print total # of items
#stop when user enter -1
#if negative (<-1) ask user to try again
#utilize list
price=0
total=0
i=1
itemPrices=[]
#one while loop
SENT_VALUE=-1
MIN_PRICE=0
#sentinel (in this example negative number will stop loop)
while price !=SENT_VALUE:
    #display item number
    price=float(input("Enter price for item #%d (enter %d to stop): " %(i,SENT_VALUE)))
    #one method of ending the loop
    #if price<0:
    #    print("End of sale transaction")
    #    break
    if price >=MIN_PRICE:
        i=i+1
        itemPrices.append(price)
        total=sum(itemPrices)
        print("Total is $%.2f" %total)
    elif price==SENT_VALUE:
        i=len(itemPrices)
        minPrice=min(itemPrices)
        maxPrice=max(itemPrices)
        print("-"*50)
        print("Number of items:", i)
        print("Total is $%.2f" %total)
        print("Cheapest item is:", minPrice)
        print("Most expensive item is:", maxPrice)
        
        break
    else:
        print("Invalid entry, please try again")




    







