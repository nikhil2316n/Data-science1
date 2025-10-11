#09/09/25  HomeWork
#d1(2,3) d2(8,11) p(1,2)
#d1(x1,y1) d2(x2,y2)
import math
def dist(x1,x2,y1,y2):
    a=(x2-x1)**2
    b=(y2-y1)**2
    result=math.sqrt(a+b)
    return result
x1=int(input("Enter X coordinate of User :"))
y1=int(input("Enter Y coordinate of User :"))
x2=int(input("Enter X coordinate of Driver D1 :"))
y2=int(input("Enter Y coordinate of Driver D1 :"))
x3=int(input("Enter X coordinate of Driver D2 :"))
y3=int(input("Enter Y coordinate of Driver D2 :"))

x=dist(x1,x2,y1,y2)# distance between d2 and p
y=dist(x1,x3,y1,y3) # distance between d1 and p

if(x>y):
    print("Driver D2 is assigned ")
else:
    print("Driver D1 is assigned")


print("Exited ")