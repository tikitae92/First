#write a program that asks the user to enter their review/comments
#then calculates the number of chr and print
#max=50 chr

MAX_LENGTH=250

reviewLength=len(input("Please leave your review: "))
chrRemaining=MAX_LENGTH-reviewLength
print("Length of review:",reviewLength)
print("# Chr remaining:", chrRemaining)
