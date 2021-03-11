#define a function that calculates the volume of a cube
#result=x**3
DECIMAL_PLACES=2
def cubeVol(x):
    result=x**3
    return result
#get side length from user
print("This program calculates the volume of a cube")
side=float(input("Enter length: "))
while side<=0:
    print("Invalid entry, length must be a positive number")
    side=float(input("Enter length: "))
#calculating using the defined function
totalVolume=cubeVol(side)

#print result
print("The volume of the cube is:", round(totalVolume,DECIMAL_PLACES))
