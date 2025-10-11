# Write a short Python function, minmax(data), that takes a list of three or more numbers,
# and returns the smallest and largest numbers



a=int(input("Enter First  Number :"))
b=int(input("Enter second Number :"))
c=int(input("Enter Third  Number :"))

def grestnum(x,y,z):
    if(x>y and x>z):
        print(f"{x} is the greatest number")

    elif(y>x and y>z):
        print(f"{y} is the greatest Number")

    else:
        print(f"{z} is the greatest numbet")

def smallnum(x,y,z):
    if(x<y and x<z):
        print(f"{x} is the smallest number")

    elif(y<x and y<z):
        print(f"{y} is the smallest Number")

    else:
        print(f"{z} is the smallest numbet")

grestnum(a,b,c)
smallnum(a,b,c)