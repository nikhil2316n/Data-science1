#15/09/25

#Write a program to 
# 2 list ,take

evenlst=[]
oddlst=[]

num=int(input("Enter a number"))
if(num%2==0):
    evenlst.append(num)

else:
    oddlst.append(num)

print("Even Number list ",evenlst)
print("Odd Number list ",oddlst)
