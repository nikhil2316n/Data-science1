#08/09/25
#Build a module called area 
#1.The function to calculate volume  of sphere =4/3pier**2
#2.volume of cuboid =l*b*h
#
import math
a=math.pi

def volsph(r):
    volume=(4/3)*a*r*r
    return volume

def volcuboid(l,b,h):
    volume=l*b*h
    return volume


print(volsph(7))
print(volcuboid(2,3,4))


