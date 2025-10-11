#8/09/25
#Distance between two points
import math


def dist(x1,x2,y1,y2):
    a=(x2-x1)**2
    b=(y2-y1)**2
    result=math.sqrt(a+b)
    return result

print(dist(5,5,10,10))

