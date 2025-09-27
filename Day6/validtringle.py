#10/09/25
#Given 3 angles of a triange check if it is a valid triangle

x=int(input("Enter the angle1"))
y=int(input("Enter the angle2"))
z=int(input("Enter the angle3"))
if(x+y+z==180):
    print("Valid triangle")

else:
    print("Invalid Triangle")