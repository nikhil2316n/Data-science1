#09/09/25
#Functio which tales any two numbers as input and the operation and print the result

def cal(a,b,c="add"):
    if(c=="add"):
        return a+b
    elif(c=="-"):
        return a-b
    elif(c=="*"):
        return a*b
    elif(c=="/"):
        return a/b
    elif(c=="%"):
        return a%b
    else:
        print("invalid input")

a=int(input("Enter a Number"))
b=int(input("Enter a Number"))
ops=input("Enter the operation")

print(cal(a,b,ops))
