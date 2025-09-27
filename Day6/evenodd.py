#10/09/25
#Write a program to check wheather a number is even or not
def evenodd(n):
    if(n%2==0):
        x="Even number"
    else:
        x="Odd Number"

    return x

x=int(input("Enter a Number :"))
print(evenodd(x))
