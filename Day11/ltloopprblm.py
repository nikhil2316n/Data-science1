#19/09/25

#Write a program to print output like this{2:4,4:16,6:36 .......100:}

a=0
dict={}
while a<=100:
    if(a%2==0):
        dict[a]=a*a
    
    a=a+1

print(dict)
